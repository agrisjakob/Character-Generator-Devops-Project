pipeline{
	agent any
	env.TESTING_URI = credentials('TEST_DB_URI')
	stages{
		stage('Tests'){
			steps{
				sh ". /home/jenkins/.jenkins/workspace/char-gen/CI/jenkins/tests.sh"
			}
		}
	}
}
