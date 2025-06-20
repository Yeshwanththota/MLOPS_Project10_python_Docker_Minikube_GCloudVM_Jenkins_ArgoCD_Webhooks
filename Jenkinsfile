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
                sh '''
                    echo 'installing Kubectl & ArgoCD cli...'
                    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                    chmod +x kubectl
                    mv kubectl /usr/local/bin/kubectl
                    curl -sSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
                    chmod +x /usr/local/bin/argocd
                '''
            }
        }
        stage('Apply Kubernetes & Sync App with ArgoCD') {
            steps {
                script {
                    kubeconfig(credentialsId: 'kubeconfig', serverUrl: 'https://192.168.49.2:8443') {
                        sh '''
                        argocd login 35.192.126.138:31581 --username admin --password $(kubectl get secret -n argocd argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d) --insecure
                        argocd app sync gitopsapp
                        '''
                }         
                
            }
        }
    }
}

