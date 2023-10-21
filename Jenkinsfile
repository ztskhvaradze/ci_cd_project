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
                sh 'python3 -m venv venv'  // Create a virtual environment named 'venv'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'source venv/bin/activate'  // Activate the virtual environment
                sh 'pip install -r requirements.txt'  // Install project dependencies within the virtual environment
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'source venv/bin/activate'  // Activate the virtual environment
                sh 'pytest test_adventureworks2012.py'  // Run pytest within the virtual environment
            }
        }
    }
}
