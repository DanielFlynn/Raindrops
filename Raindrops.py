def raindrops(number):
    statement = ''
    if number % 3 == 0:
        statement += 'Pling'
    if number % 5 == 0:
        statement += 'Plang'
    if number % 7 == 0:
        statement += 'Plong'
    if len(statement) == 0:
        statement += str(number)
    return statement