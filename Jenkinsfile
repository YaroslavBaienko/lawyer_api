pipeline {
    agent {
        label 'ubuntu-agent' // Задаем метку для агента
    }

    environment {
        VENV_DIR = "venv" // Директория виртуального окружения
        APP_DIR = "/home/jenkins/lawyer_api" // Директория проекта на агенте
        HOST = "0.0.0.0" // Хост для запуска приложения
        PORT = "8000" // Порт для запуска приложения
        LOG_FILE = "uvicorn.log" // Лог файл для записи логов uvicorn
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo "Cloning the repository"
                }
                // Клонирование кода на агенте
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    echo "Setting up Python environment"
                }
                // Установка виртуального окружения и зависимостей
                sh '''
                cd ${APP_DIR}
                if [ ! -d ${VENV_DIR} ]; then
                    python3 -m venv ${VENV_DIR}
                fi
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                script {
                    echo "Running FastAPI application"
                }
                // Остановка старого процесса на порту
                sh '''
                PID=$(lsof -t -i:${PORT})
                if [ ! -z "$PID" ]; then
                    kill -9 $PID
                fi
                '''
                // Запуск приложения через uvicorn
                sh '''
                cd ${APP_DIR}
                source ${VENV_DIR}/bin/activate
                nohup uvicorn main:app --host ${HOST} --port ${PORT} > ${LOG_FILE} 2>&1 &
                '''
            }
        }

        stage('Health Check') {
            steps {
                script {
                    echo "Checking if application is running"
                }
                // Проверка доступности сервиса
                sh '''
                sleep 5
                curl -f http://127.0.0.1:${PORT} || exit 1
                '''
            }
        }
    }

    post {
        success {
            echo "Application deployed successfully!"
        }
        failure {
            echo "Deployment failed. Check logs for details."
            sh '''
            cat ${APP_DIR}/${LOG_FILE}
            '''
        }
        always {
            echo "Pipeline execution completed."
        }
    }
}
