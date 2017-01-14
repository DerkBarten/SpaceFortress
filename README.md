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

# Installation
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
make sysinstall
```
Clean up the dowloaded folder
```sh
cd ..
rm -rf neon
```
### Gym
Install prerequisites:
```sh
# Use 'sudo apt-get install pip' to get pip if you haven't already
pip install -r gym/requirements.txt
```
Since we have already installed the spacefortress environment in gym, it is far easier to use our gym folder than installing it yourself. Using the following commands we can move the folder to the appropriate location.. 
```sh
# Move the gym folder to the place where python modules are installed, this is the default location
sudo mv gym /usr/lib/python2.7/dist-packages/
# Create a symbolic link to the environments of gym
sudo ln -s /usr/lib/python2.7/dist-packages/gym/envs/ "$PWD/Envs"
```

### Cairo
Cairo is a 2D graphics library with support for multiple output devices. Currently supported output targets include the X Window System (via both Xlib and XCB), Quartz, Win32, image buffers, PostScript, PDF, and SVG file output. Experimental backends include OpenGL, BeOS, OS/2, and DirectFB. The game uses this engine to render scenes. We can get is very easily with aptitude package manager:
```sh
sudo apt-get install libcairo2-dev
```
If you run into any problems installing, please visit [this](https://www.cairographics.org/download/) page
### Shared Libraries
The learning environment needs shared libraries, which can be built from the sourcecode of the SpaceFortress game. In the folder 'game' are multiple subfolders which are subtasks of the original game.
* SF is the game with most elements included 
* AIM is the stripped version of the game which focusses on the aiming task
* SFC is the stripped version of the game which focusses on the control task

The Makefile has multple build options,
```sh
make SF
make AIM
make SFC
make all    # makes all versions of the game
make clean  # removes all built files
```
A few notes:
* When using the make commands, please make sure you have first installed gym, since the Makefile relies on the symbolic link redirecting to the gym environments
* In the Makefile, it is possible to build without GUI support by setting USE_GUI to 'no'
* You need execute the Makefile as root since the shared library files will be placed in the python dist-packages folder where normal users have no permissions.

### Other dependencies
A list with dependencies we encountered during installation/runtime ourselves.
```sh
sudo apt-get install python-xlib
sudo apt-get install pynput
```


## Run

