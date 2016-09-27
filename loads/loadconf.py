import os

from loads import (
    DIR_TEMP,
    PEM_FILE,
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
                 {0}/loads-broker'.format(DIR_TEMP),
            'Installing loads-broker'
        )
        process(
            'cd {0}/loads-broker; \
             pip install -r test-requirements.txt'.format(DIR_TEMP),
            'Installing loads-broker libraries'
        )
        process(
            'cd {0}/loads-broker;python setup.py develop'.format(DIR_TEMP),
            'Setting up loads-broker'
        )


def print_menu(plans):
    Log.header('RUN MENU')
    i = 1
    for item in plans:
        print('{0}. {1}'.format(i, item['description']))
        i += 1


def loads_broker_run(github_owner_repo, filename='loads.json'):
    owner, repo = github_owner_repo.split('/', 1)
    proc, plans = process_parse(
        'loads-broker -k {0} --no-influx \
        --initial-db {1}/scenarios/{2}/{3}/{4}'.format(
            PEM_FILE, DIR_TEMP, owner, repo, filename),
        'START LOADS-BROKER',
    )
    print_menu(plans)
    Log.header('RUN MENU')
    return proc, plans
