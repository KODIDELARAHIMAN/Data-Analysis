import pandas as pd
import numpy as np

float_data = pd.Series([1.2, -3.5, np.nan, 0])
print(float_data)

0    1.2
1   -3.5
2    NaN
3    0.0
dtype: float64

float_data.isna()
Out[3]: 
0    False
1    False
2     True
3    False
dtype: bool

## Pandas uses the term "NA" (Not Applicable or Not Available), adopted from R, to refer to missing data

## NA can represent data that does not exists or data that wan not observed due to collection issues. 

## Analyzing missing data itself is important for identifying collection problems or biases. 

## The built-in Python value None is also treated as NA with in pandas.

string_data = pd.Series(['aardvark',np.nan, None, 'avacado'])

string_data
Out[9]: 
0    aardvark
1         NaN
2        None
3     avacado
dtype: object

string_data.isna()
Out[10]: 
0    False
1     True
2     True
3    False
dtype: bool

float_data = pd.Serires([1, 2, None], dtype='float64')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[11], line 1
----> 1 float_data = pd.Serires([1, 2, None], dtype='float64')

AttributeError: module 'pandas' has no attribute 'Serires'

float_data = pd.Series([1, 2, None], dtype='float64')

float_data
Out[13]: 
0    1.0
1    2.0
2    NaN
dtype: float64

float_data.isna()
Out[14]: 
0    False
1    False
2     True
dtype: bool

## The pandas library aims to provide consistent handling of missing data across different daata types.

## Utility funcitions like pandas.isna simplify the process by hiding many complex details. 

## dropna = Removes labels from an axis if their associated values contain missing data. with options to set thresholds for the amount of missing data allowed. 

## fillna = Replace missing values with specified value or fills them in using techniques like forward fill(ffill) or backward fill(bfill).

## isna = Returns a Boolean mask, indicating which entries are missing.

## notna = The opposite of isna; returns True for valid entries and False for missing ones. 

"""Filtering Out Missing Data"""
Out[21]: 'Filtering Out Missing Data'

data = pd.Series([1, np.nan, 3.5, np.nan, 7])

data.dropna()
Out[23]: 
0    1.0
2    3.5
4    7.0
dtype: float64

data
Out[24]: 
0    1.0
1    NaN
2    3.5
3    NaN
4    7.0
dtype: float64

## data.dropna() is the same thing as below code does. 

data[data.notna()]
Out[26]: 
0    1.0
2    3.5
4    7.0
dtype: float64

## With DataFrame objects, there are different ways to remove missing data. You want to drop rows or columsn that are all NA, or only those rows or columns containing an NAs at all. 

## dropna by default drops any row containg a missing value. 

data = pd.DataFrame([[1., 6.5, 3.],[1., np.nan, np.nan], 
                     [np.nan, np.nan, np.nan],[np.nan, 6.5, 3.]])

data
Out[30]: 
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0

data.dropna()
Out[31]: 
     0    1    2
0  1.0  6.5  3.0

## passing how='all' will drop only rows only that are all NA

data.dropna(how='all')
Out[33]: 
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
3  NaN  6.5  3.0

## keep in mind that these functions return new objects by default and do not modify the content of the original object.

## To drop columns in the same way, pass axis='columns':

data[4] = np.nan

data
Out[37]: 
     0    1    2   4
0  1.0  6.5  3.0 NaN
1  1.0  NaN  NaN NaN
2  NaN  NaN  NaN NaN
3  NaN  6.5  3.0 NaN

data.dropna(axis='columns', how='all')
Out[38]: 
     0    1    2
0  1.0  6.5  3.0
1  1.0  NaN  NaN
2  NaN  NaN  NaN
3  NaN  6.5  3.0

## suppose you want to keep only rows containg at most certain number of missing observations . you can indicate this with the thresh argument:

df = pd.DataFrame(np.random.standard_normal((7, 3))
)

