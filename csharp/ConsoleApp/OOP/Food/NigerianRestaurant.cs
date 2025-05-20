using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class NigerianRestaurant : Restaurant
    {
        public override string Cuisine { get; set; } = "Nigerian";

        public override string ToString()
        {
            return $"{Cuisine} Restaurant";
        }

        public override void ServeDish(string dish)
        {
            Console.WriteLine(messaging.AboutDish(this, dish));
        }

        public override void ServeDrink(string drink) // overrides the default behaviour in base class
        {
            Console.WriteLine(messaging.AboutDrink(this, drink));
        }
    }
}
