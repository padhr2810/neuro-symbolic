
use rand::Rng;        // dependency was specified in TOML
use std::cmp::Ordering;    
use std::io;

// By default, Rust has a set of items defined in the standard library that it brings into the scope of every program. This set is called the prelude, see docs.
// If a type you want to use isn’t in the prelude, you have to bring that type into scope explicitly with a use statement. 
// Using the std::io library provides you with a number of useful features, including the ability to accept user input.

// Remember that a crate is a collection of Rust source code files. The project we’ve been building is a binary crate, which is an executable. 
// The rand crate is a library crate, which contains code that is intended to be used in other programs and can’t be executed on its own.

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();  // let mut = create a mutable var
                                        // String::new, a function that returns a new instance of a String
                                        // The :: syntax in the ::new line indicates that new is an associated function of the String type. 
                                        // An associated function is a function that’s implemented on a type, in this case String
                                        // This new function creates a new, empty string. You’ll find a new function on many types 

        io::stdin()
            .read_line(&mut guess)        // read_line implies get input from user (store in the guess var)
            .expect("Failed to read line");    // If this instance of Result is an Err value, expect will cause the program to crash and display this error message
                                            // The & indicates that this argument is a reference, which gives you a way to let multiple parts of your code access one piece of data >>>
                                            // without needing to copy that data into memory multiple times
                                            // like variables, references are immutable by default. Hence, you need to write &mut guess rather than &guess to make it mutable
                                            // "read_line" gives a Result also. Result’s variants are Ok and Err. 
                                                // The Err variant means the operation failed, and Err contains information about how or why the operation failed.
                                            // If you don’t call expect, the program will compile, but you’ll get a warning:
        
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
