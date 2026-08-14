from demo4_shopping_cart.item_module import Item


item1=Item(101,"mobile",4,9000)
item2=Item(102,"watch",1,5000)


# item2.print_discounted_price()

# item1.print_discounted_price()

print(item1.price)
item1.set_discounted_price()

print(item1.price)

print(item2.price)
item2.set_discounted_price()
print(item2.price)


