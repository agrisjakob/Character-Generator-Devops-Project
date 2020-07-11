pipeline{
	agent any

	stages{
		stage('Tests'){
			environment { 	
			 TESTING_URI = credentials('TEST_DB_URI')
			}
			steps{
				sh ". /home/jenkins/.jenkins/workspace/char-gen/CI/jenkins/tests.sh"
			}
		}
		stage('Build and push docker images'){
			environment {
				docker_password = credentials('docker_password')
				docker_username = credentials('docker_username')
			}
			steps{
				sh ". /home/jenkins/.jenkins/workspace/char-gen/CI/jenkins/build.sh"
			}
		}
	}
}
