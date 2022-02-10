import pyclip
import re

#For when you have to grab a bunch of common field values from pages quickly and don't have api access for proper automation.
#Copy the desired page to your clipboard
class scrapers:
    cb_data = pyclip.paste()
    #This function adapts nicely for grabbing several specific fields from pages quickly for use elsewhere. 
    def field_grabs(cb_data):
        #created an empty dictionary for key value pairs
        supported_fields = {}
        try:
            field_value1_list = re.findall(r'(<=field_name1: ).*(?=\n)',cb_data)
            #Using findall when searching for a field that I only expect find one result for allows me to use index 0 for my try block and return N/A if it doesn't find a value
            supported_fields["field_name1"] = str(field_value1_list[0])
        except:
            supported_fields["field_name1"] = 'N/A'
        try:
            field_value2_list = re.findall(r'(<=field_name2: ).*(?=\n)',cb_data)
            supported_fields["field_name2"] = str(field_value2_list[0])
        except:
            supported_fields["field_name2"] = 'N/A'
        try:
            field_value3_list = re.findall(r'(<=field_name3: ).*(?=\n)',cb_data)
            supported_fields["field_name3"] = str(field_value3_list[0])
        except:
            supported_fields["field_name3"] = 'N/A'
        # Repeat the try/excepts for as many fields as you need to return. 
        # return a dictionary of key value pairs
        return supported_fields

    #what if there there are multiple groups of text with the same fields and you want to capture from each group just from the text
    #without having to get into overly complex regex, we can just grab text chunks and loop the existing function above.
    def field_groups(cb_data,field_grabs):
        supported_field_groups = []
        # GROUP_HEADER_TEXT is just my way of indicating what text comes right before the group of fields you're trying to grab. 
        # Same for GROUP_FOOTER_TEXT, except it's the section right after your group. 
        # We'll use compile in this situation to allow us to use the DOTALL flag necessary to grab the entire text chunk and ignore whitespace and new lines
        groups_re = re.compile(r'(?<=GROUP_HEADER_TEXT).+?(?=GROUP_FOOTER_TEXT)',re.DOTALL)
        groups = re.findall(groups_re,cb_data)
        for group in groups:
            supported_fields = field_grabs(group)
            supported_field_groups.append(supported_fields)
        #return a list of dictionaries 
        return supported_field_groups
