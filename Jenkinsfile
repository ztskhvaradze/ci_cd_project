pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m virtualenv venv'  // Create a virtual environment named 'venv' using virtualenv
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '. venv/bin/activate'  // Activate the virtual environment (for non-Bash shells)
                sh 'pip install -r requirements.txt'  // Install project dependencies within the virtual environment
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate'  // Activate the virtual environment (for non-Bash shells)
                sh 'pytest test_adventureworks2012.py'  // Run pytest for the test_adventureworks2012.py file
            }
        }
    }
}
