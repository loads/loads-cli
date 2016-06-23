import os
import socket
from subprocess import Popen, PIPE, STDOUT
import pprint
from outlawg import Outlawg


Log = Outlawg()

SEP = ', UUID: '
LABEL_PLAN_FOUND = 'Found plan: '
LABEL_PLAN_ADDED = 'Added plan: '
HOST = '127.0.0.1'
PORT = 8080
STOP_FLAG = 'Listening on port'


def process(cmd, header_label):
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    Log.header(header_label.upper())
    for line in iter(proc.stdout.readline, b''):
        print(line.strip())


def description_parse(description_raw):
    tmp = description_raw.replace(LABEL_PLAN_FOUND, "")
    return tmp.replace(LABEL_PLAN_FOUND, "")

def process_parse(cmd, header_label):
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    Log.header(header_label.upper())
    uuids = []

    for line in iter(proc.stdout.readline, b''):
        line_clean = str(line.strip())
        print(line_clean)

        line_chunks = line_clean.split(SEP)

        # database is loaded, exit from readline
        if STOP_FLAG in line_clean:
            break

        if SEP in line_clean:
            menu_item = line_chunks[0].split('] ')

            d = {}
            d['description'] = menu_item[1].replace(LABEL_PLAN_FOUND, "")
            d['uuid'] = line_chunks[1].replace("\'", "")

            uuids.append(d)

    return uuids
