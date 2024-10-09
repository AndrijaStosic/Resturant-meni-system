from tkinter import *
import socket
import threading

brojac = 0
narudzbine = []
list = []

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  
    server_socket.listen(1)
    print("Waiting to cliend...")
    
    client_socket, address = server_socket.accept()
    print(f"Connested to {address}")
    
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Order confirmed: {data}")
    
    client_socket.close()
    server_socket.close()

# Uključi server u drugi thread
threading.Thread(target=start_server, daemon=True).start()

prozor = Tk()
prozor.geometry("1250x800")
prozor.title('Restaurant Menu System')
prozor.config(bg="lightblue")

def slano():
    brisi_widgete()

    def pica():
        global brojac
        narudzbine.append("Pica")
        brojac += 1

    def Pasta():
        global brojac
        narudzbine.append("Pasta")
        brojac += 1

    def burger():
        global brojac
        narudzbine.append("Burger")
        brojac += 1

    def meat():
        global brojac
        narudzbine.append("Meso")
        brojac += 1

    pasta = Button(text="Pasta", background='orange', fg='BLACK', height=15, width=20, command=Pasta)
    pasta.place(x=150, y=250)
    list.append(pasta)

    pizza = Button(text="Pizza", background='tomato', fg='BLACK', height=15, width=20, command=pica)
    pizza.place(x=400, y=250)
    list.append(pizza)

    burger = Button(text="Burger", background='chocolate', fg='BLACK', height=15, width=20, command=burger)
    burger.place(x=650, y=250)
    list.append(burger)

    meat = Button(text="Meat", background='skyblue', fg='BLACK', height=15, width=20, command=meat)
    meat.place(x=900, y=250)
    list.append(meat)

    go_back = Button(text="GO BACK", bg='blue', fg='white', height=3, width=10, command=pocetak)
    go_back.place(x=1, y=750)
    list.append(go_back)

def pice():
    brisi_widgete()

    def cola():
        global brojac
        narudzbine.append("Kola")
        brojac += 1

    def fanta():
        global brojac
        narudzbine.append("Fanta")
        brojac += 1

    def sprite():
        global brojac
        narudzbine.append("Sprite")
        brojac += 1

    def apple_juice():
        global brojac
        narudzbine.append("Sok od jabuke")
        brojac += 1

    cola = Button(text="Cola", background='chocolate', fg='BLACK', height=15, width=20, command=cola)
    cola.place(x=150, y=250)
    list.append(cola)

    fanta = Button(text="Fanta", background='Orange', fg='BLACK', height=15, width=20, command=fanta)
    fanta.place(x=400, y=250)
    list.append(fanta)

    sprite = Button(text="Sprite", background='gray', fg='BLACK', height=15, width=20, command=sprite)
    sprite.place(x=650, y=250)
    list.append(sprite)

    apple_juice = Button(text="Apple Juice", background='tomato3', fg='BLACK', height=15, width=20, command=apple_juice)
    apple_juice.place(x=900, y=250)
    list.append(apple_juice)

    go_back = Button(text="GO BACK", bg='blue', fg='white', height=3, width=10, command=pocetak)
    go_back.place(x=1, y=750)
    list.append(go_back)

def gricke():
    brisi_widgete()

    def chips():
        global brojac
        narudzbine.append("Chips")
        brojac += 1

    def chitos():
        global brojac
        narudzbine.append("Chitos")
        brojac += 1

    def hot_chips():
        global brojac
        narudzbine.append("Hot Chips")
        brojac += 1

    def popcorn():
        global brojac
        narudzbine.append("Popcorn")
        brojac += 1

    chips = Button(text="Chips", background='gold2', fg='BLACK', height=15, width=20, command=chips)
    chips.place(x=150, y=250)
    list.append(chips)

    chitos = Button(text="Chitos", background='Orange', fg='BLACK', height=15, width=20, command=chitos)
    chitos.place(x=400, y=250)
    list.append(chitos)

    hot_chips = Button(text="Hot chips", background='red', fg='BLACK', height=15, width=20, command=hot_chips)
    hot_chips.place(x=650, y=250)
    list.append(hot_chips)

    popcorn = Button(text="Popcorn", background='gray', fg='BLACK', height=15, width=20, command=popcorn)
    popcorn.place(x=900, y=250)
    list.append(popcorn)

    go_back = Button(text="GO BACK", bg='blue', fg='white', height=3, width=10, command=pocetak)
    go_back.place(x=1, y=750)
    list.append(go_back)

def slatko():
    brisi_widgete()

    def chocolate_cake():
        global brojac
        narudzbine.append("Chocolate Cake")
        brojac += 1

    def strawberry_cake():
        global brojac
        narudzbine.append("Strawberry Cake")
        brojac += 1

    def cupcake():
        global brojac
        narudzbine.append("Cupcake")
        brojac += 1

    def chocolate_sticks():
        global brojac
        narudzbine.append("Chocolate Sticks")
        brojac += 1

    chocolate_cake = Button(text="Chocolate Cake", background='chocolate', fg='BLACK', height=15, width=20, command=chocolate_cake)
    chocolate_cake.place(x=150, y=250)
    list.append(chocolate_cake)

    strawberry_cake = Button(text="Strawberry Cake", background='Pink', fg='BLACK', height=15, width=20, command=strawberry_cake)
    strawberry_cake.place(x=400, y=250)
    list.append(strawberry_cake)

    cupcake = Button(text="Cupcake", background='gray', fg='BLACK', height=15, width=20, command=cupcake)
    cupcake.place(x=650, y=250)
    list.append(cupcake)

    chocolate_sticks = Button(text="Chocolate Sticks", background='orange3', fg='BLACK', height=15, width=20, command=chocolate_sticks)
    chocolate_sticks.place(x=900, y=250)
    list.append(chocolate_sticks)

    go_back = Button(text="GO BACK", bg='blue', fg='white', height=3, width=10, command=pocetak)
    go_back.place(x=1, y=750)
    list.append(go_back)

def brisi_widgete():
    global list
    for widget in list:
        widget.destroy()
    list.clear()

def potvrdi_porudzbinu():
    global brojac
    porudzbine = "Porudzbina: "
    for element in narudzbine:
        porudzbine += f"{element}, "
    print(porudzbine[:-2])  
    send_order(porudzbine[:-2])  
    narudzbine.clear()  

def send_order(order):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  
    client_socket.send(order.encode())  
    client_socket.close()

def pocetak():
    brisi_widgete()
    salt_food = Button(text="Salt food", background='yellow3', fg='BLACK', height=15, width=20, command=slano)
    salt_food.place(x=150, y=250)
    list.append(salt_food)

    drinks = Button(text="drinks", background='skyblue', fg='BLACK', height=15, width=20, command=pice)
    drinks.place(x=400, y=250)
    list.append(drinks)

    snacks = Button(text="snacks", background='lightgreen', fg='BLACK', height=15, width=20, command=gricke)
    snacks.place(x=650, y=250)
    list.append(snacks)

    sweets = Button(text="sweets", background='pink', fg='BLACK', height=15, width=20, command=slatko)
    sweets.place(x=900, y=250)
    list.append(sweets)

    confirm_order = Button(text="Confirm Order", bg='blue', fg='white', height=3, width=10, command=potvrdi_porudzbinu)
    confirm_order.place(x=600, y=500)
    list.append(confirm_order)


pocetak()
prozor.mainloop()
