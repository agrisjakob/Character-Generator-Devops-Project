pipeline{
	agent any
	environment {
	    TESTING_URI = credentials('TESTING_URI')
	}
	stages{
		stage('Tests'){
			steps{
				sh ". /home/jenkins/.jenkins/workspace/char-gen/CI/jenkins/tests.sh"
			}
		}
	}
}
