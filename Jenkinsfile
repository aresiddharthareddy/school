pipeline {
    agent any

    environment {
        IMAGE_NAME = 'django-school-app'
        CONTAINER_NAME = 'django-school-container'
        HOST_PORT = '8000'         // change if needed
        CONTAINER_PORT = '8000'    // Django default
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }
}
