import pandas as pd

t=[1,2,3,4,5]

sr = pd.Series(t)
print(type(sr))
print(sr)
print(sr[3])
print("-------")
sr[3] = 10
print(sr)