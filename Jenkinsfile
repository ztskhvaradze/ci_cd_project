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
                expression { env.BRANCH_NAME == 'dev' }
            }
            steps {
                echo "The build is running on the branch: ${env.BRANCH_NAME}"
                echo 'Testing the app' 
            }
        }
        stage('Deploy') { 
            steps {
                echo 'Deploying the app'
            }
        }
    }
}
