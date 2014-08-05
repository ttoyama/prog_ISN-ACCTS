from BeautifulSoup import BeautifulSoup as bs
from BeautifulSoup import BeautifulStoneSoup as bss
from BeautifulSoup import Tag, NavigableString
import re
import csv

f = open("xml/ICTRP-Results_saro.xml", "r")
f_data = f.readlines()
#delete data after scientific titlech   

items =['internal_number', 'trialid', 'last_refreshed_on', 
'public_title', 'scientific_title', 'primary_sponsor', 
'date_registration', 'source_register', 'web_address', 
'recruitment_status', 'other_records', 'inclusion_gender', 
'date_enrollement', 'target_size', 'study_type', 
'study_design', 'inclusion_criteria', 'exclusion_criteria', 
'condition', 'intervention', 'primary_outcome', 'secondary_id']

def make_trial_soup():
    xml = ''.join(f_data)
    soup  = bs(xml)
    ssoup = bss(xml)

    trial_soup = [] #each item of list is BeautifulSoup
    for i in soup('trial'):
        j = bs(str(i))
        trial_soup.append(j)
    return trial_soup


def make_noblank():
    result = {}
    for i in range(len(trial_soup)):
        for item in items:
            if trial_soup[i](item) == []:
                tag1  = Tag(trial_soup[i], item)
                text1 = NavigableString('NA')
                trial_soup[i].insert(0, tag1)
                tag1.insert(0, text1)
#        result[i] = {
#            item : trial_soup[i](item)[0].text
#        }





trial_soup = make_trial_soup()
make_noblank()

#if __name__ == '__main__':
    #text_output()
    #text_min_output()
    #make_csv()
    #make_pdf()