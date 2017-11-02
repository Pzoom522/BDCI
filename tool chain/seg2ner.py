import json
seg_file=open("e://SEG_DATA_T.json",mode="r",encoding="utf-16")
ner_file=open("e://ner.file",mode="a",encoding="utf-8")
seg_data=json.loads(seg_file.read())
corpus=seg_data['sentences']
isNe=False#当前词是否为机构实体
for sentence in corpus:#一句话一句话遍历
    for word in sentence['tokens']:#每句话里一个词一个词遍历
        if (word['word']=='北航'):#句子开头
            ner_file.write('\n')
        else:
            if (isNe==False and word['ner']!='ORGANIZATION'):#从普通到普通
                None
            elif (isNe==False and word['ner']=='ORGANIZATION'):#从普通到实体
                ner_file.write(word['word'])
                isNe=True
            elif (isNe and word['ner']=='ORGANIZATION'):#从实体到实体
                ner_file.write(word['word'])
            else:#从实体到普通
                ner_file.write(' ')
                isNe=False
ner_file.close()
seg_file.close()
