pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t two-tier-app .'
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh 'docker rm -f two-tier-app || true'
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    sh '''
                    docker run -d \
                    --name two-tier-app \
                    -p 5000:5000 \
                    two-tier-app
                    '''
                }
            }
        }
    }
}