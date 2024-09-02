# how to access a venv from within Jupyter Notebook

python3 -m venv env_new
cd env_new/bin
source activate

pip install ipykernel
python3 -m ipykernel install --user --name env_new

jupyter notebook
# then click on "Select Kernel" in top right and the venv name should appear there.
# This will work subsequently even if the venv has not been activated. i.e. still accessible in new jupyter notebooks
