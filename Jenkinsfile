pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Директория виртуального окружения
        APP_PORT = '8000' // Порт для запуска приложения
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', credentialsId: 'ubuntu2-vbox', url: 'git@github.com:YaroslavBaienko/lawyer_api.git'
            }
        }

        stage('Install Python and Dependencies') {
            steps {
                sh '''
                # Убедиться, что Python установлен
                sudo apt update
                sudo apt install -y python3 python3-venv python3-pip

                # Создать виртуальное окружение
                python3 -m venv ${VENV_DIR}

                # Активировать виртуальное окружение и установить зависимости
                source ${VENV_DIR}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run FastAPI Application') {
            steps {
                sh '''
                # Активировать виртуальное окружение
                source ${VENV_DIR}/bin/activate

                # Убедиться, что процесс на порту не занят
                lsof -ti:${APP_PORT} | xargs -r kill -9 || true

                # Запустить приложение в фоновом режиме
                nohup uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT} &
                '''
            }
        }
    }

    post {
        always {
            echo 'Build complete!'
        }
        success {
            echo 'FastAPI application successfully deployed!'
        }
        failure {
            echo 'Build failed. Please check the logs for errors.'
        }
    }
}
