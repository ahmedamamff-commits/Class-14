def total_calc(bill_amount, tip_percentage):
    #define function to calculate the tip on the bill
    total = bill_amount*(1 + 0.01*tip_percentage)
    print(f"Please pay ${total}")

#specify only the bill amount
#default value of tip percentage is used

total_calc(150, 20)