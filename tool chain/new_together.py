import json
com_file=open("e://workplace/test/com.file",mode='r',encoding='utf-8')#最终版本企业实体文件
gov_file=open("e://workplace/test/gov.file",mode='r',encoding='utf-8')#最终版本官方实体文件
raw_file=open("e://workplace/test/DATA_TEST.txt",mode='r',encoding='utf-8')#DATA_TEST.txt
final_result=open("e://workplace/test/FIN.json",mode='w',encoding='utf-8')
com_list=str(com_file.readline()).split()
gov_list=str(gov_file.readline()).split()
raw_line=str(raw_file.readline())

while raw_line:
    entities=""
    newsid=json.loads(raw_line)['newsId']

    for i in range(0,len(com_list)):
        entity_all="{\"eventLevel\":\"负向\",\"keywords\":\"\",\"name\":\"hhh\",\"digest\":\"摘要\"},"#单个实体模板
        #entity_all["eventLevel"]= 默认负向
        entity_all=entity_all.replace("hhh",com_list[i])
        entities=entities+entity_all
    for i in range(0,len(gov_list)):
        entity_all="{\"eventLevel\":\"中向\",\"keywords\":\"\",\"name\":\"hhh\",\"digest\":\"摘要\"},"#单个实体模板
        #entity_all["eventLevel"]= 默认中向
        entity_all=entity_all.replace("hhh",gov_list[i])
        entities=entities+entity_all
    sentence="{\"newsId\":\""+str(newsid)+"\",\"entities\":["+entities[:len(entities)-1]+"]}\n"
    #sentence=sentence.replace(" ","")
    final_result.write(sentence)

    com_list=str(com_file.readline()).split()
    gov_list=str(gov_file.readline()).split()
    raw_line=str(raw_file.readline())
com_file.close()
gov_file.close()
raw_file.close()
final_result.close()
