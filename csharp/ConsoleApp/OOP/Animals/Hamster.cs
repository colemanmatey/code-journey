using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Animals
{
    internal class Hamster : Pet
    {
        public override void BeFriendly() // implements the abstract method in the Pet class
        {
            Console.WriteLine("Doing friendly stuff");
        }
    }
}
