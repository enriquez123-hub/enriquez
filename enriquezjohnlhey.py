# Pokémon Lore System

class Pokemon:
    def __init__(self, name, type_, lore):
        self.name = name
        self.type_ = type_
        self.lore = lore

    def display_info(self):
        return f"Name: {self.name}\nType: {self.type_}\nLore: {self.lore}\n"

class Pokedex:
    def __init__(self):
        self.pokemon_list = {}

    def add_pokemon(self, name, type_, lore):
        if name in self.pokemon_list:
            print(f"{name} already exists in the Pokédex!")
        else:
            self.pokemon_list[name] = Pokemon(name, type_, lore)
            print(f"{name} has been added to the Pokédex!")

    def get_pokemon(self, name):
        pokemon = self.pokemon_list.get(name)
        if pokemon:
            return pokemon.display_info()
        else:
            return f"{name} is not in the Pokédex."

    def list_pokemon(self):
        if not self.pokemon_list:
            return "The Pokédex is empty!"
        return "\n".join([pokemon.display_info() for pokemon in self.pokemon_list.values()])


pokedex = Pokedex()

pokedex.add_pokemon("Pikachu", "Electric", "Pikachu is known as the Mouse Pokémon. It stores electricity in its cheeks.")
pokedex.add_pokemon("Charizard", "Fire/Flying", "Charizard's fiery breath can melt anything. It is very loyal to its trainer.")
pokedex.add_pokemon("Bulbasaur", "Grass/Poison", "Bulbasaur has a plant seed on its back. It grows as it absorbs sunlight.")


print(pokedex.get_pokemon("Pikachu"))
print(pokedex.list_pokemon())
