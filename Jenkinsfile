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
                sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                   '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_adventureworks2012.py
                   '''
            }
        }
    }
}
