
# With simple projects, Cargo doesn’t provide a lot of value over just using rustc, but it will prove its worth as your programs become more intricate. 
# Once programs grow to multiple files or need a dependency, it’s much easier to let Cargo coordinate the build.
# Cargo is Rust’s build system and package manager. Most Rustaceans use this tool to manage their Rust projects because Cargo handles a lot of tasks for you, 
# such as building your code, downloading the libraries your code depends on, and building those libraries. 

cargo --version

cargo new hello_cargo
cd hello_cargo
ls

# see that Cargo has generated two files and one directory for us: a Cargo.toml file and a src directory with a main.rs file inside
# It has also initialized a new Git repository along with a .gitignore file
# TOML is Cargo’s configuration format.
# In Rust, packages of code are referred to as crates.
# Cargo has generated a “Hello, world!” program for you in "main.rs"

cargo build
# This command creates an executable file in target/debug/hello_cargo

./target/debug/hello_cargo

# Running cargo build for the first time also causes Cargo to create a new file at the top level: Cargo.lock.
# This file keeps track of the exact versions of dependencies in your project.
# You won’t ever need to change this file manually; Cargo manages its contents for you.

cargo run
# cargo run = one command for both tasks - compile the code and then run the resultant executable 
# most developers use cargo run

cargo check
# quickly checks your code to make sure it compiles but doesn’t produce an executable
# faster than cargo build obviously

cargo build --release
# optimisations when ready for release
# slower compiling but runs faster.
# puts the executable in target/release instead of target/debug

# Using Cargo to run any existing projects:
# git clone example.org/someproject
# cd someproject
# cargo build
