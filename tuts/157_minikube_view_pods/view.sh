

# https://minikube.sigs.k8s.io/docs/tutorials/kubernetes_101/module3/

minikube start 

kubectl version

kubectl get nodes

# !!! Delete an existing deployment !!!
kubectl get deploy -A
# kubectl delete deploy deploymentname -n namespacename
kubectl delete deploy kubernetes-bootcamp-v2   -n default


kubectl create deployment kubernetes-bootcamp --image=gcr.io/k8s-minikube/kubernetes-bootcamp:v1

kubectl get deployments
kubectl get pods

kubectl describe pods
         # view what containers are inside that Pod and what images are used to build those containers
         #  details about the Pod’s container: IP address, the ports used and a list of events 
         # describe can be used for: node, pods, deployments etc.

         # Run the command below in a NEW TERMINAL WINDOW to run the proxy
echo -e "Starting Proxy. After starting it will not output a response. Please return to your original terminal window\n"; kubectl proxy
        # pods = we need to proxy access to them so we can debug and interact with them
        
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

        # To see the output of our application, run a curl request.
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME

kubectl logs $POD_NAME

kubectl exec $POD_NAME -- env

kubectl exec -ti $POD_NAME -- bash

cat server.js

curl localhost:8080

exit

