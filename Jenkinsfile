pipeline {
    agent any

    stages {
        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                    sudo apt-get update -y
                    sudo apt-get install -y python3-venv python3-full
                    if [ ! -d "venv" ]; then
                        python3 -m venv venv
                    fi
                    . venv/bin/activate
                    python -m ensurepip --upgrade
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest || true
                '''
            }
        }

        stage('Build Artifact') {
            steps {
                sh '''
                    mkdir -p dist
                    zip -r dist/app.zip * -x "venv/*"
                '''
                archiveArtifacts artifacts: 'dist/app.zip', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy step (e.g., copy to server or S3)'
            }
        }
    }

    post {
        always {
            echo "Pipeline Finished!"
        }
        failure {
            echo "Pipeline Failed. Check logs."
        }
    }
}
