""" The interface portion of the CB Monthly Activities and Ratios Report module.
"""

import sys
import cb_maarr

if __name__ == "__main__":
    # Get filename from args, if available
    try:
        xml_file = sys.argv[1]
    except(IndexError):
        # If no argument was passed, default to None
        xml_file = None
    
    NmCbMaarr = cb_maarr.NmCbMonthlyActivitesAndRatiosReportParser(xml_file)
    
    # DEBUG print the results
    print('NmCbMaarr.lives_per_week={}'.format(NmCbMaarr.lives_per_week))
    print('NmCbMaarr.new_clients_per_week={}'.format(NmCbMaarr.new_clients_per_week))
    print('NmCbMaarr.premium_per_week={}'.format(NmCbMaarr.premium_per_week))
    