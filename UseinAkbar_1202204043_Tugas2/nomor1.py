listData = []
listAngka = []
hasil = []

def filterJumlahAngka(value):
    for item in value:
        state = {'angka': item, 'jumlah': 1}
        if(len(listData) == 0):
            listData.append(state)
            listAngka.append(item)
        else:
            if(item in listAngka):
                for data in listData:
                    if(data['angka'] == item):
                        data['jumlah'] += 1
            else:
                listAngka.append(item)
                listData.append(state)

    for item in listData:
        if(item['jumlah'] == 1):
            hasil.append(int(item['angka']))
    
    return hasil
            
    
print(filterJumlahAngka('76523752'))