# Dictionaries

Consider an ASCII text file that contains a Python dictionary on each line. The dictionary of each line contains the same keys as the other lines. These keys contain values which can only be numbers or text. Write code that reads this file, displays the available keys to the user, and asks the user which of the available keys they are interested in. Then, for that key, it displays the most popular value, the largest and the smallest.
Example:
 Suppose your file contains the following dictionaries
 {"x":3,"y":4,"name":"bob"}
 {"x":13,"y":-4,"name":"malory"}
 {"x":-3,"y":104,"name":"trudy"}
 {"x":1,"y":14,"name":"alice"}
 Your code displays to the user: x, y, name
 It asks the user for the key. If he chooses y, your code should return the values -4 and 104.
