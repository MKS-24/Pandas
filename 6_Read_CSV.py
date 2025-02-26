import pandas as pd

csv = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx')


print(csv) # Yeh Pandas ko force karega ke saara data show kare
# print(csv.to_string())  # ye complete data show nh kerraha QK data zyada hai isliye ye truncate kerraha hai
 
# koi specific row print kerne keliye
csv2 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',nrows=3)
print(csv2)
print(type(csv2))




csv3 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',usecols=['Name','Email'])  # multiples colume
print(csv3)
print(type(csv3))

csv3 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',usecols=['Name']) # Single colume
print(csv3.to_string())
print(type(csv3))

csv3 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',usecols=[0]) # colume By Using Index
print(csv3.to_string())
print(type(csv3))



csv4 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',skiprows=[x for x in range(10) if x%2 == 0]) 
print(csv4.to_string())
print(type(csv4))

csv4 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',skiprows=[0,1,2,4,5]) 
print(csv4.to_string())
print(type(csv4))

csv4 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',skiprows=[1]) 
print(csv4.to_string())
print(type(csv4))



csv5 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',index_col='Name',usecols=['Name','Email'])  # index ager kisi orr colume ko banana hai tu 
print(csv5.to_string())
print(type(csv5))



csv6 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',header=4)  # ager kisi row ko header banana chata hu tu row number dedu isse hogaya ye ke header tu ban gaya saat row number se pehle wala saara data gayab
print(csv6.to_string())
print(type(csv6))




csv7 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',names=['EN','N'])  # Main header ka name change kerne ke liye use hota hai and name different use karo tu acha hai werna confussion hogi
print(csv7.to_string())
print(type(csv7))


csv7 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',names=['N','N'])  # Main header ka name change kerne ke liye use hota hai and name different use karo tu acha hai werna confussion hogi
print(csv7.to_string())
print(type(csv7))
