from tkinter import *
def exam6():
    
    class Beverage:
        def __init__(self, name, price, stock, company):
            self.name = name
            self.price = price
            self.stock = stock
            self.company = company

        def Calculate(self, num):
            beverage_price = self.price*num
            return beverage_price

        def Stock(self):
            beverage_stock = self.stock

    ###투입금액을 입력받아서 윈도우창에 투입금액 표시###
    def insert():
        insertcoin = entry_insertcoin.get()
        label_insertcoin.config(text = "투입금액: " + insertcoin+"원")
        return insertcoin
    
    ###윈도우 창에 계산결과###
    def pay_show():
        insertcoin = insert() #투입 금액 저장
        
        global beverage_coffee_num
        beverage_coffee_num = int(entry_can.get())

        global beverage_soda_num
        beverage_soda_num = int(entry_soda.get())
            
        global beverage_water_num
        beverage_water_num = int(entry_water.get())

        global beverage_coke_num
        beverage_coke_num = int(entry_coke.get())
        
        beverage_coffee = Beverage("캔커피", 800, 10, "상명")
        beverage_coffee_price = beverage_coffee.Calculate(beverage_coffee_num)

        beverage_soda = Beverage("소다", 600, 10, "상명대")
        beverage_soda_price = beverage_soda.Calculate(beverage_soda_num)

        beverage_water = Beverage("생수", 500, 10, "상명대")
        beverage_water_price = beverage_water.Calculate(beverage_water_num)

        beverage_coke = Beverage("콜라", 1000, 10, "상명대")
        beverage_coke_price = beverage_coke.Calculate(beverage_coke_num)

        beverage_total_price = beverage_coffee_price + beverage_soda_price + beverage_water_price + beverage_coke_price

        changecoin = int(insertcoin) - beverage_total_price
        
        if beverage_total_price > int(insertcoin): #만약 총액의 값이 투입 값보다 크면
            label_pay_result.config(text = "금액이 부족합니다.") #금액이 부족하다는 출력결과
            return
        else:   
            label_pay_result.config(text = "결제금액: "+ str(beverage_total_price)+"원\t"+"거스름돈: "+ str(changecoin) +"원")   
            label_beverage_result.config(text = "결제내역: "+str(beverage_coffee.name)+str(beverage_coffee_num)+"개  "+str(beverage_soda.name)+str(beverage_soda_num)+"개  "+str(beverage_water.name)+str(beverage_water_num)+"개 "+str(beverage_coke.name)+str(beverage_coke_num)+"개")
            
    window = Tk()
    window.title("자판기 프로그램")
    window.geometry("800x600")

    label_title = Label(window, text = "상명 파이썬 GUI 자판기 (객체지향)", font = ("맑은 고딕", 22), fg = "blue")
    label_title.pack()

    entry_insertcoin = Entry(window, width = 20)
    entry_insertcoin.pack()

    button_insertcoin = Button(window, text = "투입", command = insert)
    button_insertcoin.pack()

    label_insertcoin = Label(window, text ="투입금액: "+"원", font = ("맑은 고딕", 12) )
    label_insertcoin.pack()
    
    label_beverage_result = Label(window, text = "구매내용", font = ("맑은 고딕", 12), fg = "red")
    label_beverage_result.pack()

    label_pay_result = Label(window, text = "결제내용", font = ("맑은 고딕", 12), fg = "green")
    label_pay_result.pack()
    
    img_can = PhotoImage(file = "can.gif")
    img_soda = PhotoImage(file = "soda.gif")
    img_water = PhotoImage(file = "water.gif")
    img_coke = PhotoImage(file = "coke.gif")

    label_img_can = Label(window, image = img_can, width = 100, height = 200)
    label_img_can.place(x = 200, y = 250)
    
    entry_can = Entry(window, width = 15)
    entry_can.place(x = 200, y = 430)
    
    label_img_soda = Label(window, image = img_soda, width = 100, height = 200)
    label_img_soda.place(x = 350, y = 250)
    
    entry_soda = Entry(window, width = 15)
    entry_soda.place(x = 350, y = 430)
    
    label_img_water = Label(window, image = img_water, width = 100, height = 200)
    label_img_water.place(x = 500, y = 250)
    
    entry_water = Entry(window, width = 15)
    entry_water.place(x = 500, y = 430)

    label_img_coke = Label(window, image = img_coke, width = 100, height = 200)
    label_img_coke.place(x = 650, y = 250)
    
    entry_coke = Entry(window, width = 15)
    entry_coke.place(x = 650, y = 430)


    button_pay = Button(window, text = "계산하기", command = pay_show)
    button_pay.place(x = 380, y = 500)
 

    window.mainloop()
exam6()