import pytest
from api_client import YougileAPI


INVALID_PROJECT_ID = "00000000-0000-0000-0000-000000000000"


@pytest.fixture
def created_project():
    response = YougileAPI.create_project("Тестовый проект")
    assert response.status_code == 201, (
        f"Не удалось создать проект: {response.text}"
    )
    project_id = response.json().get("id")
    yield project_id


class TestCreateProject:

    def test_create_project_positive(self):
        response = YougileAPI.create_project("Мой первый проект")
        assert response.status_code == 201
        assert "id" in response.json()
        assert isinstance(response.json()["id"], str)

    def test_create_project_negative_empty_title(self):
        response = YougileAPI.create_project("")
        assert response.status_code == 400
        assert ("error" in response.text.lower() or
                "title" in response.text.lower())


class TestGetProject:

    def test_get_project_positive(self, created_project):
        response = YougileAPI.get_project(created_project)
        assert response.status_code == 200
        assert response.json().get("id") == created_project
        assert "title" in response.json()

    def test_get_project_negative_not_exists(self):
        response = YougileAPI.get_project(INVALID_PROJECT_ID)
        assert response.status_code == 404
        assert "error" in response.json()


class TestUpdateProject:

    def test_update_project_positive(self, created_project):
        new_title = "Обновленное название"
        response = YougileAPI.update_project(created_project, title=new_title)
        assert response.status_code == 200

        get_response = YougileAPI.get_project(created_project)
        assert get_response.json().get("title") == new_title

    def test_update_project_negative_invalid_id(self):
        response = YougileAPI.update_project(
            INVALID_PROJECT_ID, title="Новое название"
        )
        assert response.status_code == 404
        assert "error" in response.json()
