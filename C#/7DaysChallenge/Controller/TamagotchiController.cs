using System;
using RestSharp;
using System.Text.Json;

class TamagotchiController
{
    static void Main()
    {
        TamagotchiView view = new TamagotchiView();
        TamagotchiController controller = new TamagotchiController();
        view.Title();
        string name = view.Name();
        controller.ShowMenu(view, name);
    }

    public void ShowMenu(TamagotchiView view, string name)
    {
        string menuAction = view.Menu(name);
        MenuOptions(menuAction, view, name);
    }

    public void MenuOptions(string action, TamagotchiView view, string name)
    {
        switch (action)
        {
            case "1":
                GetOption(view, name);
                break;
            case "2":
                SeeOption();
                break;
            case "3":
                break;
            default:
                break;
        }
    }
    void GetOption(TamagotchiView view, string name)
    {
        string pokemon = view.GetPokemon(name);
        switch (pokemon)
        {
            case "1":
                pokemon = "Bulbasaur";
                break;
            case "2":
                pokemon = "Charmander";
                break;
            case "3":
                pokemon = "Squirtle";
                break;
            default:
                break;
        }
        PokemonOption(view, name, pokemon);


    }
    void PokemonOption(TamagotchiView view, string name, string pokemon)
    {
        string option = view.pokemonMenu(name, pokemon);
        switch (option)
        {
            case "1":
                Pokemon p = RequestPokemon(pokemon.ToLower());
                view.PokemonInfo(p);
                PokemonOption(view, name, pokemon);
                break;
            case "2":
            view.Catch(pokemon);
                break;
            case "3":
                ShowMenu(view, name);
                break;
            default:
                break;
        }


    }
    void SeeOption()
    { }
    Pokemon RequestPokemon(string pokemon)
    {
        var client = new RestClient($"https://pokeapi.co/api/v2/pokemon/{pokemon}");
        var request = new RestRequest("", Method.Get);
        var response = client.Execute(request);
        if (response.IsSuccessful)
        {
            Pokemon p = JsonSerializer.Deserialize<Pokemon>(response.Content);
            return p;
        }
        else
        {
            Console.WriteLine($"Erro: {response.ErrorMessage}");
            return null;
        }

    }

}