#create variable Input_city and ask the user to input the city or town they live in
#create variable cities and set it to the list of cities
#create variable province and set it to the list of provinces
#create variable connacht and set it to the cities in Connacht
#create variable leinster and set it to the cities in Leinster
#create variable munster and set it to the cities in Munster
#create variable ulster and set it to the cities in Ulster
#if Input_city is in cities
#    if Input_city is in connacht
#        print that Input_city is in Connacht
#    elif Input_city is in leinster
#        print that Input_city is in Leinster
#    elif Input_city is in munster
#        print that Input_city is in Munster
#    elif Input_city is in ulster
#        print that Input_city is in Ulster
#else
#    print that the name was not recognised

Input_city = str(input('Enter the city or town you live in? '))

cities = 'Dublin', 'Belfast', 'Cork', 'Limerick', 'Derry','Galway', 'Lisburn', 'Kilkenny', 'Waterford', 'Sligo'

connacht = 'Galway','Sligo' 
leinster = 'Dublin','Kilkenny'
munster = 'Cork','Limerick','Waterford'
ulster = 'Belfast','Derry','Lisburn'




if Input_city in cities:
    if Input_city in connacht:
        print('You entered',Input_city + ".", Input_city,'is in Connacht.')
    elif Input_city in leinster:
        print('You entered',Input_city + ".", Input_city,'is in Leinster.')
    elif Input_city in munster:
        print('You entered',Input_city + ".", Input_city,'is in Munster.')
    elif Input_city in ulster:
        print('You entered',Input_city + ".", Input_city,'is in Ulster.')
else:
    print('Sorry, I didn’t recognise that name.')
    
        

      


    