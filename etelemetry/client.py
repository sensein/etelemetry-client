from requests import request, ConnectionError

from .config import ET_PROJECTS


def _etrequest(endpoint, method="get", **kwargs):
    try:
        res = request(method, endpoint, **kwargs)
    except ConnectionError:
        raise RuntimeError("Connection to server could not be made")
    res.raise_for_status()
    return res


def get_project(repo):
    """
    Fetch latest version from server.

    Parameters
    ==========
    repo : str
        GitHub repository as <owner>/<project>

    Returns
    =======
    response
        Dictionary with `version` field
    """
    if "/" not in repo:
        raise ValueError("Invalid repository")
    res = _etrequest(ET_PROJECTS + repo)
    return res.json(encoding="utf-8")
