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

def get_tree(path_and_filename):
    """ Given the path and filename of an xml doc, return the tree.
    """
    tree = etree.parse(path_and_filename)
    
    return tree

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

    # DEBUG print
    print(path_and_filename)

    # Parse the xml
    # Get the etree object
    tree = get_tree(path_and_filename)

    # CB Monthly Activites and Ratios XML Structure
    # Are these text box name### fields consistent between reports?
    # <BusinessActivity2
    #   Textbox172=[Submitted Lives Data]
    #   Textbox173=[Submitted Annual Premium Data]
    #   Textbox174=[Placed Lives Goal Data]
    #   Textbox175=[Placed NC Goal Data]
    #   Textbox176=[Placed Annual Premium Goal Data]
    #   Textbox57=["Total" Label]
    #   Textbox128=[Submitted Lives Total Data]
    #   Textbox130=[Submitted Annual Premium Total Data]
    #   Textbox143=[Placed Lives Total Data]
    #   Textbox136=[Placed NC Total Data]
    #   Textbox141=[Placed Annual Premium Total Data]
    #   Textbox38=["Avg/Mth" Label]
    #   Textbox30=[Submitted "Avg/Mth" Lives Data]
    #   Textbox31=[Submitted "Avg/Mth" Annual Prem Data]
    #   Textbox32=[Placed "Avg/Mth" Lives Data]
    #   Textbox34=[Placed "Avg/Mth" NC Data]
    #   Textbox36=[Placed "Avg/Mth" Annual Prem Data]
    #   Textbox47=[Submitted Lives Data, Annualized]
    #   Textbox48=[Submitted Annual Prem Data, Annualized
    #   Textbox50=[Placed Lives Data, Annualized]
    #   Textbox51=[Placed NC Data, Annualized]
    #   Textbox53=[Placed Annual Prem Data, Annualized]
    #   >

    # Don't automatically exit when finished.
    input('Press <ENTER> to exit')
