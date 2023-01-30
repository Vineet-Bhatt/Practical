def count():
    fh = open("poem.txt" , 'r')
    #Initializing variables
    countMe = 0
    countMy = 0
    rawData = fh.read()
    data = rawData.split()
    # Iterating over data
    for word in data:
        # Incrementing counters
        if word.lower() == 'me':
            countMe += 1
        if word.lower() == 'my':
            countMy += 1
    # P
    print("Number of me : ", countMe)   # If there are me printing them
    print("Number of my : ", countMy)
        

count()
