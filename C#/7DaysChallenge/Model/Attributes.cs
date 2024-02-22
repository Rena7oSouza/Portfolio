public class Attributes
{
    int happiness = 5;
    int hungry = 5;

    public int getHappiness()
    {
        return happiness;
    }
    public void setHappiness(int value)
    {
        happiness += value;
        if (happiness > 10)
        {
            happiness = 10;
        }
        if (happiness < 0)
        {
            happiness = 0;
        }
    }
    public int getHungry()
    {
        return hungry;
    }
    public void setHungry(int value)
    {
        hungry += value;
        if (hungry > 10)
        {
            hungry = 10;
        }
        if (hungry < 0)
        {
            hungry = 0;
        }
    }
}