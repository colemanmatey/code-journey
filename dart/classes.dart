void main() {
  var person = Person("Coleman", "Matey", 29);
  print(person.fullname());

  Car car = Car('Totoya', 'Camry', 2025);
  car.info();
}

// Dynamic attribute types
class Person {
  var firstname;
  var lastname;
  var age;

  Person(first, last, age) {
    this.firstname = first;
    this.lastname = last;
    this.age = age;
  }

  fullname() {
    return "$firstname $lastname";
  }
}


// Specific data types
class Car {
  String? make;
  String? model;
  int? year;

  Car(String make, String model, int year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  void info(){
    print("Make: ${this.make}");
    print("Model: ${this.model}");
    print("Year: ${this.year}");
  }
}