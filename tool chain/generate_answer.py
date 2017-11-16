import json
ne_sen_file=open("e://workplace/inter/table+pos_ne_sen_0.file",mode='r',encoding='utf-8')#集成处理后的实体文件
raw_file=open("e://workplace/test/DATA_TEST.txt",mode='r',encoding='utf-8')#DATA_TEST.txt
final_result=open("e://workplace/inter/FIN.json",mode='w',encoding='utf-8')

ne_sen_list=str(ne_sen_file.readline()).split()
raw_line=str(raw_file.readline())
while raw_line:
    entities=""
    newsid=json.loads(raw_line)['newsId']
    for item in ne_sen_list:
        entity,emotion=item.split('=')
        entity_all="{\"eventLevel\":\"负向\",\"keywords\":\"\",\"name\":\"hhh\",\"digest\":\"摘要\"},"#单个实体模板
        entity_all=entity_all.replace('hhh',entity)
        entity_all=entity_all.replace('负向',emotion)
        entities=entities+entity_all
    sentence="{\"newsId\":\""+str(newsid)+"\",\"entities\":["+entities[:len(entities)-1]+"]}\n"
    final_result.write(sentence)

    ne_sen_list=str(ne_sen_file.readline()).split()
    raw_line=str(raw_file.readline())
    
ne_sen_file.close()
raw_file.close()
final_result.close()
