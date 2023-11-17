# README for BMI Calculation Application Project

## Introduction
This project demonstrates the setup of a Kubernetes cluster using a WiFi router, 4 Raspberry Pi units, and MicroK8s. The cluster consists of 4 nodes and 2 master controllers. The primary application is a BMI (Body Mass Index) calculation service, segmented into four distinct containerized services: Frontend, Calculator, Classification, and Risk services.

## System Architecture
- **Frontend Service:** Provides the user interface for inputting weight and height.
- **Calculator Service:** Calculates BMI from user-provided data.
- **Classification Service:** Categorizes BMI into different classifications (e.g., underweight, normal, overweight).
- **Risk Service:** Assesses potential health risks associated with the BMI classification.

## Device Checklist 
- 4 Raspberry Pi units
- 1 WiFi router TP-Link TL WR841N

> [!NOTE]
> If master and workers nodes are already install microk8s and set up kubebernetes cluster, can skip to [Application Deployment](#application-deployment)

## Setup and Installation

### Initial Configuration
1. **Prepare Raspberry Pi Units:**
   - Check whether the 64-bit Ubuntu images are installed on pi ```uname -m``` (if not installed, flash the OS on pi)
   - Edit `/boot/cmdline.txt` to include `cgroup_enable=memory cgroup_memory=1`.
   - Reboot each Raspberry Pi.

2. **Install MicroK8s on pi:**
   ```
   sudo apt update
   sudo apt install snapd
   sudo snap install microk8s --classic
   ```
3. **Install MicroK8s on VM:**
   ```
   sudo apt install snapd
   sudo snap install microk8s --classic
   ```

## Kubernetes Cluster Setup

### Introduction
This section outlines the process of setting up a Kubernetes cluster using Raspberry Pi units and MicroK8s. It is intended for a project involving a BMI calculation application.

### Configuration Steps
1. **Prepare Raspberry Pi Units:**
   - Modify `/boot/cmdline.txt` to enable memory cgroup.
   - Set hostnames and passwords.

2. **Install MicroK8s:**
   - Update and install necessary packages.
   - Install MicroK8s using Snap.

3. **Initialize Cluster:**

   3.1 **Initialize Master Node:**
       
   - On the master node, run `sudo microk8s.add-node` to generate a join token.
   - Record the generated `<ip>:<port>/<token>` for worker nodes.

   3.2 **Network Configuration:**
   - Add hostname and IP to `/etc/hosts` of Master.
   - Enable and start `systemd-resolved` in each pi:
     ```
     sudo systemctl enable systemd-resolved
     sudo systemctl start systemd-resolved
     ```
    - Then, ```cd /run/systemd/resolve/``` and make sure there is stuff.

   3.3 **Joining Worker Nodes:**
   - On each worker node, execute:
     ```microk8s join <ip>:<port>/<token> --worker```
   - Follow on-screen instructions to resolve any permission issues.

### Verification
- Use `microk8s status` to confirm the health of the cluster.

## Application Deployment

### Introduction
This section describes the steps to deploy the BMI calculation application within the Kubernetes cluster.


### Build and Deployment Process
1. **Using Pre-built Docker Images:**
   - The Docker images for each service (Frontend, Calculator, Classification, Risk) have already been built and are available in the Docker registry.
   - Pull images directly from the Docker registry:
     ```
     docker pull looknat/classification-service:release-10
     docker pull looknat/calculator-service:release-3
     docker pull looknat/frontend-service:release-2
     docker pull looknat/risk-service:release-2
     ```
   - Note: Building the images is not necessary as they are already available.

2. **Deploying Services Using Kubernetes Configuration Files:**
   - Kubernetes configuration files for each service are already prepared and can be applied directly.
   - Use the `kubectl apply -f <file name>` command to deploy each service. For example:
      ```
      microk8s.kubectl apply -f classification-deployment.yaml
      microk8s.kubectl apply -f calculation-deployment.yaml
      microk8s.kubectl apply -f risk-deployment.yaml
      microk8s.kubectl apply -f frontend-deployment.yaml
      
      microk8s.kubectl apply -f frontend-service.yaml
      microk8s.kubectl apply -f calculator-service.yaml
      microk8s.kubectl apply -f classification-service.yaml
      microk8s.kubectl apply -f risk-service.yaml
      ``` 
   - Alternatively, you can deploy all services at once using the provided start.sh script:
     ```./start.sh```
   - This script contains all the necessary commands to start the services and should be used for a streamlined deployment process.

### Accessing the Frontend Service from Another Host
- To access the Frontend service from a host other than the master node in the same network:
  - Edit the ```final_project_deployment/frontend-service.yaml``` file:
    - Change the externalIPs field to the IP address of the master node that is running the service.
    - After making this change, the Frontend service can be accessed from any host in the network using the URL ```http://<master node ip>:5000```.

### Managing Services
- Use `microk8s.kubectl` to manage pods and services. 
  - For example, to view all running pods:
    ```
    microk8s.kubectl get pods
    ```
  - For detailed service information:
    ```
    microk8s.kubectl get services
    ```
- To see all running pods and the nodes they are running on:
  ```
  microk8s.kubectl get pods -o wide
  ```
- For more detailed information about a specific service:
  ```
  microk8s.kubectl describe pod <pod-name>
  ```
- Removing Services and Deployments (Optional):
  - If you need to delete any service or deployment, you can use the delete.sh script. This script automates the deletion process for all services and deployments: ```./delete.sh```


## Troubleshooting
- Ensure all Raspberry Pis can connect to the internet (`ping google.com`).
- Check and adjust IP addresses in `/etc/hosts` as needed.
- Reinstall MicroK8s if issues persist (`snap remove microk8s`, `snap install microk8s --classic`).
