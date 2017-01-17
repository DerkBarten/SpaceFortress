# Setup
Our SpaceFortress Q-learning implementation exists mainly of the following parts
* [OpenAI Gym](https://gym.openai.com/)
* [Simple DQN](https://github.com/tambetm/simple_dqn)
* The SpaceFortress Game

### OpenAI Gym
A toolkit for developing and comparing reinforcement learning algorithms. It supports teaching agents everything from walking to playing games like Pong or Go.
Gym will basically create an environment in which the learning algorithm can learn the game.

### Simple DQN
Deep Q-learning agent for replicating DeepMind's results in paper "Human-level control through deep reinforcement learning". It is designed to be simple, fast and easy to extend. This is the workhorse of our project.

### Space Fortress
An old DOS game, but pretty complex nevertheless. We will train a network to play this game.

# Download
Download the repository. Make sure you execute the command in which you want to install the repository.
```sh
sudo git clone https://github.com/Noswis/SpaceFortress.git 
cd SpaceFortress
```

# Installation
During the installation process, please make sure you are in the SpaceFortress folder.
### Neon
[Neon](https://github.com/NervanaSystems/neon) is Nervana's Python based Deep Learning framework and achieves the fastest performance on modern deep neural networks such as AlexNet, VGG and GoogLeNet. Designed for ease-of-use and extensibility. The Simple DQN learning algorithm was built on neon, so we need to install this.

Install prerequisites:
```sh
sudo apt-get install libhdf5-dev libyaml-dev libopencv-dev pkg-config
sudo apt-get install python python-dev python-pip python-virtualenv
```

Check out and compile the code:

```sh
git clone https://github.com/NervanaSystems/neon.git
cd neon
sudo make sysinstall
```
Clean up the dowloaded folder
```sh
cd ..
sudo rm -rf neon
```
### Gym
Install prerequisites:
```sh
# Use 'sudo apt-get install pip' to get pip if you haven't already
sudo pip install -r gym/requirements.txt
```
Connect python to gym
```sh
# add the gym directory to the python path in bashrc
echo "export PYTHONPATH=$PYTHONPATH:$PWD" >> ~/.bashrc
```
Note: please make sure the path doesn't have any spaces
### Cairo
Cairo is a 2D graphics library with support for multiple output devices. Currently supported output targets include the X Window System (via both Xlib and XCB), Quartz, Win32, image buffers, PostScript, PDF, and SVG file output. Experimental backends include OpenGL, BeOS, OS/2, and DirectFB. The game uses this engine to render scenes. We can get is very easily with aptitude package manager:
```sh
sudo apt-get install libcairo2-dev
```
If you run into any problems installing, please visit [this](https://www.cairographics.org/download/) page
### Shared Libraries
Go to the Game folder
The learning environment needs shared libraries, which can be built from the sourcecode of the SpaceFortress game. In the folder 'game' are multiple subfolders which are subtasks of the original game.
* SF is the game with most elements included 
* AIM is the stripped version of the game which focusses on the aiming task
* SFC is the stripped version of the game which focusses on the control task

Make sure you have the clang compiler installed
```sh
sudo apt-get install clang
```

The Makefile has multple build options,
```sh
cd Game
sudo make SF
sudo make AIM
sudo make SFC
sudo make all    # makes all versions of the game
sudo make clean  # removes all built files
```

### Other dependencies
A list with dependencies we encountered during installation/runtime ourselves.
```sh
sudo apt-get install python-xlib
sudo pip install pynput
sudo pip install pathlib
sudo pip install opencv-python
sudo apt-get install gtk2.0
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgtk-3-dev
sudo apt-get pkg-config
```


## Run

### 
The trained network can be tested using the gym library. The main script is located in gym/envs/space_fortress
and is named run.py. Run.py can be used in the following way.

```sh
usage: run.py [-h] [-m {human,minimal,terminal,rgb_array}] [-s {slow,fast}]
              {SFS,SF,SFC,AIM}

optional arguments:
  -h, --help            show this help message and exit

Game:
  {SFS,SF,SFC,AIM}      Specify which game you want to run

Rendering:
  -m {human,minimal,terminal,rgb_array}
                        Determine the render mode of the game
  -s {slow,fast}        Determine the render speed of the game

```