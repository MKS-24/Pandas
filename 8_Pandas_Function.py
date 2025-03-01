import pandas as pd
csv = pd.read_excel('E:\\4_Pandas\\Dropna_fillna.xlsx')
print(csv)


# Ager me us data ko drop kerwana chata hu ke jis bhi row me koi colum ki value nan means empty hu tu dropna
print(csv.dropna(axis=0)) # ye row ke respect se complete row ko delete kerta hai
#  By default axis 0 hta means row hota


# for colume prespective
print(csv.dropna(axis=1)) # wo saare colume delete hojaege jinme nan mean empty hogi koi bhi value

print(csv)
print(csv.dropna(how='any')) # same as dropna() QK by default any hota hai dropna
print(csv.dropna(how='all')) # ab ager me chata hu ke wo data remove hojae jis me all value nan ya zero hu tu,      # Row = 7 gayab hogai hai ab QK sb col me (nan nan nan) hai


print(csv.dropna(subset=['Name']))  # ye sirf un nan wale data ko remove kare ga jo Name colume ke ander koi bhi value nan hogi         # row 7 gayab hogi QK only name colume me 7th row ka data empty hai


print(csv.dropna(thresh=1)) # Kam az kam 1 non-NaN value ho, warna row delete
print(csv.dropna(thresh=2)) # Kam az kam 2 non-NaN values ho, warna row delete



#  Ager me all nan value ko kisi se replace kerna chahu tu
print(csv.fillna('Khali'))




#  Ager me all nan value ko kisi se replace kerna chahu tu
print(csv.fillna({      # har colume ki nan value ko kisi chez se replace kerna
    'Email' : 'khalimail',
    'Name' : 'DekhoKalli'      # Number ke col ko mene kisi se change nh kiya tu wo nan hi show kare ga
}))


print(csv.fillna({      # har colume ki nan value ko kisi chez se replace kerna
    0 : 'khalimail',      # Colume ko index ke use se call kerke change ker diya
    1 : 'DekhoKalli'      # Number ke col ko mene kisi se change nh kiya tu wo nan hi show kare ga
}))



#  Ab jo nan value hai me chahta hu ke nan apne previous data se change hojae tu 
print(csv.fillna(method='bfill'))  #for backword filling (bottom se top)   ye pehle use kiya jata tah
print(csv.fillna(method='ffill'))  #for Forward filling  (top se bottom)   ye pehle use kiya jata tah
print(csv.ffill()) #for Forward filling  (top se bottom)
print(csv.bfill()) #for Backward filling  (top se bottom)

print(csv.bfill(axis=1))  #for backword filling (bottom se top)   ab column wise left to right fill hoga 
print(csv.fillna(method='ffill',axis=1))  #for Foeward filling  (top se bottom)     ab column wise left to right fill hoga   ye other way hai lekin warning de sakhta hai
print(csv.ffill(axis=1))  #for backword filling (bottom se top)   ab column wise right to left fill hoga 


# csv.dropna(inplace=True) # ye kerta ye hai csv = csv.dropna()
# print(csv)


# csv.fillna('any value',inplace=True) # ye kerta ye hai csv = csv.fillna('any value')  and nan me 'any value' daaldiya
# print(csv)


print("\n\n",csv.fillna('"khali"',limit=3))  # means her colume me 3 nan value tak hi change kerdu or indexing limit ki 1 se chalti hai