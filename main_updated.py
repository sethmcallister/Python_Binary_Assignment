# Assigns a function with the name of convert, and the parameter of i
def convert(i):
    # Checks if the parameter of i is equal to 0
    if i == 0:
        # If return 0
        return "0"
    # Assigns variable of 's' to an empty string
    s = ''
    # does a while i loop; forever
    while i:
        # Uses the bitwise operand of AND (Acts if they where a string of binary data) i & 1 == 1
        if i & 1 == 1:
            # Adds '0' to the front of the variable named 's' and adds 's' back onto itself at the end
            s = "1" + s
        else:
            # Adds '0' to the front of the variable named 's' and adds 's' back onto itself at the end
            s = "0" + s
        # Assigns i back to i / 2 (same as i = i / 2)
        i /= 2
    # Returns the variable of 's' which is a string
    return s


# Assigns a function with the name of equalize, and two parameters of a, and b
def equalize(a, b):
    # Checks if the length of variable a is greater than the length of variable b
    if len(a) > len(b):
        # Does a for loop for every number between 0 and the different between the two variables length
        for i in range(0, len(a) - len(b)):
            # inserts the int 0 at the 0th index in variable b
            b.insert(0, 0)
    # else if the length of a is less than the length of b
    elif len(a) < len(b):
        # Does a for loop for every number between 0 and the different between the two variables
        for i in range(0, len(b) - len(a)):
            # inserts 0 at the 0th index in variable a
            a.insert(0, 0)
    # Returns both a and b
    return a, b


# Assigns a function with the name of sum, and has three parameters, a, b, and ctr
def sum(a, b, ctr):
    # Crates a new variable out assigned to ''
    out = ''

    # Checks if the parameter ctr is greater than 0
    if ctr > 0:
        # Adds the -1th index of the list a to the -1th index of list b and checks if they equal 2
        if a[-1] + b[-1] == 2:
            # sets the variable out to '1'
            out = '1'
        # Adds the -1th index of the list a to the -1th index of the list b and checks if they equal 0
        elif a[-1] + b[-1] == 0:
            # Sets the variable out to '1'
            out = '1'
            # Subtracts one from ctr (same as ctr = ctr -1)
            ctr -= 1
        # If the conditions don't meet previous two statements
        else:
            # out is set to '0'
            out = '0'
    # If the conditions doesn't meet previous statement
    else:
        # Checks if the -1th index in list a added to the -1th index of list b equals 2
        if a[-1] + b[-1] == 2:
            # Sets the variable of out to '0'
            out = '0'
            # Adds one to ctr (Same as ctr = ctr + 1)
            ctr += 1
        # Adds the -1th index of a to the -1th index of b and checks if they equal 0
        elif a[-1] + b[-1] == 0:
            # Sets the variable of out to '0'
            out = '0'
        # If none of the previous conditions are met
        else:
            # The variable out is set to '0'
            out = '1'
    # Returns both the out and ctr variables
    return out, ctr


# Creatse the function sum_check the parameter a, b
def sum_check(a, b):
    # Sets the variable ctr to '0'
    ctr = 0
    # Sets the out variable to an empty list
    out = []
    # Sets the variable of n to the length of the variable a
    n = len(a)
    # Loops through every number between 0 and the variable of n
    for i in range(n):
        # Checks if i does not equal 0
        if i != 0:
            # Sets the variable a to the same list as a previously but excluding the 1 item
            a = a[:-1]
            # Sets the variable b to the same list as b previously but excluding the 1 item
            b = b[:-1]

        # Sets the variables new_out and ctr to the function result of sum(a, b, ctr)
        new_out, ctr = sum(a, b, ctr)
        # Appends out array with the new_out variable
        out.append(new_out)

    # Appends the out array with the ctr variable casted to a String
    out.append(str(ctr))
    # Returns the out variable
    return out


# Creates a function called add with the two paramters a, b
def add(a, b):

    # Returns an array for each line of the input (Generator expression)
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    # Sets both variables a, b to the equalized values of each
    a, b = equalize(a, b)

    # Prints the word 'Result: ' followed by everything in the array returned by the sum_check method except the last
    #  item
    print('Result: ' + ''.join(sum_check(a, b)[::-1]))

# Prints "Please select your first number" into the CLI
print("Please select your first number")

# Takes the first input as a string
in1 = input(">> ")

# Prints "Please select your second number" into the CLI
print("Please select your second number")

# Takes the second input as a string
in2 = input(">> ")

# Assigns each value to the string version that have been converted to binary
bin1 = convert(int(in1))
bin2 = convert(int(in2))

# Will use the function add to add both of the previous variables
add(bin1, bin2)
