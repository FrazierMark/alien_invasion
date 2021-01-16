# alien_invasion

#### Video Demo:

#### Description
This is an arcade game styled after old space invaders using Pygame to learn basic Object Oriented programing.

Hit the "P" button or click "Play" to begin the game.

Use the arrow keys to manuever your ship and hit the spacebar button to fire bullets.
You can choose to hold down the space bar to continually fire bullets.

The object of the game is to destory the incoming aliens before they reach the bottom of the screen.

With every fleet destroyed, the game increases in pace.

You get a total of three ships. If you lose all three ships the game is over.

The score and level information is displayed in the top right corner of the screen. The highscore is in the center.
The number of ships left is in the top left of the screen.

I'm including LOTS of comments in the code!

The MAIN program file is alien_invasion.py wherein contains various functions that detect events, update screen information, check for collisions,
update positional information, create aliens fleets, and trigger the game to start.

Our main class is AlienInvasion in which other Classes reference in order for Classes like Ship
to access all the game resources defined in AlienInvasion. Many of the other classes like Scoreboard, Alien, and GameStats do this.

To make changes to the the game like score_scale, alien or ship speed, or speedup scale simply make that changes in settings
and they will be applied to the game.

References from Pygame Shmup from KidsCanCode, Python Crash Course by Eric Matthes, ClearCode, Tech With Tim.

Press 'Q' to quit.
