# https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/

kubectl get deployments

kubectl get pods

kubectl describe pods

        # To update the image of the application to version 2, use the set image subcommand, followed by the deployment name and the new image version:
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/k8s-minikube/kubernetes-bootcamp:v2
        # The command notified the Deployment to use a different image for your app and initiated a rolling update. 
        # Check the status of the new Pods, and view the old one terminating with the get pods subcommand:
        
kubectl get pods

#  !!!!!!!! Verify an update !!!!!!!!
        # First, check that the service is running, as you might have deleted it in previous tutorial step
kubectl describe services/kubernetes-bootcamp

        # If it's missing, you can create it again with.
kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

        # Every time you run the curl command, you will hit a different Pod. Notice that all Pods are now running the latest version (v2).
curl $(minikube ip):$NODE_PORT

        # You can also confirm the update by running the rollout status subcommand:
kubectl rollout status deployments/kubernetes-bootcamp

        # To view the current image version of the app, run the describe pods subcommand:
kubectl describe pods

# !!!!!!!!!!!!!!!!!! Roll back an update !!!!!!!!!!!!!!!!!!

        # Let’s perform another update, and try to deploy an image tagged with v10:
        # the v10 image does NOT exist in the registry.
kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/k8s-minikube/kubernetes-bootcamp:v10

kubectl get deployments

        # Notice that some of the Pods have a status of ImagePullBackOff.
kubectl get pods

        # In the Events section of the output for the affected Pods, notice that the v10 image version did not exist in the repository.
kubectl describe pods

        # To roll back the deployment to your last working version, use the rollout undo subcommand.
        # The rollout undo command reverts the deployment to the previous known state (v2 of the image). 
        # Updates are versioned and you can revert to any previously known state of a Deployment.
kubectl rollout undo deployments/kubernetes-bootcamp

        # The Deployment is once again using a stable version of the app (v2). The rollback was successful.
kubectl get pods
kubectl describe pods

        # Remember to clean up your local cluster
kubectl delete deployments/kubernetes-bootcamp services/kubernetes-bootcamp
