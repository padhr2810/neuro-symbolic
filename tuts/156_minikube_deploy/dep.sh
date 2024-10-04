
# this works fine - but needed to add :
#         export POD_NAME=""
# because for some reason it was appending multiple pod names and this raised errors subsequently.

# https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/


kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
    # name = kubernetes-bootcamp
    # --image = ... [need full repository url for images hosted outside Docker Hub]
    
kubectl get deployments

        # Pods that are running inside Kubernetes are running on a private, isolated network. 
        # By default they are visible from other pods and services within the same Kubernetes cluster, but not outside that network. 
        # When we use kubectl, we're interacting through an API endpoint to communicate with our application.
        # We will cover other options on how to expose your application outside the Kubernetes cluster later, in Module 4.
        # The kubectl proxy command can create a proxy that will forward communications into the cluster-wide, private network. 
        # The proxy can be terminated by pressing control-C and won't show any output while it's running.
    
kubectl proxy

# !!! THEN IN A DIFFERENT TERMINAL !!!
curl http://localhost:8001/version
        # SHOWS THE VERSION OF KUBERNETES YOU ARE RUNNING E.G. V1.30 
        #         {
        #          "major": "1",
        #          "minor": "30", ........ }

export POD_NAME=""
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
        # The API server will automatically create an endpoint for each pod, based on the pod name, that is also accessible through the proxy.
        # First we need to get the Pod name, and we'll store it in the environment variable POD_NAME:

curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/
        # You can access the Pod through the proxied API like so ...
        
