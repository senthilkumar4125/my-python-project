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
        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m unittest discover -s . -p "test_*.py"
                '''
            }
        }
        stage('Build Artifact') {
            steps {
                sh '''
                    mkdir -p build
                    echo "Build artifact created on $(date)" > build/output.txt
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    . venv/bin/activate
                    python deploy.py || echo "No deploy.py found"
                '''
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
