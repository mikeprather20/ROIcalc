#Simple ROI Calc

investment = 40000
monthlyCashFlow = 700
expenses = 1000

def ROI(investment, monthlyCashFlow, expenses):
    annualCashFlow = monthlyCashFlow * 12 - expenses
    ROI = (annualCashFlow/investment)*100
    print(ROI)

ROI(investment, monthlyCashFlow, expenses)