pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "instant-icon-457207-s8"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
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

        stage('Building and pushing Docker image to GCR'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                        echo 'Building and pushing Docker image to GCR...'
                        sh '''
                            export PATH=$PATH:$(GCLOUD_PATH)
                            gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                            gcloud config set project ${GCP_PROJECT}
                            gcloud auth configure-docker --quiet
                            docker build -t gcr.io/${GCP_PROJECT}/hotel-revenue-management:latest .
                            docker push gcr.io/${GCP_PROJECT}/hotel-revenue-management:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Google Cloud Run'){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script{
                        echo 'Deploy to Google Cloud Run...'
                        sh '''
                            export PATH=$PATH:$(GCLOUD_PATH)
                            gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                            gcloud config set project ${GCP_PROJECT}
                            gcloud run deploy hotel-revenue-management \
                            --image=gcr.io/${GCP_PROJECT}/hotel-revenue-management:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow-unauthenticated
                            
                        '''
                    }
                }
            }
        }
    }
}