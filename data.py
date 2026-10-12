import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Name": ["Arun", "Bharath", "Charan", "Divya", "Esha",
             "Farhan", "Gita", "Hari", "Isha", "Kiran"],
    "Maths": [85, 72, 90, 65, 95, 55,21, 88, 60, 82],
    "Science": [88, 75, 92, 70, 22, 60, 80, 85, 68, 79],
    "English": [78, 80, 33, 75, 90, 65, 82, 33, 72, 84],
    
}




df = pd.DataFrame(data, index = range(1,len(data["Name"]) +1))

print("Data Befere analysis :")
print(df)
print()


