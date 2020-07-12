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

### Core service (app/app1)
This service uses get requests to get your character's weapon and class, and then posts the information to service four (power level) to generate your character's power level. It also contains the database structure and configuration.

### Weapon generator
This service chooses a random weapon out of a list of six, which can be retrieved with a get request.

### Class generator.
This service chooses a random class out of a list of six, which can be retrieved with a get request.

### Power level
This service sets your character's power level by assessing the compatability between your weapon and class, which need to be posted to the service. If your weapon and class are compatible (each character is compatible with one weapon and vice versa) then your character is likely to have a higher power level than another character who's weapon and class are not compatible.

## Architecture
### ERD
This app uses a very simple database, consisting of just one table.
#### Initial ERD
![ERD 1.0](https://i.imgur.com/WS5RbJY.jpg?1)
#### Final ERD
![ERD 1.1](https://i.imgur.com/2tcxQAH.jpg)

## CI Pipeline
The CI folder contains files and configurations for a fully automated CI pipeline that will detect commits to the master branch, run unit tests, and update and deploy the new app (see image below).
![CI Pipeline](https://i.imgur.com/ySTtrdf.png)

## Load balancer
The app utilises NGINX as a load balancer, nginx.conf file is included in the CI/nginx/tasks folder. Furthermore, the initialisation-playbook.yaml file contains the necessary configuration for ansible to install nginx on a fresh VM (see the ansible section below for more information).
![Load balancing](https://i.imgur.com/wjcXVxu.png)



