# Expense Tracker CLI

Simple CLI app to track expenses.

## Features

- add expense (name, amount, category)
- show all expenses
- total expenses
- total by category
- delete expense
- input validation (empty input, invalid numbers, invalid commands)
- data is saved to file

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

---

### show

Show all expenses.

Example:

```text
1. bread – 12 – food
2. bus – 6 – transport
```

---

### total

Show total amount of all expenses.

Example:

```text
total: 18
```

---

### by_category

Show total for a specific category.

Example:

```text
by_category: food
food: 12
```

---

### delete

Delete an expense by number.

Example:

```text
command: delete
expense num: 1
expense deleted
```

---

### exit

Exit the program.

---

### help

Show available commands.

---

## Notes

- expenses are saved in `expenses.json`
- data stays after restart
- `expenses.json` is local (not pushed to GitHub)
- amount must be an integer
- empty input is handled
- invalid expense number is handled
- category not found is handled
