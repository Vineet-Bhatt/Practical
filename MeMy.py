def count():
    fh = open("poem.txt" , 'r')
    countMe = 0
    countMy = 0
    rawData = fh.read()
    data = rawData.split()
    for word in data:
        if word.lower() == 'me':
            countMe += 1
        if word.lower() == 'my':
            countMy += 1
    if countMe < 1:
        print("There are no 'me' in the file!")
    else:
        print("Number of me : ", countMe)
    if countMy < 1:
        print("There are no 'my' in the file!")
    else:
        print("Number of my : ", countMy)
        

count()
