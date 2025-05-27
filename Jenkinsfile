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
            when {
                expression { true } // always run
            }
            steps {
                echo '🔐 Running bandit...'
                sh 'pip install bandit || true'
                sh 'bandit garage/core.py || true'
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
            script {
                try {
                    sh 'docker rm -f garage-app'
                } catch (err) {
                    echo "⚠️ No container to remove, likely skipped deploy: ${err.getMessage()}"
                }
            }
        }
    }

}
