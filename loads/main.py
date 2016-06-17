import sys
from argparse import ArgumentParser
from loads.fetchconf import fetch
from loads.loadconf import load_config
from loads.utils import process 

from pprint import pprint


def main(argv=None):
    if argv is None:
        argv = sys.argv

    conf_parser = ArgumentParser(prog='loads-cli')
    conf_parser.add_argument("-c", "--config-overview",
                             help="Return summary overview of project config")
    conf_parser.add_argument("-r", "--run",
                             help="Launches interactive testplan runner"
                             "i.e.: <repo owner>/<repo name>")
    conf_parser.add_argument("-a", "--abort",
                             help="Abort run")
    conf_parser.add_argument("-d", "--delete",
                             help="Delete run from database (KILL THIS?)")
    conf_parser.add_argument("-i", "--info",
                             help="Get historical run info from loads-broker")
    conf_parser.add_argument("-s", "--status",
                             help="Show status of current test run")

    args = conf_parser.parse_args()

    if args.run:
        fetch(args.run)
        plans = load_config(args.run)

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
