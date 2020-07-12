# Character Generator (CG)

CG is a Python web application, consutrcted using the Flask web framework. The app generates a character class, weapon and power level for you to use in a dungeons and dragons game, as you see fit. No registration is required to use the app. The app comes with pre-made unit tests and a fully configured continuous integration pipeline.
This app is ran on a Google CLoud Platform Ubuntu 18.04 virtual machine, via docker swarm, using the Python-based HTTP web server Gunicorn.
The app's database is hosted on a GCP MySQL server.

## Resources
[WebApp](http://34.89.84.81/)
[Trello Board](https://trello.com/b/LAOKAzoo/character-generator)
[Risk Assessment](https://docs.google.com/spreadsheets/d/1yAafiJ76UwzMyKsj6W3heGlLeubrjCGEj5deukhhuLk/edit?usp=sharing)

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
![ERD 1.0](https://i.imgur.com/AD9C9ZY.png)
#### Final ERD
![ERD 1.1](https://i.imgur.com/2tcxQAH.jpg)

## CI Pipeline
The CI folder contains files and configurations for a fully automated CI pipeline that will detect commits to the master branch, run unit tests, and update and deploy the new app (see image below).
![CI Pipeline](https://i.imgur.com/ySTtrdf.png)

## Jenkins VM Set-up
Jenkins is set-up on a separate GCP VM with Ansible, docker, docker-compose and a python venv with the necessary requirements for unit testing installed.
The Jenkins server uses a webhook to trigger a pipeline build whenever a change is made to the master branch of this repo. The first step of the build runs unit tests with pytest, followed by building the docker images, using docker-compose and pushing them to my dockerhub repository. The final step uses Ansible to install all the dependencies and requirements on the docker-swarm manager and worker nodes, as well as updates the swarm.
Additionally, Jenkins credentials are used to safely store passwords and other secret variables.

### Ansible set-up
In order to use Ansible for configuration management, the Jenkins VM is set-up to be able to SSH into the swarm-manager and worker nodes. 
#### Ansible inventory
Ansible recognises IPs in it's own private network, hence to set up connections in the inventory it is enough to refer to each VMs name (as assigned on GCP). This works as a safety measure and means that you do not have to expose the IPs of each VM. 
#### Ansible roles
Ansible roles are used to easily configure different machines to meet each machine's specific needs. For example, initiation of the swarm on the swarm manager machine. 
#### Ansible-vault
Ansible vault is used to encrypt and store the database URI variable for the CI/deploy task within the CI/deploy/vars/main.yaml. However, in order for Ansible to decrypt this file you must provide the right vault password, which is simply stored in a file outside of the repository on the Jenkins VM.
## Load balancer
The app utilises NGINX as a load balancer, nginx.conf file is included in the CI/nginx/tasks folder. Furthermore, the initialisation-playbook.yaml file contains the necessary configuration for ansible to install nginx on a fresh VM (see the ansible section above for more information).
![Load balancing](https://i.imgur.com/wjcXVxu.png)

## Testing
The app uses pytest unit tests with essentially a 100% test coverage, as the functionality of each service is completely covered. However, one line is missed in each service's coverage report. The line being: "app.run(debug=True,port=5000, host='0.0.0.0')", as this can't be tested. However, this can be easily overcome by using a different application structure. The results of each test are automatically stored within service_name/test-results folder on the Jenkins VM as a html file, named according to time and date that the test was performed on. For example, the tests for the Class Generator service are stored in class/test-results.

### Coverage
As previously mentioned the tests essentially cover 100% of the python code within the app. This means that the unit tests make the app run each line of code present and that the test assertions are met for each test. A high unit test coverage indicates that your app is working as intended, however the significance of this measure heavily relies on how good your unit tests are. 
#### Sample test results
![test results](https://i.imgur.com/cukwN5Q.png)

### Integration tests
While the app could benefit from having integration testing (for example using Selenium to see that the Core service returns the correct html template), I don't believe these tests are currently necessary, due to the extreme simplicity of the app itself.

## Risk Assessment
### Initial Risk Assessment
A risk assessment was conducted prior to project start, identifying general web server issues, as well as CI pipeline specific issues (see image below).
![Initial risk assessment](https://i.imgur.com/Y480Foa.png)

### Risk Assessment Review
A risk assessment review was conducted after the completion of the project. Overall, no risks had occurred and most of the current mitigations seem to be enough to deal with any issues (see image below).
![Risk assessment review](https://i.imgur.com/9urRZ8Q.png)



