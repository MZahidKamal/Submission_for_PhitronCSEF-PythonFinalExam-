import datetime

class Transaction:
    @staticmethod
    def record(account_number, transaction_type, amount):
        transaction = {
            'AccountNo': account_number,
            'DateAndTime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'TransactionType': transaction_type,
            'Amount': amount
        }
        return transaction
