﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal class Customer
    {
        public readonly Messaging messaging = new Messaging();
        public void MakeOrder(Restaurant restaurant, string dish, string drink) // restaurant can be any type of restaurant
        {
            if (restaurant.IsOpen)
            {
                restaurant.ServeDish(dish);
                restaurant.ServeDrink(drink);
            } 
            else
            {
                Console.WriteLine(messaging.RestaurantNotOpen(restaurant));
            }
        }
    }
}
