pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/YaroslavBaienko/lawyer_api.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Создаем виртуальное окружение
                python3 -m venv venv
                source venv/bin/activate

                # Устанавливаем зависимости
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy to Node') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'remote-node', // Настройка SSH-соединения
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**',
                                    remoteDirectory: '/home/ubuntu/lawyer_api', // Путь на ноде
                                    removePrefix: '',
                                    execCommand: '''
                                    cd /home/ubuntu/lawyer_api
                                    source venv/bin/activate
                                    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
                                    '''
                                )
                            ],
                            verbose: true
                        )
                    ]
                )
            }
        }
    }
}
