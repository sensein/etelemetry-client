import requests

from .config import ET_PROJECTS


def _etrequest(endpoint, request="GET", valid_codes=(200,)):
    try:
        res = requests.get(endpoint)
    except requests.ConnectionError:
        raise RuntimeError("Connection to server could not be made")
    if res.status_code not in valid_codes:
        raise RuntimeError("Response %s is not valid" % res)
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
        raise TypeError("Invalid repository")
    res = _etrequest(ET_PROJECTS + repo)
    return res.json(encoding="utf-8")
