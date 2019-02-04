cars = ["Ford" , "BMW", "Kia", "is it working?"]


def printCars():

    i = 0
    for car in cars:
        if i == 0:
            print "The top car is " + cars[i]
            i = i +1
        elif i == 1:
            print "The second car is " + cars[i]
            i = i +1
        elif i == 2:
            print "The third care is " + cars[i]
            i = i +1
        else:
            print "That is all the cars!"

printCars()

