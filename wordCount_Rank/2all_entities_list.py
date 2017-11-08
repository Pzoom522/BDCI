import json
com_file=open("e://workplace/train/seg_pos_list.file",mode="w",encoding="utf-8")
seg_file=open("e://workplace/train/all_entities.csv.json",mode="r",encoding="utf-8")
seg_data=json.loads(seg_file.read())
corpus=seg_data['sentences']
for sentence in corpus:#一句话一句话遍历
    output="[\""+str(sentence['index'])+"\",\""
    for word in sentence['tokens']:
        if (word['word']!='。'):
            output=output+word['word']+","+word['pos']+' '
    output=output+"\"]\n"
    com_file.write(output)
com_file.close()
seg_file.close()
