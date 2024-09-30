# https://kubernetes.io/docs/tutorials/hello-minikube/

minikube start
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
kubectl get deployments
kubectl get pods
kubectl get events
kubectl config view
kubectl get pods
kubectl logs hello-node-55fdcd95bf-kj8wr
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl get services
minikube service hello-node
minikube addons list
minikube addons enable metrics-server
kubectl get pod,svc -n kube-system
kubectl top pods
kubectl get pod,svc -n kube-system
kubectl top pods
minikube addons disable metrics-server
kubectl delete service hello-node
kubectl delete deployment hello-node
minikube stop
minikube delete
