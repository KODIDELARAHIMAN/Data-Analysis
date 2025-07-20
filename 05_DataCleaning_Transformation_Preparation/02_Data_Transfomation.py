
import pandas as pd

import numpy as np

data = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"], "k2": [1, 1, 2, 3, 3, 4, 4]})

data
Out[4]: 
    k1  k2
0  one   1
1  two   1
2  one   2
3  two   3
4  one   3
5  two   4
6  two   4
""" duplicated - method in DataFrame identifies duplicate rows"""
Out[5]: ' duplicated - method in DataFrame identifies duplicate rows'

## returns a boolean series(true/false) , each value indicates whether the corresponding row is a duplicate.

data.duplicated()
Out[7]: 
0    False
1    False
2    False
3    False
4    False
5    False
6     True
dtype: bool

### drop_duplicates - returns a DataFrame with rows where the duplicated array is False filtered out.

data.drop_duplicates()
Out[9]: 
    k1  k2
0  one   1
1  two   1
2  one   2
3  two   3
4  one   3
5  two   4

## by default both moethods check for duplicated across all columns.

## you can optionally specify a subset of columns to focus the duplicate check., eg: to detect duplicates based on "k1" column - pass subset=['k1'] to the method.

data['v1'] = range(7)

data
Out[13]: 
    k1  k2  v1
0  one   1   0
1  two   1   1
2  one   2   2
3  two   3   3
4  one   3   4
5  two   4   5
6  two   4   6

data.drop_duplicates(subset=['k1'])
Out[14]: 
    k1  k2  v1
0  one   1   0
1  two   1   1

## duplicated and drop_duplictes by default keep the first observed value combination. Passing "keep='last'" wil lreturn the last one

data.drop_duplicates(['k1', 'k2'], keep='last')
Out[16]: 
    k1  k2  v1
0  one   1   0
1  two   1   1
2  one   2   2
3  two   3   3
4  one   3   4
6  two   4   6

""" Transforming Data using a Functions or Mapping """
Out[17]: ' Transforming Data using a Functions or Mapping '

## To transform data based on values in an array. Series, or DataFrame column, you can apply ustom logic to each element - such as in a dataset tracking different types of meat.

