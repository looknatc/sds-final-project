microk8s.kubectl apply -f classification-deployment.yaml
microk8s.kubectl apply -f calculation-deployment.yaml
microk8s.kubectl apply -f risk-deployment.yaml
microk8s.kubectl apply -f frontend-deployment.yaml
microk8s.kubectl apply -f frontend-service.yaml
microk8s.kubectl apply -f calculation-service.yaml
microk8s.kubectl apply -f classification-service.yaml
microk8s.kubectl apply -f risk-service.yaml
