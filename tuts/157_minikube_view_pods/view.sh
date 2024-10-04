# Status: this all works.
# added this to make sure only one pod name
        #     export POD_NAME=""

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

         # !!!!!!!!!!!!!!!!!!!!!!   *************  NEW TERMINAL  *************   !!!!!!!!!!!!!!!!!!!!!!
         # Run the command below in a NEW TERMINAL WINDOW to run the proxy
echo -e "Starting Proxy. After starting it will not output a response. Please return to your original terminal window\n"; kubectl proxy
        # pods = we need to proxy access to them so we can debug and interact with them

export POD_NAME=""
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

        # To see the output of our application, run a curl request.
        # The URL is the route to the API of the Pod.
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME

        # *Note: We don’t need to specify the container name, because we only have one container inside the pod.
kubectl logs $POD_NAME

        # We can execute commands directly on the container once the Pod is up and running. 
        # let's list the environment variables
kubectl exec $POD_NAME -- env

        # start a bash session in the Pod’s container:
kubectl exec -ti $POD_NAME -- bash

        # We have now an open console on the container where we run our NodeJS application. The source code of the app is in the server.js file:
cat server.js

        # check that the application is up
        # Note: here we used localhost because we executed the command inside the NodeJS Pod. 
        # If you cannot connect to localhost:8080, check to make sure you have run the kubectl exec command and are launching the command from within the Pod
curl localhost:8080

        # To close your container connection
exit

