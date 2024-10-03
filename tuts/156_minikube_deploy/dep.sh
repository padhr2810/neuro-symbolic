
# https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/


kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1
    # name = kubernetes-bootcamp
    # --image = ... [need full repository url for images hosted outside Docker Hub]
    
kubectl get deployments
kubectl proxy

# !!! THEN IN A DIFFERENT TERMINAL !!!
curl http://localhost:8001/version
export POD_NAME=$(kubectl get pods -o go-template --template '{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}')
echo Name of the Pod: $POD_NAME
curl http://localhost:8001/api/v1/namespaces/default/pods/$POD_NAME:8080/proxy/
