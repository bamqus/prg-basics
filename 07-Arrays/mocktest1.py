def card(player1,player2):
    suma = 0
    suma1 = 0
    print(f"{player1}:",end=" ")
    for i in player1:
        if i == "A":
            suma += 10
        elif i == "J":
            suma += 10
        elif i == "K":
            suma += 10
        elif i == "Q":
            suma += 10
        elif i == "T":
            suma += 10
        else:
            suma += int(i)
    print(suma)
   
    print(f"{player2}:",end=" ")
    for i in player2:
        if i == "A":
            suma1 += 10
        elif i == "J":
            suma1 += 10
        elif i == "K":
            suma1 += 10
        elif i == "Q":
            suma1 += 10
        elif i == "T":
            suma1 += 10
        else:
            suma1 += int(i)
    print(suma1)

    if suma > suma1:
        return True
    else:
        return False

     
    

    # for i in player2:
    #     print(i)
      


print(card("9532","K8"))