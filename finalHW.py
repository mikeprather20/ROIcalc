class Calculator():

    def __init__(self):
        None


    def intro(self):

        print('\n=====================================================')
        print('Welcome to the ROI (Return on Investment) Calculator!')
        print('=====================================================\n')

        enter = input('To start, type (start): ').lower()

        while enter != 'start':
            print('Invalid Input!\n')
            enter = input('To start, type (start): ').lower()


    def income(self):

        print('\nINCOME SECTION')
        print('================')
        print('Enter 0 for empty values and only use whole numbers!\n')

        while True:
            try:
                rent = int(input('Rental Income: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                laundry = int(input('Laundry Income: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                storage = int(input('Storage Income: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                misc = int(input('Misc Income: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        self.monthly_income = rent + laundry + storage + misc
        print(f'[[[[Your Total Monthly Income = ${self.monthly_income}]]]]')


    def expenses(self):

        print('\nEXPENSES SECTION')
        print('==================')
        print('Enter 0 for empty values and only use whole numbers!\n')

        while True:
            try:
                tax = int(input('Tax Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                ins = int(input('Insurance Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                electric = int(input('Electric Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                waterAsewer = int(input('Water and/or Sewage Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                garbage = int(input('Garbage Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                gas = int(input('Gas Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                hoa = int(input('HOA Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                lawnAsnow = int(input('Lawn/Snow Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                vacancy = int(input('Vacancy Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                repairs = int(input('Repair Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                capEx = int(input('CapEx Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                propmang = int(input('Property Management Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        mortgage = int(input('Mortgage Expense: $'))
        while True:
            try:
                mortgage = int(input('Mortgage Expense: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        self.monthly_expenses = tax + ins + electric + waterAsewer + garbage + gas + hoa + lawnAsnow + vacancy + repairs + capEx + propmang + mortgage
        print(f'\n[[[[Your Total Monthly Expenses = ${self.monthly_expenses}]]]]')


    def a_cashflow(self):

        print('\n==================================')
        print('CALCULATING YOUR ANNUAL CASH FLOW!')
        print('==================================')

        self.annual_cash_flow = (int(self.monthly_income) - int(self.monthly_expenses))*12
        print(f'\n[[[[Your Annual Cash Flow Is: ${self.annual_cash_flow}]]]]')


    def investment(self):

        print('\nINVESTMENT SECTION')
        print('==================')
        print('Enter 0 for empty values and only use whole numbers!\n')

        while True:
            try:
                down_pmt = int(input('Down Payment Cost: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                closing_cost = int(input('Closing Cost: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                rehab = int(input('Rehabbing Cost: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue

        while True:
            try:
                misc_other = int(input('Misc Other Cost: $'))
                break
            except ValueError:
                print('Please only use a whole number.')
                continue


        self.total_invest = down_pmt + closing_cost + rehab + misc_other
        print(f'\n[[[[Your Total Investment is: ${self.total_invest}]]]]')


    def returnRoi(self):

        print('\n==========================================')
        print('CALCULATING YOUR ROI (RETURN ON INVESTMENT)!')
        print('==========================================')

        roi = float(self.annual_cash_flow / self.total_invest)*100
        print(f'\n[[[[Your ROI (Return on Investment) is: {roi}%]]]]\n')


def calcRoi():

    property = Calculator()
    keep_looping = True

    while keep_looping == True:

        print('\nDo you want to calculate the ROI on your new property, for the low amount of $100.00 !?')
        greeting = input('Enter (yes) or (no): ').lower()

        if greeting != 'no':
            property.intro()
            property.income()
            property.expenses()
            property.a_cashflow()
            property.investment()
            property.returnRoi()
        else:
            enter3 = input('Maybe next time! Please type (exit) to leave: ').lower()

            if enter3 != 'exit':
                print('Invalid Input!\n')
                enter3 = input('To exit please type (x): ').lower()
            else:
                break
calcRoi()
