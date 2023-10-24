pipeline {
    agent any

    stages {
        stage('Clone GitHub Repository') {
            steps {
                checkout scm
            }
        }
        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m virtualenv venv'
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
        stage('Git Merge and Push') {
            steps {
                script {
                    // Merge the 'dev' branch into the 'main' branch
                    GITHUB_URL = "https://github.com/ztskhvaradze/ci_cd_project"
                    GITHUB_BRANCH = "main"
                    GITHUB_MERGE_BRANCH = "dev"

                    sh(script: """
                        git config --global user.email "${env.GIT_AUTHOR_EMAIL}"
                        git config --global user.name "${env.GIT_AUTHOR_NAME}"
                        git checkout ${GITHUB_BRANCH}
                        git merge ${GITHUB_MERGE_BRANCH}
                        git push ${GITHUB_URL} ${GITHUB_BRANCH}
                    """, returnStdout: true)
                }
            }
        }
    }
}
