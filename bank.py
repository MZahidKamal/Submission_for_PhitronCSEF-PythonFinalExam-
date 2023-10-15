class Bank:
    AllAccounts = []
    AllSavingAccounts = []
    AllCurrentAccounts = []
    TotalBankBalance = 0
    TotalLoanTaken = 0
    Loan_Feature_Controller = True
    Banking_Service_Controller = True

    def __init__(self, name, road, house_no, zip_code, city, state, country, url):
        self.Name = name
        self.Road = road
        self.HouseNo = house_no
        self.ZIPCode = zip_code
        self.City = city
        self.State = state
        self.Country = country
        self.Website = url

    def bank_info(self):
        print(f'\n----- Bank Information -----\n{self.Name}\n{self.Road} {self.HouseNo}\n{self.ZIPCode} {self.City}\n{self.State} {self.Country}\n{self.Website}')

    @classmethod
    def show_all_account_info(cls):

        for sv_account in cls.AllSavingAccounts:
            print('Account No:', sv_account['AccountNumber'], '\tType:', sv_account['AccountType'], '\tBalance:', sv_account['CurrentBalance'], '€', '\tName:', sv_account['Name'])

        for cr_account in Bank.AllCurrentAccounts:
            print('Account No:', cr_account['AccountNumber'], '\tType:', cr_account['AccountType'], '\tBalance:', cr_account['CurrentBalance'], '€', '\tLoan:', cr_account['LoanTaken'], '€', '\tName:', cr_account['Name'])

    def show_bank_volt_balance(self):
        print(f'Currently total bank volt balance is {self.TotalBankBalance}€')

    def show_total_bank_loan_amount(self):
        print(f'Currently total bank loan amount is {self.TotalLoanTaken}€')

    @classmethod
    def delete_account(cls, target_account_number):
        if target_account_number[:2] == 'SV':
            for sv_account in cls.AllSavingAccounts:
                if sv_account['AccountNumber'] == target_account_number:
                    balance = sv_account['CurrentBalance']
                    cls.AllSavingAccounts.remove(sv_account)
                    cls.AllAccounts.remove(sv_account)
                    cls.TotalBankBalance -= balance
                    if balance == 0:
                        print(f'Successfully removed account {target_account_number}.')
                    else:
                        print(f'Successfully removed account {target_account_number} and cash returned {balance}€.')
        elif target_account_number[:2] == 'CR':
            for cr_account in cls.AllCurrentAccounts:
                if cr_account['AccountNumber'] == target_account_number:
                    loan = cr_account['LoanTaken']
                    balance = cr_account['CurrentBalance']
                    if loan == 0:
                        if balance == 0:
                            cls.AllCurrentAccounts.remove(cr_account)
                            cls.AllAccounts.remove(cr_account)
                            cls.TotalBankBalance -= balance
                            print(f'Successfully removed account {target_account_number}.')
                        else:
                            cls.AllCurrentAccounts.remove(cr_account)
                            cls.AllAccounts.remove(cr_account)
                            cls.TotalBankBalance -= balance
                            print(f'Successfully removed account {target_account_number} and cash returned {balance}€.')
                    else:
                        print(f'To delete the account {target_account_number}, please refund the {loan}€ loan please.')
        else:
            print(f'Account {target_account_number} does not exist.')

    @classmethod
    def loan_feature_controller(cls, decision):
        if decision == 'ON':
            cls.Loan_Feature_Controller = True
            print(f'The bank has launched the loan feature. Therefore applications can be submitted.')
        elif decision == 'OFF':
            cls.Loan_Feature_Controller = False
            print(f'The bank has discontinued the loan feature. Therefore no application will be granted.')

    @classmethod
    def declare_bankruptcy(cls):
        user_input = input('Are you sure that the bank will declare bankruptcy? (y/n): ')
        if user_input == 'y':
            user_input = input('For normal operation, you have to restart the program again. Still sure? (y/n): ')
            if user_input == 'y':
                cls.Banking_Service_Controller = False
                print(f'The Bank declared bankruptcy. Any kind of public service/transactions are discouraged.')
            elif user_input == 'n':
                return
        elif user_input == 'n':
            return
        else:
            print('Invalid Option Selected.')
            return
