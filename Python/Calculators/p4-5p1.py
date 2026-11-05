#create variable eu_us_exchange and ask the user to input the euro amount they want to exchange
#create variable exrate and ask the user to input the current Euro to USD exchange rate
#if eu_us_exchange is less than 0
#    print relevant message
#else
#    print the euro amount converted to dollars


eu_us_exchange = float(input('Input euro amount you want to exchange to dollars:'))

exrate = float(input('Input the current Euro to USD exchange rate:'))

if eu_us_exchange <0:
    print('Amount must be >= 0. Please try again.')
else:
    print('Your Euro to Dollar exchange =','$',eu_us_exchange*exrate)
