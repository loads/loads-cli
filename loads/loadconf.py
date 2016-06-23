import os

from loads import (
    DIR_TEMP,
)
from loads.utils import (
   process,
   process_parse
)
from outlawg import Outlawg

Log = Outlawg()
PATH_LOADS_BROKER = '{0}/loads-broker'.format(DIR_TEMP)


def load_config(github_owner_repo):
    loads_broker_install()

    """
    Returns the loads-broker process handle and a list of dicts that represent
    plans for the user to select
    """
    return loads_broker_run(github_owner_repo)


def read_file(owner, repo, filename='loads.json'):
    path = os.path.join(DIR_TEMP, 'scenarios', owner, repo)
    os.makedirs(path, exist_ok=True)

    path = os.path.join(path, filename)
    with open(path, 'r') as fh:
        out = fh.read()
    return out


def loads_broker_install():
    if not (os.path.isdir(PATH_LOADS_BROKER)):
        Log.header('INSTALL LOADS-BROKER')
        process(
            'git clone https://github.com/loads/loads-broker \
                 _temp/loads-broker',
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


def print_menu(plans):
    Log.header('RUN MENU')
    i = 1
    for item in plans:
        print('{0}. {1}'.format(i, item['description']))
        i += 1


def loads_broker_run(github_owner_repo):
    owner, repo = github_owner_repo.split('/', 1)
    proc, plans = process_parse(
        'loads-broker -k /Users/chartjes/.ssh/loads.pem --no-influx \
        --initial-db _temp/scenarios/rpappalax/dummy-app-01/loads.json',
        'START LOADS-BROKER',
    )
    print_menu(plans)
    return proc, plans
