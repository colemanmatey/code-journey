void main () {
  // Create a map
  var bio = {"name": "Coleman", "age": 29, "isMarried": false};
  print(bio);

  // Display keys
  print(bio.keys);

  // Display values
  print(bio.values);

  // Display the length of the map
  print(bio.length);

  // Add an item to the map
  bio["occupation"] = "Junior Developer";
  print(bio);

  // Add multiple key-value pairs
  bio.addAll({"salary": 150000});
  print(bio);

  // Remove item from map
  bio.remove("isMarried");
  print(bio);

  // Empty the map
  bio.clear();
  print(bio);
}
