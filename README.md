# Expense Tracker CLI

Simple CLI app to track expenses.

## Status

Early learning project.

This project was later integrated into `life-cli`.

Main portfolio version: `life-cli`.

---

## Features

- add expense (name, amount, category)
- show all expenses
- find expenses
- total expenses
- total by category
- edit expense
- delete expense
- input validation
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

### find

Find expenses by text or amount.

You can use:

- any text → search in expense name and category
- number → search by exact amount

Example (text search):

```text
command: find
find: food
1. bread – 12 – food
```

Example (amount search):

```text
command: find
find: 12
1. bread – 12 – food
```

If nothing is found:

```text
command: find
find: xyz
not found
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

### edit

Edit an expense by number.

You can update:

- name
- amount
- category

Fields can be left empty to keep old values.

Example:

```text
command: edit
expense num: 1
new name: milk
new amount: 15
new category: food

expense updated
```

If nothing was changed:

```text
expense not updated
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

### help

Show available commands.

---

### exit

Exit the program.

---

## Notes

- expenses are saved in `expenses.json`
- data stays after restart
- `expenses.json` is local (not pushed to GitHub)
- amount must be an integer
- empty input is handled
- invalid expense number is handled
- category not found is handled
- no expenses case is handled
