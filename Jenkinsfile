pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'pip install -r requirements.txt'  // Install project dependencies
                sh 'pytest test_adventureworks2012.py'  // Run pytest on a specific test file
            }
        }
    }
}
