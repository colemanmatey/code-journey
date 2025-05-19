using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class NigerianRestaurant : Restaurant
    {
        public override string ToString()
        {
            return "Nigerian";
        }

        public override void ServeDish(string dish)
        {
            Console.WriteLine($"We serve the best of Nigerian {dish}!");
        }

        public override void ServeDrink(string drink) // overrides the default behaviour in base class
        {
            Console.WriteLine($"We give you the best Nigerian {drink} you have ever tasted\n");
        }
    }
}
