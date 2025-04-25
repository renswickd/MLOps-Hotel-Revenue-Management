pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage('cloning GitHub repo to Jenkins'){
            steps{
                script{
                    echo 'cloning GitHub repo to Jenkins...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-github-pat', url: 'https://github.com/renswickd/MLOps-Hotel-Revenue-Management.git']])
                }
            }
        }

        stage('Setting up our virtual environment and installing dependencies'){
            steps{
                script{
                    echo 'Setting up our virtual environment and installing dependencies...'
                    sh '''
                        python3 -m venv $VENV_DIR
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                    '''
                
                }
            }
        }
    }
}