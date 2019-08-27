import pytest

from ..config import ET_ROOT
from ..client import _etrequest, get_project


def test_request():
    endpoint = "http://fakeendpoint/"
    with pytest.raises(Exception):
        _etrequest(endpoint, method="get")
    assert _etrequest(ET_ROOT)


def test_get_project():
    repo = "invalidrepo"
    with pytest.raises(ValueError):
        get_project(repo)
    repo = "github/hub"
    res = get_project(repo)
    assert "version" in res
