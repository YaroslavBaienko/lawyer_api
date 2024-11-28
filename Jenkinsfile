pipeline {
    agent any
    environment {
        VENV_DIR = 'venv' // Путь к виртуальному окружению
        APP_PORT = '8000' // Порт, на котором будет работать приложение
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: 'master',
                    credentialsId: 'ubuntu2-vbox',
                    url: 'https://github.com/YaroslavBaienko/lawyer_api.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Application') {
            steps {
                echo 'Starting the application...'
                sh '''
                source ${VENV_DIR}/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port ${APP_PORT} > uvicorn.log 2>&1 &
                '''
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Application successfully deployed!'
        }
        failure {
            echo 'Deployment failed. Check the logs for details.'
            sh 'cat uvicorn.log'
        }
    }
}
