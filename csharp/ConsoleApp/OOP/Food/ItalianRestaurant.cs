using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class ItalianRestaurant : Restaurant
    {
        public override void ServeDish(string dish)
        {
            Console.WriteLine($"We serve the best of Italian {dish}!\n");
        }
    }
}