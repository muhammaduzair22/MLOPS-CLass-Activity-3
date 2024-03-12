pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                // Install the required dependencies
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Execute the tests
                sh 'pytest test.py'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    deploy(env.BRANCH_NAME)
                }
            }
        }
    }
}

def deploy(String branchName) {
    if (branchName == 'main') {
        echo "Deploying to production"
       // deploy
    } else if (branchName == 'dev') {
        echo "Deploying to UAT"
      //deploy
    } else {
        echo "Deploying to a non-production/non-UAT branch: ${branchName}"
       //deploy
    }
}