# https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/

kubectl get deployments

kubectl get pods

kubectl describe pods

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/k8s-minikube/kubernetes-bootcamp:v2

kubectl get pods

kubectl describe services/kubernetes-bootcamp

export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

curl $(minikube ip):$NODE_PORT

kubectl rollout status deployments/kubernetes-bootcamp

kubectl describe pods

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/k8s-minikube/kubernetes-bootcamp:v10

kubectl get deployments

kubectl get pods

kubectl describe pods

kubectl rollout undo deployments/kubernetes-bootcamp

kubectl get pods

kubectl describe pods

