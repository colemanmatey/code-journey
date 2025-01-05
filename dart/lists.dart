void main () {
  // Create a list
  List fruits = ["apple", "banana", "pear"];
  print(fruits);

  // Get an item from the list
  var fruit = fruits[0];
  print(fruit);

  // Add item to list
  fruits.add("kiwi");
  print(fruits);

  // Add multiple items to list
  fruits.addAll(["guava", "pineapple"]);
  print(fruits);

  // Insert one item at a particular index
  fruits.insert(2, "grapefruit");
  print(fruits);

  // Insert multiple items at a particular index
  fruits.insertAll(4, ["mango", "watermelon"]);
  print(fruits);

  // mixed lists
  var mixedlist = [1, 2, 3, "one", "two", "three"];
  print(mixedlist);

  // remove an item
  mixedlist.remove(2);
  print(mixedlist);

  // remove at specific index
  mixedlist.removeAt(3);
  print(mixedlist);

  // remove the last item in the list
  mixedlist.removeLast();
  print(mixedlist);

  // remove a range
  fruits.removeRange(2, 4);
  print(fruits);

  // remove multiple based on condition
  fruits.removeWhere((item) => item.length == 5);
  print(fruits);
}
