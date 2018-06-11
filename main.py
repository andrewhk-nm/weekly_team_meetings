""" Main module for my weekly report functions.
"""

## CB Monthly Activities and Ratios
#   Default filename:
#       'CB Monthly Activity and Ratios.xml'
#   Data I want:
#       Lives
#       New Clients
#       Annual Premium
#   What do I do with it?
#       Lives / week needed (can use nm.per_week)
#       Compare to Benchmark
#           Lives: 4 / week
#           NC: 1.38 / week
#           Prem: $5770 / week
#       Compare to last week.

import xml.etree.ElementTree as etree
import sys # for argv

if __name__ == '__main__':
    # Probably grab the file name from the arg.
    args = sys.argv

    ## Make sure it gets the right info from the args.
    #for arg in args:
    #    print(arg)

    # If no args are passed, ask for the file path and name.
    try:
        path_and_filename = args[1]
    except(IndexError):
        path_and_filename = input('''Please enter the path and filename for \
the "CB Monthly Activity and Ratios.xml" XML file. ''')

    print(path_and_filename)
    
    input()
