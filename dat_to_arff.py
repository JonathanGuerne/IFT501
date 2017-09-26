transaction_list = {}

max_id_produit = 0

with open('BMS-POS.dat', 'r', encoding='utf-8') as fin:
    for line in fin:
        line_array = line.split("\t")
        if len(line_array) > 1:
            if line_array[0] not in transaction_list.keys():
                transaction_list[line_array[0]] = []
            transaction_list[line_array[0]].append(line_array[1])
            if (int(line_array[1]) > max_id_produit):
                max_id_produit = int(line_array[1])


# with open('BMS-POS.arff', 'w', encoding='utf-8') as fou:
#     fou.write("@relation produits\n\n")
#     for key in transaction_list.keys():
#         fou.write("@attribute " + str(key) + " {NO,YES}\n")
#
#     fou.write("\n")
#     fou.write("@data\n")
#     fou.write("\n")
#
#     for key in transaction_list.keys():
#         for i in range(max_id_produit + 1):
#             if str(i) in transaction_list[key]:
#                 fou.write("YES")
#             else:
#                 fou.write("NO")
#         fou.write(("" if i == max_id_produit else ","))
#     fou.write("\n")
# fou.write("\n")
