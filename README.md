# Hanged Game App

It's a script to play the game "hanged game" or more so a simplified version.

# Setup

In the same folder that is the Dockerfile, use the commands:

1.-docker build -t hanged-game . (Creates the image with docker)
2.-docker run -it hanged-game (Instanciate the image, creating the container and entering immediately the shell.)


# Arquitecture of the App

hanged_game--|--src--|--main.py (Main file where it is instantiated the Class from game.py.)
             |       |--game_score--|--game.py (File with Class that initiate the game.)
             |       |--utils--|--game_methods.py (File with a Class with methods for the game to run properly.)
             |                 |--words.csv (File with a list of words for the game.)
             |
             |--docker-compose.yml (Unnecessary at the moment, but it may prove useful in case of need of more containers.)
             |--Dockerfile (Set up the image for the game in docker.)
             |--requirements.txt (Necessary libraries)
             