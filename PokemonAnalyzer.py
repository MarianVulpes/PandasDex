import pandas as pd

class PokemonAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def type_combinations_percentage(self):
        type_combinations = self.df.groupby(['Type 1', 'Type 2']).size().reset_index(name='Count')
        total_rows = len(self.df)
        type_combinations['Percentage'] = (type_combinations['Count'] / total_rows) * 100
        type_combinations = type_combinations.sort_values(by='Percentage', ascending=False)
        return type_combinations
    
    def top_5_status(self, status):
        top_5_highest = self.df.nlargest(5, status)
        top_5_lowest = self.df.nsmallest(5, status)
        return top_5_highest, top_5_lowest
    
    def top_5_average_status(self, *stats):
        averages = self.df[list(stats)].mean(axis=1)
        top_5_highest_indices = averages.nlargest(5).index
        top_5_lowest_indices = averages.nsmallest(5).index
        top_5_pokemon_highest = self.df.loc[top_5_highest_indices, 'Name']
        top_5_pokemon_lowest = self.df.loc[top_5_lowest_indices, 'Name']
        top_5_averages_highest = averages[top_5_highest_indices]
        top_5_averages_lowest = averages[top_5_lowest_indices]
        highest_df = pd.DataFrame({'Name': top_5_pokemon_highest, 'Average': top_5_averages_highest})
        lowest_df = pd.DataFrame({'Name': top_5_pokemon_lowest, 'Average': top_5_averages_lowest})
        return highest_df, lowest_df


df = pd.read_excel('dex.xlsx')
analyzer = PokemonAnalyzer(df)

def display_menu():
    print("\nEscolha a função que deseja utilizar:")
    print("1. Porcentagem de combinações de tipos (Type 1 e Type 2)")
    print("2. Top 5 Pokémon com MAIOR e MENOR de um status específico")
    print("3. Top 5 Pokémon com MAIOR e MENOR média entre 2 ou 3 status escolhidos")
    print("4. Sair do programa")


if __name__ == '__main__':
    while True:
        display_menu()
        choice = input("Digite o número da função desejada: ")

        if choice == '1':
            print("\nPorcentagem de combinações de tipos (Type 1 e Type 2):")
            print(analyzer.type_combinations_percentage())
        elif choice == '2':
            stats = input("Qual status gostaria de verificar? \nHP, Attack, Defense, Sp. Atk, Sp. Def, Speed\nResposta: ")
            highest, lowest = analyzer.top_5_status(stats)
            print(f"\nTop 5 Pokémon com MAIOR {stats}:")
            print(highest[['Name', stats]])
            print(f"\nTop 5 Pokémon com MENOR {stats}:")
            print(lowest[['Name', stats]])
        elif choice == '3':
            stats = input("Quais status gostaria de verificar? Separe por vírgula (Ex: HP, Attack, Defense)\nResposta: ").split(', ')
            highest, lowest = analyzer.top_5_average_status(*stats)
            print(f"\nTop 5 Pokémon com MAIOR média entre {', '.join(stats)}:")
            print(highest)
            print(f"\nTop 5 Pokémon com MENOR média entre {', '.join(stats)}:")
            print(lowest)
        elif choice == '4':
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida. Por favor, selecione uma opção válida.")

        restart = input("\nDeseja recomeçar? (Yes/No): ")
        if restart.lower() != 'yes':
            print("Saindo do programa...")
            break