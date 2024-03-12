pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Using a virtual environment for isolation
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Execute test.py') {
            steps {
                script {
                    sh 'python test.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()

                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // Add your production deployment commands here
                    } else {
                        echo 'Deploying to UAT'
                        // Add your UAT deployment commands here
                    }
                }
            }
        }
    }
}
