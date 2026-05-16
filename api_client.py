import requests
from config import BASE_URL, HEADERS


class YougileAPI:
    """Простой клиент для работы с API Yougile"""

    @staticmethod
    def _request(method, endpoint, json=None):
        url = f"{BASE_URL}/{endpoint}"
        response = requests.request(method, url, headers=HEADERS, json=json)
        return response

    @staticmethod
    def create_project(title, users=None):
        """POST /projects - создать проект"""
        data = {"title": title}
        if users:
            data["users"] = users
        return YougileAPI._request("POST", "projects", json=data)

    @staticmethod
    def get_project(project_id):
        """GET /projects/{id} - получить проект"""
        return YougileAPI._request("GET", f"projects/{project_id}")

    @staticmethod
    def update_project(project_id, title=None, users=None,
                       is_archived=None, is_deleted=None):
        """PUT /projects/{id} - обновить проект"""
        data = {}
        if title is not None:
            data["title"] = title
        if users is not None:
            data["users"] = users
        if is_archived is not None:
            data["isArchived"] = is_archived
        if is_deleted is not None:
            data["isDeleted"] = is_deleted
        return YougileAPI._request("PUT", f"projects/{project_id}", json=data)
