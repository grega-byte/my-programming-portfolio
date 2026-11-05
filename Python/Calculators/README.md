# Calculators

## 1. Project Name

Calculators

## 2. Overview

A collection of interactive and fixed-value calculation exercises for currency conversion, geometric measurements, and tax examples.

## 3. Features

- Converts an entered euro amount using an entered exchange rate.
- Calculates square, circle, cube, sphere, and cylinder measurements.
- Calculates example tax amounts using fixed percentage splits.
- Some later versions reject negative amounts or lengths.

## 4. Technologies Used

- Python
- Python standard library `math` module for pi in the geometry exercises

## 5. Key Concepts Demonstrated

- Numeric input and floating-point arithmetic
- Variables and expressions
- Conditional validation
- Use of `math.pi`

## 6. How to Run

Run any exercise individually, for example:

```text
python p4-5p1.py
```

The interactive exercises request values in the terminal. `p4p1.py` and `p4p2.py` do not apply the negative-input checks present in their later variants.

## 7. Project Structure

- `p4p1.py` and `p4-5p1.py`: euro-to-dollar calculations; the latter checks that the amount is non-negative.
- `p4p2.py` and `p4-5p2.py`: geometric calculations; the latter checks that the length is non-negative.
- `p4p3.py` and `p4-5p3.py`: tax calculations with different percentage assumptions.

## 8. What I Learned

The exercises practise translating formulas into expressions and using input values and conditionals in small calculator programs.

## 9. Future Improvements

- Add clearer input validation for all calculator exercises.
- Separate repeated calculations into functions.
