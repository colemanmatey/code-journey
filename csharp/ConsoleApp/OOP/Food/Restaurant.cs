using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal abstract class Restaurant : IRestaurant
    {
        public abstract string Cuisine { get; set; }

        public bool IsOpen { get; set; } = false;

        public readonly Messaging messaging = new Messaging();

        public override string ToString()
        {
            return "Restaurant";
        }

        // arrow syntax to define simple function body
        public void OpenRestaurant() => IsOpen = true;
        public void CloseRestaurant() => IsOpen = false;

        public abstract void ServeDish(string dish); // must be implemented by all its derived classes

        public virtual void ServeDrink(string drink) // a default behaviour that can be optionally overriden by a derived class
        {
            Console.WriteLine($"We give you the best {drink} you have ever tasted\n");
        }
    }
}
