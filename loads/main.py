import sys
from argparse import ArgumentParser
from loads.fetchconf import fetch
from loads.loadconf import load_config
from loads.run import run_test


def main(argv=None):
    if argv is None:
        argv = sys.argv

    conf_parser = ArgumentParser(prog='loads-cli')
    conf_parser.add_argument("-r", "--run",
                             help="Launches interactive testplan runner"
                             "i.e.: <repo owner>/<repo name>")

    args = conf_parser.parse_args()

    if args.run:
        fetch(args.run)
        proc, plans = load_config(args.run)

        while True:
            response = input('Enter plan #: ')

            msg_err = 'ERROR: plan # {0} not found. \
                       Choose from existing options'.format(response)

            try:
                plan_number = int(response)
                plan_number -= 1
                uuid = plans[plan_number]['uuid']
                print(run_test(proc, uuid))
                break
            except:
                print(msg_err)

    return(0)


if __name__ == "__main__":

    sys.exit(main())
