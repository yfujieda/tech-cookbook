import pandas as pd

# data = {'Toyota':["Corolla", "Camry", "Tacoma", "RAV4"], 
# 'Honda': ["Civic", "Accord", "Pilot", "CR-V"]}

data = {'Toyota':["Rav4", "Camry", "Tacoma", "Corolla"]}


df = pd.DataFrame(data)
print(df)

print(df.sort_values(['Toyota'], ascending=True))
