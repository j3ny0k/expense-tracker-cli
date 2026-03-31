# Expense Tracker CLI

Simple CLI app to track expenses.

## Features

- add expense (name, amount, category)
- show all expenses
- total expenses
- total by category
- input validation (empty input, invalid command)
- help command

---

## Usage

Run the program:

```bash
python expense-tracker-cli.py
```

---

## Commands

### add

Add a new expense.

Example:

```text
command: add
name: bread
amount: 12
category: food
```

### show

Show all expenses.

Example:

```text
1. bread – 12 – food
2. bus – 6 – transport
```

### total

Show total amount of all expenses.

Example:

```text
total: 18
```

### by_category

Show total for a specific category.

Example:

```text
by_category: food
food: 12
```

### exit

Exit the program.

### help

Show available commands.

---

## Notes

- data is stored in memory (resets after restart)
- amount must be a number
- empty input is handled
- category not found is handled
