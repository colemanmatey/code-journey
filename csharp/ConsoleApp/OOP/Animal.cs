using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP
{
    internal class Animal
    {
        private string name; // private field

        public string Name { // property to specify getters and setters
            get { return name; } 
            set { name = value; }
        }

        public int Age { get; set; } // shorthand for property

        public Animal() { }
        public Animal(string name, int age) // setting inherited fields to values during instantiation
        {
            this.Name = name;
            this.Age = age;
        }

        public string MakeSound()
        {
            return "make any sound";
        }

        public virtual string BeHappy()
        {
            return "do random stuff";
        }

    }
}
