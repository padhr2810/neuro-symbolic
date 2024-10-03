
# https://github.com/GoogleContainerTools/kaniko/tree/main?tab=readme-ov-file

# https://stackoverflow.com/questions/66347900/setting-up-container-registry-for-kubeflow

:'
we'll assume that you've set your container registry via an environment variable
$CONTAINER_REGISTRY, in your shell ...
NOTE: If you use registry that isn't on Google Cloud Platform, 
you will need to configure Kubeflow pipelines container builder to have access to your registry 
by following the Kaniko configuration guide -> https://oreil.ly/88Ep-

1. You set the environment variable using export CONTAINER_REGISTRY=docker.io/your_username in your terminal (or in your ~/.bash_profile and run source ~/.bash_profile).
2. Your .docker/config.json does not have your password in plain text but in base64, for example the output of echo -n 'username:password' | base64
3. The docker build and the docker push are two separate commands, in your example they're seen as one command, unlike the book.

THE QUERY ON STACK OVERFLOW (SAME ISSUE THAT I HAD):
"I've gone into Kaniko config guide and did everything as told -> creating config.json with "auth":"mypassword for dockerhub". After that In the book it says:
To make sure your docker installation is properly configured, you can write one line Dc and push it to your registry."
Example 2.7 Specify the new container is built on top of Kubeflow's container

FROM gcr.io/kubeflow-images-public/tensorflow-2.1.0-notebook-cpu:1.0.0

Example 2.8 Build new container and push to registry for use

IMAGE="${CONTAINER_REGISTRY}/kubeflow/test:v1" 
docker build  -t "${IMAGE}" -f Dockerfile . docker push "${IMAGE}"

I've created Dockerfile with code from Example2.7 inside it, then ran code from Example 2.8 however not working.
'

