
letterPositions = []

zero = {'connections' : [1, 3]}
one = {'connections' : [0, 2, 3]}
two = {'connections' : [1, 3]}
three = {'connections' : [0, 1, 2, 4, 5, 6]}
four = {'connections' : [3, 5]}
five = {'connections' : [3, 4, 6]}
six = {'connections' : [3, 5]}

letterPositions.append(zero)
letterPositions.append(one)
letterPositions.append(two)
letterPositions.append(three)
letterPositions.append(four)
letterPositions.append(five)
letterPositions.append(six)

#orders = ['0', '1', '2', '3', '4']
orders = []

for x in range (len(letterPositions)):
    orders.append(str(x))

print(orders)

length = len(orders)

def GetNextPosition(order) :
    global length
    global orders
    global letterPositions

    latestNum = int(order[len(order)-1])

    for i in range(len(letterPositions[latestNum]['connections'])):
        newOrder = order + str(letterPositions[latestNum]['connections'][i])
        orders.append(newOrder)
        length += 1
        return newOrder

    stringPos = str(newOrder)

def AppendNewOrder(order) :
    global length
    global orders
    global letterPositions

    latestNum = int(order[len(order)-1])

    # If all numbers are already in the order
    if all(str(x) in order for x in letterPositions[latestNum]['connections']):
        orders.append(order)
        return

    for i in range(len(letterPositions[latestNum]['connections'])):

        if str(letterPositions[latestNum]['connections'][i]) in order:
            continue

        newOrder = order + str(letterPositions[latestNum]['connections'][i])

        if(len(newOrder) < 7):
            AppendNewOrder(newOrder)
        else:
            orders.append(newOrder)

for x in range(len(letterPositions)):
    AppendNewOrder(str(x))

mainOrder = []

for order in orders:

    b = []
    for x in range(len(order)):
        b.append(int(order[x]))
        
    mainOrder.append(b)

for each in mainOrder:
    print(str(each) + ",")
#print(mainOrder)
#print(orders)
