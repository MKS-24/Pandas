import pandas as pd
#  Operation between dataframe column
var = pd.DataFrame({
    'A' : [10,12,30,40],
    'B' : [5,6,7,8]
})

var['Sum'] = var['A'] + var['B']
print(var)
var['Subtraction'] = var['A'] - var['B']
print(var)
var['Division'] = var['A'] / var['B']
print(var)
var['DivInt'] = var['A'] // var['B']
print(var)
var['Power'] = var['A'] ** var['B']
print(var)
var['Product'] = var['A'] * var['B']
print(var)

var['<20'] = var['A'] < 20  # for applying condition
print(var)



n = pd.DataFrame([[1,2,3],[1,7,8,2]])
print(n)
n['sum'] = n[0] + n[1] + n[2]
print(n,end='\n\n\n')

