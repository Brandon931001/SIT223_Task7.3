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
            def windowsPath = pwd()
            def dockerPath = windowsPath.replaceAll('^([A-Z]):\\\\', '/$1/').replaceAll('\\\\', '/').toLowerCase()

            sh """
                docker build -f Dockerfile-pytest -t garage-test-image .
                docker run --rm -v ${dockerPath}:/app garage-test-image
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
