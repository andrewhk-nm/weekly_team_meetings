""" CB Monthly Activities and Ratios Report Parser
"""

import xml.etree.ElementTree as etree
import sys # for argv
from nm import per_week
import tkinter as tk
from tkinter import filedialog

class NmCbMonthlyActivitesAndRatiosReportParser():

    # I think this might be able to be wrapped in a class...
    # class NmCbMonthlyActivitesAndRatiosReportParser
    #     expose
    #       new(filename or prompt for one)
    #       output
    #           lives_per_week
    #           new_clients_per_week
    #           premium_per_week    

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

    #lives_per_week
    #new_clients_per_week
    #premium_per_week   
    
    def __init__(self):
        # Initialize the exposed attributes/variables
        self.lives_per_week = None
        self.new_clients_per_week = None
        self.premium_per_week = None
        
        # Open the file
        path_and_filename = self._get_xml_file()
    
        # DEBUG print the file name and path that was selected.
        print(path_and_filename)
        
        # Parse the xml
        # Get the etree object
        root = self._get_root(path_and_filename)
        
        # Get the xml namespace from the first tag. Include the braces.
        xmlns = '{' + root.tag.split('}')[0] + '}'
        print('root={}'.format(root))

    
    def _get_xml_file(self):
        """ If an xml file was passed to the command line, use it.
        Otherwise prompt the user for one.
        """
        
        # Grab the args
        args = sys.argv
        
        # If no args are passed, ask for the file path and name.
        try:
            path_and_filename = args[1]
        except(IndexError):
            path_and_filename = self._prompt_for_xml_file()
        
        return path_and_filename
        
    def _prompt_for_xml_file(self):
        """ Prompt the user for the input file if none was passed.
        Return a string with the path + filename
        """
        
        # Use tkinter instead of an input
        #input('''Please enter the path and filename for the "CB Monthly Activity and Ratios.xml" XML file. ''')

        # Create a tkinter object
        root = tk.Tk()
        # Withdraw the root window so it doesn't interfere
        root.withdraw()
        
        # TODO: Only look for xml files by default.
        file_path_name = filedialog.askopenfilename(initialdir='/', 
                                                    title='Select XML File to parse',
                                                    filetypes=(('xml files', '*.xml'), 
                                                               ('All Files', '*.*')),
                                                    )
        return file_path_name
        
    def _get_root(self, path_and_filename):
        """ Given the path and filename of an xml doc, return the tree.
        """
        tree = etree.parse(path_and_filename)
        root = tree.getroot()
        
        return root
        
    def _get_dict_of_fields(self):
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


                
if __name__ == "__main__":
    # create a NmCbMonthlyActivitesAndRatiosReportParser object
    NmCbMaarr = NmCbMonthlyActivitesAndRatiosReportParser()
    
    