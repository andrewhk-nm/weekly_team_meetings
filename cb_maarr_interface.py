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
    

"""Lives / week needed: {lives_per_week}    {d_lives_last_week} Lives last week
{d_lives_from_last_time} from last time
Benchmark: {lives_benchmark}"""

"""NC / week needed: {nc_per_week}    {d_nc_last_week} NC last week
{d_nc_from_last_time} from last time
Benchmark: {nc_benchmark}"""

"""Premium / week needed: {premium_per_week}    {d_premium_last_week} Premium last week
{d_premium_from_last_time} from last time
Benchmark: {premium_benchmark}"""
