import random

def heppyeatinbiryaaneericeteppan(Yumable="lamb"):

    price=0
    
    if Yumable=="lamb":
        print("1.1 buy biryani-lamb from indus valley")
        price=40
          
    elif Yumable=="dajjaj":
        print("1.2 buy biryani-dajjaj from indus valley")
        price=30
    
    elif Yumable=="camel":
        print("1.3 buy biryani-camel from indus valley")
        price=55

    else:
        print("1.4 buy biryani-arrnab from indus valley")
        price=50

        
    print("2. open da packages")
    print("3. take da food outta box")
    print("4. take ur plate")
    print("5. put ur biryani and ",Yumable," inplate")
    print("6. enjoy ur biryani-",Yumable," rice with ur hand washed with flowing water!")
    
    return price
    
heppyeatinbiryaaneericeteppan("lamb")
heppyeatinbiryaaneericeteppan("dajjaj")

totalprice=0

for i in range(100):
    print(i+1)
    totalprice+=heppyeatinbiryaaneericeteppan(random.choice(["lamb", "dajjaj", "camel", "arrnab"]))

heppyeatinbiryaaneericeteppan()
print(totalprice)
print(heppyeatinbiryaaneericeteppan())
print(random.choice([1,2,3,4]))
print(range(10))