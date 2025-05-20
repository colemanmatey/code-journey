using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class Messaging
    {

        public string AboutDish(Restaurant restaurant, string dish)
        {
            return $"We serve the best of {restaurant.Cuisine} {dish}!";
        }
        

        public string AboutDrink(Restaurant restaurant, string drink)
        {
            return $"We give you the best {restaurant.Cuisine} {drink} you have ever tasted\n";
        }

        public string RestaurantNotOpen(Restaurant restaurant)
        {
            return $"Sorry, you cannot place an order at the {restaurant.ToString()} right now\n";
        }
    }
}
