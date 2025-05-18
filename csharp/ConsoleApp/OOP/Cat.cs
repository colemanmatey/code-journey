using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP
{
    internal sealed class Cat : Animal // Restricts any inheritance from the Cat class
    {
        public Cat() : base(){}
        public Cat(string name, int age) : base(name, age) { }
        public new string MakeSound()
        {
            return "Meooowwww!";
        }

        public override string BeHappy()
        {
            return "catwalk";
        }

        public string SelfReflect()
        {
            return base.MakeSound(); // the base keyword references the parent class
        }
    }
}
