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
    
    # Create the string replacement dictionaries
    # TODO: Calculate the difference numbers too
    # TODO: Calculate the bench mark numbers
    lives_dict = {'lives_per_week': NmCbMaarr.lives_per_week,
                  'd_lives_last_week': "TODO",
                  'd_lives_from_last_time': "TODO",
                  'lives_benchmark': "TODO",
                  }
                  
    nc_dict = {'nc_per_week': NmCbMaarr.new_clients_per_week,
               'd_nc_last_week': "TODO",
               'd_nc_from_last_time': "TODO",
               'nc_benchmark': "TODO",
               }

    premium_dict = {'premium_per_week': NmCbMaarr.premium_per_week,
                    'd_premium_last_week': "TODO",
                    'd_premium_from_last_time': "TODO",
                    'premium_benchmark': "TODO",
                    }                  
    
    # Create the pretty print strings.
    # TODO: Use better string commands to format the spacing.
    str_lives = \
    """Lives / week needed: {lives_per_week}    {d_lives_last_week:+} Lives last week
{d_lives_from_last_time:+} from last time
Benchmark: {lives_benchmark}""".format(**lives_dict)

    str_nc = \
    """NC / week needed: {nc_per_week}    {d_nc_last_week:+} NC last week
{d_nc_from_last_time} from last time
Benchmark: {nc_benchmark}""".format(**nc_dict)

    str_premium = \
    """Premium / week needed: ${premium_per_week}    {d_premium_last_week:+} Premium last week
{d_premium_from_last_time:+} from last time
Benchmark: ${premium_benchmark}""".format(**premium_dict)

    # DEBUG Print the pretty printed results
    print()
    print(str_lives)
    print()
    print(str_nc)
    print()
    print(str_premium)
    print()
    
    # Don't automatically exit
    input('Press <ENTER> to quit.')