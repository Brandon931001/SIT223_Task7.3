pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔨 Building Docker Image...'
                sh 'docker build -t garage-system .'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running Tests...'
                script {
                    def workspace = pwd().replaceAll('\\\\', '/')
                    sh """
                        docker run --rm -v "${workspace}:/app" -w /app python:3.10-slim bash -c "pip install pytest && pytest"
                    """
                }
            }
        }




        stage('Code Quality') {
            steps {
                echo '📏 Running pylint...'
                sh 'pip install pylint'
                sh 'pylint app.py'
            }
        }

        stage('Security') {
            steps {
                echo '🔐 Running bandit...'
                sh 'pip install bandit'
                sh 'bandit app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Running the app in Docker...'
                sh 'docker run -d --name garage-app garage-system'
                sh 'docker ps'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up Docker container...'
            sh 'docker rm -f garage-app || true'
        }
    }
}
