# Define an anonymous (lambda) function that calculates the arithmetic mean of two numbers. Details on how to define an anonymous function can be found at:
n1 = int(input("Please give me the first number: "))
n2 = int(input("Please give me the second number: "))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)

print(result)