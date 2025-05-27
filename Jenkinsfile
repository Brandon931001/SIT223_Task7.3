pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔨 Building Docker Image...'
                sh 'docker build -f Dockerfile -t garage-system .'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running Tests...'
                script {
                    sh """
                        docker build -f Dockerfile-pytest -t garage-test-image .
                        docker run --rm garage-test-image
                    """
                }
            }
        }

        stage('Code Quality') {
            steps {
                echo '📏 Running pylint...'
                sh 'pip install pylint'
                sh 'pylint garage/core.py'
            }
        }

        stage('Security') {
            when { expression { true } }
            steps {
                echo '🔐 Running bandit...'
                sh 'pip install bandit'
                sh 'bandit garage/core.py || true'
            }
        }



        stage('Deploy') {
            when { expression { true } }
            steps {
                echo '🚀 Running the app in Docker...'
                sh 'docker run -d --name garage-app garage-system || true'
                sh 'docker ps'
            }
        }


    post {
            always {
                echo '🧹 Cleaning up Docker container...'
                script {
                    def result = sh(script: "docker ps -a --format '{{.Names}}' | grep -w garage-app || true", returnStdout: true).trim()
                    if (result == "garage-app") {
                        sh 'docker rm -f garage-app'
                    } else {
                        echo '🟡 No container named garage-app found. Skipping removal.'
                    }
                }
            }
        }
    }

}
