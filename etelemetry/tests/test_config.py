import pytest

from etelemetry.config import setup


def test_setup():
    default_endpoints = setup()
    assert default_endpoints.root == 'https://rig.mit.edu/et'
    assert default_endpoints.projects == 'https://rig.mit.edu/et/projects'

    # assert values cannot be changed once initialized
    with pytest.raises(AttributeError):
        default_endpoints.root = "new_value"

    new_endpoints = setup(protocol='http')
    assert new_endpoints.root != 'http://rig.mit.edu/et'
    # but re-initialized, that is ok
    new_endpoints = setup(
        protocol='http', root_endpoint='/', projects_endpoint='/custom/route', reinit=True,
    )
    assert new_endpoints.root == 'http://rig.mit.edu/'
    assert new_endpoints.projects == 'http://rig.mit.edu/custom/route'
