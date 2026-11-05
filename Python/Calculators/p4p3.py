print('Tax calculator')
amount = float(input('Please enter amount you want to calculate:')) 
large_amount = amount*0.60
small_amount = amount*0.40
lrg_amount_rate = 0.135
smll_amount_rate = 0.23

taxed_lrg = large_amount*lrg_amount_rate
taxed_smll = small_amount*smll_amount_rate
total = large_amount+small_amount+taxed_lrg + taxed_smll

print('Initial amount:',amount)
print('13.5% tax for large amount:',taxed_lrg)
print('23% tax for small amount:',taxed_smll)
print('Total tax due:',taxed_lrg+taxed_smll)
print('Total amount plus tax:',total)

