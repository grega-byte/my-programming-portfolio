amount = 261598.05
large_amount = amount*0.60
small_amount = amount*0.40
hightax_rate = 0.23
lowtax_rate = 0.135
total = amount + large_amount*lowtax_rate + small_amount*hightax_rate
print('Total:',total)