def input_price():70

    price = int(input("Введите цену"))
    discount = int(input("Введите скидку"))
    discount_fun(price, discount)

def discount_fun(price, discount):
    if (price or discount) < 0:
        print("Скидка или цена не может быть отрицательной! Введите еще раз.")
        input_price()
    price_with_discount = price * discount / 100
    print(price_with_discount)
    
input_price()






