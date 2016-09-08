# Programming-challanges

Author: Edin Citaku
-----------
Description
-----------
In this project I will do the programming challanges from r/dailyprogrammer.
The goal for me is to learn some programming and to get hands-on experience with git.
In the near future I will be doing these challanges in Python but other languages will follow.
The name of the files will begin with the Challange Number, followed by the difficulty.
This is so you can find them more easily in this table: 
https://www.reddit.com/r/dailyprogrammer/wiki/challenges

Note: The following descriptions are copied from the links in the different challanges.
-----------
277-Intermediate-FakeCoins
-----------
Link:		 https://www.reddit.com/r/dailyprogrammer/comments/4utlaz/20160727_challenge_277_intermediate_fake_coins/

Description: 	Their are some false golden coins, wich are lighter then others, in the treasure chest. The assistant has weighed the coins, but can not figure out which are false and which are not.
		Each coin is labeled with a letter, and is put on the scale in groups or by itself. The input consist of the coins on the left side, the coins on the right side and the way the scale  		tipped. This can be left, right or equal when the two sides wheigt the same. It is assumed, that only one coins is lighter then the others 

How to use:	 simply put the arrangment of the coins into a file called "Input"(which has to be in the same file as the script) and start the python script 

Input-File:	 The format is as in the link showed above. Multible lines are allowed. One line has this format:
		 <LeftSide> <RightSide> <Side>  
		 <LeftSide> and <RightSide> should have the same number of coins. Both of them consist of characters, each represanting a different coin
		 <Side> has three different values: left, right, equal

-----------
277-Hard-Trippy-Julia-Fractals
-----------
Link:		https://www.reddit.com/r/dailyprogrammer/comments/4v5h3u/20160729_challenge_277_hard_trippy_julia_fractals/

Description:	You’re making a music video for an acid rock band. Far out man! Of course they want visual effects with fractals, because they’ve googled fractals, and they’re super trippy. Of course, 			they don’t know the mad programming needed to make these fractals. But you do, and that’s why they pay you money.

A Julia set is made by applying a function to the complex numbers repeatedly and keeping track of when the resulting numbers reach a threshold value. One number may take 200 iterations to achieve and absolute value over a certain threshold, value while an almost identical one might only take 10 iterations.
 
Here, we’re interested in Julia sets because you can make pretty pictures with them if you map each complex input number to a pixel on the screen. The task today is to write a program 		that does all the math necessary for your computer to draw one of these beautiful pictures. In addition to making a buck from the band, you can also make a set of nice wallpapers for 			your desktop!

How to use:	pick your desired function into a file called "Input-Function" and start the script. Before your picture(in bmp format) is generated you have to pick your desired resolution.

Input-File:	The format looks like that +/- az^n +/- bz^m .... lz^v + oi 	
	 	All the characters exzeot the z and i are variables. Furthermore the numbers after the ^ have to be integers, while the numbers in front of the z can be floats aswell. The numbers 
	 	before the i can be a float too	
		The function in the link would look like that in the input file: + 1z^2 -0.221z^0 - 0.713i 

>>>>>>> 311407acc4d8a2242ced57cc6addfafc7aac8d77
