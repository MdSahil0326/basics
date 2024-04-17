class card:
    def __init__(self,imageurl,devicetype,price,rating):
        self.imageurl=imageurl
        self.devicetype=devicetype
        self.price=price
        self.rating=rating

product1=card("Dummy-url 1","Mobile",56000 , 4.5)
print("Product - 1 :")
print("imageUrl:",product1.imageurl)
print("deviceType:",product1.devicetype)
print("price:",product1.price)
print("rating:",product1.rating)
print()


product2=card("Dummy-url 2","Laptop",94000 , 4.8)
print("Product - 2 :")
print("imageUrl:",product2.imageurl)
print("deviceType:",product2.devicetype)
print("price:",product2.price)
print("rating:",product2.rating)
print()

product3=card("Dummy-url 3","Smart-watch",18000 , 3.5)
print("Product - 3 :")
print("imageUrl:",product3.imageurl)
print("deviceType:",product3.devicetype)
print("price:",product3.price)
print("rating:",product3.rating)
print()

