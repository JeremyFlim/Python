# What is this?
This is just a collection of random Python projects (usually pretty old) I've decided to upload here and don't belong anywhere else.

# Bad Calculator
A simple command-line calculator. You have to manually type operations (e.g. Addition, Multiplication. Type operationslist for a list) and then type the two numbers you wish to perform that calculation on. For now, it can only handle two numbers at a time and four operations: Addition, Subtraction, Multiplication, and Division. It rounds divisions with very high values.

Just run the program to use it (requires Python)

# Gambling Simulator
A command-line classic gambler's ruin simulator. This simulator will "toss a coin" (but with adjustable odds) and winning will award $1 while losing will cost you $1. 

You are able to input the starting money, the goal money, the win chance in percentage (anything above 99 will result in a 100% chance of winning), and the number of games to play. A game will end when the player has either reached the set goal or has $0 left. It will run the number of games specified and display a win-lose graph, a winrate over time graph and then state the overall winrate and the number of steps ("coinflips") per game in the command line. Try it out!

Be aware that higher values of starting money, goal money, a win chance closer to 50%, and a high number of games will take a very long time to run.

To run this program, you will need to install matplotlib. To do that, run this in your command prompt:
```
pip install matplotlib
```
