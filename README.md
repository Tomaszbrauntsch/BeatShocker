# BeatShocker
Have you ever wanted to make Beat Saber harder for you? I sure know I did. Introducing BeatShocker, the new way to make playing Beat Saber more shocking!

## Getting Started
Make sure you have python3 installed, with the prerequisites also install and items on the parts list

### Prerequisites 
The Raspberry Pi already has the required installed in the standard libary

On PC where Beat Saber will be running install the following packages:
```
pyscreenshot #Used to take image while in game
pytesseract #Used to filter text from the game
```

### Installing
The packages needed can be installed using pip3
```
pip3 install -r requirements.txt
```


### Parts List
The parts that are needed for this project:
```
TENS unit
Spliced TENS unit lead wires
Relay
Raspberry Pi
PC where game will be played
```

## Configuration
On the RPi make sure that the relay is installed on digital pin 17 (physical pin 11), if you didn't use pin 17 please make sure to change either the GPIO to pin 17 or modify my code.

## Deployment
Run the server.py on the RPi then run the mainClient.py on the game PC.

## Authors
* **Tomasz Brauntsch** - [tomaszbrauntsch](https://github.com/tomaszbrauntsch)

## License
This project is licensed under the CC0 License - see the [LICENSE](LICENSE) file for details
