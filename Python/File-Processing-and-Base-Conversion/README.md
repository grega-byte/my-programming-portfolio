# File Processing and Base Conversion

## 1. Project Name

File Processing and Base Conversion Exercises

## 2. Overview

Exercises that read local files, inspect saved HTML text, and convert integer values between decimal and bases from 2 through 10.

## 3. Features

- Reads a user-selected text file and counts lines.
- Reads a local HTML file and examines its contents, including bracket counts.
- Converts between decimal integers and bases 2–10.

## 4. Technologies Used

- Python
- Python standard library `os` module for file existence checks in one exercise

## 5. Key Concepts Demonstrated

- Opening and reading text files
- File paths and existence checks
- String traversal and character counting
- Quotient and remainder conversion

## 6. How to Run

Run an exercise from this directory, for example:

```text
python p19p1.py
```

`p18p6.py` and `p19p3.py` use `websourcegit.html`, which is included here. `p20.p1.py` accepts a filename; if left blank, it looks for `lines.txt` in the current working directory. That input file is not included. The conversion exercises request values in the terminal and support bases 2 through 10.

## 7. Project Structure

- `p18p6.py` and `p19p3.py`: read and inspect `websourcegit.html`.
- `p19p1.py`–`p19p2.py`: convert integer values to and from bases 2–10.
- `p20.p1.py`: counts lines in a selected file or the default `lines.txt`.
- `websourcegit.html`: local input used by the HTML-reading exercises.

## 8. What I Learned

The exercises practise reading files from disk, processing their text, and using repeated division or positional values for base conversion.

## 9. Future Improvements

- Handle missing files and invalid file contents consistently.
- Add examples that verify conversions by converting values in both directions.
