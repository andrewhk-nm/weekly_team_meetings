""" CB Monthly Activities and Ratios Report Parser
"""

# Does not check if goals change mid year (or ever)

import xml.etree.ElementTree as etree
#import sys # for argv
from nm import per_week

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
    
    
    # Publicly accessable class variables that hold the results (current)
    lives_per_week = None
    new_clients_per_week = None
    premium_per_week = None
    
    # Publicly accessable class variables that hold the results (historical)
    lives_per_week_hist = None
    new_clients_per_week_hist = None
    premium_per_week_hist = None
    
    # Publicly accessable delta class variables
    d_lives_last_week = None
    d_nc_last_week = None
    d_premium_last_week = None
    
    # Benchmark values
    # Benchmark = Goal / 52 (weeks per year)
    lives_per_week_benchmark = None
    new_clients_per_week_benchmark = None
    premium_per_week_benchmark = None
    
  
    def __init__(self, xml_file, xml_file_hist=None):
        # If the xml_file_hist is None, don't print the comparisons, just the data for this week.
              
        # validate the current and historical report xml file
        path_and_filename = self._validate_xml_file(xml_file)
        if xml_file_hist is not None: path_and_filename_hist = self._validate_xml_file(xml_file_hist)
               
        # Parse the xml
        # Get the etree object
        root = self._get_root(path_and_filename)
        if xml_file_hist is not None: root_hist = self._get_root(path_and_filename_hist)
        # DEBUG Print root tree for hist xml file
        print('root_hist={}'.format(root_hist))
        
        # Get the xml namespace from the first tag. Include the braces.
        # As far as I know, the xmlns will be the same for all the xml files.
        xmlns = root.tag.split('}')[0] + '}'
       
        # Monthly Activity & Ratio Report (maarr) info that are needed for my weekly reports
        # is called "BusinessActivity2". I don't currently use any of the other info.
        maarr = root.find(xmlns + 'BusinessActivity2')
        if xml_file_hist is not None: maarr_hist = root_hist.find(xmlns + 'BusinessActivity2')
            
        # Get the current lives goal and data
        lives_goal = float(maarr.get(self._get_fieldname_from_dict('Placed Lives Goal Data')))
        lives_placed = float(maarr.get(self._get_fieldname_from_dict('Placed Lives Total Data')))
        nc_goal = float(maarr.get(self._get_fieldname_from_dict('Placed NC Goal Data')))
        nc_placed = float(maarr.get(self._get_fieldname_from_dict('Placed NC Total Data')))
        prem_goal = float(maarr.get(self._get_fieldname_from_dict('Placed Annual Premium Goal Data')))
        prem_placed = float(maarr.get(self._get_fieldname_from_dict('Placed Annual Premium Total Data')))

        # Get the historical lives goal and data
        if xml_file_hist is not None: 
            lives_goal_hist = float(maarr_hist.get(self._get_fieldname_from_dict('Placed Lives Goal Data')))
            lives_placed_hist = float(maarr_hist.get(self._get_fieldname_from_dict('Placed Lives Total Data')))
            nc_goal_hist = float(maarr_hist.get(self._get_fieldname_from_dict('Placed NC Goal Data')))
            nc_placed_hist = float(maarr_hist.get(self._get_fieldname_from_dict('Placed NC Total Data')))
            prem_goal_hist = float(maarr_hist.get(self._get_fieldname_from_dict('Placed Annual Premium Goal Data')))
            prem_placed_hist = float(maarr_hist.get(self._get_fieldname_from_dict('Placed Annual Premium Total Data')))
        
        # calculate the lives, nc, and prem needed per week. (current)
        lives_pw = per_week(lives_goal, lives_placed)
        nc_pw = per_week(nc_goal, nc_placed)
        prem_pw = per_week(prem_goal, prem_placed)
        
        # calculate the lives, nc, and prem needed per week. (historical)
        if xml_file_hist is not None: 
            lives_pw_hist = per_week(lives_goal_hist, lives_placed_hist)
            nc_pw_hist = per_week(nc_goal_hist, nc_placed_hist)
            prem_pw_hist = per_week(prem_goal_hist, prem_placed_hist)
        
        # Calculate the lives, nc, and prem per week benchmarks.
        self.lives_per_week_benchmark = lives_goal / 52
        self.new_clients_per_week_benchmark = nc_goal / 52
        self.premium_per_week_benchmark = prem_goal / 52
        
        # Not calculating historical benchmarks right now because I'm not tracking historicial goal changes.
                
        # Set the results to the publically available vars (current)
        self.lives_per_week = lives_pw
        self.new_clients_per_week = nc_pw
        self.premium_per_week = prem_pw
        
        # Set the results to the publically available vars (historical)
        if xml_file_hist is not None: 
            self.lives_per_week_hist = lives_pw_hist
            self.new_clients_per_week_hist = nc_pw_hist
            self.premium_per_week_hist = prem_pw_hist
            self.d_lives_last_week = lives_placed - lives_placed_hist
            self.d_nc_last_week = nc_placed - nc_placed_hist
            self.d_premium_last_week = prem_placed - prem_placed_hist
            
            
        
        
        
    
    def _validate_xml_file(self, xml_file):
        """ TODO: This function should validation, on both the current and historical xml files.
        """

        # The initial xml file is required now, so this should probably just do validations now...
        path_and_filename = xml_file
        
        # TODO: Perhaps Verify the file is the correct type, etc. here.
        
        return path_and_filename
        

        
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
    