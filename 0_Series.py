import pandas as pd

# 1d data structure


arr = [1,2,3,4]
var = pd.Series(arr)
print(var)
print(type(var))
print(var[2])

#  For Changing index

var = pd.Series(arr,index=['*','*','*','*']) #jitne index honge utne index change kerwana honge
print(var)
print(type(var))
print(var['*'])

var = pd.Series(arr,index=['*','a','b','c']) #jitne index honge utne index change kerwana honge
print(var)
print(type(var))
print(var['*'])

var = pd.Series(arr,index=['*','a','b','c'],dtype='str') #jitne index honge utne index change kerwana honge
print(var)
print(type(var))
print(var['*'])

var = pd.Series(arr,index=['*','a','b','c'],dtype='float') #data type bhi change kersakhte hai set ki
print(var)
print(type(var))
print(var['*'])

var = pd.Series(arr,index=['*','a','b','c'],dtype='float',name='khan') #data type bhi change kersakhte hai set ki
print(var)
print(type(var))
print(var['*'])

new = {
    "name" : ['python' , 'c' , 'c++' , 'java'],
    'pou' : [12,13,14,15],
    'rank':[1,4,5,2]
}
print(new,end='\n\n\n\n')
var1 = pd.Series(new)
print(var1)


new2 = {
    2 : 1,
    22 : 1,
    222 : 1
}
print(pd.Series(new2))
print(type(pd.Series(new2)))

new2 = { 
    (2,): [12, 13, 14, 15],   # tuple banane ke liye kerna perta hai    ->  t1 = (2) # Yeh integer hai,  -> t2 = (2,) # Yeh tuple hai
    (22,): [12, 13, 14, 15],
    (222,): [12, 13, 14, 15]
}

print(pd.Series(new2))


print(pd.Series((1,2,2,3,4)))
print(pd.Series((1)))
print(pd.Series((1,2.4)))
print(pd.Series((1,'2.4')))



# pandas me ager series me int howa tu dtype int show kare ga
# pandas me ager series me 1 bhi float howa tu dtype float show kare ga
# pandas me ager series me 1 bhi str howa tu dtype object show kare ga
# pandas me ager series me mix data type howa tu dtype object show kare ga


x = pd.Series(6,index=[1,2,3,4,5,6,7])  # multiple block banadega
print(x)


y = pd.Series(5,index=[1,2,3])
print(x+y)  # series me hum koi bhi operation tab perform ker sakhte hai jab dono set me same numberof data hota hai jabke panda aapko wo bhi kerdeta hai or jaha usse operattion ke kiye nh milta tu wo not a number show kerta hai
y = pd.Series(4,index=[99,9,9,9,99,99,9,9])
print(x+y)
print(x.add(y, fill_value=0)) # 0 for Numeric data  ager index match nh kerte tu ye aese print hojae ge apne index ke saath seperately

x = pd.Series('a',index=[1,2,3])
print(x)
y = pd.Series('b',index=[1,2,3])
print(x+y)
y = pd.Series('b',index=[99,99,99,99])
print(x+y)
print(x.add(y,fill_value=''))
 
a = pd.Series(['a','b','c','d',5])
b = pd.Series([2,7,'z',5])
print(a.astype(str)+b.astype(str))   # ye pehle string me convert kare ga data ko than concatinate kare ga
print(a+b) # error aaega QK same nh hai data ki types

# indexing ke through operation perform kerta hai