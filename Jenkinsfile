pipeline{
    agent any

    stages{
        stage('cloning GitHub repo to Jenkins'){
            steps{
                script{
                    echo 'cloning GitHub repo to Jenkins...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-github-pat', url: 'https://github.com/renswickd/MLOps-Hotel-Revenue-Management.git']])
                }
            }
        }
    }
}