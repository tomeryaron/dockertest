pipeline {
    agent any
    stages {
        stage('ONE') {
            steps {
                sh 'pip install docker'
                sh 'python DockerAndJenkins.py'
            }
        }
    }
}
