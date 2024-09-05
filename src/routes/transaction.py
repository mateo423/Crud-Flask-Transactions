from flask import Flask, render_template, request, redirect, url_for, Blueprint, jsonify

transactiox = Blueprint('transaction', __name__, template_folder='templates')

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@transactiox.route('/')
def get_transactions():
    return render_template("transactions.html", transactions=transactions)
# Create operation
@transactiox.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for('transaction.get_transactions'))  # Cambiado aquí
    
    return render_template('form.html')

# Update operation
@transactiox.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
        
        return redirect(url_for('transaction.get_transactions'))  # Cambiado aquí
    
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)

    return {'message': 'Transaction not found'}, 404

# Delete operation
@transactiox.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    global transactions
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  
    return redirect(url_for('transaction.get_transactions'))  



@transactiox.route('/search', methods=['GET', 'POST'])
def search_transactions():
    filtered_transactions = []  # Lista para almacenar las transacciones filtradas

    if request.method == 'POST':
        min_amount = request.form.get('min_amount')
        max_amount = request.form.get('max_amount')

        min_amount = float(min_amount) 
        max_amount = float(max_amount)

        filtered_transactions = [
            transaction for transaction in transactions
            if min_amount <= transaction['amount'] <= max_amount
        ]
        return render_template('transactions.html', transactions=filtered_transactions)

    return render_template('search.html')

@transactiox.route('/balance', methods=['GET', 'POST'])
def get_balance():
    total_amount = sum(transaction['amount'] for transaction in transactions)
    return f'El balance total es {total_amount}'

