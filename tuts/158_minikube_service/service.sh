#https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/
#https://minikube.sigs.k8s.io/docs/tutorials/kubernetes_101/module4/

# DEBUGGING --- https://stackoverflow.com/questions/75607181/minikube-curl-6-could-not-resolve-host-service-name

minikube start 

kubectl version

kubectl get nodes

# !!! Delete an existing deployment !!!
kubectl get deploy -A
# kubectl delete deploy deploymentname -n namespacename
kubectl delete deploy kubernetes-bootcamp   -n default


kubectl create deployment kubernetes-bootcamp --image=gcr.io/k8s-minikube/kubernetes-bootcamp:v1

kubectl get pods
kubectl get services
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl get services
kubectl describe services/kubernetes-bootcamp

export NODE_PORT=""
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

curl $(minikube ip):$NODE_PORT

kubectl describe deployment

kubectl get pods -l app=kubernetes-bootcamp

kubectl get services -l app=kubernetes-bootcamp

export POD_NAME=""
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

kubectl label pods $POD_NAME version=v1

kubectl describe pods $POD_NAME

kubectl get pods -l version=v1

kubectl delete service -l app=kubernetes-bootcamp

kubectl get services

curl $(minikube ip):$NODE_PORT

kubectl exec -ti $POD_NAME -- curl localhost:8080


