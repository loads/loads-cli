import requests


def run_test(proc, plan_uuid):
    """
    Build our POST request
    Send it to loads-broker
    Stand back and let it run
    """
    url = 'http://localhost:8080/api/orchestrate/{0}'.format(plan_uuid)
    r = requests.post(url)
    print(r.text)

    for line in iter(proc.stdout.readline, b''):
        print(line.strip())

    return 0
