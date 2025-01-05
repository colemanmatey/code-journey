import 'dart:io';

void main() {
  // version 1
  for (int i = 1; i < 101; i++) {
    if (i % 3 == 0) {
      stdout.write("$i fizz");
      if (i % 5 == 0) {
        stdout.write("buzz");
      }
      stdout.write("\n");
    } else if (i % 5 == 0) {
      stdout.write("$i buzz");
      if (i % 3 == 0) {
        stdout.write("fizz");
      }
      stdout.write("\n");
    } else {
      print(i);
    }
  }

  // version 2
  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0) {
      print("$i fizz");
    } else if (i % 5 == 0) {
      print("$i buzz");
    } else if (i % 3 == 0 && i % 5 == 0) {
      print("$i fizzbuzz");
    }
  }

  // version 3
  for (int i = 1; i <= 100; i++) { 
    String output = ''; 
    if (i % 3 == 0) output += 'fizz'; 
    if (i % 5 == 0) output += 'buzz'; 
    if (output.isEmpty) { 
      print(i); 
    } else { 
      print('$i $output'); 
    } 
  }
}