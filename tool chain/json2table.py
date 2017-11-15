import json
import os
import pattern_dealer
input_data=open("e://workplace/test/DATA_TEST.txt",mode="r",encoding="utf-8")
all_ne    =open("e:/output.file"                  ,mode="r",encoding="utf-8")
table_nes =open("e://workplace/test/table_ne.temp",mode="w",encoding="utf-8")
line = json.loads(input_data.readline())
ne_corpus=str(all_ne.readline()).split()
while line:
        body=str(line['body'])
        news_id=str(line['newsId'])
        pre_table=pattern_dealer.target_news(body)
        tables=pre_table.tableFinder()
        for table in tables:
            possible_ne_cols={}#每张表分别对待
            for row in table:
                for i in range(0,len(row)):
                    if row[i] in ne_corpus:
                        possible_ne_cols[str(i)]=''

            for row in table:
                for col in possible_ne_cols:
                    try:
                        if row[int(col)]!='/':
                            table_nes.write(row[int(col)]+' ')
                    except Exception:
                        print('777')
                        pass
        table_nes.write('\n')
        line = json.loads(input_data.readline())
        ne_corpus=str(all_ne.readline()).split()
input_data.close()
all_ne.close()
table_nes.close()
