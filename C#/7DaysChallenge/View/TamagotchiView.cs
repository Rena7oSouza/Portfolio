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
        while(name == "")
        {
        Console.WriteLine("What's your name?");
        name = Console.ReadLine();
        }
        return name;
    }

    public string Menu(string name)
    {
        string answer = "";
        while(answer != "1" || answer != "2" || answer != "3")
        {
        Console.WriteLine(name + "what do you want?\n 1 - Get a Pokémon\n 2 - See your Pokémon\n 3- Exit");
        answer = Console.ReadLine();
        }
        return answer;
    }
}