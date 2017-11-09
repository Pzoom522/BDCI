def isgov(entity):
    gov_prefixes = ['国家','中国','世界','联合国']
    gov_suffixes = ['研究院','研究所','委员会','局','法院','办公室','办公厅','大学','中学','学院','银行','卫视','频道','政府','党委','党校','工会','学会','总队','大队','支队','检察院','检测院','检验所','举报中心','金融中心','控制中心','领域']
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

ner_file=open("e://workplace/try/ner.file",mode="r",encoding="utf-8")
gov_file=open("e://workplace/test/gov.file",mode="w",encoding="utf-8")
line=ner_file.readline()
while line:
    words=str(line).split()
    for word in words:
        if isgov(word):
            gov_file.write(word+' ')
    gov_file.write('\n')
    line=ner_file.readline()

ner_file.close()
gov_file.close()
