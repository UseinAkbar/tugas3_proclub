hasil = []

def penjumlahanAngka(value, target):
    for item1 in value:
        for item2 in value:
            if(item1 + item2 == target):
                hasil.append(value.index(item1))
                hasil.append(value.index(item2))
                return

penjumlahanAngka([2,5,9,11], 11)
print(hasil)