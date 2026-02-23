# Arithmetic Formatter
This project is based on one of the certification progress on the freeCodeCamp Scientific Computing with Python curriculum. And I learnt a lot of stuff and got a lot of experiences like exploring the code, understanding the core, the algorithm, and especially solving the problems by myself without following step-by-step tutorials like the other FCC projects.

## Personal Tweak
Originally, the certification progress gave me numbers to print, but I changed it to `input()` so the users can input the problems by theirself on the terminal.

## Features
* Arranges addition and subtraction problems vertically.
* Automatically aligns numbers and operators.
* Supports an optional argument to display answer.
* Handles input validation (max 5 problems, digits only, max 4 digits)

## Project Structure
Inside this repository, you will find:
* `main.py` — The script that runs arithmetic formatting.
* `README.md` — The documentation you are reading right now.

## How It Works (The Logic)
The script takes your math problems and cleans them up before formatting. Here’s the breakdown:
1. **Input Parsing**: It takes a single string of problems (separated by commas), splits them into a list, and removes any accidental spaces using `split()` and `strip()`.
2. **Validation**: It checks if the problems are valid (e.g., only addition/subtraction, numbers only, and no more than 4 digits).
3. **Alignment**: Every number is right-aligned based on the longest operand in that specific problem.
4. **Formatting**: It builds the output line by line (top numbers, bottom numbers, dashes) and combines them into one clean vertical layout.
5. **Optional Answers**: If you set the second argument to `True`, it calculates the result and adds a fourth line with the answers.

## Output Example
For an example, I inserted 1298 - 562, 182 + 873, 12 + 189 in my terminal:
<p align="center">
    <img src="https://imgur.com/46d2Obj.jpg" width="1000" title="Output Example">
</p>