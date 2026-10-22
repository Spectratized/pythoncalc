# 🧮 Python Calculator

A clean, modular, and beginner-friendly command-line calculator written in Python. This project demonstrates core programming practices such as pure functions, type annotations, error handling, interactive CLI menus, and unit testing.

---

## ✨ Features

- **Basic Operations**: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
- **Advanced Operations**: Exponentiation (`^`), Modulus (`%`)
- **Input Validation**: Gracefully handles non-numeric user inputs.
- **Error Handling**: Catches and alerts on invalid operations (e.g., division by zero).
- **Unit Tested**: Fully covered with Python's built-in `unittest` module.
- **Zero External Dependencies**: Runs on standard Python 3 with no extra packages required.

---

## 📁 Project Structure

```text
python-calculator/
├── calculator.py       # Main calculator program and logic
├── test_calculator.py  # Unit tests covering all arithmetic functions
├── .gitignore          # Rules for ignoring bytecode and virtual environments
└── README.md           # Project documentation and guide
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/) installed on your computer.

### Running the Calculator

Open your terminal or command prompt in the project directory and run:

```bash
python calculator.py
```

Follow the interactive prompts in your terminal:
```text
==============================
      PYTHON CALCULATOR      
==============================
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exponentiation (^)
6. Modulus (%)
7. Exit
==============================
Select an option (1-7): 1

Selected: Addition
Enter the first number: 12
Enter the second number: 8

Result: 12.0 + 8.0 = 20
```

---

## 🧪 Running Unit Tests

To run the automated tests, execute:

```bash
python -m unittest test_calculator.py
```

Expected output:
```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

---

## 🐙 How to Upload This Project to GitHub

Follow these steps to initialize Git and publish your repository to GitHub:

### Step 1: Initialize Git in your project folder
Open a terminal in this project directory (`python-calculator`) and run:

```bash
git init
```

### Step 2: Stage and commit your files
Stage all your files and create your first commit:

```bash
git add .
git commit -m "Initial commit: Python calculator with unit tests"
```

### Step 3: Create a new repository on GitHub
1. Log into [GitHub](https://github.com/).
2. In the top right corner, click the **`+`** icon and select **New repository**.
3. Name your repository (e.g., `python-calculator`).
4. **Leave "Initialize this repository with a README" unchecked** (since you already have one).
5. Click **Create repository**.

### Step 4: Link your local repository and push
Copy the repository URL from GitHub (e.g., `https://github.com/<your-username>/python-calculator.git`), then run:

```bash
# Rename default branch to main (if not already main)
git branch -M main

# Link your local repo to GitHub
git remote add origin https://github.com/<your-username>/python-calculator.git

# Push your code to GitHub
git push -u origin main
```

---

## 📄 License

This project is open-source and free to use for educational purposes under the [MIT License](https://opensource.org/licenses/MIT).
