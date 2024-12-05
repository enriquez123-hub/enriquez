import json

class Pokemon:
    def __init__(self, name, type_, lore, abilities=None, evolution=None):
        self.name = name
        self.type_ = type_
        self.lore = lore
        self.abilities = abilities or []  
        self.evolution = evolution       

    def display_info(self):
        abilities = ", ".join(self.abilities) if self.abilities else "None"
        evolution = self.evolution if self.evolution else "None"
        return (
            f"Name: {self.name}\n"
            f"Type: {self.type_}\n"
            f"Lore: {self.lore}\n"
            f"Abilities: {abilities}\n"
            f"Evolution: {evolution}\n"
        )

class Pokedex:
    def __init__(self):
        self.pokemon_list = {}

    def add_pokemon(self, name, type_, lore, abilities=None, evolution=None):
        """Add a new Pokémon with additional attributes."""
        name = name.title()
        if name in self.pokemon_list:
            return f"{name} already exists in the Pokédex!"
        self.pokemon_list[name] = Pokemon(name, type_, lore, abilities, evolution)
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

    def search_by_ability(self, ability):
        """Search Pokémon by ability."""
        results = [
            pokemon.display_info()
            for pokemon in self.pokemon_list.values()
            if ability.title() in pokemon.abilities
        ]
        return "\n".join(results) if results else f"No Pokémon found with ability: {ability}"

    def save_to_file(self, filename="pokedex.json"):
        """Save the Pokédex data to a JSON file."""
        data = {
            name: {
                "type": pokemon.type_,
                "lore": pokemon.lore,
                "abilities": pokemon.abilities,
                "evolution": pokemon.evolution,
            }
            for name, pokemon in self.pokemon_list.items()
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        return f"Pokédex saved to {filename}."

    def load_from_file(self, filename="pokedex.json"):
        """Load the Pokédex data from a JSON file."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            for name, details in data.items():
                self.pokemon_list[name] = Pokemon(
                    name,
                    details["type"],
                    details["lore"],
                    details.get("abilities"),
                    details.get("evolution"),
                )
            return f"Pokédex loaded from {filename}."
        except FileNotFoundError:
            return f"File {filename} not found!"
        except json.JSONDecodeError:
            return "Error: File is not a valid JSON file!"

if __name__ == "__main__":
    pokedex = Pokedex()

    print(pokedex.add_pokemon(
        "Pikachu", "Electric", 
        "Pikachu generates electricity from its cheeks.", 
        abilities=["Static", "Lightning Rod"], 
        evolution="Raichu"
    ))

    print(pokedex.add_pokemon(
        "Charmander", "Fire", 
        "Charmander's tail flame shows its vitality.", 
        abilities=["Blaze", "Solar Power"], 
        evolution="Charmeleon -> Charizard"
    ))

    print(pokedex.add_pokemon(
        "Bulbasaur", "Grass/Poison", 
        "Bulbasaur grows with sunlight.", 
        abilities=["Overgrow"], 
        evolution="Ivysaur -> Venusaur"
    ))

    print("\n--- Retrieving Pokémon ---")
    print(pokedex.get_pokemon("Pikachu"))

    print("\n--- Searching by Ability ---")
    print(pokedex.search_by_ability("Blaze"))

    print("\n--- Saving to File ---")
    print(pokedex.save_to_file())

    print("\n--- Loading from File ---")
    new_pokedex = Pokedex()
    print(new_pokedex.load_from_file())
    print(new_pokedex.list_pokemon())
