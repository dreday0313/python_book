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

# Tuples stores objects in specific order. Tuples are immutable. Represented with parentheeses
# Separate items in a tuple with a comma

my_tuple = tuple ()
my_tuple2 = ()

rndm = ("M. Jackson", 1958, True)
rndm
print(rndm)

dys = ("1984", "Brave New World", "Fahrenheit 451")

print(dys[2])


if "1984" in dys:
    print(True)
else:
    print("Not in the Tuple.")


# Dictionaries
# Used to link one object called a key to another object called a value.
# Linking one object to another is called mapping
# The result is called a key-value pair
# Can look up a key and gets the value in return
# Can not lookup value and get key
# Dictionaries are mutable
# Dictionaries are not stored in a specific order
# Dictionaries not represented with curly brackets 



# add key value pair with syntax key separated from value by a colon
my_fruits = {"Apple":"Red", "Banana":"Yellow"}
print(my_fruits)

#create dictonary
facts = dict ()
# add a value
facts ["code"] = "fun"
#look up a key and return the value
facts["code"]


#add a value
facts["Bill"] = "Gates"
# look up a key
facts["Bill"]

#add
facts ["founded"] = "1776"

print(facts["Bill"])

if "Bill" in facts:
    print("The key is in there.")
else:
    print("The listed key is not in there.")

books = {"Dracula": "Stoker", "1984": "Orwell", "The Trial": "Kafka"}
# delete key-value pair with keyword del
del books["The Trial"]
print(books)
#add it back
books["The Trial"] = "Kafka"
print(books["The Trial"])

#dictionary example

rhymes = {"1": "fun", "2": "blue", "3": "me", "4": "floor", "5": "live"}

n = input ("Type a number:")
if n in rhymes:
    rhyme = rhymes [n]
    print(rhyme)
else:
    print ("Not found!")
#You can store containers in containers
lists = []
rap = ["Kayne West", "Jay-Z", "Eninem", "Nas"]
rock = ["Bob Dyan", "The Beatles", "Led Zeppelin"]
djs = ["DJ Woo", "Zeds Dead", "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

rap = lists[0]
print(rap)

rap.append("kendrick Lamar")
print(rap)
print(lists)




    
