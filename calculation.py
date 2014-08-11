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