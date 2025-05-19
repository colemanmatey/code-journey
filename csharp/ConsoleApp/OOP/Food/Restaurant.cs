using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class Restaurant
    {
        public virtual void ServeDish(string dish) // default implementation of ServeDish()
        {
            Console.WriteLine($"We serve your {dish} with a smile\n");
        }
    }
}