data = pd.DataFrame({"food" : ["bacon", "pulled chicken", "bacon","pastrami", "corned beek", "bacon", "pastrami", "honey ham", "nova lox"], "ounces":[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

data
Out[20]: 
             food  ounces
0           bacon     4.0
1  pulled chicken     3.0
2           bacon    12.0
3        pastrami     6.0
4     corned beek     7.5
5           bacon     8.0
6        pastrami     3.0
7       honey ham     5.0
8        nova lox     6.0

## to indicate the source animal for each meat type, create a mapping that links each distinct meat to its corresponding animal. 

meat_to_animal = {
  "bacon": "pig",
  "pulled pork": "pig",
  "pastrami": "cow",
  "corned beef": "cow",
  "honey ham": "pig",
  "nova lox": "salmon"
}

## map - method on a Series accepts a function or dictionary-like object containing a mapping to do the transformation of values.



data["animal"] = data["food"].map(meat_to_animal)

data
Out[25]: 
             food  ounces  animal
0           bacon     4.0     pig
1  pulled chicken     3.0     NaN
2           bacon    12.0     pig
3        pastrami     6.0     cow
4     corned beek     7.5     NaN
5           bacon     8.0     pig
6        pastrami     3.0     cow
7       honey ham     5.0     pig
8        nova lox     6.0  salmon

## we could also have passed a function that does all work.

def get_animal(x):
    return meat_to_animal[x]
    



data["food"].map(get_animal)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[28], line 1
----> 1 data["food"].map(get_animal)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\series.py:4711, in Series.map(self, arg, na_action)
   4631 def map(
   4632     self,
   4633     arg: Callable | Mapping | Series,
   4634     na_action: Literal["ignore"] | None = None,
   4635 ) -> Series:
   4636     """
   4637     Map values of Series according to an input mapping or function.
   4638 
   (...)
   4709     dtype: object
   4710     """
-> 4711     new_values = self._map_values(arg, na_action=na_action)
   4712     return self._constructor(new_values, index=self.index, copy=False).__finalize__(
   4713         self, method="map"
   4714     )

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\base.py:925, in IndexOpsMixin._map_values(self, mapper, na_action, convert)
    922 if isinstance(arr, ExtensionArray):
    923     return arr.map(mapper, na_action=na_action)
--> 925 return algorithms.map_array(arr, mapper, na_action=na_action, convert=convert)

File ~\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\algorithms.py:1743, in map_array(arr, mapper, na_action, convert)
   1741 values = arr.astype(object, copy=False)
   1742 if na_action is None:
-> 1743     return lib.map_infer(values, mapper, convert=convert)
   1744 else:
   1745     return lib.map_infer_mask(
   1746         values, mapper, mask=isna(values).view(np.uint8), convert=convert
   1747     )

File pandas/_libs/lib.pyx:2999, in pandas._libs.lib.map_infer()

Cell In[27], line 2, in get_animal(x)
      1 def get_animal(x):
----> 2     return meat_to_animal[x]

KeyError: 'pulled chicken'

def get_animal(x):
    return meat_to_animal.get(x, None)
    

data["food"].map(get_animal)
Out[30]: 
0       pig
1      None
2       pig
3       cow
4      None
5       pig
6       cow
7       pig
8    salmon
Name: food, dtype: object

import pandas as pd

data = pd.read_csv("C:\Users\y55364\Desktop\Patching_Projects\Projects_Docs\DB2_Team_Incidents.csv")

data
  Cell In[31], line 3
    data = pd.read_csv("C:\Users\y55364\Desktop\Patching_Projects\Projects_Docs\DB2_Team_Incidents.csv")
                       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


print(data.head())
             food  ounces animal
0           bacon     4.0    pig
1  pulled chicken     3.0    NaN
2           bacon    12.0    pig
3        pastrami     6.0    cow
4     corned beek     7.5    NaN

%runfile C:/Users/y55364/Documents/Python/untitled0.py --wdir
  File <unknown>:10
    data = pd.read_csv("C:\Users\y55364\Desktop\Patching_Projects\Projects_Docs\DB2_Team_Incidents.csv")
                       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


%runfile C:/Users/y55364/Documents/Python/untitled0.py --wdir
  File <unknown>:10
    data = pd.read_csv("C:\Users\y55364\Desktop\Patching_Projects\Projects_Docs\DB2_Team_Incidents.csv")
                       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


data.head(5)
Out[35]: 
             food  ounces animal
0           bacon     4.0    pig
1  pulled chicken     3.0    NaN
2           bacon    12.0    pig
3        pastrami     6.0    cow
4     corned beek     7.5    NaN


""" Replacing Values """ 
Out[42]: ' Replacing Values '

## Filling in missing data with fillna method is a special case of more general value replacement. As  you already seen map can be used to modify a subset of values in an object, but replace provides a simpler and more flexible way to do so.

data = pd.Series([1., -999., 2., -999., -1000., 3.])

data
Out[45]: 
0       1.0
1    -999.0
2       2.0
3    -999.0
4   -1000.0
5       3.0
dtype: float64



## The -999 might be sentinel valeus for missing data. To replace these with NA values that pandas understands, we can use replace, producing a new Series.

data.replace(-999., np.nan)
Out[47]: 
0       1.0
1       NaN
2       2.0
3       NaN
4   -1000.0
5       3.0
dtype: float64

## If you want to replace multiple values at once, you instead pass a list and then substitute values. 

data.replace([-999., -1000], np.nan)
Out[49]: 
0    1.0
1    NaN
2    2.0
3    NaN
4    NaN
5    3.0
dtype: float64

## To use a different replacement for each value, pass a list of substitutes.

data.replace([-999, -1000], [np.nan, 0])
Out[51]: 
0    1.0
1    NaN
2    2.0
3    NaN
4    0.0
5    3.0
dtype: float64

## The argument passed can be a dictionary.

data.replace({-999: np.nan, -1000:0})
Out[53]: 
0    1.0
1    NaN
2    2.0
3    NaN
4    0.0
5    3.0
dtype: float64

##### The data.replace method is distinct from data.str.replace which performs element wise string substitution. 

""" Renaming Axis Indexex """
Out[55]: ' Renaming Axis Indexex '

## Like values in Series axis labels can be similarly transformed by a function or mapping of some form to produce new, differenlty labled objects. you can also modify the axes in place without creating a new data structure.

data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=["Ohio","Colorado","New York"], columns=["one", "two", "three", "four"])

def transform(x):
    return x[:4].upper()
    

data.index.map(transform)
Out[59]: Index(['OHIO', 'COLO', 'NEW '], dtype='object')

## you can assign to the index attribute, modifying the DataFrame 

data.index = data.index.map(transform)

data
Out[62]: 
      one  two  three  four
OHIO    0    1      2     3
COLO    4    5      6     7
NEW     8    9     10    11



## if you want to create a transformed version of a dataset without modifying the original, a useful method is rename


data.rename(index=str.title, columns=str.upper)
Out[65]: 
      ONE  TWO  THREE  FOUR
Ohio    0    1      2     3
Colo    4    5      6     7
New     8    9     10    11

## Notably rename can be used in conjuction with a dictionary like object prpviding new values for a subset of the axis lables.



data.rename(index={"OHIO":"INDIANA"}, columns={"three":"peekaboo"})
Out[68]: 
         one  two  peekaboo  four
INDIANA    0    1         2     3
COLO       4    5         6     7
NEW        8    9        10    11

## rename saves you from the chore of copying the DataFrame manually and assiging new valeus to its index and columsn attributes.

""" Discretization and Binning" 
""
"""
Out[70]: ' Discretization and Binning" \n""\n'



## Continuous data is often grouped into dicrete bins for analysis, such as categorizing people in a study into age ranges.

ages = [20, 22, 25, 26, 21, 27, 24, 23, 37, 31, 61, 45, 41, 32]

##Group continous age data into custom bins - 18-25, 26-35, 36-60 and 61+ using pandas.cut for easier analysis.

bins = [18, 25, 35, 60, 100]

age_categories = pd.cut(ages, bins)

age_categories
Out[76]: 
[(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
Length: 14
Categories (4, interval[int64, right]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]

## pandas returns a special categorized object that describes the bins computed by pandas.cut, where each bin is represented bu a unique interval indicating its lower and upper limits. 

age_categories.codes
Out[78]: array([0, 0, 0, 1, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)

age-categories.categories
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[79], line 1
----> 1 age-categories.categories

NameError: name 'age' is not defined

age_categories.categories
Out[80]: IntervalIndex([(18, 25], (25, 35], (35, 60], (60, 100]], dtype='interval[int64, right]')


pd.value_counts(age_categories)
C:\Users\y55364\AppData\Local\Temp\ipykernel_9144\3010498523.py:1: FutureWarning: pandas.value_counts is deprecated and will be removed in a future version. Use pd.Series(obj).value_counts() instead.
  pd.value_counts(age_categories)
Out[84]: 
(18, 25]     6
(25, 35]     4
(35, 60]     3
(60, 100]    1
Name: count, dtype: int64

## pd.value-counts(categories) gives the count of values in each bin create by pandas.cut; in interval notation paranthesis mean open (exclusive) and square brackets  mean closed(inclusive) you can switch side is closed by setting right=False

pd.cut(ages, bins, right=False)
Out[86]: 
[[18, 25), [18, 25), [25, 35), [25, 35), [18, 25), ..., [25, 35), [60, 100), [35, 60), [35, 60), [25, 35)]
Length: 14
Categories (4, interval[int64, left]): [[18, 25) < [25, 35) < [35, 60) < [60, 100)]

## you can override the default interval based bin labelling by passing a list or array to the labels. 

group_names = ["youth", "youngadult", "MiddleAged", "Senior"]

pd.cut(ages, bins, labels=group_names)
Out[90]: 
['youth', 'youth', 'youth', 'youngadult', 'youth', ..., 'youngadult', 'Senior', 'MiddleAged', 'MiddleAged', 'youngadult']
Length: 14
Categories (4, object): ['youth' < 'youngadult' < 'MiddleAged' < 'Senior']
