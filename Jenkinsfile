stage('Setup Virtual Environment & Install Dependencies') {
    steps {
        sh '''
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
