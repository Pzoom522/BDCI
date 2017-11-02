import json
ner_file=open("ner.file",mode='r',encoding='utf-8')#最终版本命名实体文件
sen_file=open("sen.file",mode='r',encoding='utf-8')#最终版本情感极性文件
raw_file=open("raw.file",mode='r',encoding='utf-8')#DATA_TEST.txt
final_result=open("FIN.txt",mode='w',encoding='utf-8')
ner_list=str(ner_file.readline()).split()
sen_list=str(sen_file.readline()).split()
raw_line=str(raw_file.readline())

while raw_line:
        newsid=json.loads(raw_line)['newsId']
        entities=[]
        
        for i in range(0,len(sen_list)):
            entity_all={"eventLevel":"负向","keywords":"","name":"","digest":"摘要"}#单个实体模板
            entity_all["eventLevel"]=sen_list[i]
            entity_all["name"]=ner_list[i]
            entities.append(entity_all)
        sentence="{\"newsId\":"+str(newsid)+"\",\"entities\":"+str(entities)+"}\n"
        final_result.write(sentence)

        ner_list=str(ner_file.readline()).split()
        sen_list=str(sen_file.readline()).split()
        raw_line=str(raw_file.readline())
ner_file.close()
sen_file.close()
raw_file.close()
final_result.close()
