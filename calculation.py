import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

import extract_2

soup = extract_2.soup_dict

data = DataFrame(soup)

data2 = data.stack().swaplevel(0, 1).unstack()
data2.head()