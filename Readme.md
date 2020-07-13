# Character Generator (CG)

CG is a Python web application, consutrcted using the Flask web framework. The app generates a character class, weapon and power level for you to use in a role-playing game, such as Dungeons and Dragons, as you see fit. No registration is required to use the app. The app comes with pre-made unit tests and a fully configured continuous integration pipeline.
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

### Core service (/app/app1)
This service uses get requests to get your character's weapon and class, and then posts the information to service four (power level) to generate your character's power level. It also contains the database structure and configuration.

### Weapon generator (/weapons/app2)
This service chooses a random weapon out of a list of six, which can be retrieved with a get request.

### Class generator (/class/app3)
This service chooses a random class out of a list of six, which can be retrieved with a get request.

### Power level (/power/app4)
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
![CI Pipeline](https://i.imgur.com/BhfrCkg.png)

## Jenkins pipeline
The Jenkins pipeline has three main stages that occur in this order: testing, updating docker images and updating the docker-swarm. Logs can be easily accessed by mousing over each section and clicking “logs” to see any errors that may have occurred.

![pipeline](https://i.imgur.com/xlV7KBS.png)

![logs](https://i.imgur.com/uCLF1iq.png)

## Pipeline improvements
Currently, the pipeline takes about 2 minutes to finish, some improvements could be made to shorten this. The final update and deploy step, arguably contains some unnecessary steps that could be moved out of the playbook.yaml file and into the initialisation-playbook.yaml file to shorten build time. For example, the install docker tasks, as each node will already have docker on it.


## Jenkins VM Set-up
Jenkins is set-up on a separate GCP VM with Ansible, docker, docker-compose and a python venv with the necessary requirements for unit testing installed.
The Jenkins server uses a webhook to trigger a pipeline build whenever a change is made to the master branch of this repo. The first step of the build runs unit tests with pytest, followed by building the docker images, using docker-compose and pushing them to my dockerhub repository. The final step uses Ansible to install all the dependencies and requirements on the docker-swarm manager and worker nodes, as well as updates the swarm.
Additionally, Jenkins credentials are used to safely store passwords and other secret variables.


### Ansible set-up
In order to use Ansible for configuration management, the Jenkins VM is set-up to be able to SSH into the swarm-manager and worker nodes. Furthermore, if you wish to set-up your own pipeline, the initialisation-playbook.yaml (rather than playbook.yaml) file should be ran the first time the VM network is set-up, as it includes the necessary configuration to set-up NGINX as a load balancer.
#### Ansible inventory
Ansible recognises IPs in it's own private network, hence to set up connections in the inventory it is enough to refer to each VMs name (as assigned on GCP). This works as a safety measure and means that you do not have to expose the IPs of each VM. 
#### Ansible roles
Ansible roles are used to easily configure different machines to meet each machine's specific needs. For example, initiation of the swarm on the swarm manager machine. 
#### Ansible-vault
Ansible vault is used to encrypt and store the database URI variable for the CI/deploy task within the CI/deploy/vars/main.yaml. However, in order for Ansible to decrypt this file you must provide the right vault password, which is simply stored in a file outside of the repository on the Jenkins VM.
## Load balancer
The app utilises NGINX as a load balancer, nginx.conf file is included in the CI/nginx/tasks folder. Furthermore, the initialisation-playbook.yaml file contains the necessary configuration for ansible to install nginx on a fresh VM (see the ansible section above for more information).
Users can indirectly access the app by connecting to the NGINX server, which forwards client requests to the app's services.
Using NGINX as a load balancer allows for an additional layer of stability, as it is a useful solution for dealing with a high amount of incoming traffic, preventing it from crashing a server, by simply sending the requests to another available server.The load balancer in this case sends requests to the server with the least number of active connections (specified by the 'least_conn' statement in the nginx.conf file. Furthermore, if a server crashes the requests can be sent to an available server.
The image below represents the use of NGINX as a load balancer for this application. It is ran on a VM outside of the docker-swarm, allowing each node in the swarm to be indirectly accessed, but without having to disclose each node's IP address to the public, mitigating security threats. The image below is a representation of load balancing that the app uses, however do note that the app currently uses only one worker and manager node.

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

## Project tracking
A simple kanban board on Trello was used for project tracking and planning, as well as user stories, and can be accessed [here](https://trello.com/b/LAOKAzoo/character-generator)
![trello](https://i.imgur.com/dtarL2W.png)
![user story](https://i.imgur.com/LNmNkV9.png)

## Future improvements
### More complexity
The app is currently very simple and only generates a character and a weapon. This could be expanded upon to generate attributes like a character's class or a weapon enchantment for a more immersive and interesting character.

### Selenium Integration Testing
While the integration tests don't seem to be currently necessary (due to the app's simplicity as discussed previously), an integration test using Selenium would be a great additional failsafe against the implementation of errors in the code.



