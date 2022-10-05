cont = ("yes")

name = input("what's your name? ")

print ("Hello " + name + ". Thank you for choosing our store. Here are the available sections. \n Produce, Deli, Bakery, Alcohol, Beverages, Frozen foods, Pharmacy")

Produce = {'lettuce':'$2','apples':'$1.80/lb','oranges':'$2.50/lb','grapes':'$2/lb','watermelon':'$5','mango':'$0.80','celery':'$1.79','bananas':'$0.49/lb','strawberries':'$3/lb','kiwis':'$4/lb'}
Deli = {'turkey':'$6.50','ham':'$6.50','roast beef':'$6.50','pepperoni':'$5','chicken':'$4/lb','steak':'$14/lb','sandwich':'$5','salad':'$4','cheese':'$3','soup':'$2.70'}
Bakery = {'bread':'$4','cake':'$6','cupcakes':'$3.50','donuts':'$3','brownies':'$5','pie':'$4','cheesecake':'$4','muffins':'$3','cookies':'$2.50','rolls':'$5'}
Alcohol = {'wine':'10','whiskey':'$30','beer':'$16','vodka':'$14','tequila':'$40','bourbon':'$35','sake':'$10','champagne':'$45','seltzers':'$13','sparkling water':'$10'}
Beverages = {'rootbeer':'$2','sprite':'$2','monster':'$3.50','redbull':'$3','fanta':'$2','coke':'$2','dr pepper':'$2','pepsi':'$2','mtn dew':'$2','coffee':'$3.50'}
Frozen = {'ice cream':'$3.75','pizza':'$6','fries':'$4','breakfast sandwich':'$4','vegetables':'$5','pizza rolls':'$3.50','waffles':'$3','fish':'$6','chicken':'$5.50','hash browns':'$4'}
Pharmacy = {'advil':'$7','tylenol':'$11','icyhot':'$8.40','vitamins':'$9','protein':'$18','toothpaste':'$2.50','deodorant':'$7','shampoo':'$9','soap':'$6','wipes':'$5'}

#checkpoint
def func(x):
    for key, value in x.items():
        print(key, value)

while (cont == "yes"):

    sec = input("Please enter a section. ")

    if sec == 'Produce':
        func(Produce)

    elif sec == 'Deli':
        func(Deli)
        
    elif sec == 'Bakery':
        func(Bakery)

    elif sec == 'Alcohol':
        func(Alcohol)

    elif sec == 'Beverages':
        func(Beverages)

    elif sec == 'Frozen':
        func(Frozen)

    elif sec == 'Pharmacy':
        func(Pharmacy)

    cont = input('Would you like to check the price of more items? ')