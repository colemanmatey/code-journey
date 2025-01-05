import 'dart:io';

void main() {
  // string to integer
  var a = 50;
  var b = "5";

  var sum = a + int.parse(b);
  print(sum);

  // string to double
  var m = 40;
  var n = "2.5";

  var total = m + double.parse(n);
  print(total);

  // numbers to string
  var age = 29;
  print(age.toString());

  // input type conversion
  stdout.write("How much do you earn? ");
  var salary = stdin.readLineSync();
  print(int.parse(salary ?? '0'));
}