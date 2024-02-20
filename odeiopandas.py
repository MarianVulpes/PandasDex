import pandas as pd

df = pd.read_excel('dex.xlsx') #Lê o arquivo xlsx

type_combinations = df.groupby(['Type 1', 'Type 2']).size().reset_index(name='Count')
total_rows = len(df)
type_combinations['Percentage'] = (type_combinations['Count'] / total_rows) * 100
type_combinations = type_combinations.sort_values(by='Percentage', ascending=False)

print("\nPorcentagem de combinações de tipos (Type 1 e Type 2):")
print(type_combinations)