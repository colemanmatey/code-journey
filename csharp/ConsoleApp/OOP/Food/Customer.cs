using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class Customer
    {
        public void MakeOrder(Restaurant restaurant, string dish) // restaurant can be any type of restaurant
        {
            restaurant.ServeDish(dish);
        }
    }
}
