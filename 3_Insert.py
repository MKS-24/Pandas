import pandas as pd
#  list ka Structure hota hai horizontal
#  Dictionary ka Structure hota hai vertical
var = pd.DataFrame([[1,2,3,4],[5,6,7,8]] , index=['A','B'])
print(var,end='\n\n\n')

var.insert(1,'New1', ['New','Value'])   # (index , Col_Name , values)
print(var,end='\n\n\n')

var.insert(3,'New2', [9,9])   # (index , Col_Name , values)
print(var,end='\n\n\n')
var.insert(5,'New3', var[3])   
print(var,end='\n\n\n')

var = pd.DataFrame([[1,2,3,4],[5,6,7,8],[1,1,1,1],[2,2,2,2]] , index=['A','B','C','D'])
print(var,end='\n\n')

var['python'] = var[2][0:2].fillna(0)  # jabbhi nan aaega colume me tu wo us colum ko float banadega
print(var) # isme mene ye chaha hai ke new col me col 2 ke 0 se 1 tak ka data only copy hojae

