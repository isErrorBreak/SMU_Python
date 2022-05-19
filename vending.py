#전역 변수 : Global
#RDBMS(관계형 데이터 베이스) SQL
#table


beverage_soda = 10
beverage_can= 20
beverage_water = 20
beverage_ion = 20

Beverage = {'사이다':600,'캔커피':800,'생수':500,'이온음료':1000}
def DiaplayMenu():
    print("===========================상명파이썬자판기 v0.2===================================")
    for k in Beverage.keys():
        print("%s %i \t" %(k, Beverage[k]),end = ' ')
    
    #print("사이다 600원\t 2.캔커피 800원\t 3.생수 500원\t 4.이온음료 1000원")
    print("\n=================================================================================")
    
def InsertCoin():
    
    coin = int(input("금액을 넣으세요"))

    if coin < 500:
        print("금액이 부족합니다 다시 입력하세요.")
        InsertCoin()

    return coin
        
def BeverageInput():
    
    beverage = int(input("음료를 선택하세요"))
    beverage_num = int(input("음료의 수량을 입력하세요"))
    
    return beverage, beverage_num


def Calc(beverage,beverage_num):
    global beverage_soda, beverage_can, beverage_ion, beverage_water

    if beverage==1:
        beverage_price = 600
        beverage_name="사이다"
        beverage_soda -= beverage_num
        print(beverage_name,"남은 수량",beverage_soda)
        
        
    elif beverage==2:
        beverage_price = 800
        beverage_name="캔커피"
        beverage_can -= beverage_num
        print(beverage_name,"남은 수량",beverage_can)
        
    elif beverage==3:
        beverage_price = 500
        beverage_name="생수"
        beverage_water -= beverage_num
        print(beverage_name,"남은 수량",beverage_water)

    elif beverage==4:
        beverage_price = 1000
        beverage_name="이온음료"
        beverage_ion -= beverage_num
        print(beverage_name,"남은 수량",beverage_ion)


    total_price = beverage_num * beverage_price

    print(beverage_name,"음료",beverage_num,"개를 선택하셨습니다")


    return total_price
    
def VendingMachine():
    DiaplayMenu()

    
    insert_coin=InsertCoin()
    print(insert_coin,"원을 투입하셨습니다")

    beverage,beverage_num = BeverageInput()


    totalprice = Calc(beverage,beverage_num)
    print("총금액",totalprice,"원 입니다")
    return_money = insert_coin-totalprice
    if return_money< 0:
        print("돈이",return_money,"원 부족합니다")
        InsertCoin()
    else:
        print("거스름돈",return_money,"원 입니다")
        
       



    

VendingMachine()

    

