import pandas as pd

var = pd.DataFrame([["Khuzaima", "Rafay"],["03213798935", "03123456789"],["mksprogramify@gmail.com", "rafayanwar07@gmail.com"],["Male", "Male"]],index=["Full Name", "Contact No", "Email Address", "Gender"])
print(var)

var.to_csv("Hamara_Data.csv")
var.to_csv("Hamara_Data_Remove_Index.csv", index=False)
var.to_csv("Hamara_Data_Change_Header.csv", index=False, header=["Detail 1", "Detail 2"])



var = pd.DataFrame(
    {
        "Name": ["Khuzaima", "Rafay"],
        "Number": ["03213798935", "03123456789"],
        "Email": ["mksprogramify@gmail.com", "rafayanwar07@gmail.com"],
        "Gender": ["Male", "Male"],
    }
)

print(var) 

var.to_csv("Dic_Hamara_Data.csv", index=False) 
var.to_csv("Dic_Hamara_Data_Remove_Index.csv", index=False) 
var.to_csv("Dic_Hamara_Data_Change_Header.csv",index=False,header=["Full Name", "Contact No", "Email Address", "Gender"])  
