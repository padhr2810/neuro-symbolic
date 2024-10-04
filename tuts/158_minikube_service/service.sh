# Status: all runs ok EXCEPT FOR 2ND LAST LINE ---- curl $(minikube ip):$NODE_PORT


# More information about the different types of Services can be found in the Using Source IP tutorial. Also see Connecting Applications with Services.
#         lINK: https://kubernetes.io/docs/tutorials/services/source-ip/
#         LiNK: https://kubernetes.io/docs/tutorials/services/connect-applications-service/

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
          #  We have a Service called kubernetes that is created by default when minikube starts the cluster. 
          #  To create a new service and expose it to external traffic we'll use the expose command with NodePort as parameter.
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080
kubectl get services

:'
Services can be exposed in different ways by specifying a type in the spec of the Service:
    --    ClusterIP (default) - Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
    --    NodePort - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
    --    LoadBalancer - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.
    --    ExternalName - Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com), by returning a CNAME record with its value. No proxying of any kind is set up. This type requires v1.7 or higher of kube-dns, or CoreDNS version 0.0.8 or higher.
'

        # To find out what port was opened externally (for the type: NodePort Service) we’ll run the describe service subcommand:
kubectl describe services/kubernetes-bootcamp

export NODE_PORT=""
export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

        #  test that the app is exposed outside of the cluster using curl, the IP address of the Node and the externally exposed port:
curl $(minikube ip):$NODE_PORT

#    !!!!!!!!!!!!!!!!!!!!!!!  Step 2: Using labels  !!!!!!!!!!!!!!!!!!!!!!!

        # The Deployment created automatically a label for our Pod. With the describe deployment subcommand you can see the name (the key) of that label:
kubectl describe deployment

        # Let’s use this label to query our list of Pods. We’ll use the kubectl get pods command with -l as a parameter, followed by the label values:
kubectl get pods -l app=kubernetes-bootcamp

        # You can do the same to list the existing Services:
kubectl get services -l app=kubernetes-bootcamp

export POD_NAME=""
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME

        # To apply a new label we use the label subcommand followed by the object type, object name and the new label
        # This will apply a new label to our Pod (we pinned the application version to the Pod), and we can check it with the describe pod command:
kubectl label pods $POD_NAME version=v1

kubectl describe pods $POD_NAME

kubectl get pods -l version=v1

#    !!!!!!!!!!!!!!!!!!!!!!!  Step 3: Deleting a service  !!!!!!!!!!!!!!!!!!!!!!!

        # Labels can also be used to delete a service.
kubectl delete service -l app=kubernetes-bootcamp

        # Confirm that the Service is gone:
kubectl get services

        # To confirm that route is not exposed anymore you can curl the previously exposed IP and port ... this FAILS, proving that the application is not reachable anymore from outside of the cluster.
curl $(minikube ip):$NODE_PORT

        # You can confirm that the app is still running with a curl from inside the pod:
kubectl exec -ti $POD_NAME -- curl localhost:8080


