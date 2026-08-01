def main(): 
    n = int(input("What's n? "))
    print_square(n)


def print_square(size):
    for i in range(size):
        # Loop inside a loop
        for j in range(size):
            print('#', end='')
        print()

main()