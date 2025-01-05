void main() {
  greet();
  print(getAge());
  print(welcome("Daniel"));
  print("The area of a sphere of radius 5cm is: ${ areaOfSphere(5) }cm squared");
  print(getSalary(1000, 200, 150));
}


// No return value
void greet() {
  print("Hello!");
}

// return a value
int getAge() {
  return 29;
}

// pass an argument
String welcome(String person) {
  return "Welcome $person";
}

// default arguments
double areaOfSphere(int radius, {double pi = 3.14}) {
  return pi * radius * radius;
}

// functions without specifying return and parameter types
getSalary(gross, deductions, tax) {
  return gross - deductions - tax;
}