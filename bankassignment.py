data        age          job  marital  ... previous poutcome  deposit
0       59       admin.  married  ...        0  unknown      yes
1       56       admin.  married  ...        0  unknown      yes
2       41   technician  married  ...        0  unknown      yes
3       55     services  married  ...        0  unknown      yes
4       54       admin.  married  ...        0  unknown      yes
...    ...          ...      ...  ...      ...      ...      ...
11157   33  blue-collar   single  ...        0  unknown       no
11158   39     services  married  ...        0  unknown       no
11159   32   technician   single  ...        0  unknown       no
11160   43   technician  married  ...        5  failure       no
11161   34   technician  married  ...        0  unknown       no

[11162 rows x 17 columns]
null age          False
job          False
marital      False
education    False
default      False
balance      False
housing      False
loan         False
contact      False
day          False
month        False
duration     False
campaign     False
pdays        False
previous     False
poutcome     False
deposit      False
dtype: bool
0        1
1        1
2        1
3        1
4        1
        ..
11157    0
11158    0
11159    0
11160    0
11161    0
Name: deposit, Length: 11162, dtype: int64
       age          job  marital  ... pdays  previous deposit
0       59       admin.  married  ...    -1         0       1
1       56       admin.  married  ...    -1         0       1
2       41   technician  married  ...    -1         0       1
3       55     services  married  ...    -1         0       1
4       54       admin.  married  ...    -1         0       1
...    ...          ...      ...  ...   ...       ...     ...
11157   33  blue-collar   single  ...    -1         0       0
11158   39     services  married  ...    -1         0       0
11159   32   technician   single  ...    -1         0       0
11160   43   technician  married  ...   172         5       0
11161   34   technician  married  ...    -1         0       0

[11162 rows x 14 columns]
['admin.' 'technician' 'services' 'management' 'retired' 'blue-collar'
 'unemployed' 'entrepreneur' 'housemaid' 'unknown' 'self-employed'
 'student']
['married' 'single' 'divorced']
['secondary' 'tertiary' 'primary' 'unknown']
['yes' 'no']
['no' 'yes']
['may' 'jun' 'jul' 'aug' 'oct' 'nov' 'dec' 'jan' 'feb' 'mar' 'apr' 'sep']
x: [[59 'admin.' 'married' ... 1 -1 0]
 [56 'admin.' 'married' ... 1 -1 0]
 [41 'technician' 'married' ... 1 -1 0]
 ...
 [32 'technician' 'single' ... 2 -1 0]
 [43 'technician' 'married' ... 2 172 5]
 [34 'technician' 'married' ... 1 -1 0]]
y: [1 1 1 ... 0 0 0]
[[1.0 0.0 0.0 ... 1 -1 0]
 [1.0 0.0 0.0 ... 1 -1 0]
 [0.0 0.0 0.0 ... 1 -1 0]
 ...
 [0.0 0.0 0.0 ... 2 -1 0]
 [0.0 0.0 0.0 ... 2 172 5]
 [0.0 0.0 0.0 ... 1 -1 0]]
xtest [[-0.35506564 -0.46571851 -0.16329932 ... -0.51893725  2.62409874
   0.62465525]
 [-0.35506564 -0.46571851 -0.16329932 ... -0.51893725  1.30248101
   1.63872661]
 [-0.35506564 -0.46571851 -0.16329932 ... -0.17189116 -0.46885387
  -0.38941612]
 ...
 [-0.35506564 -0.46571851 -0.16329932 ... -0.17189116 -0.46885387
  -0.38941612]
 [ 2.81638066 -0.46571851 -0.16329932 ... -0.51893725 -0.46885387
  -0.38941612]
 [-0.35506564 -0.46571851 -0.16329932 ... -0.17189116 -0.46885387
  -0.38941612]]
ypred [0 1 0 ... 1 0 0]
ytest [0 1 0 ... 1 1 0]
0.7944469323779668

[Program finished]