
def raindrops(number): #Creating a function called raindrops
    string = '' #Here I've created an object and initialized this as an empty string
    if number % 3 == 0:  #Here I've created a if statement. If number has a factor of 3, it will expect an outcome of 'Pling'
        string += 'Pling'
    if number % 5 == 0:  #If number has a factor of 5, it will expect an outcome of 'Plang'
        string += 'Plang'
    if number % 7 == 0:
        string += 'Plong'  #If number has a factor of 5, it will expect an outcome of 'Plong'
    if len(string) == 0:
        string += str(number) #If the number does not have a factor of 3,5 or 7 it will return the number as string
    return string