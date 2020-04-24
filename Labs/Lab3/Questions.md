# Assignment 3 - Kubernetes
## Question 1

### 1. Describe differences between master node and worker nodes?

The master coordinates the cluster while the nodes are the workers that run different applications. The master coordinate all activities such as scheduling and maintanance. The node is a VM or physical computer within the cluster.

### 2. What version of minkube is used in the tutorial?

minikube version: v1.8.1

## Question 2

### 1. Describe kubectl?

Interaction with kubernetes cluster.  

### 2. What is the output of kubectl get nodes

Get the current active nodes, their status, age, role and version

### 3. What is the ouput of kubectl get deployments

Error: must specify one of -f and -k. Otherwise if we specify name and image we deploy and application. If we already deployed an image we get their name, ready, up to date, avaibable and age.

## Question 3

### 1. What is a pod, describe its entities?

A group of one ore more applications. Shared storage,Networking (Unique Ip addresses),Information about how to run each container

### 2. What information do the kubectl describe pods command give

Information of container, IP address, the ports and events

## Question 4
### 1. Describe what a service is in Kubernetes?

Services allow your applications to receive traffic.

### 2. What do the kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080 command do?

Expose a service to external traffic on port 8080.

## Question 5
### 1. How do labels and Label Selector objects relate to a Service?

Allows logical operation on objects in kubernetes, Example: Embed version tags, Classify an object using tags

### 2. What is the outputkubectl get rs command?

ReplicaSet created by the Deploymen: NAME, READY, UP-TO-DATE, AVAILABLE, AGE

## Question 6
### 1. Describe rolling updates in Kubernetes?

Update pods without having any downtime. Only update pods with available resources. 

### 2. Whats doe the kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=jocatalin/kubernetes-bootcamp:v2 command do?

Updates an pod to another version

## Question 7
Based on the command "kubectl run derp --image=nginx --replicas=1 --port=1234
Worth noticing is that replicas is depricated and should no longer be used (and is therefor ignored by the system). This is based on the error message "Flag --replicas has been deprecated, has no effect and will be removed in the future.".

### 1. What does the web browser show when you access the web server?

No, this was not possible with the command given.

### 2. What is the output from the kubectl get pods command

|NAME       |  TYPE      |  CLUSTER-IP |  EXTERNAL-IP |  PORT(S) |  AGE   |
|-----------|------------|-------------|--------------|----------|--------|
|kubernetes |  ClusterIP |  10.96.0.1  |  <none>      |  443/TCP |  5m55s |

### 3. What is the output from the kubectl get deployment command

|NAME  |  READY |  STATUS  |  RESTARTS |  AGE  |
|------|--------|----------|-----------|-------|
|nginx |  1/1   |  Running |  0        |  115s |

### 4. What is the output from the kubectl get services command

No resources found in default namespace.

__Alternative approach__

However if we follow the tutorial instead and ignore that command we can get the following based on the questions above:

We could access the site by calling the service nginx1 "minicube service nginx1". This will give some info and open up the browser. 

The output started with the following: "Welcome to nginx! If you see this page, the nginx web server is successfully installed and working. Further configuration is required."

### Table 1
| NAME                     | READY |  STATUS  |  RESTARTS |  AGE |
|--------------------------|-------|----------|-----------|------|
| nginx1-56db585f94-qf6s6  | 1/1   |  Running |  0        |  37s |

### Table 2

|NAME    | READY | UP-TO-DATE |  AVAILABLE |  AGE    |
|--------|-------|------------|------------|---------|
|nginx1  | 1/1   |  1         |   1        |   6m24s |

### Table 3

|NAME       |  TYPE      |  CLUSTER-IP    |  EXTERNAL-IP |  PORT(S)      |  AGE   |
|-----------|------------|----------------|--------------|---------------|--------|
|kubernetes |  ClusterIP |  10.96.0.1     |  <none>      |  443/TCP      |  13m   |
|nginx1     |  NodePort  |  10.101.133.13 |  <none>      |  80:32023/TCP |  3m32s |