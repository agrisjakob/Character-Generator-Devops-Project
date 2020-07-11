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
	}
}
