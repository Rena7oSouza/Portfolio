using System.Formats.Asn1;
using System.Runtime.CompilerServices;

public class TamagotchiView
{
    public void Title()
    {
        Console.WriteLine(@"

   ___      _                         _____                                  _       _     _ 
  / _ \___ | | ___ __ ___   ___  _ __/__   \__ _ _ __ ___   __ _  __ _  ___ | |_ ___| |__ (_)
 / /_)/ _ \| |/ / '_ ` _ \ / _ \| '_ \ / /\/ _` | '_ ` _ \ / _` |/ _` |/ _ \| __/ __| '_ \| |
/ ___/ (_) |   <| | | | | | (_) | | | / / | (_| | | | | | | (_| | (_| | (_) | || (__| | | | |
\/    \___/|_|\_\_| |_| |_|\___/|_| |_\/   \__,_|_| |_| |_|\__,_|\__, |\___/ \__\___|_| |_|_|
                                                                 |___/                       


");
    }
    public string Name()
    {
        string name = "";
        while (name == "")
        {
            Console.WriteLine("What's your name?");
            name = Console.ReadLine();
        }
        return name;
    }

    public string Menu(string name)
    {
        string answer = "";
        Console.WriteLine("\n\n-------------Menu-------------\n");
        Console.WriteLine(name + ", what do you want?\n 1 - Get a Pokémon\n 2 - See your Pokémon\n 3 - Exit");
        while (answer != "1" && answer != "2" && answer != "3")
        {
            answer = Console.ReadLine().ToString();
            if (answer != "1" && answer != "2" && answer != "3")
            {
                Console.WriteLine("\nInvalid Option! Please select again \n 1 - Get a Pokémon\n 2 - See your Pokémon\n 3 - Exit");
            }
        }
        return answer;
    }

    public string GetPokemon(string name)
    {
        string answer = "";
        Console.WriteLine("\n\n---------Get Pokémon----------\n");
        Console.WriteLine(name + ", which one do you choose?\n 1 - Bulbasaur\n 2 - Charmander\n 3 - Squirtle");

        while (answer != "1" && answer != "2" && answer != "3")
        {
            answer = Console.ReadLine().ToString();
            if (answer != "1" && answer != "2" && answer != "3")
            {
                Console.WriteLine("\nInvalid Option! Please select again \n 1 - Bulbasaur\n 2 - Charmander\n 3 - Squirtle");
            }
        }
        return answer;
    }
    public string pokemonMenu(string name, string pokemonName)
    {
        string answer = "";
        Console.WriteLine("\n------------------------------\n");
        Console.WriteLine(name + $", what do you want?\n 1 - More info about {pokemonName}\n 2 - Catch {pokemonName}\n 3 - Back");
        while (answer != "1" && answer != "2" && answer != "3")
        {
            answer = Console.ReadLine().ToString();
            if (answer != "1" && answer != "2" && answer != "3")
            {
                Console.WriteLine("\nInvalid Option! Please select again \n 1 More info about{pokemonName}\n 2 - Catch {pokemonName}\n 3 Back");
            }
        }
        return answer;
    }
    public void PokemonInfo(Pokemon pokemon)
    {
        Console.WriteLine("------------------------------");
        Console.WriteLine(@$"
        Pokemon: {Char.ToUpper(pokemon.name[0]) + pokemon.name.Substring(1)}
        Weight: {pokemon.weight}
        Height: {pokemon.height}
        Abilities: {string.Join("/", pokemon.abilities.Select(x => x.ability.name)).ToUpper()}");
    }

    public void Catch(string pokemon)
    {
        Console.WriteLine($"Gotcha! You caught {Char.ToUpper(pokemon[0]) + pokemon.Substring(1)}!");
    }

    public string ShowPokemon(List<Pokemon> p)
    {
        Console.WriteLine("\n------------------------------");
        if (p.Count == 0)
        {
            Console.WriteLine("You don't have Pokémon yet!");
            return "0";
        }
        else
        {
            for (int i = 0; i < p.Count; i++)
            {
                Console.WriteLine($"{i+1} - {p[i].name}");
            }
        }
    }
}
