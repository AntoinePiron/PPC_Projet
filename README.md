# PPC project
*By Tristan Devin and Antoine Piron 3TC2*

The purpose of this repository is to track the evolution of our final project in PPC.


Playing the game is quite straightforward, following the instructions given in the terminal.

The minimum player count is 3, and playing is possible with up to  7 players. The server will ask if the players want to
start the game when 3 players are connected, and, if someone decides to wait, it will ask each player with every new connection

Hands are then distributed. If a player decides to put up an offer, he waits until someone accept his offer

When a player decides to choose an offer, he is presented with the current offer list, and choose one of the offers


Cards are then exchanged, and the new hand is displayed

At the beginning of the choices, someone can always say he has a winning hand. If that is true, a signal is send from the server. It will print the winner for all players, then terminates every server/player programm.

Have fun !