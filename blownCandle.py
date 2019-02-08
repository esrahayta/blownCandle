import random

class ChildAge:

    print('------------------------------------------')
    print('    Children Birthday Cake Candles')
    print('------------------------------------------')
    print()
    
#cocuk pastası oldugundan random atanan yas 15'e kadar alındı   
def candle(cls):
    #10 tane random sayı üretildi
    for i in range(1,11):
        age=random.randint(1,15)
        print(age, "age", age,"candle")
        candleList=[]
        #her yaş için random sayıda mum boyları candleList'e atandı.(mum=yaş)
        for j in range(1,age+1):
            size=random.randint(1,age)
            candleList.append(size)
        print("candles lengths=    ", candleList)
        #en uzun mum ve üflenecek mum sayısı
        print("longest candle:",max(candleList))
        blowNumber=max(candleList)
        print("number of candles to be blown : ",candleList.count(blowNumber))
        
class List():
    pass
                
List.my_method = classmethod(candle)
List.my_method()
