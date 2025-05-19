using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class NigerianRestaurant : Restaurant
    {
        public void ServeWine(string wine)
        {
            Console.WriteLine($"We give you the best {wine} you have ever tasted");
        }
    }
}
