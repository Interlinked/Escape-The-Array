# Escape-The-Array
A console based dungeon crawler that uses a 2D array to provide a map for the player to traverse. 
Uses curses to receive player input, and procedurally generates levels that get harder as the game progresses
Mainly used as a way to practice 2D array movement for future projects, so this won't be updated much, if ever. 


# How to play

Read the instructions. 
WASD moves, you run into enemies to kill them, and try to get as far as possible without running out of moves. 

# Current Issues

On level generation, there is a very low, and I mean low, chance that the goal tries to spawn on the player. If it does, there will be no goal and you will be softlocked.
This is incredibely rare, and is a simple fix, so i'm fighting laziness to fix it. 
![image](https://github.com/user-attachments/assets/9a6134b6-3897-4b05-bd3b-f3a7bff8de23)
Graph for reference. X axis is levels, Y is probability. At level 10 there's a 0.25 chance for this bug to happen. 

Holding keys uses moves very quickly without updating the counter. This is an issue with curses, and while I'm sure my logic could be tweaked, I don't really care. Don't hold keys anyways.

The goal tends to spawn in the first two rows. This is an issue with probability, as the map gets larger, it becomes more and more likely for the goal to spawn earlier and earlier. May start array randomization at random points to counteract this, or make elements spawn rarer as the game progresses. This might actually get done because it sounds interesting. 

# Updates?
Might add enemy combat, might not.


# Have fun, and escape the array!



