from bank import Bank
from savings_account import SavingsAccount
from current_account import CurrentAccount
import sys

def main():
    commerzbank = Bank('CommerzBank', 'Wellknown Street', 55, 46589, 'Frankfurt', 'Hessen', 'Germany', 'www.commerzbank.de')


#---Some dummy data for test purposes-----------------------------------------------------------------------------------
    SavingsAccount('Robert Bosch', 'Offenbach', 'robert@bosch.com')
    SavingsAccount('Alice Johnson', 'Springfield', 'alice@example.com')
    SavingsAccount('Bob Smith', 'Pleasant ville', 'bob@example.com')

    CurrentAccount('Jane Smith', 'Pleasant ville', 'jane@example.com')
    CurrentAccount('Michael Johnson', 'Sunset City', 'michael@example.com')
    CurrentAccount('Lisa Williams', 'Bayside', 'lisa@example.com')
#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------R E P L I C A  S Y S T E M---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

    print(f'\n---------- Welcome to {commerzbank.Name} ----------')
    while True:

        print('\nSelect Option:'
              '\n\t[1] Show Bank Information'
              '\n\t[2] Admin/Manager Login'
              '\n\t[3] User/Account Holder Login'
              '\n\t[4] Log out')

        user_input = input('Your selection: ')

#-----------------------------------------------------------------------------------------------------------------------

        if user_input == '1':
            commerzbank.bank_info()
            continue

#-----------------------------------------------------------------------------------------------------------------------

        elif user_input == '2':
            print('\n----- Admin/Managerial access given -----')
            while True:
                print('\nSelect Option:'
                      '\n\t[1] Create Savings Account'
                      '\n\t[2] Create Current Account'
                      '\n\t[3] Delete Account'
                      '\n\t[4] Show All User Account List'
                      '\n\t[5] Show Bank Volt Balance'
                      '\n\t[6] Show Bank Loan Balance'
                      '\n\t[7] NO/OFF Loan Feature'
                      '\n\t[8] Declare Bankrupt'
                      '\n\t[9] Sign out')

                user_input = input('Your selection: ')

                if user_input == '1':
                    name = input('Enter your name: ')
                    city = input('City: ')
                    email = input('Email: ')
                    SavingsAccount(name, city, email)

                elif user_input == '2':
                    name = input('Enter your name: ')
                    city = input('City: ')
                    email = input('Email: ')
                    CurrentAccount(name, city, email)

                elif user_input == '3':
                    account_number = input('Enter your account number: ')
                    commerzbank.delete_account(account_number)

                elif user_input == '4':
                    commerzbank.show_all_account_info()

                elif user_input == '5':
                    commerzbank.show_bank_volt_balance()

                elif user_input == '6':
                    commerzbank.show_total_bank_loan_amount()

                elif user_input == '7':
                    print('\nSelect Option:'
                          '\n\t[1] Turn ON Loan Feature'
                          '\n\t[2] Turn OFF Loan Feature')
                    user_input = input('Your selection: ')
                    if user_input == '1':
                        commerzbank.loan_feature_controller('ON')
                    elif user_input == '2':
                        commerzbank.loan_feature_controller('OFF')
                    else:
                        print('Invalid Option Selected.')

                elif user_input == '8':
                    commerzbank.declare_bankruptcy()

                elif user_input == '9':
                    print('Logged out from Admin/Managerial access.')
                    break

                else:
                    print('Invalid Option Selected.')
                    continue

#-----------------------------------------------------------------------------------------------------------------------

        elif user_input == '3':
            print('\n----- User/Account Holder access given -----')
            while True:
                print('\nSelect Option:'
                      '\n\t[1] Create Account'
                      '\n\t[2] Show Available Balance'
                      '\n\t[3] Deposit Money'
                      '\n\t[4] Withdraw Money'
                      '\n\t[5] Transfer Money'
                      '\n\t[6] Apply for Loan'
                      '\n\t[7] Show Loan Balance'
                      '\n\t[8] Show Transaction History'
                      '\n\t[9] Sign out')

                user_input = input('Your selection: ')

                if user_input == '1':
                    while True:
                        print('\nAccount Type:'
                              '\n\t[1] Savings Account'
                              '\n\t[2] Current Account')

                        user_input = input('Your selection: ')

                        if user_input == '1':
                            name = input('Enter your name: ')
                            city = input('City: ')
                            email = input('Email: ')
                            SavingsAccount(name, city, email)
                            break

                        elif user_input == '2':
                            name = input('Enter your name: ')
                            city = input('City: ')
                            email = input('Email: ')
                            CurrentAccount(name, city, email)
                            break

                        else:
                            print('Invalid Option Selected.')
                            continue

                elif user_input == '2':
                    account_number = input('Enter your account number: ')
                    if account_number[:2] == 'SV':
                        SavingsAccount.check_balance(account_number)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.check_balance(account_number)
                    else:
                        print(f'Invalid account number.')

                elif user_input == '3':
                    account_number = input('Enter your account number: ')
                    deposit_amount = int(input('How much you want to deposit: '))

                    if account_number[:2] == 'SV':
                        SavingsAccount.deposit_money(account_number, deposit_amount)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.deposit_money(account_number, deposit_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == '4':
                    account_number = input('Enter your account number: ')
                    desire_amount = int(input('How much you want to withdraw: '))

                    if account_number[:2] == 'SV':
                        SavingsAccount.withdraw_money(account_number, desire_amount)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.withdraw_money(account_number, desire_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == '5':
                    your_account_number = input('Enter your account number: ')
                    target_account_number = input('Enter beneficiary account number: ')
                    transfer_amount = int(input('How much you want to transfer: '))

                    if your_account_number[:2] == 'SV':
                        SavingsAccount.transfer_money(your_account_number, target_account_number, transfer_amount)
                    elif your_account_number[:2] == 'CR':
                        CurrentAccount.transfer_money(your_account_number, target_account_number, transfer_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == '6':
                    account_number = input('Enter your account number: ')
                    loan_amount = int(input('How much you want to loan: '))

                    if account_number[:2] == 'SV':
                        print('Loan feature is only available for Current accounts.')
                    elif account_number[:2] == 'CR':
                        CurrentAccount.apply_loan(account_number, loan_amount)
                    else:
                        print(f'Invalid account number.')

                elif user_input == '7':
                    account_number = input('Enter your account number: ')
                    if account_number[:2] == 'SV':
                        print('Loan feature is only available for Current accounts.')
                    elif account_number[:2] == 'CR':
                        account_exists = False
                        for account in commerzbank.AllCurrentAccounts:
                            if account['AccountNumber'] == account_number:
                                account_exists = True
                                print('Currently total loan taken under your account is', account['LoanTaken'], '€')
                                continue
                        if not account_exists:
                            print(f'Account {account_number} does not exist.')
                    else:
                        print(f'Invalid account number.')

                elif user_input == '8':
                    account_number = input('Enter your account number: ')
                    if account_number[:2] == 'SV':
                        SavingsAccount.show_transaction_history(account_number)
                    elif account_number[:2] == 'CR':
                        CurrentAccount.show_transaction_history(account_number)
                    else:
                        print(f'Invalid account number.')

                elif user_input == '9':
                    print('Logged out from User/Account Holder access.')
                    break
                else:
                    print('Invalid Option Selected.')
                    continue

#-----------------------------------------------------------------------------------------------------------------------

        elif user_input == '4':
            print('Logged out from Total System.')
            sys.exit()

#-----------------------------------------------------------------------------------------------------------------------

        else:
            print('Invalid Option Selected.')
            continue

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
