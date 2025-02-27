import pandas as pd

csv1 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx')
print(csv1)


# Get Only Index
print(csv1.index)

# Get colume
print(csv1.columns)



# Function
print(csv1.describe())   # Apply Only for Numeric data
# 25% (Q1) = 38.00 → 25% data is value se chhota ya barabar hai.
# 50% (Median/Q2) = 81.00 → Middle value, aadha data chhota, aadha bara hai.
# 75% (Q3) = 454.75 → 75% data is value se chhota ya barabar hai.
# Mean (Average) = 823.42 → Saari values ka average hai.
# Min = 6 → Sabse chhoti value.
# Max = 5499 → Sabse bari value.
# Standard Deviation (std) = 1594.80 → Data ka variation zyada hai.



#  ager fixed ammount a data show kerwana hai tu top se
print(csv1.head(2))


#  ager fixed ammount a data show kerwana hai tu bottom se
print(csv1.tail(5),end='\n\n\n\n')

#  ager specific row tak kaa data show kerwana hai tu slicing kare ge 
print(csv1[5:10]) # means 5 se 9 tak ka data show kerwana chata humme
print(type(csv1))
print(csv1.index.array)
print(csv1.index.array.astype(str))
print(csv1.index.array.astype(float))
print(csv1.index.array.astype(int))



# convert in transpose
print(csv1.transpose()) # for transpose
print(csv1)


# print(csv1.to_clipboard()) # for clipboard 
csv1.to_clipboard()  # for copy paste

# For Html 
print(csv1.to_html())  # html text me paste kerde ga

print(csv1.to_dict())  # convert in dictionary

csv1.to_feather('data.feather')  # data ko binary me convert kerta hai for fast assessing
x = pd.read_feather('E:/4_Pandas/data.feather')
print(x)

#  convert into numpy
print(csv1.to_numpy())

# or
import numpy as np
# Both method are work same
v = np.asarray(csv1)
print(v)



# for decending order
print(csv1.sort_index(axis=0,ascending=False))  # axis 0 mean row ke respect se sort kerrahe and 1 ka mean colume ke respect  
print(csv1.sort_index(axis=1,ascending=False))  # axis 0 mean row ke respect se sort kerrahe and 1 ka mean colume ke respect


# for changing data in csv
print(csv1)
csv1['Email'][0] = 'Change hogaya'  # [col_name][Row_Number]   # aik method ye hai jo warning bhi saath deta hai
print(csv1)

#  Other Method
csv1.loc[0,'Email'] = 'Best way me chage Hogaya' # without Warning
print(csv1)


# Ager specific data ko get kerna hai tu
print(csv1.loc[[2,5,0],['Name','Number']])  # [[list of row jo chahiye] , [List of Colume jinme se chahiye]]
 
print(csv1.loc[:,['Name','Number']])  # [: , [List of Colume jinme se chahiye]]     => : for sb row
print(csv1.loc[[2,6],:])  # [[list of row jo chahiye] , [List of Colume jinme se chahiye]]

#  by using iloc method to get data
print(csv1.iloc[0,1])   # [row_no , colume_no jiska data chahiye] index number hone chahiye


# for drop any data
print(csv1.drop('Email',axis=1))  # for delete colume axis 1
print(csv1)
# for drop specific row
print(csv1.drop(1,axis=0)) # row 1 delete hogai 
