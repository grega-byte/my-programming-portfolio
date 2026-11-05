#print tax calculator
#create variable amount and ask the user to input the amount of income
#create variable large_amount and set it to 60% of amount
#create variable small_amount and set it to 40% of amount
#create variable lrg_amount_rate and set it to 20%
#create variable smll_amount_rate and set it to 40%
#calculate the tax on the large amount
#calculate the tax on the small amount
#calculate the total amount
#calculate the total tax
#if amount is less than 0
#    print relevant message
#else
#    print the initial amount
#    print the tax on the large amount
#    print the tax on the small amount
#    print the total tax
#    print the total amount without the tax

print('Tax calculator')
amount = float(input('Please enter amount you want to calculate:')) 
large_amount = amount*0.60
small_amount = amount*0.40
lrg_amount_rate = 0.20
smll_amount_rate = 0.40

taxed_lrg = large_amount*lrg_amount_rate
taxed_smll = small_amount*smll_amount_rate
total = large_amount+small_amount
tax_total = taxed_lrg+taxed_smll

if amount < 0:
    print('Amount of income must be >= 0. Please try again.')
else:
    print('Initial amount:',amount)
    print('20% tax for large amount:',taxed_lrg)
    print('40% tax for small amount:',taxed_smll)
    print('Total tax due:',tax_total)
    print('Total amount less tax:',total-tax_total)



