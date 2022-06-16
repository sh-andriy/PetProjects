import pytest
import ProgramsV2.apps as apps


class TestClass:
    @pytest.mark.parametrize("repeat", range(10))
    def test_dict(self, repeat):
        assert apps.unique_character_calculator_dict("abbbccdf") == 3

    @pytest.mark.parametrize("repeat", range(10))
    def test_list_comp(self, repeat):
        assert apps.unique_character_calculator_list_comp("abbbccdf") == 3

    @pytest.mark.parametrize("repeat", range(10))
    def test_collection(self, repeat):
        assert apps.unique_character_calculator_collections("abbbccdf") == 3

    def test_empty_string(self):
        assert apps.unique_character_calculator_collections("") == 0

    def test_number(self):
        with pytest.raises(ValueError):
            apps.unique_character_calculator_collections(1)


@apps.show_timing
def dict_speed(method_name):
    for times in range(100):
        apps.unique_character_calculator_dict("abbbccdf")


@apps.show_timing
def list_comp_speed(method_name):
    for times in range(100):
        apps.unique_character_calculator_list_comp("abbbccdf")


@apps.show_timing
def collections_speed(method_name):
    for times in range(100):
        apps.unique_character_calculator_collections("abbbccdf")


dict_speed("Dictionary")
list_comp_speed("List comprehension")
collections_speed("Collections")
