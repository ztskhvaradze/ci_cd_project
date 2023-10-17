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
                    env.BRANCH_NAME = 'dev'
                    echo "The build is running on the branch: ${env.BRANCH_NAME}
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
