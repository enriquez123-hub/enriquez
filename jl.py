# Enhanced Pokémon Lore System

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
        """Add a new Pokémon to the Pokédex."""
        name = name.title()
        if name in self.pokemon_list:
            return f"{name} already exists in the Pokédex!"
        self.pokemon_list[name] = Pokemon(name, type_, lore)
        return f"{name} has been added to the Pokédex!"

    def get_pokemon(self, name):
        """Retrieve a Pokémon by name."""
        name = name.title()
        pokemon = self.pokemon_list.get(name)
        if pokemon:
            return pokemon.display_info()
        return f"{name} is not in the Pokédex."

    def list_pokemon(self):
        """List all Pokémon in the Pokédex."""
        if not self.pokemon_list:
            return "The Pokédex is empty!"
        return "\n".join([pokemon.display_info() for pokemon in self.pokemon_list.values()])

    def search_by_type(self, type_):
        """Search for Pokémon by type."""
        type_ = type_.title()
        results = [pokemon.display_info() for pokemon in self.pokemon_list.values() if type_ in pokemon.type_]
        return "\n".join(results) if results else f"No Pokémon found with type: {type_}"

    def update_lore(self, name, new_lore):
        """Update the lore of a Pokémon."""
        name = name.title()
        if name in self.pokemon_list:
            self.pokemon_list[name].lore = new_lore
            return f"{name}'s lore has been updated!"
        return f"{name} is not in the Pokédex."

    def remove_pokemon(self, name):
        """Remove a Pokémon from the Pokédex."""
        name = name.title()
        if name in self.pokemon_list:
            del self.pokemon_list[name]
            return f"{name} has been removed from the Pokédex."
        return f"{name} is not in the Pokédex."

if __name__ == "__main__":
    pokedex = Pokedex()

    print(pokedex.add_pokemon("Pikachu", "Electric", "Pikachu is known as the Mouse Pokémon. It stores electricity in its cheeks."))
    print(pokedex.add_pokemon("Charizard", "Fire/Flying", "Charizard's fiery breath can melt anything. It is very loyal to its trainer."))
    print(pokedex.add_pokemon("Bulbasaur", "Grass/Poison", "Bulbasaur has a plant seed on its back. It grows as it absorbs sunlight."))

    print("\n--- Retrieving Pokémon ---")
    print(pokedex.get_pokemon("Pikachu"))
    print(pokedex.get_pokemon("Eevee"))

    print("\n--- Listing All Pokémon ---")
    print(pokedex.list_pokemon())

    print("\n--- Searching by Type ---")
    print(pokedex.search_by_type("Electric"))
    print(pokedex.search_by_type("Water"))

    print("\n--- Updating Lore ---")
    print(pokedex.update_lore("Pikachu", "Pikachu generates powerful electricity and shares a deep bond with its trainer."))
    print(pokedex.get_pokemon("Pikachu"))

    print("\n--- Removing Pokémon ---")
    print(pokedex.remove_pokemon("Bulbasaur"))
    print(pokedex.list_pokemon())
