import sys
# import argparse
from argparse import ArgumentParser
from loads.fetchconf import fetch
from loads.loadconf import load_config
from loads.utils import process 

from pprint import pprint


def plan_list():
    dummy_out = """
    Pulling CoreOS AMI info...
    Verifying database setup.

    Finished database setup.
    Listening on port 8080...
    Found 0 instances to recover.
    Finished initializing: None.

    --------------------------
    PROJECT: Autopush Architecture
    --------------------------

    PLANS
    """
    print(dummy_out)
    return [
        '1. Long Connection Test - 80',
        '2. Long Connection Test - 40 - us east 1',
        '3. Long Connection Test - 80 - us west 1',
        '4. Long Connection Test - 80 - us west 2',
        '5. Long Connection Test - 80 - us west 2 - bigger',
        '6. Loadtest',
    ]


def main(argv=None):
    if argv is None:
        argv = sys.argv

    # it doesn't parse -h and print help.
    """
    conf_parser = argparse.ArgumentParser(
        description=__doc__, # printed with -h/--help
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=False
        )
    """
    conf_parser = ArgumentParser(prog='loads-cli')

    conf_parser.add_argument("-f", "--fetchconf",
                             help="Fetch config (json) file from GitHub repo\n"
                             "i.e.: <repo owner>/<repo name>")
    conf_parser.add_argument("-l", "--loadconf",
                             help="Load config (json) file\n"
                             "use same format ast for fetchconfg\n"
                             "i.e.: <repo owner>/<repo name>")
    conf_parser.add_argument("-c", "--config-overview",
                             help="Return summary overview of project config")
    conf_parser.add_argument("-r", "--run",
                             help="Launches interactive testplan runner",
                             action='store_true')
    conf_parser.add_argument("-a", "--abort",
                             help="Abort run")
    conf_parser.add_argument("-d", "--delete",
                             help="Delete run from database (KILL THIS?)")
    conf_parser.add_argument("-i", "--info",
                             help="Get historical run info from loads-broker")
    conf_parser.add_argument("-s", "--status",
                             help="Show status of current test run")

    args = conf_parser.parse_args()

    if args.fetchconf:
        fetch(args.fetchconf)

    if args.loadconf:
        load_config(args.loadconf)

    if args.run:
        plans = plan_list()
        pprint(plans)

        while True:
            response = input('Enter plan #: ')

            msg_err = 'ERROR: plan # {0} not found. \
                       Choose from existing options'.format(response)

            try:
                plan_number = int(response)
                plan_number -= 1
                if plans[plan_number]:
                    print('yay!')
                    break
            except:
                print(msg_err)

        print(plans[int(plan_number)])

    return(0)


if __name__ == "__main__":

    sys.exit(main())
