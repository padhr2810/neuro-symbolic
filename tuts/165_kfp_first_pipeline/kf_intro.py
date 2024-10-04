

### https://www.kubeflow.org/docs/components/pipelines/getting-started/
### Kubeflow Pipelines.
### create your first pipeline.

"""
NEED 2 TERMINALS.

IN 1ST TERMINAL:
    Deploy the Kubeflow Pipelines:
	export PIPELINE_VERSION=2.3.0
	kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
	kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
	kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=$PIPELINE_VERSION"
    Run the following to port-forward the Kubeflow Pipelines UI:
        kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80 
        
THEN IN THE 2ND TERMINAL:
	run this module
THEN IN UI:
	open the URL (with localhost) THAT APPEARS IN THE OUTPUT OF TERMINAL 2.
"""

from kfp import dsl
print(f"\n Imported dsl \n")

@dsl.component
def say_hello(name: str) -> str:
    hello_text = f'Hello, {name}!'
    print(hello_text)
    return hello_text
print(f"\n Defined 'say_hello' \n")

@dsl.pipeline
def hello_pipeline(recipient: str) -> str:
    hello_task = say_hello(name=recipient)
    return hello_task.output
print(f"\n Defined 'hello_pipeline' \n")

from kfp import compiler
print(f"\n Imported compiler \n")

compiler.Compiler().compile(hello_pipeline, 'pipeline.yaml')
print(f"\n Ran the compiler... \n")

from kfp.client import Client
print(f"\n Imported Client \n")

"""
You can submit the YAML file to a KFP-conformant backend for execution. 
If you have already deployed a KFP open source backend instance and obtained the endpoint for your deployment, you can submit the pipeline for execution using the KFP SDK Client. 
The following submits the pipeline for execution with the argument recipient='World':
"""

# Kubeflow Pipelines - open-source backend instance.
# https://www.kubeflow.org/docs/components/pipelines/operator-guides/installation/

MY_KFP_ENDPOINT = "http://localhost:8080"	# NOTE: DOESN'T WORK WITH 127.0.0.1 ...... NEEDS TO BE "Localhost"
client = Client(host=MY_KFP_ENDPOINT)

print(f"\n Initialised the client... \n")

run = client.create_run_from_pipeline_package(
    'pipeline.yaml',
    arguments={
        'recipient': 'World',
    },
)
print(f"\n Ran the client... \n")

# Next step: https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/connect-api/ 

