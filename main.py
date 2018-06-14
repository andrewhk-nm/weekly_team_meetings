""" Main module for my weekly report functions.
"""



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
    root = get_root(path_and_filename)
    # Get the xml namespace from the first tag. Include the braces.
    xmlns = '{' + root.tag.split('}')[0].strip('{') + '}'
    print('root={}'.format(root))

    # CB Monthly Activites and Ratios XML Structure
    # Are these text box name### fields consistent between reports?
	#	Based on 6/4 & 6/12, they are consistent.
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
	
    # Create a dictionary of the Textbox fields as shown above.
    dict_of_fields = get_dict_of_fields()
    
    textbox_test = root.find(xmlns + 'BusinessActivity2').get(dict_of_fields['Placed Annual Premium Goal Data'])
    print('textbox_test attrib={}'.format(textbox_test))
    
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
    lives_goal = float(maarr.get(dict_of_fields['Placed Lives Goal Data']))
    lives_placed = float(maarr.get(dict_of_fields['Placed Lives Total Data']))
    nc_goal = float(maarr.get(dict_of_fields['Placed NC Goal Data']))
    nc_placed = float(maarr.get(dict_of_fields['Placed NC Total Data']))
    prem_goal = float(maarr.get(dict_of_fields['Placed Annual Premium Goal Data']))
    prem_placed = float(maarr.get(dict_of_fields['Placed Annual Premium Total Data']))
    
    # print the data I extracted
    print(lives_goal)
    print(lives_placed)
    print(nc_goal)
    print(nc_placed)
    print(prem_goal)
    print(prem_placed)
    
    # calculate the lives, nc, and prem needed per week.
    lives_pw = per_week(lives_goal, lives_placed)
    nc_pw = per_week(nc_goal, nc_placed)
    prem_pw = per_week(prem_goal, prem_placed)
    
    print(lives_pw)
    print(nc_pw)
    print(prem_pw)
    

    # Don't automatically exit when finished.
    input('Press <ENTER> to exit')
