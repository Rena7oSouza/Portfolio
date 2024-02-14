using System.Text.Json.Serialization;
using Newtonsoft.Json;
public class Generationiii
{
    public Emerald emerald {get; set;}
    [JsonProperty("ruby-sapphire")]
    public RubySapphire rubysapphire {get; set;}
    [JsonProperty("firered-leafgreen")]
    public FireRedLeafGreen fireredleafgreen {get; set;}
}