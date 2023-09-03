import pandas as pd

data = pd.DataFrame({"Name": ["alice", "marcolon", "muneca"], "Age": [1, 2, 3], "Country": ['texaS', 'LIMA', 'MAMANI']})

data.to_csv("dates.csv", index=False)

print(data)