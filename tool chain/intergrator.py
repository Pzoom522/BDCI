#文件来源：去重之后的【表格实体+情感】文件(file_A)；去重并长度过滤后的【POS实体+情感】文件(file_B)
#       1）如果存在表格，则收录file_A全文
#       2）如果不存在表格，则收录file_B全文

TARGET_NUM=21100#最优实体总数
file_A=open("e://workplace/inter/table_ne_sen.file",mode='r',encoding='utf-8')
file_B=open("e://workplace/inter/pos_ne_sen.file",mode='r',encoding='utf-8')
file_out=open("e://workplace/inter/table+pos_ne_sen_0.file",mode='w',encoding='utf-8')
line_A=str(file_A.readline())
line_B=str(file_B.readline())
line_out=''
while line_B:#共有2000条实体
    #print('【'+str(i))
    if (len(line_A)<2):#此条新闻没有提取表格
        #print(line_B)
        file_out.write(line_B)
    else:
        #print(line_A)
        file_out.write(line_A)
    line_A=str(file_A.readline())
    line_B=str(file_B.readline())
file_A.close()
file_B.close()
