pipeline {
    agent {
        label 'ubuntu2-vbox'
    }

    environment {
        PROJECT_DIR = "/home/attor/workspace/lawyer-api"
        VENV_DIR = "${PROJECT_DIR}/venv"
    }

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    echo "Setting up system dependencies..."
                    sh '''
                    echo "your_password" | sudo -S apt update
                    echo "your_password" | sudo -S apt install -y python3-distutils python3-venv
                    '''
                    echo "Setting up Python environment..."
                    sh '''
                    cd ${PROJECT_DIR}
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip setuptools
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    echo "Running the application..."
                    sh '''
                    cd ${PROJECT_DIR}
                    . ${VENV_DIR}/bin/activate
                    nohup uvicorn main:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
                    '''
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    echo "Checking if the application is running..."
                    sh 'curl -f http://127.0.0.1:8000 || exit 1'
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful."
        }
        failure {
            echo "Deployment failed. Check logs for details."
            sh '''
            if [ -f ${PROJECT_DIR}/uvicorn.log ]; then
                cat ${PROJECT_DIR}/uvicorn.log
            fi
            '''
        }
    }
}
