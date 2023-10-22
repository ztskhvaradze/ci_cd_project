pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install ODBC Driver for SQL Server') {
            steps {
                sh '''
                    apt-get update
                    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
                    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
                    apt-get update
                    ACCEPT_EULA=Y apt-get install -y msodbcsql17
                   '''
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
