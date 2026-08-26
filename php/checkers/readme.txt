index.php
---------

Main control - setups the screen.

Sets the difficulty: 
- Easy picks randomly among a few legal moves (weak play)
- Medium searches 4 plies ahead based on material + king value + advancement + center control.
- Hard searches 6 plies ahead with the same evaluation function.

script.js 
---------
This is the rules engine written in JavaScript: 
enforces mandatory captures and forced multi-jump chains for your red pieces, highlighting only legal destinations.

compute.php
-----------
This is the AI engine written in PHP. This regenerates all legal moves (including full jump chains), scores resulting positions, and searches with minimax + alpha-beta pruning.

  
style.css
---------
Has all the screen colours and styles for the HTML sections. Displays the board and sets piece colours for the player and computer.


Designed by Surjit Randhawa 2026


