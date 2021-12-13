listData = []
listItem = []

def mostAppearItem(value):
    for item in value:
        state = {'nama': item, 'jumlah': 1}
        if(len(listData) == 0):
            listData.append(state)
            listItem.append(item)
        else:
            if(item in listItem):
                for data in listData:
                    if(data['nama'] == item):
                        data['jumlah'] += 1
            else:
                listItem.append(item)
                listData.append(state)

    hasil = sorted(listData, key=lambda d: d['jumlah']) 
    
    for item in hasil:
        print(f'{item["nama"]}: {item["jumlah"]}')


mostAppearItem(['js', 'js', 'go', 'php', 'go', 'python'])