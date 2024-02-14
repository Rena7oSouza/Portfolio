using Newtonsoft.Json;
public class Generationiv{
    [JsonProperty("diamond-pearl")]
    public DiamondPearl diamondpearl{get;set;}
    [JsonProperty("heartgold-soulsilver")]
    public HeartGoldSoulSilver heartgoldsoulsilver{get;set;}
    public Platinum platinum{get;set;}

}