# Rock-Paper-Scissors  
This is a simple game called 'Rock, Paper and Scissors'. The model pre-trained can recognize 3 gestures : rock, paper and scissors. Rock beats scissors, scissors beat paper, and paper beats rock. You just need to run the game, and put your hand in front of your camera with your chosen gesture, then compete with computer's choice. You can exit by pressing [Ctrl + C] at any time.  
## The Algorithm  
The re-trained resnet18 model was trained on Jetson Nano with a dataset of rock-paper-scissors gestures. The program would automatically load the model.  
## Running This Project  
* Follow these steps to run this project.  
1. Clone jetson-inference project from Github.  
```
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
```
2. Make sure to have python packages installed.  
```
$ sudo apt-get install libpython3-dev python3-numpy
```
3. Build jetson-inference from source.  
```
$ mkdir build
$ cd build
$ cmake ../
$ make
$ sudo make install
$ sudo ldconfig
```
4. Clone this repository from Github.  
```
$ git clone https://github.com/LykBran/rock-paper-scissors.git
```
5. Run the main program.  
tips: Replace A with your camera device  
```
$ cd rock-paper-scissors
$ python3 game.py A
```
Now enjoy playing!  

---

Dataset URL : https://www.kaggle.com/datasets/sanikamal/rock-paper-scissors-dataset  
