void main() {
  // for loop
  for (var i = 0; i < 10; i++) {
    print("$i: Hello there!");
  }

  // for-in loop
  List names = ["Mary", "Simon", "Joseph", "Peter", "James"];
  for (var name in names) {
    print("$name was a disciple of Jesus");
  }

  // while loop
  int i = 0;
  while(i < 20) {
    print ("$i is less than 20");
    i++;
  }

  // do while loop
  int y = 0;
  do {
    print("This loop runs at least once");
    y += 1;
  } while (y < 5);
}
