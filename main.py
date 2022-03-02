
f = open('D:\\base_NIRS\\multimodal_only_samples\\multimodal_train.tsv', encoding='utf-8')
info = f.read()
tmp = info.split('\n')
tmp1 = []
for i in range(len(tmp)):
    tmp1.append(tmp[i].split('\t')[10:11])
# убираем повторы
value = []
for j in tmp1:
    if j not in value and j != []:
        value.append(j)
with open('D:\\base_NIRS\\multimodal_only_samples\\image_info.tsv', 'w') as fp:
    # пишем построчно
    for i in range(len(value)):
        fp.write(value[i][0] + '\n')