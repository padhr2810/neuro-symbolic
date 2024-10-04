# https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/
# https://minikube.sigs.k8s.io/docs/tutorials/kubernetes_101/module5/

kubectl delete service kubernetes-bootcamp

kubectl expose deployment/kubernetes-bootcamp --type="LoadBalancer" --port 8080

kubectl get deployments
:'
    NAME lists the names of the Deployments in the cluster.
    READY shows the ratio of CURRENT/DESIRED replicas
    UP-TO-DATE displays the number of replicas that have been updated to achieve the desired state.
    AVAILABLE displays how many replicas of the application are available to your users.
    AGE displays the amount of time that the application has been running.
'

        # To see the ReplicaSet created by the Deployment
kubectl get rs

        # Scaling is accomplished by changing the number of replicas in a Deployment
       #  In this section, it is assumed that a service with type: LoadBalancer is created for the kubernetes-bootcamp Deployment.

:'
Notice that the name of the ReplicaSet is always formatted as [DEPLOYMENT-NAME]-[RANDOM-STRING]. The random string is randomly generated and uses the pod-template-hash as a seed.
Two important columns of this output are:
    DESIRED displays the desired number of replicas of the application, which you define when you create the Deployment. This is the desired state.
    CURRENT displays how many replicas are currently running.
'


kubectl scale deployments/kubernetes-bootcamp --replicas=4

kubectl get deployments

        # confirm there are 4 pods with unique IP addresses.
kubectl get pods -o wide

        # The change was registered in the Deployment events log. To check that, use the describe subcommand:
kubectl describe deployments/kubernetes-bootcamp

        # Let's check that the Service is load-balancing the traffic. To find out the exposed IP and Port we can use the describe service as we learned in the previous part of the tutorial:
kubectl describe services/kubernetes-bootcamp

export NODE_PORT=$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')
echo NODE_PORT=$NODE_PORT

        # Execute the command multiple times:
        # We hit a different Pod with every request. This demonstrates that the load-balancing is working.
curl $(minikube ip):$NODE_PORT

        # SCALE DOWN TO 2 REPLICAS.
kubectl scale deployments/kubernetes-bootcamp --replicas=2

        # confirm the change was deployed.
kubectl get deployments

kubectl get pods -o wide
