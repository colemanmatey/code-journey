import 'dart:io';

void main() {
  // Using the var keyword
  stdout.write("Enter a number: ");
  var number = stdin.readLineSync();
  print("You entered the number '$number'\n");

  // String vs String?
  stdout.write("What is your name? ");
  String? name = stdin.readLineSync();
  print("Your name is $name");

}