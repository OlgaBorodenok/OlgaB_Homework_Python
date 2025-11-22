import pytest
from string_utils import StringUtils

string_utils = StringUtils()

class TestCapitalize:
        
    @pytest.mark.positive
    def test_capitalize_regular_string(self):
        """Позитивный: обычная строка с маленькой буквы"""
        assert string_utils.capitalize("skypro") == "Skypro"
    
    @pytest.mark.positive  
    def test_capitalize_string_with_spaces(self):
        """Позитивный: строка с пробелами"""
        assert string_utils.capitalize("hello world") == "Hello world"
    
    @pytest.mark.negative
    def test_capitalize_empty_string(self):
        """Негативный: пустая строка"""
        assert string_utils.capitalize("") == ""
    
    @pytest.mark.negative
    def test_capitalize_already_capitalized(self):
        """Негативный: уже заглавная первая буква"""
        assert string_utils.capitalize("Skypro") == "Skypro"


class TestTrim:
        
    @pytest.mark.positive
    def test_trim_multiple_spaces(self):
        """Позитивный: несколько пробелов в начале"""
        assert string_utils.trim("   skypro") == "skypro"
    
    @pytest.mark.positive
    def test_trim_one_space(self):
        """Позитивный: один пробел в начале"""
        assert string_utils.trim(" python") == "python"
    
    @pytest.mark.negative
    def test_trim_empty_string(self):
        """Негативный: пустая строка"""
        assert string_utils.trim("") == ""
    
    @pytest.mark.negative
    def test_trim_no_leading_spaces(self):
        """Негативный: строка без начальных пробелов"""
        assert string_utils.trim("skypro") == "skypro"


class TestContains:
        
    @pytest.mark.positive
    def test_contains_symbol_exists(self):
        """Позитивный: символ существует в строке"""
        assert string_utils.contains("SkyPro", "S") == True
    
    @pytest.mark.positive
    def test_contains_substring_exists(self):
        """Позитивный: подстрока существует"""
        assert string_utils.contains("SkyPro", "Pro") == True
    
    @pytest.mark.negative
    def test_contains_symbol_not_exists(self):
        """Негативный: символ не существует"""
        assert string_utils.contains("SkyPro", "U") == False
    
    @pytest.mark.negative
    def test_contains_empty_string(self):
        """Негативный: поиск в пустой строке"""
        assert string_utils.contains("", "a") == False


class TestDeleteSymbol:
        
    @pytest.mark.positive
    def test_delete_single_character(self):
        """Позитивный: удаление одного символа"""
        assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    
    @pytest.mark.positive
    def test_delete_substring(self):
        """Позитивный: удаление подстроки"""
        assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    
    @pytest.mark.negative
    def test_delete_nonexistent_symbol(self):
        """Негативный: удаление несуществующего символа"""
        assert string_utils.delete_symbol("SkyPro", "X") == "SkyPro"
    
    @pytest.mark.negative
    def test_delete_from_empty_string(self):
        """Негативный: удаление из пустой строки"""
        assert string_utils.delete_symbol("", "a") == ""