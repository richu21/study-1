import pandas as pd

t = {
    "Name": ["appu","abin","krishna","rahul"],
    "age" : [10,20,30,40]

}
dt = pd.DataFrame(t)

for label in dt.index : 
    if dt.loc[label,"age"] > 20:
        print(dt.loc[label])