""" The interface portion of the CB Monthly Activities and Ratios Report module.
"""

# TODO: Output as HTML with colors?
#       Output the chart as well?
# TODO: Refactor __name__ == "__main__"!
# TODO: Respond appropriately when "--help" or "-h" is passed as an argument.

import sys
import cb_maarr
import tkinter as tk
from tkinter import filedialog

def _prompt_for_xml_file(title):
    """ Prompt the user for the input file if none was passed.
    Return a string with the path + filename
    """

    # Create a tkinter object
    root = tk.Tk()
    # Withdraw the root window so it doesn't interfere
    root.withdraw()
    
    # TODO: Only look for xml files by default.
    file_path_name = filedialog.askopenfilename(initialdir='/', 
                                                title=title,
                                                filetypes=(('Monthly Activities XML file', '*CB Monthly Activity and Ratios*.xml'),
                                                           ('XML files', '*.xml'), 
                                                           ('All Files', '*.*')),
                                                )
    return file_path_name

def main()
    """ The main entry point for the Monthly Activities and Ratios Report interface module.
    This module instantiates the report calculator object, and formats the results in 
    a manner that can be easily inserted into my weekly report.
    """
    
    # Get filename from args, if available (this week's file)
    try:
        xml_file = sys.argv[1]
        
    except(IndexError):
        # If no argument was passed, prompt the user for one.
        print("Please use the File Dialog box to select the current xml report data file.")
        xml_file = _prompt_for_xml_file("Select XML File to parse (today's report)")
    finally:
        # If no file is returned (aka 'Cancel' is pressed) quit immediately with error.
        if xml_file == '': 
            sys.exit('No file was selected. Stopping execution.')
        else:
            print("Using '{}' as the current xml report data file.".format(xml_file))
            
        
    # Get filename from args, if available (last week's file)
    try:
        xml_file = sys.argv[2]
    except(IndexError):
        # If no argument was passed, prompt the user for one.
        print("\nPlease use the File Dialog box to select the historical xml report data file for delta comparisons.\nPress cancel to skip comparisons.")
        xml_file_hist = _prompt_for_xml_file("Select XML File to parse (last week's report) (Press 'Cancel' to skip historical comparisons)")
    finally:
        # If no file is returned (aka 'Cancel' is pressed) set the file to None.
        if xml_file_hist == '':
            xml_file_hist = None
            print("No historical xml report data file selected. Skipping historical comparisons.")
        else:
            print("Using '{}' as the historical xml report data file for comparison.".format(xml_file_hist))
    
    NmCbMaarr = cb_maarr.NmCbMonthlyActivitesAndRatiosReportParser(xml_file, xml_file_hist)
    
    # # DEBUG print the results
    # print('NmCbMaarr.lives_per_week={}'.format(NmCbMaarr.lives_per_week))
    # print('NmCbMaarr.new_clients_per_week={}'.format(NmCbMaarr.new_clients_per_week))
    # print('NmCbMaarr.premium_per_week={}'.format(NmCbMaarr.premium_per_week))
    
    # Create the string replacement dictionaries
    if xml_file_hist is None:
        # No historical file selected, there will be no deltas.
        lives_dict = {'lives_per_week': round(NmCbMaarr.lives_per_week, 2),
                      'lives_benchmark': NmCbMaarr.lives_per_week_benchmark,
                      }
                      
        nc_dict = {'nc_per_week': round(NmCbMaarr.new_clients_per_week, 2),
                   'nc_benchmark': NmCbMaarr.new_clients_per_week_benchmark,
                   }

        premium_dict = {'premium_per_week': round(NmCbMaarr.premium_per_week),
                        'premium_benchmark': round(NmCbMaarr.premium_per_week_benchmark),
                        }                  
    else:        
        # Historical file was selected, get the deltas, too.            
        lives_dict = {'lives_per_week': round(NmCbMaarr.lives_per_week, 2),
                      'd_lives_last_week': round(NmCbMaarr.d_lives_last_week, 1),
                      'd_lives_from_last_time': round(NmCbMaarr.d_lives_per_week, 2),
                      'lives_benchmark': NmCbMaarr.lives_per_week_benchmark,
                      }
                      
        nc_dict = {'nc_per_week': round(NmCbMaarr.new_clients_per_week, 2),
                   'd_nc_last_week': round(NmCbMaarr.d_new_clients_last_week, 1),
                   'd_nc_from_last_time': round(NmCbMaarr.d_new_clients_per_week, 2),
                   'nc_benchmark': NmCbMaarr.new_clients_per_week_benchmark,
                   }

        premium_dict = {'premium_per_week': round(NmCbMaarr.premium_per_week),
                        'd_premium_last_week': round(NmCbMaarr.d_premium_last_week),
                        'd_premium_from_last_time': round(NmCbMaarr.d_premium_per_week),
                        'premium_benchmark': round(NmCbMaarr.premium_per_week_benchmark),
                        }                  
    
    # Create the pretty print strings.
    # TODO: Use better string commands to format the spacing.
    if xml_file_hist is None:
        # No historical file selected, don't print the delta fields.       
        str_lives = \
        """Lives / week needed: {lives_per_week}
Benchmark: {lives_benchmark:.2f} / week""".format(**lives_dict)

        str_nc = \
        """NC / week needed: {nc_per_week}
Benchmark: {nc_benchmark:.2f} / week""".format(**nc_dict)

        str_premium = \
        """Premium / week needed: ${premium_per_week}
Benchmark: ${premium_benchmark:.0f} / week""".format(**premium_dict)
        
    else:
        # Historical file was selected, print the deltas, too.    
        str_lives = \
        """Lives / week needed: {lives_per_week}    {d_lives_last_week:+} Lives last week
{d_lives_from_last_time:+} from last time
Benchmark: {lives_benchmark:.2f} / week""".format(**lives_dict)

        str_nc = \
        """NC / week needed: {nc_per_week}    {d_nc_last_week:+} NC last week
{d_nc_from_last_time:+} from last time
Benchmark: {nc_benchmark:.2f} / week""".format(**nc_dict)

        str_premium = \
        """Premium / week needed: ${premium_per_week}    {d_premium_last_week:+} Premium last week
{d_premium_from_last_time:+} from last time
Benchmark: ${premium_benchmark:.0f} / week""".format(**premium_dict)

    # Print the pretty printed results
    print('\nResults:\n')
    print(str_lives)
    print()
    print(str_nc)
    print()
    print(str_premium)
    print()
    
    
    
if __name__ == "__main__":

    # Launch the main function
    main()
    
    # Don't automatically exit
    input('Press <ENTER> to quit.')