# CS50 Coursework Exercises

## 1. Project Name

CS50 Coursework Exercises

## 2. Overview

A collection of C exercises kept clearly identified as CS50 coursework. The source files are preserved as supplied.

## 3. Features

- Greets a user by name.
- Prints rows of hash characters based on an entered height.
- Scores two words using Scrabble letter values.
- Counts letters, words, and sentence-ending punctuation to estimate a reading grade.
- Prompts for and prints contact details.

## 4. Technologies Used

- C
- CS50 library (`cs50.h`)
- Standard C headers including `stdio.h` and, in some programs, `ctype.h` and `math.h`

## 5. Key Concepts Demonstrated

- Functions and return values
- Input and formatted output
- Loops and conditionals
- Arrays, strings, and character classification
- Basic arithmetic

## 6. How to Run

These files include `cs50.h` and call CS50 input functions, so a C compiler and an environment with the CS50 library available are required. In a CS50 environment, compile an individual file with its matching target, for example:

```text
make hello
```

Then run the resulting program using that environment's normal command. Build instructions may vary outside the CS50 environment.

## 7. Project Structure

- `hello.c`: prompts for a name and prints a greeting.
- `mario.c` and `extra.c`: prompt for a positive height and print increasing rows of `#` characters. These two files are byte-for-byte duplicates in the supplied collection; both are retained.
- `readability.c`: counts letters, spaces as word boundaries, and sentence punctuation, then prints a grade estimate.
- `scrabble.c`: calculates and compares two word scores using a letter-value array.
- `contacts.c` and `contactlist.c`: prompt for contact details and print them.

## 8. What I Learned

These exercises practise C input and output, loops, arrays, character handling, and breaking calculations into functions.

## 9. Future Improvements

- Check CS50 coursework publication permissions before making these solutions public.
- Add build notes for a specific compiler environment once that environment is selected.
