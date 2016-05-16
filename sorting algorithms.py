##############################################
with open('rosalind_mer(3).txt', 'r') as myfile:
    myfile = myfile.read().split("\n")

myarray = [map(int, myfile[1].split(" ")),
           map(int, myfile[3].split(" "))]


def merge(c1, c2):
    merged = []
    counter1 = 0
    counter2 = 0
    
    while counter1 < len(c1) and counter2 < len(c2):
        if c1[counter1] <= c2[counter2]:
            merged.append(c1[counter1])
            counter1 += 1
        else:
            merged.append(c2[counter2])
            counter2 += 1
    if len(c1) != 0:
        merged.extend(c1[counter1:])
    else:
        merged.extend(c2[counter2:])
    
    return merged




foo = merge(myarray[0], myarray[1])

)

