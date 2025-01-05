void main() {
  // if
  int score = 90;
  if (score >= 90) {
    print("You have an 'A'");
  }

  // if else
  String fruit = 'apple';
  if (fruit == 'apple') {
    print("This is an apple");
  } else {
    print("This is not an apple");
  }

  // if else if
  String name = "Cole";
  if (name.length == 5) {
    print("$name has 5 characters");
  } else if (name.length == 4) {
    print("$name has 4 characters");
  } else {
    print("I am not sure how many characters are in $name");
  }
}