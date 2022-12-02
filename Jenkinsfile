pipeline {
    agent {
        label 'agent1'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'python3.10 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python3 -m pytest -s'
            }
        }
    }
}