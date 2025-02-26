# 2d data structure

import pandas as pd


lst=[1,2,3,4,5,6]
arr = pd.DataFrame(lst)
print(type(arr))
print(arr)

# lst2 = {
#     11 :'Saeed',
#     17 :'Abdul Rafay',
#     19 :'Muneeb',
#     27 :'Abdul Rehman',
#     29 :'Khuzaima'
# }

# lst2 = {
#     'a' : [1,2,3,4,5],    # length of data must be same
#     'b' : [1,2,3,4,5,6] # abhi error dega QK data me 1 value zyada hai
# }
# var = pd.DataFrame(lst2)
# print(var)

dic = {
    'a' : [1,2,3,4,5],    # length of data must be same
    'b' : [10,20,30,40,0], # abhi error nh dega QK both datas equal hai
    'c' : [5,4,4,1,9],
    'd' : [-5,4,40,1,9],
}
var = pd.DataFrame(dic)
print(var)
print(type(arr))

var = pd.DataFrame(dic,columns=['c','a'])
print(var)
print(type(arr))

print(var['c'][3])
var.loc[3, 'c'] = 64  # a.loc[row, column] Ye 100% original DataFrame ko modify karega
print(var['c'][3],end='\n\n')
print(var,end='\n\n')
print(var.at[3, 'c'])  # Fastest way to access a single value  vrr[col_name][Row_name]


var = pd.DataFrame(dic,columns=['c','a'],index=['*','/','//','+','-']) # Name parameter dataframe me nh use hota #index tu kuch bhi desakhte hai na boss
print(var)   # yaha per 64 isiye nh aaya c ke colume me QK new data frame banaya hai
print(type(arr))

# List of List ka Data Frame
l = [[1,2,3,4,5],[6,7,8,40,50]]
a = pd.DataFrame(l)  
print(a)
print(type(a))
print(a[4][0])  # a[col_name][Row_name]

a.loc[0, 4] = 0.5  # a.loc[row, column] Row index 0 aur column index 4 per value assign ki
print(a[4][0])  # Column 4, Row 0 ki value print ki # chota se error is waja se aaega QK integer data me float ko assign kerrahe hai
print(a) 
a = pd.DataFrame(l,dtype = 'float') # chota se error ab nh aaega QK integer data list ki data type badal ker float kerdi

print(a)
print(type(a))
print(a[4][0])  # a[col_name][Row_name]

a.loc[0, 4] = 0.5  # a.loc[row, column] Row index 0 aur column index 4 per value assign ki
print(a[4][0])  # Column 4, Row 0 ki value print ki
print(a)

a = pd.DataFrame(l,dtype = 'str') # chota se error ab nh aaega QK integer data list ki data type badal ker float kerdi

print(a)
print(type(a))
print(a[4][0])  # a[col_name][Row_name]

a.loc[0, 4] = 0.5  # a.loc[row, column] Row index 0 aur column index 4 per value assign ki
print(a[4][0])  # Column 4, Row 0 ki value print ki
print(a)



#  Date dame created by using series

sr = {
    's' : pd.Series([1,2,3,4]), 
    'g' : pd.Series([5,7,6,5])
    }
print(pd.DataFrame(sr))


sr = {
    's' : pd.Series([1,2,3,4]), 
    'g' : pd.Series([5,7,6,5,6,5])
    }
print(pd.DataFrame(sr)) #Jab Pandas NaN (Not a Number) insert karta hai, to poori column ki data type float

