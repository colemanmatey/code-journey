namespace WebAPI.Entities
{
    public class Recipe
    {
        public int Id { get; set; }
        public required string Name { get; set; }
        public List<Ingredient>? Ingredients { get; set; }
        public string? Instructions { get; set; }
    }
}