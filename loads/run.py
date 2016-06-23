from loads import HOST, PORT

import requests


def run_test(proc, plan_uuid):
    """
    Build our POST request
    Send it to loads-broker
    Stand back and let it run
    """
    url = 'http://{0}:{1}/api/orchestrate/{2}'.format(HOST, PORT, plan_uuid)
    r = requests.post(url)
    print(r.text)

    for line in iter(proc.stdout.readline, b''):
        print(line.strip())

    return 0
