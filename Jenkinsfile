pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = "yeshwanththota33/mlopsproject10"
        DOCKER_HUB_CREDENTIALS = "mlops10"
    }
    stages {
        stage('Checkout Github') {
            steps {
                echo 'Checking out code from GitHub...'
		checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github_token', url: 'https://github.com/Yeshwanththota/MLOPS_Project10_python_Docker_Minikube_GCloudVM_Jenkins_ArgoCD_Webhooks.git']])
		    }
        }        
        stage('Build Docker Image') {
            steps {
               
                script {
                     echo 'Building Docker image...'
                     dockerImage = docker.build("${DOCKER_HUB_REPO}:latest")

                }
            }
        }
        stage('Push Image to DockerHub') {
            steps {
                script {
                    echo 'Pushing Docker image to DockerHub...'
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_HUB_CREDENTIALS) {
                        dockerImage.push('latest')
                        
                    }

                }
                
            }
        }
        stage('Install Kubectl & ArgoCD CLI') {
            steps {
                echo 'Installing Kubectl and ArgoCD CLI...'
            }
        }
        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                echo 'Applying Kubernetes and syncing with ArgoCD...'
            }
        }
    }
}

