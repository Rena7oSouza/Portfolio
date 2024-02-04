using System;
using RestSharp;
using System.Text.Json;

public class Ability
{
    public string name{get;set;}
    public string url {get;set;}
    public int slot {get;set;}
    public bool is_hidden{get;set;}
}
public class Pokemon
{

    public string name { get; set; }
    public int id { get; set; }
    public int base_experience { get; set; }
    public bool is_default {get;set;}
    public string location_area_encounters {get;set;}
    public int order {get;set;}
    public int weight {get; set;}
    public List<Ability> abilities{get;set;}

    public override string ToString()
    {
        return $"Name: {name}\n Id: {id}\n Base Experience: {base_experience}\n Is Default:{ is_default}\n Location Area: {location_area_encounters}\n Order: {order}\n Weight: {weight} ";
    }

}

class Program
{
    static void Main()
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
