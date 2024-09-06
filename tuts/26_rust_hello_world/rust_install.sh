#On Ubuntu, the recommended way to install Rust is using rustup:
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

#However, this raised an error on my Ubuntu machine:
# `curl: (23) Failure writing output to destination`

# To install rustup on Ubuntu, make sure that curl is installed via apt, not snapd.

sudo snap remove curl
sudo apt-get install curl

#This fixed the problem.


rustc --version
