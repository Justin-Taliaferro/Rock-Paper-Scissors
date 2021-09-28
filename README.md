# Rock-Paper-Scissors

An example Python application for someone to play the computer in a classic game of Rock, Paper, Scissors on windows.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/Justin-Taliaferro/Rock-Paper-Scissors.git) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

# setup
After cloning the repo, navigate there from the command line. 
```
cd Downloads/
cd Rock-Paper-Scissors-main
``` 

Use the pwd command to check that your present working desktop is Rock-Paper-Scissors-main

On the windows os you may get an error that says: "No such file or directory exists." In this case you will have to navigate to your environment step by step, make sure you are running the repository's root directory where the requirements.txt file exists (see the initial `cd` step above).

```
cd ~/Downloads
ls
cd Rock-Paper-Scissors-main
cd Rock-Paper-Scissors-main
```
NOTE: My file was saved twice so I had to navigate there an extra time with the same cd command. 

Once you are in the game file create your game environment using anaconda and specify which version of python you are currently using.

```
conda create -n my-game-env python=3.8
```
After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```
pip install -r requirements.txt
```

Simply type "y" to the "proceed ([y]/n)? promt. Once the packages are installed active your game environment with the following command:

```
conda activate my-game-env
```
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

    PLAYER_NAME="Type your player name"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

You will now be acting in the game environment, save your code in your game file and then run the game with the following command:

```
python game.py
```
(or python ______.py for whatever you saved your game file as, then your file will start running and prompt the user for an input.)

NOTE: Make sure to read the requirements.txt file to install the correct packages if you have any issues.

Happy Playing!

