import pypokedex
import pandas as pd
import numpy as np

class Pokedex:
    def __init__(self):
        self.Pokedex = np.arange(1, 1025)
        
    def write_pokemon(self, filename):
        data = []
        
        for num in self.Pokedex:
            info = self.get_by_dex(int(num))
            print(info)
            data.append(info)
        
        columns = ['Dex', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
        df = pd.DataFrame(data, columns=columns)
        
        df.to_excel(filename, index=False)
        print(f"Arquivo '{filename}' salvo com sucesso.")

    def get_by_dex(self, num):
        assert isinstance(num, int), "Dex must be an integer"
        pok = pypokedex.get(dex=num)
        name = pok.name
        return self.get_poke(name=name)

    def get_poke(self, name: str):
        assert isinstance(name, str), "Name must be a string"
        p = pypokedex.get(name= name)
        dex = p.dex
        name = name.capitalize()
        types = p.types
        if types:
            first_type = types[0]

            second_type = types[1] if len(types) > 1 else None
        hp = p.base_stats.hp
        attack = p.base_stats.attack
        defense = p.base_stats.defense
        sp_atk = p.base_stats.sp_atk
        sp_def = p.base_stats.sp_def      
        speed = p.base_stats.speed
        return [dex, name, first_type, second_type, hp, attack, defense, sp_atk, sp_def, speed]

poke = Pokedex()
poke.write_pokemon("dex.xlsx")