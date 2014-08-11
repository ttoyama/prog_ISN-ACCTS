import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

import extract_2

soup = extract_2.soup_dict

data = DataFrame(soup)
data = data.T

print data.info()
print data['source_register'].value_counts()

def after_str(data):
    patterns = ['Planned Sample Size: ', 'UK Sample Size: ', 'More than ', 'Total ']
    for pattern in patterns:
        pattern_1 = '('+ pattern + ')([0-9]+)'
        print   data['target_size'][data['target_size'].str.contains(pattern)].tail()
        temp  = data['target_size'][data['target_size'].str.contains(pattern)]
        temp2 = temp.str.findall(pattern_1).str[0].str[1]
        for i in temp.index:
            data['target_size'].ix[i] = temp2.ix[i]

def before_str(data):
    patterns = [' patients to be recruited', ' \(212 by end of recruitment']
    for pattern in patterns:
        pattern_1 = '([0-9]+)('+ pattern + ')'
        print   data['target_size'][data['target_size'].str.contains(pattern)].tail()
        temp  = data['target_size'][data['target_size'].str.contains(pattern)]
        temp2 = temp.str.findall(pattern_1).str[0].str[0]
        for i in temp.index:
            data['target_size'].ix[i] = temp2.ix[i]

after_str(data)
before_str(data)