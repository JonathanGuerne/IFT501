"""Preprocess a list of products into .arff format."""

product_name = []

with open('description_produit.data', 'r', encoding='utf-8') as fin:
    for line in fin :
        line_array = line.split("\t")
        #print(line_array[1][:-1])
        if(len(line_array)>1):
            product_name.append(line_array[1][:-1])


with open('produits.data', 'r', encoding='utf-8') as fin, open('produits.arff', 'w', encoding='utf-8') as fou:
    fou.write("@relation produits\n\n")
    for i in range(100):
        fou.write("@attribute " + '"' + product_name[i] + '"' + " {0,1}\n")

    fou.write("\n")
    fou.write("@data\n")
    fou.write("\n")

    for line in fin:
        data = line.split("\t")
        for i in range(100):
            if (str(i+1)) in data:
                fou.write("1")
            else:
                fou.write("0")
            fou.write(("" if i == 100 else ','))
        fou.write("\n")
    fou.write("\n")
