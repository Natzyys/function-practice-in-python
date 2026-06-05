'''Latihan fungsi'''

import os 

# # menghitung luas dan keliling persegi panjang
# os.system("cls")
# print(f"{"MENGHITUNG LUAS DAN":^50}")
# print(f"{"KELILING PERSEGI PANJANG  ":^50}")
# print(f"{"="*50:^50}")


# #input user
# PANJANG = int(input("Panjang ="))
# LEBAR = int(input("Lebar ="))

# # menghitung luas 
# LUAS = PANJANG * LEBAR
# KELILING = 2*PANJANG + 2*LEBAR

# # show the result
# print(f"result perhitungan LUAS ={LUAS}")
# print(f"result perhitungan KELILING ={KELILING}")

def header():
    os.system("cls")
    print(f"{"calculating the area and":^50}")
    print(f"{"perimeter of a rectangle":^50}")
    print(f"{"="*50:^50}")

def input_user():
    Lengt = int(input(f"Length ="))
    Width = int(input(f"Width ="))
    return Lengt, Width

def area(Length,Width):
    return Length*Width

def perimeter(Length, Width):
    return 2*(Length + Width)

def display(message, value):
    print(f"result of the {message} calculation = {value}")


# Main Program
while True:
    header()
    option = input("type 1 = area\ntype 2 = perimeter\n:")
    if option == "1":
        WIDTH,LENGTH = input_user()
        AREA = area(LENGTH,WIDTH)
        display("area", AREA)
    elif option == "2":
        WIDTH,LENGTH = input_user()
        PERIMETER = perimeter(LENGTH,WIDTH)
        display("perimeter", PERIMETER)
    else:
        print("pls type correctly")
    Continue = input("shall we continue? (y/n):")
    if Continue != "y":
        break

print(f"end the program")




