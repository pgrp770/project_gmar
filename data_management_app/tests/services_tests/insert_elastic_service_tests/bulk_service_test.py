import pytest

from data_management_app.services.insert_elastic_service.bulk_service import from_list_to_actions


@pytest.fixture(scope='module')
def actions():
    return [{"test0": "test0"}, {"test1": "test1"}, {"test2": "test2"}]


def test_from_list_to_actions(actions):
    result = from_list_to_actions("test", actions)
    assert all(action["_index"] == "test" for action in result)
