**Tech Stack**

<p align="left"> 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" title="Google Cloud VM" alt="GCP" width="40" height="40"/>&nbsp; 
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp; 
  <img src="https://raw.githubusercontent.com/cncf/artwork/master/projects/argo/icon/color/argo-icon-color.svg" title="ArgoCD" alt="ArgoCD" width="40" height="40"/>&nbsp; 
  <img src="https://raw.githubusercontent.com/kubernetes/minikube/master/site/static/images/logo.png" title="Minikube" alt="Minikube" width="40" height="40"/>&nbsp; 
  <img src="https://img.icons8.com/ios-filled/50/000000/webhook.png" title="Webhooks" alt="Webhooks" width="40" height="40"/>&nbsp; </p>

**Summary:** Implemented a GitOps workflow using Jenkins for CI, ArgoCD for CD, and Minikube for local Kubernetes clusters on a GCP VM. Automated the build, push, and deployment of Docker images, with ArgoCD ensuring continuous delivery and rollback on failure. Integrated GitHub webhooks for end-to-end automation.

![Screenshot 2025-06-20 192836](https://github.com/user-attachments/assets/aa782dc4-80f0-4349-b416-db92826df478)

**Highlights**

1.	GItOps – Truth source
2.	Google Virtual Machines
3.	Minikube (Inside vm we create our own cluster for kubernetes)
4.	Jenkins (CI)
5.	Argocd (only for CD)
6.	Kubernetes

**CI-CD using Jenkins:** First time, we build, push and deploy the image to GKE.
Second time we build, push and deploy, this run deploy step fails and entire workflow fails. App shuts.

**CI- Jenkins/ CD – ArgoCD:** 
Here gitops is used as truth source (commits all the actions).
We push all the code to github -  using Jenkins you make CI pipeline (build and push)- All these commits are recorded in github- Now as the image is pushed- argoCD take cares of deployment part and this is also recorded in github.

If we make changes and run the CI-CD again, and if error occurred in deploy part and failed. But the app never shuts because argocd detects this pipeline is failed and rollback to previous commit (successful pipeline).

Workflow of the project:

Project setup – Data processing- Model training – user app building (flask)- create Dockerfile, Kubernetes manifests – Data & code versioning – VM Instance setup (install minikube, kubectl, docker) – Jenkins setup – github integration with Jenkins -CI pipeline (build & push stages)- push to dockerhub – ArgoCD install & configuration – CD pipeline – argocd deployment and automation (webhooks) – as soon as something pushed to github the webhooks make the whole pipeline build automatically.

 
Step 1

Project setup
1.	Creating virtual Environment in project folder.
2.	Creating required folders and files. (artifacts for outputs, pipeline folder, src where main project code lies, (static , templates for html,css,js and flask automatically finds them in project directory), utils for common functions, requirements and setup file. To make a folder a package we need to create a __init__.py file inside it so that the methods/files can be accessed from other places.
3.	Next, we code for setup, custom exceptions, logger, requirements files (basic things at first like numpy, pandas) .
4.	Then we run setup.py in venv in cmd using pip install -e . This will install all the required dependencies for the project make the project directory ready for next steps. This step automatically created a folder with project name given in the setup.py

Step 2
1.	After jupyter notebook testing we start with Data processing.
2.	Create data_processing.py, code it and test. You should see the artifacts in the project directory.
3.	Now model_training.py in src, code it and test. Should see the model.pkl in the artifacts.
4.	Create training_pipeline.py in pipeline folder, code and run.

Step 3
User App building using Flask
1.	Create application.py in root , code and test. Make sure flask in requirements.
2.	Create index.html, style.css and code, Run.

Step 4

Data & Code versioning, Dockerfile, Manifests building
1.	Create Dockerfile, code it
2.	Create manifests folder in root and create deoplyment.yaml , service.yaml and code it.
3.	Create gitignore in the project.
4.	Now push all the code to github after creating the repo.

Step 5

Google cloud VM instance setup and Minikube Configurations
1.	Go to GCP console, search for VM instances- compute Engine- create VM- select 16GB Ram under standard- select ubuntu in OS – in networking tick for allow HTTP traffic, HTTPS traffic, allow load balancer health checks, IP forwarding-create.
2.	After creating, let’s connect to the machine. In the same page go to the connect and select SSH and open in new window. It is your VM created just before.
3.	Now we need to copy our project code to this VM.
4.	If while cloning , if it shows git is not found, then likely you need to install it. So sudo apt update
5.	sudo apt install git -y
6.	Now create a token in github. Go to settings -developer settings- tokens(classic)-generate one for general use- give atleast repo access-copy the token. Now in VM run the clone cmd and enter github username and password (paste the token). Now your github project is cloned into VM. Run ls to see the project.
7.	Go inside the project using cd
8.	Now we need to install docker inside the VM.
9.	Search web , docker for ubuntu in web and install.
10.	https://docs.docker.com/engine/install/ubuntu/
11.	Copy the command under “setup docker’s apt repository” and paste in VM, run.
12.	Now copy the command in the same page for installing packages. Run in VM.
13.	Now verify with next cmd in same page.
14.	Now we done installing docker in VM.
15.	https://docs.docker.com/engine/install/linux-postinstall/
16.	Run first 4 cmds in this links.
17.	Now we need to configure the docker. So in the same page under configure docker copy the first 2 commands and run in VM.
18.	Let’s check if docker is active by running systemctl status docker
19.	It should show active running in green. Ctrl c to exit

Install and configure minikube in VM
1.	Go to https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download
2.	Copy the first 2 cmds and run in VM
3.	Now start by running minikube start
4.	We need to install kubectl now by running below cmds.
5.	curl -LO  “https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl”
6.	sudo snap install kubectl –classic
7.	to check kubectl version –client
8.	Done

Step 6

Jenkins installation and configuration on VM
1.	Minikube inside docker, Jenkins inside docker, so Jenkins inside minikube. This is docker in docker.
2.	docker network ls
3.	we need to make sure minikube and Jenkins run on the same server
4.	follow the material for installing Jenkins in VM.
5.	Copy the full cmd and run in VM.
6.	Then docker ps
7.	You will see the Jenkins image 
8.	Now run docker logs Jenkins
9.	It will give you password. Copy
10.	Now what to do with this pwd. How to open Jenkins?
11.	First go to gcp-search firewall – network security – create firewall rule – give name – targets (select all instances in the network)-source IPV4 ranges (give 0.0.0.0/0)-protocols and ports (allow all)-create
12.	 Now go to gcp-VM instance and copy external IP and add :8080
13.	You will see Jenkins opening and asking for pwd. Now paste the pswd here.
14.	Install suggested plugnis
15.	Create user by giving details. Continue
16.	Go to dashboard – manage Jenkins – Plugins – select docker, docker pipeline, Kubernetes and install .
17.	Now restart Jenkins by running docker restart docker name(Jenkins our case)
18.	Sign in
19.	Now we need to install dependencies like python
20.	Go to the material and run the cmds line by line
21.	Restart Jenkins after step 20
22.	Refresh Jenkins page.
23.	Now we have installed and configured Jenkins on our VM successfully.

Step 7

GitHub Integration with Jenkins
1.	Firs go to the github token we generated before and give more permissions to it (repo, workflow, admin:org, admin:public_key, admin:repo_hook, admin:org_hook) and update.
2.	Go to Jenkins dashboard – manage Jenkins – credentials – system- global-add- username(github username) – pswd (paste the token)-given some ID and description- create.
3.	Go to dashboard-new item- give name-select pipelines-OK-in configure -pipeline-definition (select script from SCM)- repositoty URL (paste the https URL from github repo under code)-select credentials-change to main branch if not before- apply- save.
4.	Now go to pipeline syntax – under sample step (select checkout)- give repo URL-credentials-main-generate syntax-copy.
5.	Now we need to create Jenkins file.
6.	Lets do it form VM. Run vi JenkinsfIle 
7.	We don’t have vi editor installed on our VM. So let’s install by 
8.	sudo apt update
9.	sudo apt install vim -y
10.	now run vi Jenkinsfile
11.	now take the copied syntax and paste in the material (in the jenkinsfile under first echo). Copy all the code and paste in VM and add :wq! At last, now run
12.	ls
13.	you will see the file in the project now.
14.	This is way to create the file inside the VM
15.	Time to connect github repo
16.	In VM, run the below one by one
17.	 git config –global user.email “give your email here”
18.	 git config –global user.name “give name”
19.	 Git add .
20.	Git commit -m “commit message”
21.	Git push origin main
22.	It will ask for username and pswd (token from github)
23.	 Now you will see the Jenkinsfile in github which means the github integration is successful with jenkins.
24.	 Go to Jenkins and build. After successful build you will see all the project files in the Jenkins/projects/workspaces.
25.	Done

Step 8

CI pipeline
1.	We will build docker image and push to dockerhub.
2.	Go to Jenkins dashboard- manage Jenkins- tools- in the bottom docker installations-add-give name-tick for install automatically- for add installer (select download from docker.com)-latest-apply-save
3.	Now docker is installed on Jenkins.
4.	Pull the updates we made through VM in before steps to github. We need them in local (vscode). So, git pull origin main. You will see the pulled version from github.
5.	Search web for dockerhub- sign in-create repo
6.	We need a token for dockerhub also. So go to profile-settings-personal access tokens- give name – access permissions (read,write,detete)-generate-keep the page open for next steps
7.	Go to Jenkins dashboard – manage Jenkins – credentials – system- global-add- username(dockerhub username from 6) – pswd (paste the token from 6)-given some ID and description- create.
8.	Make changes to Jenkinsfile and deployment.yaml file
9.	Push the changes to github.
10.	 Go to Jenkins and build.
11.	 You should see the success message in console output.

Step 9

Argo CD Installation and Configuration
1.	First in VM, create a namespace by running kubectl create ns argocd
2.	Kubectl get namespace
3.	You will see the one we created now.
4.	From material, let’s install and configure argo cd. Run one by one.
5.	After running first command. Run kubeclt get all -n argo
6.	Make sure everything is running. Don’t proceed until this.
7.	kubectl get svc -n argocd
8.	you will see the argocd-server type is clusterIP but we need to convert to NodePort , because clusterIP can be accessed only internally but the other one accessed externally also.
9.	Kubectl edit svc argocd-server -n argocd
10.	You will see a argocd configuration file, search for clusterIp, delete it and write NodePort, press ctrl c, then give :wq!
11.	Now if you run kubectl get svc -n argocd , you will see the type is changed for argocd-server.
12.	 Now run the 2nd cmd in materia. Change the port to what you see for argocd-server
13.	Now go to gcp-vm page-copy the External IP-copy-open in another page- add to to :port_number_you_see_in_argocd_server
14.	For example 35.192.126.138:31581 , here 31581 is the port I see for me in argocd-server when I run kubectl get svc -n argocd
15.	Now when you go that address-not safe- advanced- continue- you will see the argocd page.
16.	 Now go to gcp-vm page- connect to another window- because the previous will be froze after we run 2nd cmd.
17.	 Go to project using cd
18.	 Now run the third cmd, you will get pwd. Take it and go and sign in the argocd that you opened in step 15. Username admin and pwd
19.	You are in argocd now.
20.	Got to root by running cd ..
21.	The ls -la , it will show all the files in the root. You will see a .kube file which all the configurations. We need to modify it according to us.
22.	So run ls -la .kube/
23.	It has two files. We need to modify config file
24.	cat .kube/config
25.	copy all content and paste in notepad
26.	do some edits in that like add -data to these certificate-authority-data, client-certificate-data, client-key-data
27.	 now we edit their (above three) contents
28.	Copy the first one path-open second vm – we will convert the path to base64-  so in VM cat paste path | base64 -w 0; echo
29.	It will give you encoded thing – copy – paste it in the place of path in notepad.
30.	Now second one and third path, do the same as before
31.	We need to save this file. So open gitbash (if you had installed git cli, you will have this in pc)- cd downloads – vi kubeconfig- it will give space to write – copy all from notepad- paste here – ctrl c – write :wq!- close gitbash
32.	You will see the file now saved in downloads
33.	This is our configuration file for our Kubernetes
34.	 Now go to Jenkins – manage jenkins – credentials – global – select secret file -upload our file- give id and description-create
35.	 Now go project – pipeline – configure – go to bottom and click the pipeline syntax - Sample Step (select Kubernetes one) – for Kubernetes server endpoint , go to VM run kubectl cluster-info, you will see control pane is running at “URL”, copy and paste in server endpoint- then select the credentials you created in step 34- generate- copy
36.	 So, till now we configured our argoCD.

Installing argoCD and Kubectl in docker container (In Vm instance we already did but not in docker container)
1.	In VScode , modify the jenkinsfile using material.
2.	Copy the script from step 35 and paste in the jenkinsfile in the pply Kubernetes & Sync App with ArgoCD stage
3.	 Now copy the last cmd from the material and change the IP address from the argocd page running in your pc.
4.	Save the file

Step 10

CI-CD Automation using Jenkins, ArgoCD, Webhooks
1.	Go to argocd page -  settings – connect repo – VIA HTTPS -Type(git)-name it-project (default)- URL (github under code https one)-username (from github)- pwd (github token)-connect
2.	You should see a successful message there.
3.	Now go to applications- new app- application name (you should give the same name what you have given in the Jenkins file argocd app sync gitopsapp, here name give is gitopsapp – so give the same- Project Name (default)- sync policy (automatic)- check the prune resources and self hal – source select the github url- revision(main)-path(manifests)-cluster URL (select the one given)- namespace(argocd, we created in the start)-create
4.	Now click on the app card. Things are running. Wait until HEALTHY message is shown.
5.	Push the changes in Jenkins to github.
6.	Now go to Jenkins-project-build
7.	Wait until successful build.
8.	Now we need to make the minikube accessible externally also, for now it is only accessible internally. This is the reason if we go to pods running in argocd- logs – take the URL and if we put it in search- it won’t work.
9.	So, let’s do this. In VM run kubectl get deploy -n argocd
10.	 You will see pods running
11.	 Run minikube tunnel (this command makes the minikube available externally also)
12.	Now this ssh terminal is froze.
13.	So go and open another terminal and go to project dir using cd.
14.	Make sure other two terminals are running. One is argocd, other is minikube from step 11
15.	Run in new terminal kubectl port-forward svc/mlops-service -n argocd --address 0.0.0.0 9090:80
16.	Here mlops-service is your service name in service.yaml, should be same
17.	9090 is new port we are giving where our app will be available, because 8080 is given already to argocd. And 80 is where it is listening.
18.	 Now copy external IP in VM page in gcp. Paste in URL tab and add :9090
19.	It will run successfully.
20.	Final step is webhooks.
21.	Why we need because, everytime we push the changes from vscode to github, we need to go to Jenkins and build. To automate this we use webhooks.
22.	Go to github. Settings – webhooks- add-payload url(give Jenkins url until http://35.192.126.138:8080/  and add github-webhook/ so it is http://35.192.126.138:8080/ github-webhook/)- content type (application/json)-add webhook.
23.	Go to Jenkins-project-configure-triggers (tick the github hook trigger for GITScm polling)-apply-save
24.	Now to test, change some stage name in Jenkins file and push the changes to github.
25.	Now the build will automatically trigger in Jenkins and argocd will be synced. Everything is synced and you can open the app with External Ip in VM and add :9090
26.	Clean up. Delete VM
27.	Done



