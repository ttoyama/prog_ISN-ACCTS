from BeautifulSoup import BeautifulSoup as bs
from BeautifulSoup import BeautifulStoneSoup as bss
from BeautifulSoup import Tag, NavigableString
import re
import csv
import codecs
import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series

f = open("xml/ICTRP-Results.xml", "r")
f_data = f.readlines()
#delete data after scientific titlech   

items =['internal_number', 'trialid', 'secondary_id',
'source_register', 'web_address', 
'date_registration', 'date_enrollement', 'last_refreshed_on', 
'public_title', 'scientific_title', 'primary_sponsor', 
'recruitment_status', 'other_records', 'inclusion_gender', 
'target_size', 'study_type', 
'study_design', 'inclusion_criteria', 'exclusion_criteria', 
'condition', 'intervention', 'primary_outcome']

#Change 'internal_number' into 'INTERNAL NUMBER'
def make_title_item(source):
    result = []
    regex1 = re.compile('_')
    for i in source:
        i = regex1.sub(' ', i)
        i = i.upper()
        result.append(i)
    return result

def make_trial_soup():
    xml = ''.join(f_data)
    soup  = bs(xml)
    ssoup = bss(xml)

    trial_soup = [] #each item of list is BeautifulSoup
    for i in ssoup('trial'):
        j = bs(str(i))
        trial_soup.append(j)
    return trial_soup

#Delete blank from soup
def make_noblank(soup_with_blank):
    result = []
    for i in range(len(soup_with_blank)):
        for item in items:
            if soup_with_blank[i](item) == []:
                tag1  = Tag(soup_with_blank[i], item)
                text1 = NavigableString('NA')
                soup_with_blank[i].insert(0, tag1)
                tag1.insert(0, text1)
                #print 'found blanks!!!'

            if  ('<target_size>\n<study_type>' in soup_with_blank[i](item)[0].prettify()) == True:
                #if some content is blank, they include following tags
                tag1  = Tag(soup_with_blank[i], item)
                text1 = NavigableString('NA')
                soup_with_blank[i].insert(0, tag1)
                tag1.insert(0, text1)
                #print i, item, 'found target!!'


        result.append(soup_with_blank[i])
    return result

def make_soup_dic(soup):
    result = {}
    for i in range(len(soup)):
        trial = {}
        for item in items:
            trial[item] = soup[i](item)[0].text
        result[i] = trial
    return result


def reshape(soup_dict):
    #regex_space = re.compile('   +')
    regex_ltbrgt = re.compile('&lt;br&gt;')
    regex_andgt = re.compile('&gt;')
    regex_feed = re.compile('\n')
    regex_doublen = re.compile('\n\n+')

    for i in range(len(soup_dict)):
        for item in items:
            pre_reshape = soup_dict[i][item]
            pre_reshape = pre_reshape.strip()
            pre_reshape = regex_ltbrgt.sub('\n', pre_reshape)
            pre_reshape = regex_andgt.sub('>', pre_reshape)
            pre_reshape = regex_doublen.sub('\n', pre_reshape)
            pre_reshape = regex_feed.sub('\n    ', pre_reshape)
            pre_reshape = pre_reshape.rstrip('\n')
            soup_dict[i][item] = pre_reshape


def make_text(soup_dict):
    f = codecs.open('output/output.txt', 'w', encoding='utf-8')
    for i in soup_dict:
        obj = "="*25 + "%03d" %(i+1) + "="*25 +"\n"
        for i in range(len(items)):
            obj += title_items[i] + ': ' + soup_dict[i][items[i]] + '\n'
        f.write(obj)
        f.write('\n')
    f.close()

def make_text_from_df(df):
    f = codecs.open('output/output_2.txt', 'w', encoding='utf-8')
    for i in df.index:
        obj = "="*25 + "%03d" %(i+1) + "="*25 +"\n"
        for j in range(len(items)):
            obj += title_items[j] + ': '
            obj += '%s' %df.ix[i,items[j]]
            obj += '\n'
        f.write(obj)
        f.write('\n')
    f.close()


title_items = make_title_item(items)
trial_soup = make_trial_soup()
trial_soup = make_noblank(trial_soup)
soup_dict = make_soup_dic(trial_soup)
reshape(soup_dict)
make_text(soup_dict)

#create dataframe from soup_dict and make .txt
df = DataFrame(soup_dict)
df = df.T
df = df.drop_duplicates().reset_index()
make_text_from_df(df)



#if __name__ == '__main__':
    #text_output()
    #text_min_output()
    #make_csv()
    #make_pdf()