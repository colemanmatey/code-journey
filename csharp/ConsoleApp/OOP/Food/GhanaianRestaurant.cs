using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class GhanaianRestaurant : Restaurant
    {
        public override string ToString()
        {
            return "Ghanaian Restaurant";
        }

        public override void ServeDish(string dish)
        {
            Console.WriteLine($"We serve the best of Ghanaian {dish}!");
        }
    }
}
