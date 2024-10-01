# https://kubernetes.io/docs/tutorials/hello-minikube/

minikube start
        # creates a minikube cluster

# !!! run this command in a different terminal and leave it running !!!
minikube dashboard
        # You can create Kubernetes resources on the dashboard such as Deployment and Service
        # By default, the dashboard is only accessible from within the internal Kubernetes virtual network. 
        # The dashboard command creates a temporary proxy to make the dashboard accessible from outside the Kubernetes virtual network.
        # To stop the proxy, run Ctrl+C to exit the process. 
        # After the command exits, the dashboard remains running in the Kubernetes cluster. 
        # You can run the dashboard command again to create another proxy to access the dashboard.

:'
A Kubernetes Pod is a group of one or more Containers, tied together for the purposes of administration and networking. 
The Pod in this tutorial has only one Container. 
A Kubernetes Deployment checks on the health of your Pod and restarts the Pod's Container if it terminates. 
Deployments are the recommended way to manage the creation and scaling of Pods.
'

kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
        # create a Deployment that manages a Pod. The Pod runs a Container based on the provided Docker image.

kubectl get deployments
        # view deployments
kubectl get pods
        # view pods
kubectl get events
        # view events on the cluster.
kubectl get namespaces
        # view namespaces
        # 'get namespaces' works after 'minikube start' ... doesn't require a deployment.

kubectl config view
        # view the configuration of kubectl 
        
kubectl get pods
        # running this again to get the name of the pod.
        
kubectl logs hello-node-55fdcd95bf-kj8wr
        #  View application logs for a container in a pod
        # the name of the pod (starting with 'hello-node ...' is retrieved by 'kubectl get pods' )

# !!! Create a service !!!
:' 
By default, the Pod is only accessible by its internal IP address within the Kubernetes cluster. 
To make the hello-node Container accessible from outside the Kubernetes virtual network, you have to expose the Pod as a Kubernetes Service.
Do not do this on a production cluster.
' 

kubectl expose deployment hello-node --type=LoadBalancer --port=8080
        # Expose the Pod to the public internet using the kubectl expose command:
        # The --type=LoadBalancer flag indicates that you want to expose your Service outside of the cluster.
        # The application code inside the test image only listens on TCP port 8080. 
        # If you used kubectl expose to expose a different port, clients could not connect to that other port.
        # On cloud providers that support load balancers, an external IP address would be provisioned to access the Service. 
        # On minikube, the LoadBalancer type makes the Service accessible through the minikube service command.

kubectl get services
minikube service hello-node

minikube addons list
        # List supported add-ons.
        # This shows if enabled / disabled.
        
minikube addons enable metrics-server
        # enable one add-on

kubectl get pod,svc -n kube-system
        # View the Pod and Service you created by installing that addon
        
kubectl top pods
        # Check the output from metrics-server
        # If see an error message, wait, and try again
        
minikube addons disable metrics-server
        # disable the addon
        
kubectl delete service hello-node
kubectl delete deployment hello-node
minikube stop
        # stop the cluster
        
#minikube delete
        # Deletes a local Kubernetes cluster. This command deletes the VM, and removes all associated files.
        # If you want to use minikube again, you don't need to delete it.
