

public class Pokemon
{

    public string name { get; set; }
    public int id { get; set; }
    public int base_experience { get; set; }
    public bool is_default {get;set;}
    public string location_area_encounters {get;set;}
    public int order {get;set;}
    public int weight {get; set;}
    public List<Abilities> abilities{get;set;}
    public List<PForms> forms{get;set;}
    public List<GameIndices> game_indices{get;set;}
    public List<HeldItems> held_items{get;set;}
    public List<Moves> moves{get;set;}
    public Species species{get;set;}
    public List<Types> types{get;set;}
    public List<Stats> stats{get;set;}

    public override string ToString()
    {
        return $"Name: {name}\n Id: {id}\n Base Experience: {base_experience}\n Is Default:{ is_default}\n Location Area: {location_area_encounters}\n Order: {order}\n Weight: {weight} ";
    }

}