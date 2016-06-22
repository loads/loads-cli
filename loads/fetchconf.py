import os
import json
import requests
from outlawg import Outlawg

from loads import (
    URL_GITHUB_RAW,
    DIR_TEMP
)

Log = Outlawg()


# https://raw.githubusercontent.com/rpappalax/dummy-app-01/master/loads.json
def url_manifest(owner, repo, branch='master'):
    """Returns URL for a specific test manifest"""

    return '{0}/{1}/{2}/{3}/loads.json'.format(
        URL_GITHUB_RAW, owner, repo, branch
    )


def fetch_json(url):
    Log.header('DOWNLOADING JSON FILE')
    r = requests.get(url)
    if r.status_code == 200:
        print('DONE!')
    else:
        print('ERROR: DOWNLOAD FAILED!')
        exit()
    parsed = r.json()
    return json.dumps(parsed, indent=4)


def write_file(owner, repo, contents, filename='loads.json'):
    path = os.path.join(DIR_TEMP, 'scenarios', owner, repo)
    os.makedirs(path, exist_ok=True)

    path = os.path.join(path, filename)
    with open(path, 'w') as fh:
        fh.write(str(contents))


def fetch(github_owner_repo):
    owner, repo = github_owner_repo.split('/', 1)
    url = url_manifest(owner, repo)
    loads_json = fetch_json(url)
    write_file(owner, repo, loads_json)


if __name__ == '__main__':

    url = url_manifest('rpappalax', 'dummy-app-01')
    loads_json = fetch_json(url)
    write_file(loads_json)
