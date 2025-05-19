using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class MexicanRestaurant : Restaurant
    {
        public override void ServeDish(string dish)
        {
            Console.WriteLine($"We serve the best of Mexican {dish}!\n");
        }
    }
}
