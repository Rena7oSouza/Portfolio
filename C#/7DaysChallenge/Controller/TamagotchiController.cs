using System;
using RestSharp;
using System.Text.Json;

class TamagotchiController
{
    static void Main()
    {
        TamagotchiView view = new TamagotchiView();
        view.Title();
        string name = view.Name();
    }

    public void RequestPokemon()
    {
              var client = new RestClient("https://pokeapi.co/api/v2/pokemon/ditto");
        var request = new RestRequest("", Method.Get);

        var response = client.Execute(request);
        if (response.IsSuccessful)
        {
            Pokemon p = JsonSerializer.Deserialize<Pokemon>(response.Content);

            Console.WriteLine(p);
           
        }
        else
        {
            Console.WriteLine($"Erro: {response.ErrorMessage}");
        }
    }
}