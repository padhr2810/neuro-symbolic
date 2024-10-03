APPROACH 1: FROM KUBEFLOW WEBSITE:
https://www.kubeflow.org/docs/components/pipelines/legacy-v1/installation/localcluster-deployment/

export PIPELINE_VERSION=2.3.0
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic?ref=$PIPELINE_VERSION"
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80

Then, open the Kubeflow Pipelines UI at http://localhost:8080/



APPROACH 2: FOR THE TREVOR GRANT KUBEFLOW BOOK:
# is this the container builder that needs to be configured?
#       /home/p/Documents/code/pipelines/sdk/python/kfp/containers/_container_builder.py

:'
1.    Install Docker on the Linux system.
2.    Download the Kaniko binary from the official GitHub page.
3.    Move the binary to a directory in the system's PATH.
4.    Ensure that the binary has executable permissions.
'

# https://github.com/GoogleContainerTools/kaniko/tree/main?tab=readme-ov-file

# https://stackoverflow.com/questions/66347900/setting-up-container-registry-for-kubeflow

# !!!!!! GETTING THE USER CREDENTIALS !!!!!!
# for Docker Hub:
echo -n padhraigryan:MYDOCKERPASSWORD  | base64
        # i.e. this returns the input in base64 which is needed for kubeflow config.
        #     -n     do not output the trailing newline
# for Local Registry on laptop:
echo -n p:MYLOCALPASSWORD  | base64

# THIS MIGHT BE THE PLACE TO PUT CONFIG.JSON.
/etc/docker/config.json

# PUT THIS INTO config.json
{
  "auths": {
      /home/p/registry: {
      "auth": "BASE64_AUTH_HERE_FROM_ABOVE"
    }
  }
}

# set up a registry server on local network.
docker run -d -p 5000:5000 -v $HOME/registry:/var/lib/registry registry:2
# registry:2 is the name of the image - it gets pulled from docker hub the first time.
docker ps
export CONTAINER_REGISTRY=$HOME/registry



:'
we'll assume that you've set your container registry via an environment variable
$CONTAINER_REGISTRY, in your shell ...
NOTE: If you use registry that isn't on Google Cloud Platform, 
you will need to configure Kubeflow pipelines container builder to have access to your registry 
by following the Kaniko configuration guide -> https://oreil.ly/88Ep-

1. You set the environment variable using export CONTAINER_REGISTRY=docker.io/your_username in your terminal (or in your ~/.bash_profile and run source ~/.bash_profile).
2. Your .docker/config.json does not have your password in plain text but in base64, for example the output of echo -n 'username:password' | base64

THE QUERY ON STACK OVERFLOW (SAME ISSUE THAT I HAD):
"I've gone into Kaniko config guide and did everything as told -> creating config.json with "auth":"mypassword for dockerhub". After that In the book it says:
To make sure your docker installation is properly configured, you can write one line Dc and push it to your registry."
Example 2.7 Specify the new container is built on top of Kubeflow's container

FROM gcr.io/kubeflow-images-public/tensorflow-2.1.0-notebook-cpu:1.0.0

Example 2.8 Build new container and push to registry for use

IMAGE="${CONTAINER_REGISTRY}/kubeflow/test:v1" 
docker build  -t "${IMAGE}" -f Dockerfile . 
docker push "${IMAGE}"
    # BUILD AND PUSH NEED TO BE 2 SEPARATE COMMANDS... DON'T CONDENSE INTO ONE LINE.
I've created Dockerfile with code from Example2.7 inside it, then ran code from Example 2.8 however not working.
'

