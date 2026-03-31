expenses = []

while True:
    command = input('command: ')

    if command == 'exit':
        break

    elif command == 'add':
        name = input('name: ')
        amount = int(input('amount: '))
        category = input('category: ')

        expenses.append({
            'name': name,
            'amount': amount,
            'category': category
        })

    elif command == 'show':
        num = 1
        for expense in expenses:
            name = expense['name']
            amount = expense['amount']
            category = expense['category']
            print((f'{num}. {name} – {amount} – {category}'))
            num += 1
    
    elif command == 'total':
        total = 0
        for expense in expenses:
            total += expense['amount']
        print('total:', total)

    elif command == 'by_category':
        total = 0
        category_name = input('by_category: ')
        for expense in expenses:
            if expense['category'] == category_name:
                total += expense['amount']
        print(f'{category_name}: {total}')
