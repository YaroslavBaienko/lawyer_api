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
                python3.10 -m venv ${VENV_PATH}
                . ${VENV_PATH}/bin/activate
                pip install --upgrade pip setuptools wheel
                pip install numpy --only-binary :all:
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting the FastAPI application...'
                sh '''
                . ${VENV_PATH}/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 > ${APP_LOG} 2>&1 &
                '''
            }
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
