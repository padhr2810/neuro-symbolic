

### https://www.kubeflow.org/docs/components/pipelines/getting-started/
### Kubeflow Pipelines.
### create your first pipeline.

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

client = Client(host='<MY-KFP-ENDPOINT>')
print(f"\n Initialised the client... \n")

run = client.create_run_from_pipeline_package(
    'pipeline.yaml',
    arguments={
        'recipient': 'World',
    },
)
print(f"\n Ran the client... \n")

# Next step: https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/connect-api/ 

