using OOP.Animals;
using OOP.Food;

namespace OOP
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Animal animal = new Animal();
            animal.Name = "Sam";
            animal.Age = 3;

            Dog dog1 = new Dog();
            dog1.Name = "Bucky";
            dog1.Age = 2;
            dog1.Breed = "Rottweiller";


            Console.WriteLine($"Hi, {animal.Name} here");
            Console.WriteLine($"I am {animal.Age} years old. I {animal.MakeSound()}");
            Console.WriteLine($"When I am happy I {animal.BeHappy()}\n");

            Console.WriteLine($"Hi, {dog1.Name} here");
            Console.WriteLine($"I am {dog1.Age} year old {dog1.Breed}. I like to {dog1.MakeSound()}");
            Console.WriteLine($"When I am happy I {dog1.BeHappy()}\n");


            Animal dog2 = new Dog("Lassie", 1); // initializing object using constructor - Method 1
            Console.WriteLine($"I am {dog2.Name} and as an animal I sometimes {dog2.MakeSound()}"); // calls base class' method

            Animal dog3 = new Dog() // initializing object using constructor - Method 2
            {
                Name = "Leane",
                Age = 4
            };
            Console.WriteLine($"I am {dog3.Name} and I {dog3.BeHappy()} when happy\n"); // calls derived class' method

            Hamster hamster = new Hamster();
            hamster.BeFriendly();

            Cat cat = new Cat("Dore", 2);
            Console.WriteLine($"My name is {cat.Name}. When I reflect, I {cat.SelfReflect()}\n\n");


            // INHERITANCE
            Console.WriteLine("INHERITANCE\n------------");

            // Customers
            Customer peter = new Customer();
            Customer sandra = new Customer();
            
            // Restaurants
            MexicanRestaurant sobeys = new MexicanRestaurant(); // specific class instantiation
            ChineseRestaurant chinabowl = new ChineseRestaurant(); // specific class instantiation
            NigerianRestaurant obolu = new NigerianRestaurant(); // specific class instantiation

            Restaurant pizzorama = new ItalianRestaurant(); // base class reference
            Restaurant papaye = new GhanaianRestaurant(); // base class reference

            // Open restaurants
            chinabowl.IsOpen = true;
            obolu.IsOpen = true;

            // Orders
            peter.MakeOrder(sobeys, "Tacos", "Apple juice");
            peter.MakeOrder(chinabowl, "Ramen", "Champagne");
            peter.MakeOrder(obolu, "Egusi soup", "Beer");

            sandra.MakeOrder(pizzorama, "Pizza", "Pepsi");
            sandra.MakeOrder(papaye, "Jollof Rice", "Jack Daniels");




        }
    }
}
