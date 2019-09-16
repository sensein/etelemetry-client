hostname = "rig.mit.edu/"
https = True

if https is True:
    prefix = "https"
else:
    prefix = "http"

ET_ROOT = f"{prefix}://{hostname}/et/"

ET_PROJECTS = ET_ROOT + "projects/{repo}"
