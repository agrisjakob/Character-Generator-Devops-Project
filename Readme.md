# Character Generator (CG)

CG is a Python web application, consutrcted using the Flask web framework. The app generates a character class, weapon and power level for you to use in a dungeons and dragons game, as you see fit. No registration is required to use the app. The app comes with pre-made unit tests and a fully configured continuous integration pipeline.
This app is ran on a Google CLoud Platform Ubuntu 18.04 virtual machine, via docker swarm, using the Python-based HTTP web server Gunicorn.
The app's database is hosted on a GCP MySQL server.

## Resources
[WebApp](http://34.89.84.81/)

[Trello Board](https://trello.com/b/LAOKAzoo/character-generator)

## Functionality
### How-to use
The app is extremely simple and easy to use. Simply, access it via this [link](http://34.89.84.81/) to get your own randomly generated character and refresh the page if you'd like to get a different character.

### App overview
The app consists of four services:
1. Core service - interacts with the other services and renders the generated information into a html format.
2. Weapon generator - randomly chooses a weapon for your character.
3. Class generator - randomly chooses a class for your character.
4. Power level - Checks the compatability between your character's class and weapon to determine a power level.

### Core service

