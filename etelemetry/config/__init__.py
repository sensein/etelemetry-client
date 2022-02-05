import dataclasses

ENDPOINTS = None
SUPPORTED_PROTOCOLS = {'http', 'https'}


@dataclasses.dataclass(frozen=True)
class EndPoints:
    root: str
    projects: str

    def gen_repo_url(self, repo: str) -> str:
        return _safe_join_url((self.projects, repo))


def setup(
    *,
    host: str = 'rig.mit.edu',
    protocol: str = 'https',
    root_endpoint: str = '/et',
    projects_endpoint: str = '/projects',
    reinit: bool = False,
) -> EndPoints:
    """
    Initialize eTelemetry endpoints.

    If endpoints have already been initialized, reinitialized is skipped
    unless `reinit` is set to ``True``.
    """
    global ENDPOINTS
    if ENDPOINTS is not None and not reinit:
        # Setup has already occurred
        return ENDPOINTS

    if protocol not in SUPPORTED_PROTOCOLS:
        raise NotImplementedError(f'Protocol {protocol} not supported (try {SUPPORTED_PROTOCOLS})')

    root = f'{protocol}://{_safe_join_url((host, root_endpoint))}'
    projects = _safe_join_url((root, projects_endpoint))

    ENDPOINTS = EndPoints(root=root, projects=projects)
    return ENDPOINTS


def get_endpoints() -> EndPoints:
    global ENDPOINTS
    if not ENDPOINTS:
        ENDPOINTS = setup()
    return ENDPOINTS


def _safe_join_url(paths: list) -> str:
    return '/'.join((p.strip('/') for p in paths))
