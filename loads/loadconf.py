import os
from pprint import pprint

from loads import (
    DIR_TEMP,
) 
from loads.utils import (
   process,
   process_parse
)
from outlawg import Outlawg

Log = Outlawg()


def load_config(github_owner_repo):
    loads_broker_install()

    # check for loads-broker
    # - activate venv
    # - retrieve master githash from github
    # - git check local githash - if same, then continue
    # - if not then install!
    # - pip install -r test-requirements.txt
    # start loads-broker -i json-file
    loads_broker_run(github_owner_repo)


def read_file(owner, repo, filename='loads.json'):
    path = os.path.join(DIR_TEMP, 'scenarios', owner, repo)
    os.makedirs(path, exist_ok=True)

    path = os.path.join(path, filename)
    with open(path, 'r') as fh:
        out = fh.read()
    return out


def loads_broker_install():
    Log.header('INSTALL LOADS-BROKER')
    """
    process(
        'rm -rf _temp/loads-broker',
        'Cleaning up old loads-broker install'
    )
    """
    process(
        'git clone https://github.com/loads/loads-broker _temp/loads-broker',
        'Installing loads-broker'
    )
    process(
        'cd _temp/loads-broker;pip install -r test-requirements.txt',
        'Installing loads-broker libraries'
    )
    process(
        'cd _temp/loads-broker;python setup.py develop',
        'Setting up loads-broker'
    )


def loads_broker_run(github_owner_repo):
    owner, repo = github_owner_repo.split('/', 1)
    #json = read_file(owner, repo, filename='loads.json')
    #print(json)
    menu, uuids = process_parse(
        'loads-broker -k /Users/rpappalardo/.ssh/loads.pem --no-influx --initial-db _temp/scenarios/rpappalax/dummy-app-01/loads.json',
        'START LOADS-BROKER',
    )

    Log.header('HIDDEN: UUIDS')
    pprint(uuids)

    Log.header('RUN MENU')
    i = 1
    for item in menu:
        print('{0}. {1}'.format(i, item))
        i += 1
