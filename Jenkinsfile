pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-username/your-python-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'sudo apt update && sudo apt install -y python3 python3-pip'
                sh 'pip3 install --upgrade pip'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_sample.py'
            }
        }
        stage('Build Artifact') {
            steps {
                sh 'mkdir -p build && echo "Build artifact created" > build/output.txt'
            }
        }
        stage('Deploy') {
            steps {
                sh 'python3 deploy.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline Finished!'
        }
        success {
            echo 'Build and Deployment Successful!'
        }
        failure {
            echo 'Pipeline Failed. Check logs.'
        }
    }
}
