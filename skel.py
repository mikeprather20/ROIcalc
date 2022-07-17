class Calculator():

    def __init__(self):
        None

    def intro(self):
        print('\n=====================================================')
        print('Welcome to the ROI (Return on Investment) Calculator!')
        print('=====================================================\n')
        enter = input('To start please type (s): ')
        while enter != 's':
            print('Invalid Response!\n')
            enter = input('To start please type (s): ')

    def income(self):
        print('\nINCOME SECTION')
        print('================')
        print('(Round to the nearest dollar.)')
        print('Enter 0 for empty values and DO NOT use special characters(,.)!\n')
        rent = int(input('Rental Income: $'))
        laundry = int(input('Laundry Income: $'))
        storage = int(input('Storage Income: $'))
        misc = int(input('Misc. Income: $'))
        self.monthly_income = rent + laundry + storage + misc
        print(f'Your Total Monthly Income = ${self.monthly_income}')

    def expenses(self):
        print('\nEXPENSES SECTION')
        print('==================')
        print('(Round to the nearest dollar.)')
        print('Enter 0 for empty values and DO NOT use special characters(,.)!\n')
        tax = int(input('Tax Expense:\n$'))
        ins = int(input('Insurance Expense: $'))
        electric = int(input('Electric Expense: $'))
        waterAsewer = int(input('Water and/or Sewage Expense: $'))
        garbage = int(input('Garbage Expense: $'))
        gas = int(input('Gas Expense: $'))
        hoa = int(input('HOA Expense: $'))
        lawnAsnow = int(input('Lawn and Snow Expense: $'))
        vacancy = int(input('Vacancy Expense: $'))
        repairs = int(input('Repair Expense: $'))
        capEx = int(input('CapEx Expense: $'))
        propmang = int(input('Property Management Expense: $'))
        mortgage = int(input('Mortgage Expense: $'))
        self.monthly_expenses = tax + ins + electric + waterAsewer + garbage + gas + hoa + lawnAsnow + vacancy + repairs + capEx + propmang + mortgage
        print(f'\nYour Total Monthly Expenses = ${self.monthly_expenses}')

    def a_cashflow(self):
        print('\n==================================')
        print('CALCULATING YOUR ANNUAL CASH FLOW!')
        print('==================================')
        enter2 = input('To continue please type (c): ')
        while enter2 != 'c':
            print('Invalid Response!\n')
            enter2 = input('To continue please type (c): ')

        self.annual_cash_flow = (int(self.monthly_income) - int(self.monthly_expenses))*12
        print(f'\nYour Annual Cashlow is: ${self.annual_cash_flow}')

    def investment(self):
        print('\nINVESTMENT SECTION')
        print('==================')
        print('(Round to the nearest dollar.)')
        print('Enter 0 for empty values and DO NOT use special characters(,.)!\n')
        down_pmt = int(input('Down Payment Cost: $'))
        closing_cost = int(input('Closing Cost: $'))
        rehab = int(input('Rehabbing Cost: $'))
        misc_other = int(input('Misc Other Cost: $'))
        self.total_invest = down_pmt + closing_cost + rehab + misc_other
        print(f'\nYour Total Investment is: ${self.total_invest}')

    def returnRoi(self):
        print('\n==========================================')
        print('CALCULATING YOUR ROI (RETURN ON INVESTMENT)!')
        print('==========================================')
        roi = float(self.annual_cash_flow / self.total_invest)*100
        print(f'\nYour ROI (Return on Investment) is: {roi}%\n')


def calcRoi():
    property = Calculator()
    keep_looping = True
    while keep_looping == True:
        print('\nDo you wish to calculate the ROI on your property?')
        greeting = input('Enter (y) or (n): ')
        if greeting != 'n':
            property.intro()
            property.income()
            property.expenses()
            property.a_cashflow()
            property.investment()
            property.returnRoi()
        else:
            enter3 = input('To exit please type (x): ')
            if enter3 != 'x':
                print('Invalid Response!\n')
                enter3 = input('To exit please type (x): ')
            else:
                break
calcRoi()
