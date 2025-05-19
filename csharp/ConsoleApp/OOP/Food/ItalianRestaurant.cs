using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class ItalianRestaurant : Restaurant
    {
        public override string ToString()
        {
            return "Italian";
        }

        public override void ServeDish(string dish)
        {
            Console.WriteLine($"We serve the best of Italian {dish}!");
        }

        public override void ServeDrink(string drink)
        {
            Console.WriteLine($"We give you the best Italian {drink} you have ever tasted\n");
        }
    }
}