df.iloc(:4, 1] = np.nan
  Cell In[41], line 1
    df.iloc(:4, 1] = np.nan
                 ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('


df.iloc[:4, 1] = np.nan

dfiloc[:2, 2] = np.nan
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[43], line 1
----> 1 dfiloc[:2, 2] = np.nan

NameError: name 'dfiloc' is not defined

df.iloc[:2, 2] = np.nan

df
Out[45]: 
          0         1         2
0  0.176199       NaN       NaN
1  1.283496       NaN       NaN
2  0.974225       NaN -0.177675
3  0.299587       NaN  0.707916
4  0.632928  1.354868  0.369141
5 -0.825649  0.371573  2.787654
6 -0.475148 -0.211633  0.069243

df.dropna()
Out[46]: 
          0         1         2
4  0.632928  1.354868  0.369141
5 -0.825649  0.371573  2.787654
6 -0.475148 -0.211633  0.069243

df.dropna(thresh=2)
Out[47]: 
          0         1         2
2  0.974225       NaN -0.177675
3  0.299587       NaN  0.707916
4  0.632928  1.354868  0.369141
5 -0.825649  0.371573  2.787654
6 -0.475148 -0.211633  0.069243

"""Filling in Missing data"""
Out[48]: 'Filling in Missing data'

## Instead of Just removing missing data - which might result in losing other valuable data - you can choose to fill in the gaps

## The fillna method is the primary tool in pandas for this purpose. 

## using fillna with a constant value will substitute missing entires with that constant.

df.fillna(0)
Out[52]: 
          0         1         2
0  0.176199  0.000000  0.000000
1  1.283496  0.000000  0.000000
2  0.974225  0.000000 -0.177675
3  0.299587  0.000000  0.707916
4  0.632928  1.354868  0.369141
5 -0.825649  0.371573  2.787654
6 -0.475148 -0.211633  0.069243

## Calling fill na({1: 0.5, 2:0])

## Calling fillna with dictionary  - you can use a fill value for each column

df.fillna({1:0.5, 2:0])
  Cell In[55], line 1
    df.fillna({1:0.5, 2:0])
                         ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'


df.fillna({1:0.5, 2:0})
Out[56]: 
          0         1         2
0  0.176199  0.500000  0.000000
1  1.283496  0.500000  0.000000
2  0.974225  0.500000 -0.177675
3  0.299587  0.500000  0.707916
4  0.632928  1.354868  0.369141
5 -0.825649  0.371573  2.787654
6 -0.475148 -0.211633  0.069243

## The same interpolation methods available for reindexing can be used with fillna

df = pd.DataFrame(np.random.standard_normal((6, 3)))

df.iloc[2:, 1] = np.nan

df.iloc[4:, 2] = np.nan

df
Out[61]: 
          0         1         2
0 -1.663484  0.297558  0.279483
1  0.181642 -0.530689 -0.153841
2 -0.665401       NaN  0.570692
3 -0.086307       NaN -0.492008
4  1.387779       NaN       NaN
5  1.518471       NaN       NaN

df.fillna(method='ffill')
C:\Users\y55364\AppData\Local\Temp\ipykernel_1800\1193302488.py:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df.fillna(method='ffill')
Out[62]: 
          0         1         2
0 -1.663484  0.297558  0.279483
1  0.181642 -0.530689 -0.153841
2 -0.665401 -0.530689  0.570692
3 -0.086307 -0.530689 -0.492008
4  1.387779 -0.530689 -0.492008
5  1.518471 -0.530689 -0.492008

df.fillna(method='ffill', limit=2)
C:\Users\y55364\AppData\Local\Temp\ipykernel_1800\2719175769.py:1: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df.fillna(method='ffill', limit=2)
Out[63]: 
          0         1         2
0 -1.663484  0.297558  0.279483
1  0.181642 -0.530689 -0.153841
2 -0.665401 -0.530689  0.570692
3 -0.086307 -0.530689 -0.492008
4  1.387779       NaN -0.492008
5  1.518471       NaN -0.492008

## with ffill you can do lots of other things such as simple data manipulation using the median or mean statistics. 

data=pd.Series([1, np.nan, 3.5, np.nan, 7])

data.fillna(data.mean())
Out[66]: 
0    1.000000
1    3.833333
2    3.500000
3    3.833333
4    7.000000
dtype: float64

data
Out[67]: 
0    1.0
1    NaN
2    3.5
3    NaN
4    7.0
dtype: float64

### calulating mean 

1 + 3.5 + 7
Out[69]: 11.5

11.5/3
Out[70]: 3.8333333333333335

## fillna function arguments

# value  - scalar value or dictionary like object to use to fill missing values

# method - interpolation method : one of 'bfill' or 'ffill'. 

# axis = axis to fill on (index or column ) default is axis='index'

# limit = for forward and backward filling, maximum number of consecutinve periods to fill.