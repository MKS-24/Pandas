import pandas as pd

var = pd.DataFrame(
    {
        'A' : (1,2,3,4,5),
        'B' : (5,4,3,2,1),
        'C' : (1,5,9,7,5),
        'D' : (3,5,7,9,5)
    }
)
var.Name = "khan"
print(var,end='\n\n')
print(var.Name,end='\n\n')

print(var.pop('B'),end='\n\n')

var = pd.DataFrame([[1,2,3,4,5],[5,4,3,2,1],[9,5,7,4,2],[4,6,5,3,7]],index=['a','b','c','d'])
print(var,end='\n\n')

print(var.pop(2))  # name bhi dikhae ga 2 QK @ col ko delete kiya hai

del var[3] # another way of delete
print(var)

var[4] = pd.Series(dtype='float64') # another way of delete
# var = var.drop(columns=[4])  # another way of delete
print(var)

