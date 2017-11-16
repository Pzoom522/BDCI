#用于还原新闻中的表格
#主要缺点：
#1)只能找到两行以上的表（算法限制）
#2)如果表格最后一行最后一个空白字符缺失，会少找最后一行

class target_news:
    def __init__(self,raw_news):
        self.raw=raw_news
        #原字符串
        self.rows=[""]
        #字符串列表，记录表的每一行字串
        self.all_rows=[]
        #由新闻中的全部字符串列表构成的列表
        self.pattern_map=""
        #当前正在寻找的表格的间隔符模式
        self.line_num=1
        #当前正在扫描表格的第几行
        self.table_head=[]
        #每张表格的起始位置

    def tableFinder(self):#主过程
        '''
        【6fa80abb586b485575ee3735c8dd6f4396bd19e9:第二个表只有一个1】
        is_in_table=False
        for scanner in range(0,len(self.raw)):
            if (self.raw[scanner]=='1' and (not is_in_table) and self.newTable(scanner)!=0):#获得第一行，开始处理表
                is_in_table=True
                self.line_num=2
                while (self.newRow(scanner,self.newTable(scanner))):
                    self.line_num=self.line_num+1
                if (self.line_num>3):
                    self.table_head.append(scanner)
                    print(self.raw[scanner:scanner+30]+self.pattern_map)
                    self.all_rows.append(self.rows)#至少三行，算是成功找到一张表
            else:
                None
            self.pattern_map=""
            is_in_table=False
            self.rows=[""]
        return(self.tableMaker())#将此篇新闻的全部表格录入三维列表
        '''
        try:
            is_in_table=False
            for scanner in range(0,len(self.raw)):
                if (self.raw[scanner]=='1' and (not is_in_table) and self.newTable(scanner)!=0):#获得第一行，开始处理表
                    is_in_table=True
                    self.line_num=2
                    while (self.newRow(scanner,self.newTable(scanner))):
                        self.line_num=self.line_num+1
                    if (self.line_num>3):
                        self.table_head.append(scanner)
                        self.all_rows.append(self.rows)#至少三行，算是成功找到一张表
                else:
                    None
                self.pattern_map=""
                is_in_table=False
                self.rows=[""]
            return(self.tableMaker())#将此篇新闻的全部表格录入三维列表
        except Exception:
            return([[[]]])

    def tableMaker(self):
        all_table=[]#最外维。由新闻中的全部表构成的列表
        for rows in self.all_rows:
            table=[]#中间维。一张独立的表（行数至少为3）
            for row in rows:
                row_elements=row.split()#最里维。表的每一行中按列分割后的各项组成的列表
                table.append(row_elements)
            all_table.append(table)
        return all_table

    def newRow(self,starter,mode):#加入新行
        offset=0
        for row in self.rows:
            offset=offset+len(row)#从表中的一号序号开始，到当前需要考察的字符串起点的距离
        target_string=self.raw[starter+offset:]#只考察未扫描部分

        #判断当前扫描的字串开头的序号是否符合格式一致性
        num_string=''
        if   (mode==1):
            num_string='（'+str(self.line_num)+'）'
        elif (mode==2):
            num_string='('+str(self.line_num)+')'
        elif (mode==3):
            num_string='.'+str(self.line_num)+' '
        elif (mode==4):
            num_string='、'+str(self.line_num)+' '
        elif (mode==5):
            num_string=str(self.line_num)+' '
        else:
            print('FATAL ERROR at newRow()!\n')
            return False

        if (target_string.find(num_string)!=0):#字串开头不对
            return False
        else:#开始进行空白字符模式匹配
            index_pattern=0#当前已经检查匹配到的pattern_map角标
            index_next=0#待扫描字串中下一个需要匹配的空白符
            for char in self.pattern_map:
                break_point=target_string.find(char)
                if (break_point==-1):
                    return False#匹配失败
                else:
                    index_next=index_next+break_point+1
                    target_string=target_string[break_point+1:]
                    #逐一推进空白字符
                    #当pattern_map里面的字符完全匹配后，说明完成了对一行的扫描
            self.rows.append(self.raw[starter+offset:starter+offset+index_next])
        return True

    def newTable(self,index_first):
        self.pattern_map=""
        index_second=-1#第二行预期起始位置
        if (self.raw[index_first-1]=="（" and self.raw[index_first+1]=="）" and self.raw[index_first+2]==" "):
            index_mode=1
            index_second=self.raw[index_first:].find("（2） ")
        elif (self.raw[index_first-1]=="(" and self.raw[index_first+1]==")" and self.raw[index_first+2]==" "):
            index_mode=2
            index_second=self.raw[index_first:].find("(2) ")
        elif (self.raw[index_first+1]=="." and self.raw[index_first+2]==" "):
            index_mode=3
            index_second=self.raw[index_first:].find("2. ")
        elif (self.raw[index_first+1]=="、" and self.raw[index_first+2]==" "):
            index_mode=4
            index_second=self.raw[index_first:].find("2、 ")
        elif (self.raw[index_first+1]==" " and not self.raw[index_first-1].isdigit()):
            index_mode=5
            index_second=self.raw[index_first:].find("2 ")
            if (self.raw[index_second-1].isdigit()):
                index_mode=0
        else:
            index_mode=0
        #寻找第一行的模式

        if (index_second==-1):#没有第二行
            index_mode=0

        else:#抽取出模式对象
            self.rows[0]=self.raw[index_first:][:index_second]
            for inner_scanner in range(0,len(self.rows[0])):
                if (self.raw[index_first:][inner_scanner]==' ' or
                    self.raw[index_first:][inner_scanner]=='\u3000' or
                    self.raw[index_first:][inner_scanner]=='\u2003' or
                    self.raw[index_first:][inner_scanner]=='\u2002'):#空格
                    self.pattern_map=self.pattern_map+self.raw[index_first:][inner_scanner]
                else:
                    None
        return index_mode
