"Hello".upper( )
print("Hello")
#List represented by bracklets
fruit = list ()
fruit

fruit = []
fruit

fruit = ["Apple", "Orange", "Pear"]
print(fruit)

fruit.append ("Banana")
fruit.append ("Peach")
fruit
print (fruit)

random = [ ]
random.append (True)
random.append (100)
random.append (1.1)
random.append ("Hello")
random
print(random)

print("fruit 0 =", fruit[0] )

try:
    friut [9]
except (NameError):
    print ("Index position is empty")

fruit [4] = "grape"
print(fruit)

not_fruit = fruit.pop()
print(not_fruit)
print(fruit)

def fruit_check(x):
    return x in fruit
print("Yes it is in there")

fruit_check("Apple")

# def fruit_check_auto():
#   f = input ("type a fruit:")
#   f = str(f)
#   if f in fruit:
#       print("Yes your input is in there.")
#   if f not in fruit:
#       print("No, your input is not in there.")


#fruit_check_auto()

colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]

print(colors1)
print (colors2)


colors3 = colors1 + colors2

print(colors3)

length_of_colors3 = len(colors3)
print (length_of_colors3)

    


