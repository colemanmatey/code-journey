using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Food
{
    internal interface IRestaurant // all methods must be implemented by classes that implement this interface
    {
        void OpenRestaurant();
        void CloseRestaurant();
    }
}
