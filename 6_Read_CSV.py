import pandas as pd

csv = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx')


print(csv) # Yeh Pandas ko force karega ke saara data show kare
# print(csv.to_string())  # ye complete data show nh kerraha QK data zyada hai isliye ye truncate kerraha hai
 
# koi specific row print kerne keliye
csv2 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',nrows=3) # 3 rows ko print kare ga start ki
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
print(type(csv7),end='\n\n\n')

# Ab ager koi aesi file aajae jis ka header nh hu ya delete hogaya hu and first row ko header nh banana hu tu 
csv8 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',header=None)  # Main header ka name change kerne ke liye use hota hai and name different use karo tu acha hai werna confussion hogi
print(csv8.to_string())  # abhi jo header tah initially wo ab as a row show hoga
print(type(csv8))

# For CSV file not for excell Prefix se name diya jatahai col1 , col2 kerke jo aap header = none se header generate kerte hu
# csv8 = pd.read_csv('E:/4_Pandas/Certificates Creation.xlsx',header=None,prefix='col')  # Main header ka name change kerne ke liye use hota hai and name different use karo tu acha hai werna confussion hogi
# print(csv8.to_string())  # abhi jo header tah initially wo ab as a row show hoga
# print(type(csv8))


# for excell file 
csv8 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',header=None)  
# csv8.columns = ['col'+ str(i) for i in range(1,3)]
csv8.columns = [f'col{i}' for i in range(3)]
print(csv8.to_string())  
print(type(csv8))



# kisi colume ki datatype change kerni hu tu tu dictionary banker change karo ge like below
csv9 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',dtype={'Number':'float'})  # Number ki datatype joke integer thi wo change kerke float kerdi  
print(csv9.to_string())  
print(type(csv9))


csv9 = pd.read_excel('E:/4_Pandas/Certificates Creation.xlsx',dtype={'Number':'str'})  # Number ki datatype joke integer thi wo change kerke string kerdi  
print(csv9.to_string())  
print(type(csv9))