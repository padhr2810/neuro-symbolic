

# https://minikube.sigs.k8s.io/docs/tutorials/kubernetes_101/module3/

kubectl version

kubectl get nodes

kubectl create deployment kubernetes-bootcamp --image=gcr.io/k8s-minikube/kubernetes-bootcamp:v1

kubectl get deployments
kubectl get pods

kubectl describe pods

echo -e "Starting Proxy. After starting it will not output a response. Please return to your original terminal window\n"; kubectl proxy

export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME

kubectl logs $POD_NAME

kubectl exec $POD_NAME -- env

kubectl exec -ti $POD_NAME -- bash

cat server.js

curl localhost:8080

exit

