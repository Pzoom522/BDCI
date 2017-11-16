def incompleteHead(entity):#很有可能不完整
    wide_suffixes=['公司','有限公司','有限责任公司','局','店','超市','厂','中心','分公司','市场','酒店','加油站','食品店','食品厂']
    for key_word in wide_suffixes:
        if ((entity.find(key_word)!=-1) and ((len(entity)-len(key_word))<3)):
            return True
    return False

def getEmotion():
    return '负向'#默认为负向。该函数后期可以进一步实现以提升情感识别准确度

def isGov(entity):
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

UPPER_BOUND=19
LOWER_BOUND=4#合法的实体长度的上下界
input_data=open("e://workplace/inter/orig_ner.file",mode="r",encoding="utf-8")
output_data=open("e://workplace/inter/pos_ne_sen.file",mode="w",encoding="utf-8")
line=input_data.readline()
while line:
    orig_ne_list=str(line).split()
    orig_ne_list_copy=str(line).split()
    for item in orig_ne_list:
        for item_copy in orig_ne_list_copy:
            if ((item_copy.find(item)!=-1) and (item_copy!=item)):
                item='北航'
        if (incompleteHead(item)):
            item='北航'
        if ((len(item)>UPPER_BOUND) or (len(item)<LOWER_BOUND)):
            item='北航'#北航表示之后会被删除

        emotion=getEmotion()
        if (isGov(item)):
            emotion='中向'

        if (item!='北航'):
            output_data.write(item+'='+emotion+' ')
    output_data.write('\n')
    line=input_data.readline()
output_data.close()
