## Option 1:
## i = 3
## while i !=0:
##     print ("Yeehaw")
##     i -= 1

## Option 2: 
## for _ in range(3):
##     print ("Yeehaw")

## Option 3: 
## print("Yeehaw\n" * 3,end="")

## Option 4:

# Retrieve n from user and print "Yeehaw" n times
def main():
    number = get_number()
    Yeehaw(number)

# Defines a function to ask and only accept a postivie integer 
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:   # Only accept positive numbers
            break
    return n

# Defines a function that prints "Yeehaw" n times
def Yeehaw(n):
    for _ in range(n):
        print("Yeehaw")

# Execute program
main()