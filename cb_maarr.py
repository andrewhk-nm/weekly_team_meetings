""" CB Monthly Activities and Ratios Report Parser
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
from nm import per_week

def get_root(path_and_filename):
    """ Given the path and filename of an xml doc, return the tree.
    """
    tree = etree.parse(path_and_filename)
    root = tree.getroot()
    
    return root
    
def get_dict_of_fields():
    """ Return a dictionary of the poorly named Textbox attributes below with a more descriptive name.
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
    #   Textbox48=[Submitted Annual Prem Data, Annualized]
    #   Textbox50=[Placed Lives Data, Annualized]
    #   Textbox51=[Placed NC Data, Annualized]
    #   Textbox53=[Placed Annual Prem Data, Annualized]
    """
    
    return {'Submitted Lives Data': 'Textbox172',
            'Submitted Annual Premium Data': 'Textbox173',
            'Placed Lives Goal Data': 'Textbox174',
            'Placed NC Goal Data': 'Textbox175',
            'Placed Annual Premium Goal Data': 'Textbox176',
            '"Total" Label': 'Textbox57',
            'Submitted Lives Total Data': 'Textbox128',
            'Submitted Annual Premium Total Data': 'Textbox130',
            'Placed Lives Total Data': 'Textbox143',
            'Placed NC Total Data': 'Textbox136',
            'Placed Annual Premium Total Data': 'Textbox141',
            '"Avg/Mth" Label': 'Textbox38',
            'Submitted "Avg/Mth" Lives Data': 'Textbox30',
            'Submitted "Avg/Mth" Annual Prem Data': 'Textbox31',
            'Placed "Avg/Mth" Lives Data': 'Textbox32',
            'Placed "Avg/Mth" NC Data': 'Textbox34',
            'Placed "Avg/Mth" Annual Prem Data': 'Textbox36',
            'Submitted Lives Data, Annualized': 'Textbox47',
            'Submitted Annual Prem Data, Annualized': 'Textbox48',
            'Placed Lives Data, Annualized': 'Textbox50',
            'Placed NC Data, Annualized': 'Textbox51',
            'Placed Annual Prem Data, Annualized': 'Textbox53',
            }