hostname = "rig.mit.edu/"
https = True

if https is True:
    ET_ROOT = "https://" + hostname
else:
    ET_ROOT = "http://" + hostname

root_endpoint = "et/"
ET_ROOT += root_endpoint

ET_PROJECTS = ET_ROOT + "projects/"
