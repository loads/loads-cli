import os
from subprocess import Popen, PIPE, STDOUT
from outlawg import Outlawg


Log = Outlawg()

SEP = ', UUID: '
#STOP_FLAG = 'Finished initializing'
STOP_FLAG = 'Listening on port'

def process(cmd, header_label):
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    Log.header(header_label.upper())
    for line in iter(proc.stdout.readline, b''):
        print(line.strip())

def process_parse(cmd, header_label):
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    Log.header(header_label.upper())
    menu = []
    uuids = []

    for line in iter(proc.stdout.readline, b''):
        line_clean = str(line.strip())
        print(line_clean)
        line_chunks = line_clean.split(SEP)
        if SEP in line_clean:
            menu_item = line_chunks[0].split('] ')
            menu.append(menu_item[1]) 
            uuids.append(line_chunks[1])
            if STOP_FLAG in line_clean:
                break
    return menu, uuids
    """
    Log.header('DISPLAYED CONTENT')
    pprint(menu)
    Log.header('HIDDEN')
    pprint(uuids)
    """
