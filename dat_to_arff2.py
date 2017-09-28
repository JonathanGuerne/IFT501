"""Preporcess .dat into .arff format."""

transaction_id = {}
item_id = set([])

with open('BMS-POS.dat', 'r', encoding='utf-8') as fin:
    for line in fin:
        line_array = line.split("\t")
        if len(line_array) > 1:
            if line_array[0] not in transaction_id.keys():
                transaction_id[line_array[0]] = []
            transaction_id[line_array[0]].append(line_array[1][:-1])
            item_id.add(line_array[1][:-1])
    item_id = sorted(item_id, key=int)




with open('BMS-POS.dat', 'r', encoding='utf-8') as fin, open('BMS-POS.arff', 'w', encoding='utf-8') as fou:
    fou.write("@relation BMS-POS\n\n")
    for i in range(item_id.__len__()):
        fou.write("@attribute " + item_id[i] + " {0,1}\n")

    fou.write("\n@data\n\n")

    for i in range(len(transaction_id)):
        j = 0
        for item in item_id:
            if item in transaction_id[str(i+1)]:
                 fou.write(item)
                 fou.write("" if j == len(item_id) else ',')
            j = j + 1

        fou.write("\n")
        if i % 10000 == 0:
            print(str((i / len(transaction_id)) * 100)[:5] + "%")
    fou.write("\n")
