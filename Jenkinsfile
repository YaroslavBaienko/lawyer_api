pipeline {
    agent { label 'ubuntu2-vbox' }

    environment {
        VENV_PATH = "${WORKSPACE}/venv"
        APP_LOG = "${WORKSPACE}/uvicorn.log"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                echo 'Setting up system dependencies...'
                sh '''
                echo '1334keiNdeltA$' | sudo -S apt update -y
                echo '1334keiNdeltA$' | sudo -S apt install -y python3 python3-venv python3-pip build-essential libssl-dev libffi-dev python3-dev
                python3 -m venv ${VENV_PATH}
                . ${VENV_PATH}/bin/activate
                pip install --upgrade pip setuptools wheel
                pip cache purge
                pip install numpy --only-binary :all:
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting the FastAPI application...'
                sh '''
                if lsof -i:8000; then
                    echo "Port 8000 is already in use. Killing the process..."
                    kill -9 $(lsof -t -i:8000)
                fi
                . ${VENV_PATH}/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug > ${APP_LOG} 2>&1 &
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Waiting for the application to start...'
                sh 'sleep 5'
                echo 'Checking if the application is running...'
                script {
                    def response = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000', returnStdout: true).trim()
                    if (response != '200') {
                        error "Application is not running properly. HTTP status code: ${response}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        failure {
            echo 'Deployment failed. Check logs for details.'
            sh '''
            if [ -f ${APP_LOG} ]; then
                cat ${APP_LOG}
            fi
            '''
        }
        success {
            echo 'Deployment succeeded. Application is running.'
        }
    }
}
