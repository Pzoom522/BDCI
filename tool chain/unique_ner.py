ner_file=open("e://workplace/inter/table_ne.temp",mode="r",encoding="utf-8")
unique_ner_file=open("e://workplace/inter/table_ne_sen.file",mode="w",encoding="utf-8")
line=str(ner_file.readline())
while line:
    unique_list=[]#用于验证独一性
    word_list=line.split()
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
            unique_ner_file.write(word+' ')
    unique_ner_file.write('\n')
    line=str(ner_file.readline())
ner_file.close()
unique_ner_file.close()
