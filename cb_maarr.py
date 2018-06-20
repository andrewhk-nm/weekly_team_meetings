""" CB Monthly Activities and Ratios Report Parser
"""

# TODO: Calculate and return the benchmark numbers
#		Goal / 52 weeks per year

import xml.etree.ElementTree as etree
#import sys # for argv
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

    # CB Monthly Activites and Ratios XML Structure
    # Are these text box name### fields consistent between reports?
    #    Based on 6/4 & 6/12, they are consistent.
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
    #   Textbox48=[Submitted Annual Prem Data, Annualized]
    #   Textbox50=[Placed Lives Data, Annualized]
    #   Textbox51=[Placed NC Data, Annualized]
    #   Textbox53=[Placed Annual Prem Data, Annualized]
    #   >
    
    
    # Publicly accessable class variables that hold the results
    lives_per_week = None
    new_clients_per_week = None
    premium_per_week = None
    
    def __init__(self, xml_file=None):
        # Initialize the exposed attributes/variables
        self.lives_per_week = None
        self.new_clients_per_week = None
        self.premium_per_week = None
        
        # Open the file
        path_and_filename = self._get_xml_file(xml_file)
    
        # # DEBUG print the file name and path that was selected.
        # print(path_and_filename)
        
        # Parse the xml
        # Get the etree object
        root = self._get_root(path_and_filename)
        # # DEBUG Print root tree
        # print('root={}'.format(root))
        
        # Get the xml namespace from vthe first tag. Include the braces.
        xmlns = root.tag.split('}')[0] + '}'
        # # DEBUG print xmlns
        # print('xmlns={}'.format(xmlns))

        ## Create a dictionary of the Textbox fields with common names.
        #dict_of_fields = self._get_dict_of_fields()
        
        # # DEBUG Print a single attribute as a test to make sure it grabs the right thing
        # textbox_test = root.find(xmlns + 'BusinessActivity2').get(self._get_fieldname_from_dict('Placed Annual Premium Goal Data'))
        # print('textbox_test attrib={}'.format(textbox_test))
        
        # What data do I use each week?
        # lives_goal
        # lives_placed
        # nc_goal
        # nc_placed
        # prem_goal
        # prem_placed
        
        # Monthly Activity & Ratio Report (maarr) info that are needed for my weekly reports
        maarr = root.find(xmlns + 'BusinessActivity2')
            
        # Get the lives goal
        lives_goal = float(maarr.get(self._get_fieldname_from_dict('Placed Lives Goal Data')))
        lives_placed = float(maarr.get(self._get_fieldname_from_dict('Placed Lives Total Data')))
        nc_goal = float(maarr.get(self._get_fieldname_from_dict('Placed NC Goal Data')))
        nc_placed = float(maarr.get(self._get_fieldname_from_dict('Placed NC Total Data')))
        prem_goal = float(maarr.get(self._get_fieldname_from_dict('Placed Annual Premium Goal Data')))
        prem_placed = float(maarr.get(self._get_fieldname_from_dict('Placed Annual Premium Total Data')))
        
        # # print the data I extracted
        # print(lives_goal)
        # print(lives_placed)
        # print(nc_goal)
        # print(nc_placed)
        # print(prem_goal)
        # print(prem_placed)
        
        # calculate the lives, nc, and prem needed per week.
        lives_pw = per_week(lives_goal, lives_placed)
        nc_pw = per_week(nc_goal, nc_placed)
        prem_pw = per_week(prem_goal, prem_placed)
        
        # # DEBUG print the results
        # print('lives_pw={}'.format(lives_pw))
        # print('nc_pw={}'.format(nc_pw))
        # print('prem_pw={}'.format(prem_pw))
        
        # Set the results to the publically available vars
        self.lives_per_week = lives_pw
        self.new_clients_per_week = nc_pw
        self.premium_per_week = prem_pw
        
    
    def _get_xml_file(self, xml_file):
        """ If an xml file was passed to the class upon creation, use it.
        Otherwise prompt the user for one.
        """
                
        # If no xml file was passed, prompt for the file path and name.
        if xml_file is not None:
            path_and_filename = xml_file
        else:
            path_and_filename = self._prompt_for_xml_file()
        
        # TODO: Perhaps Verify the file is the correct type, etc. here.
        
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
        
    def _get_fieldname_from_dict(self, field):
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
                }[field]


                
if __name__ == "__main__":
    # create a NmCbMonthlyActivitesAndRatiosReportParser object
    NmCbMaarr = NmCbMonthlyActivitesAndRatiosReportParser()
    
    # DEBUG print the results
    print('NmCbMaarr.lives_per_week={}'.format(NmCbMaarr.lives_per_week))
    print('NmCbMaarr.new_clients_per_week={}'.format(NmCbMaarr.new_clients_per_week))
    print('NmCbMaarr.premium_per_week={}'.format(NmCbMaarr.premium_per_week))
    