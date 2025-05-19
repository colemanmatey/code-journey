using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP.Animals
{
    internal class Dog : Animal // Inheritance
    {
        public string? Breed { get; set; }

        public Dog() : base(){}
        public Dog(string name, int age) : base(name, age) { } // inherit parent's constructor


        public new string MakeSound() // hide inherited MakeSound()
        {
            return "Woof woof!";
        }

        public override string BeHappy() // override inherited MakeSound() - polymorphism
        {
            return "wag my tail";
        }
    }
}
