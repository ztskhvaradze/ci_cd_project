pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo 'Building the app' 
            }
        }
        stage('Test') { 
            when {
                expression {
                    BRANCH_NAME = 'dev'
                }
            }
            steps {
                echo 'testing the app' 
            }
        }
        stage('Deploy') { 
            steps {
                echo 'Deploying the app'
            }
        }
    }
}
