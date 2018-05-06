# PLY_Practice
Tea Shop Order System by Python PLY

Features
	User can choose six different drinks:
		Option: Greentea, Blacktea, Bubbletea, Oolongtea, Juice and Coffee
		This option must be entered
	User can choose the level of Sugar and Ice:
		Option: Extra(120%), Regular(100%), Less(70%), Half(50%), Little(30%), No(0%)
		If user doesn’t choose the level of sugar and ice, then the default level is 100% (Regular).
	User can also choose size:
		Option: Large, Medium and Small
		If user doesn’t choose the size, then the default size is large
	User can also choose how many drink they want to buy:
		Option: Any integer greater than 0
		If user doesn’t enter how many drink they want, then the default quantity is 1
	User can enter more than one orders
	User can see the menu by entering “Menu”
	User must enter “Done” after finished any one order, then the program will show total price
	User can exit the program by entering “Exit”

Tokens
	DRINK: Greentea, Blacktea, Bubbletea, Oolongtea, Juice, Coffee
	SUGAR: Sugar
	ICE: Ice
	NUMBER: {0~9}^+
	LEVEL: Extra, Less, Half, Little, No
	PERCENT: 120%, 100%, 70%, 50%, 30%, 0%
	SIZE: Large, Medium, Small
	MENU: Menu
	DONE: Done
	EXIT: Exit

Grammar
	command: order command | order | done command | done | menu | exit
	order: DRINK option
	option: quantity size Doption (Drink option), this sequence can be changed.
	Doption: Soption (Sugar option) Ioption (Ice option), this sequence can be changed
	quantity: NUMBER | empty
	size: SIZE | empty
	Soption (Sugar option): Slevel (Sugar level) | empty
	Ioption (Ice option): Ilevel (Ice level) | empty
	Slevel (Sugar level): Setlevel SUGAR
	Ilevel (Ice level): Setlevel ICE
	Setlevel: level | PERCENT
	level: LEVEL
	menu: MENU
	exit : EXIT
	done: DONE

Execution
	Run Start.py
	Enter the command you want:
	See menu: "Menu"
	Finish order: "Done", then the program will show the formal format of orders
	End the Program: "Exit"
	Order drinks: Enter your order which must contain Drink

Format
	Input Format: 
		Drink ( + Sugar option + Ice option + Size + Quantity)
	Output Format:
		Drink + Quantity + Size + Sugar option + Ice option + price

Example
	Input: 
		Blacktea 2 Large 50% Sugar 50% Ice Greentea Large No Ice No Sugar 1 Done Bubbletea Done
	Output:
		Blacktea       2    L    50%  Sugar	50%  Ice      40        
		Greentea       1    L    0%   Sugar	0%   Ice      20        
		Total Price: 60

		Bubbletea      1    L    100% Sugar	100% Ice      30        
		Total Price: 30
	
	Input:
		Menu
	Output:
		DRINK		SUGAR/ICE OPTION	SIZE
		===================================================
		1. Greentea	1. Extra (120%)		1. Large
		2. Blacktea	2. Regular (100%)	2. Medium
		3. Bubbletea	3. Less (70%)		3. Small
		4. Oolongtea	4. Half (50%)
		5. Juice	5. Little (30%)
		6. Coffee	6. No (0%)

	Input:
		Exit
	Output:
		Exit the program
