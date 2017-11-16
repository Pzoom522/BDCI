import json
import os
import pattern_dealer

def includeHead(head_index,content):
    i=head_index-1
    capture=''
    while ((i>=0) and content[i]!='。'):
        capture=content[i]+capture
        i=i-1
    return capture

def getEmotion(content):
    for word in wordbank['neg']:
        if (content.find(word)!=-1):
            content=content.replace(word,'NEG')
            return '负向'
    for word in wordbank['pos']:
        if (content.find(word)!=-1):
            content=content.replace(word,'POS')
            return '正向'
    for word in wordbank['mid']:
        if (content.find(word)!=-1):
            content=content.replace(word,'MID')
            return '中向'
    return 'X'#没有明确表示

def isgov(entity):
    gov_prefixes = ['国家','中国','世界','联合国']
    gov_suffixes = ['研究院','研究所','委员会','局','法院','办公室','办公厅','大学','中学','学院','银行','卫视','频道','政府','党委','党校','工会','学会','总队','大队','支队','检察院','检测院','检验所','中心','领域']
    gov_entities = ['国务院','腾讯','阿里巴巴']
    for i in gov_prefixes:
        if entity.startswith(i):
            return True
    for i in gov_suffixes:
        if entity.endswith(i):
            return True
    for i in gov_entities:
        if i in entity:
            return True
    return False

input_data=open("e://workplace/test/DATA_TEST.txt",mode="r",encoding="utf-8")
all_ne    =open("e:/output.file"                  ,mode="r",encoding="utf-8")
table_nes =open("e://workplace/inter/table_ne.temp",mode="w",encoding="utf-8")
wb        =open("e://workplace/wordbank.json"     ,mode='r',encoding='utf-8')
wordbank=json.loads(wb.read())#情感词词典
line = json.loads(input_data.readline())
ne_corpus=str(all_ne.readline()).split()
while line:
        body=str(line['body'])+' '
        news_id=str(line['newsId'])
        pre_table=pattern_dealer.target_news(body)
        tables=pre_table.tableFinder()
        head_list=pre_table.table_head
        all_rows=pre_table.all_rows

        for table_counter in range (0,len(tables)):
            thesis_statement=includeHead(head_list[table_counter],body)#获得标题/前言
            global_emotion=getEmotion(thesis_statement)#表头获得的情感信息
            possible_ne_cols={}#具有唯一性的含实体列号集合
            #每张表分别对待

            for row in tables[table_counter]:
                for i in range(0,len(row)):
                    if row[i] in ne_corpus:
                        possible_ne_cols[str(i)]=0

            for row_counter in range(0,len(tables[table_counter])):
                local_emotion=getEmotion(all_rows[table_counter][row_counter])#获得对应行的情感
                if (local_emotion=='X'):#没有分项情感
                    if (global_emotion=='X'):#没有主题情感
                        local_emotion='负向'#蒙负向
                    else:
                        local_emotion=global_emotion#跟随表头
                else:
                    None#分行处理

                for col in possible_ne_cols:
                    try:
                        item=tables[table_counter][row_counter][int(col)]
                        if ((item.find('/')==-1) and (item[len(item)-1]!='号') and (item[len(item)-1]!='路')):
                            if (isgov(item)):
                                local_emotion='中向'
                            table_nes.write(item+'='+local_emotion+' ')
                    except Exception:
                        pass
        table_nes.write('\n')
        line = json.loads(input_data.readline())
        ne_corpus=str(all_ne.readline()).split()
input_data.close()
all_ne.close()
table_nes.close()
wb.close()
