# sds-final-project
Project name: BMI calculation application

Services: 
- Frontend Service
- Calculator Service
- Classification Service
- Risk Service

How to create kube-cluster:
1. add node to cluster by run `microk8s add-nodes` in master node to generate token
2. add hostname and ip of 4 leaf nodes and another master node to /etc/hosts of first master node 
3. join the worker node to cluster by using `microk8s join <ip>:<port>/<token> --worker`

How to deploy application:
1. 

   


