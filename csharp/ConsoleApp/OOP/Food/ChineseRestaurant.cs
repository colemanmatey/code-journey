using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class ChineseRestaurant : Restaurant
    {
        public override string Cuisine { get; set; } = "Chinese";

        public override string ToString()
        {
            return $"{Cuisine} Restaurant";
        }

        public override void ServeDish(string dish)
        {
            Console.WriteLine(messaging.AboutDish(this, dish));
        }
    }
}
