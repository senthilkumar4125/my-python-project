pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/senthilkumar4125/my-python-project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
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
