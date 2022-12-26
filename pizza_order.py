"""         METHOD 1 """
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepp eroni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size =="S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":fi
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


"""      METHOD2             """

S, M, L, CHZ, Bl = 15, 20, 25, 1, 0
print("Welcome to Python Pizza Deliveries!")
P_O = (input("What size pizza do you want? S, M, or L ")).upper
PP_o = (input("Do you want pepperoni? Y or N ")).upper
chz_O = (input("Do you want extra cheese? Y or N ")).upper

if P_O == 'S':
    Bl = 15
    if PP_o == 'Y':
        Bl += 2
        if chz_O == 'Y':
            Bl += 1 
            print('Bill total: ', str(Bl) + ' USD') 
        else:
           print('Bill total: ', str(Bl) + ' USD') 
    else:
        Bl += 0
        if chz_O == 'Y':
            Bl += 1 
            print('Bill total: ', str(Bl) + ' USD')
        else:
           print('Bill total: ', str(Bl) + ' USD')

elif P_O == 'M':
    Bl = 20
    if PP_o == 'Y':
        Bl += 3
        if chz_O == 'Y':
            Bl += 1 
            print('Bill total: ', str(Bl) + ' USD') 
        else:
           print('Bill total: ', str(Bl) + ' USD') 
    else:
        Bl += 0
        if chz_O == 'Y':
            Bl += 1 
            print('Bill total: ', str(Bl) + ' USD')
        else:
           print('Bill total: ', str(Bl) + ' USD')

else:
    Bl = 25
    if PP_o == 'Y':
        Bl += 3
        if chz_O == 'Y':
            Bl += 1 
            print('Bill total: ', str(Bl) + ' USD') 
        else:
           print('Bill total: ', str(Bl) + ' USD') 
    else:
        Bl += 0
        if chz_O == 'Y':
            Bl += 1 
            print('Bill total: ', str(Bl) + ' USD')
        else:
           print('Bill total: ', str(Bl) + ' USD')
