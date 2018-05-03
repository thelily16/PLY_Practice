This is an order system of Tea Shop.

1. They only apply 6 kinds of drink:
   Greentea, Blacktea, Bubbletea, Oolongtea, Juice and Coffee
2. Customers can choose the level of Sugar and Ice: 
   Extra(120%), Regular(100%), Less(70%), Half(50%), Little(30%), No(0%)
3. Customers can also choose size:
   Large, Medium and Small

Execution
1. Run Start.py
2. Enter the command you want:
   (1) See menu: "Menu"
   (2) Finish order: "Done", then the program will show the formal format of orders
   (3) End the Program: "Exit"
   (4) Order drinks: Enter your oder which must contain Drink, Size, Quantity, Sugar level and Ice level

Format
1. The order you enter should look like as follow:
   "DRINK QUANTITY SIZE SUGARLEVEL ICELEVEL", where
   (a) DRINK should be the drinks in the menu and it must be the first parameter in your order
   (b) QUANTITY should be integer
   (c) SIZE should be the size in the menu
   (d) SUGARLEVEL and ICELEVEL should be the level in the menu
   (e) SUGARLEVEL and ICELEVEL must be "level + Sugar" and "level + Ice", respectively
   (f) The order of QUANTITY, SIZE, SUGARLEVEL and ICELEVEL is not fixed
2. The formal format of order are described as follow:
   "DRINK QUANTITY SIZE SUGARLEVEL ICELEVEL", where
   (a) The order of DRINK, QUANTITY, SIZE, SUGARLEVEL and ICELEVEL is fixed
   (b) The value of them must be as same as your order
   (c) SIZE is L, M or S
   (d) SUGARLEVEL and ICELEVLE are 120%, 100%, 70%, 50%, 30% and 0%

Example
Input:
Greentea Small 1 No Sugar No Ice
Blacktea 2 Large Regular Ice Half Sugar
Done

Output:
Greentea * 1	 S	 0% Sugar	0% Ice
Blacktea * 2	 L	 50% Sugar 	100% Ice