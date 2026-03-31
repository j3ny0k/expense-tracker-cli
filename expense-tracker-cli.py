help = ('add', 'show', 'total', 'by_category', 'exit', 'help')

expenses = []

def add_expense():
    name = input('\nname: ')
    amount = int(input('amount: '))
    category = input('category: ')
    print()

    expenses.append({
        'name': name,
        'amount': amount,
        'category': category
    })

def show_expenses():
    if not expenses:
            print('no expenses\n')

    num = 1

    for expense in expenses:
        name = expense['name']
        amount = expense['amount']
        category = expense['category']

        print(f'{num}. {name} – {amount} – {category}')
        print()
        num += 1

def total_expenses():
    total = 0

    for expense in expenses:
        total += expense['amount']

    print(f'total: {total}\n')

def by_category():
    category_name = input('\nby_category: ')

    if not category_name:
        print('empty input\n')
        return

    total = 0
    found = False

    for expense in expenses:
        if expense['category'] == category_name:
            total += expense['amount']
            found = True
    
    if found == False:
        print('category not found\n')
    else:
        print(f'{category_name}: {total}\n')

while True:
    command = input('command: ')
    if not command or command not in help:
        print('invalid command\n')

    if command == 'exit':
        break

    elif command == 'add':
        add_expense()

    elif command == 'show':
        show_expenses()
    
    elif command == 'total':
        total_expenses()

    elif command == 'by_category':
        by_category()

    elif command == 'help':
        print('allowed commands:', ', '.join(help), '\n')
