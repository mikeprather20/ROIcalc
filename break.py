print('=====================================================')
print('Welcome to the ROI (Return on Investment) Calculator!')
print('=====================================================\n')
enter = input('To start please type (s): ')
while enter != 's':
    print('Invalid Response!\n')
    enter = input('To start please type (s): ')

print('\nINCOME SECTION')
print('==============')
print('(Round up to the nearest dollar.)')
print('Enter 0 for empty values and DO NOT use special characters(,.)!\n')
rent = int(input('Rental Income: $'))
laundry = int(input('Laundry Income: $'))
storage = int(input('Storage Income: $'))
misc = int(input('Misc. Income: $'))
monthly_income = rent + laundry + storage + misc
print(f'Your Total Monthly Income = ${monthly_income}')

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
monthly_expenses = tax + ins + electric + waterAsewer + garbage + gas + hoa + lawnAsnow + vacancy + repairs + capEx + propmang + mortgage
print(f'\nYour Total Monthly Expenses = ${monthly_expenses}')

print('\n==================================')
print('Calculating Your Annual Cash Flow!')
print('==================================')
enter2 = input('To continue please type (c): ')
while enter2 != 'c':
    print('Invalid Response!\n')
    enter2 = input('To continue please type (c): ')
annual_cash_flow = int((monthly_income - monthly_expenses))*12
print(f'\nYour Annual Cashlow is: ${annual_cash_flow}')

print('\nINVESTMENT SECTION')
print('==================')
print('(Round to the nearest dollar.)')
print('Enter 0 for empty values and DO NOT use special characters(,.)!\n')
down_pmt = int(input('Down Payment Cost: $'))
closing_cost = int(input('Closing Cost: $'))
rehab = int(input('Rehabbing Cost: $'))
misc_other = int(input('Misc Other Cost: $'))
total_invest = down_pmt + closing_cost + rehab + misc_other
print(f'\nYour Total Investment is: ${total_invest}')

print('\n============================================')
print('CALCULATING YOUR ROI (RETURN ON INVESTMENT)!')
print('============================================')
roi = float(annual_cash_flow / total_invest)*100
print(f'\nYour ROI (Return on Investment) is: {roi}%\n')

enter3 = input('To exit please type (x): ')
while True:
    if enter3 != 'x':
        print('Invalid Response!\n')
        enter3 = input('To exit please type (x): ')
    else:
        exit

    def returnRoi(self):

        print('\n==========================================')
        print('CALCULATING YOUR ROI (RETURN ON INVESTMENT)!')
        print('==========================================')
        try:
            roi = float(self.annual_cash_flow / self.total_invest)*100
            print(f'\n[[[[Your ROI (Return on Investment) is: {roi}%]]]]\n')
            break
        except ZeroDivisionError:
            print(f'\n[[[[Your ROI (Return on Investment) is: {roi}%]]]]\n')
            continue


                    
        try:
            misc_other = int(input('Misc Other Cost: $'))
            break
        except ValueError:
            print('Please only use a whole number.')
            continue


        roi = float(self.annual_cash_flow / self.total_invest)*100
        print(f'\n[[[[Your ROI (Return on Investment) is: {roi}%]]]]\n')