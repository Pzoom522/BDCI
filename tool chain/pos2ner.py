import json
seg_file=open("e://workplace/test/input.temp.json",mode="r",encoding="utf-8")
com_file=open("e://workplace/test/com.file",mode="w",encoding="utf-8")
seg_data=json.loads(seg_file.read())
corpus=seg_data['sentences']
for sentence in corpus:#一句话一句话遍历
    tokens=sentence['tokens']
    for i in range(0,len(tokens)):#每句话里一个词一个词遍历
        if (tokens[i]['word']=='北航'):#句子开头
            com_file.write('\n')
            continue
        elif ((tokens[i]['word']=='公司') or (tokens[i]['word']=='超市') or (tokens[i]['word']=='分公司') or (tokens[i]['word']=='店') or  (tokens[i]['word'].endswith('厂'))):#核心功能
            company_name=tokens[i]['word']
            j=i-1#j是用来向前匹配的索引
            while ((tokens[j]['pos']=='NN') or (tokens[j]['pos']=='JJ') or (tokens[j]['pos']=='NR')) :#可行模式
                company_name=tokens[j]['word']+company_name
                j=j-1#继续向前匹配
                if (((tokens[j]['pos']!='NN') and (tokens[j]['pos']!='JJ') and (tokens[j]['pos']!='NR')) or (tokens[j]['word']=='公司')):#结束
                    com_file.write(company_name+' ')
                    break
        else:
            continue

com_file.close()
seg_file.close()
