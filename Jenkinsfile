pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clone the repository
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies (replace with your actual commands)
                    sh 'pip3 install pytest'
                }
            }
        }

        stage('Execute test.py') {
            steps {
                script {
                    // Execute test.py (replace with your actual commands)
                    sh 'pytest test.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Get the current branch name
                    def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()

                    // Deploy based on branch name
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
