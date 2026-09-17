# PRIMM Activity: String Slicing


# Predict

Examine the code in `string_slicing.py`. Do **not** run the code yet.

For each `print()` statement, predict exactly what will be displayed.

Record your predictions:

| Code | Prediction |
|---|---|
| `word[0:3]` | |
| `word[3:6]` | |
| `word[1:5]` | |
| `word[4:8]` | |

### Think About It

1. Does Python include the character at the `start` position?
    > Your answer

2. Does Python include the character at the `stop` position?
    > Your answer

3. How many characters would you expect from `word[2:5]`?
    > Your answer

# Run

Run the program. Compare the actual output to your predictions.

### Reflection

- Which predictions were correct?
    > Your answer

- Which were incorrect?
    > Your answer

- What rule can you write for how the `start` and `stop` values work?
    > Your answer

Complete this sentence:

> A string slice starts at __________ and stops __________.


# Investigate

In `string_slicing.py`, change the word to `creative computing`.
```python
word: str = "creative computing"
```

Add each of the example statements below. Before running each one, predict what it will do.
Then run the code and describe what it does.

## Leaving Out `start`

| Code | Prediction | Actual Value| 
|---|---|---|
| `print(word[:5])` | | |


What does Python assumes when the `start` value is missing?
> Your answer


## Leaving Out `stop`

| Code | Prediction | Actual Value| 
|---|---|---|
| `print(word[5:])` | | |

What does Python assumes when the `stop` value is missing?
> Your answer


## Using Negative Indices
| Code | Prediction | Actual Value| 
|---|---|---|
| `print(word[-8:-4:])` | | |
| `print(word[-4:])` | | |

What does a negative index mean?
> Your answer


## Adding a Step

Slices can include a third value, the step.
| Code | Prediction | Actual Value| 
|---|---|---|
| `print(word[1:5:2])` | | |
| `print(word[:8:3])` | | |
| `print(word[-2:-6:-1])` | | |
| `print(word[-3::-1])` | | |

What does a step of -1 do?
> Your answer

What does the following strange slice do?
| Code | Prediction | Actual Value| 
|---|---|---|
| `print(word[::-1])` | | |


# Modify
Complete the program in `modify.py` following these instructions.
1. Add single line comments explaning what the calls to `.index()` do
2. Write string slices to print out the following text. You should have one print statement per line of output. You may use string concatention if needed. DO NOT USE `.split()`.

```text
Apex
Creative
Computing
Apex Creative
Creative Computing
Apex Computing
```

# Make
In `make.py`, write a program that asks the user for their first, middle, and last name. It outputs a username by following these rules.
- Usernames are all lower case
- Usernames are formed by taking the first letter of the first name, first letter of the middle name (if there one), and the entire last name.
- Any spaces are replaced with dashes.
- Any apostrophes are removed.

Ensure that the user name is all lower case. Any names that have spaces, should be replaced with dashes. Any apostrophes should be replaced an empty string.

**Prompt for the first, middle, and last name separately.**

Examples

| First | Middle | Last | Username |
| --- | --- | --- | --- |
| Rachel | Melissa | Smithe | rmsmithe |
| Marty | | Christenson | mchristenson |
| Ava-Marie | Nancy | Tong | antong |
| D'Andre | | Lewis | dlewis |
| Amy | Lou | D'Agostino | aldagostino|
| Holden | Michael | Wilkes Sedlacek | hmwilkes-sedlacek |


# Final Reflection

Answer in complete sentences.

1. What does `text[2:6]` mean?
    > Your answer
2. Why is the character at index `6` not included?
    > Your answer

3. What does `text[:4]` mean?
    > Your answer

4. What does `text[4:]` mean?
    > Your answer

5. What does `text[-3:]` mean?
    > Your answer

6. What does the third number in `text[start:stop:step]` control?
    > Your answer

7. Give one situation where string slicing might be useful in a real program.
    > Your answer