# input วันเริ่มต้น แล้วก็ใส่อุณหภูมิในหน่วย celsius ถ้าหยุดให้พิมพ์ E หรือ e
# output เป็น farenheit สลับกับ kelvin (ถ้าวันเริ่มต้นเป็นเลขคู่ จะแสดงผลเป็น Fahrenheit ก่อน, ถ้าวันเริ่มเป็นเลขคี่จะแสดงผลเป็น Kelvin ก่อน)

d = int(input("Enter start date: "))
if d > 0:
    start = d
    data = []
    while True:
        x = input(f"Enter degrees Celsius of date {d}: ")
        if x[0] == "e" or x[0] == "E":
            break
        data.append(int(x))
        d = d+1
    
    d = start
    for x in data:
        if d%2 == 0:
            fah = (x*9)/5+32
            print(f"Date {d} has degrees Fahrenheit of {fah:.1f}")
        else:
            kel = x+273.15
            print(f"Date {d} has degrees Kelvin of {kel:.1f}")
        d = d+1
else:
    print("Program exits")