using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class ItalianRestaurant : Restaurant
    {
        public override string Cuisine { get; set; } = "Italian";

        public override string ToString()
        {
            return $"{Cuisine} Restaurant";
        }

        public override void ServeDish(string dish)
        {
            Console.WriteLine(messaging.AboutDish(this, dish));
        }

        public override void ServeDrink(string drink)
        {
            Console.WriteLine($"We give you the best Italian {drink} you have ever tasted\n");
        }
    }
}