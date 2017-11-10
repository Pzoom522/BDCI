#用于还原新闻中的表格
class target_news:
    def __init__(self,raw_news):
        self.raw=raw_news
        #原字符串
        self.rows=[""]
        #字符串列表，记录表的每一行字串
        self.all_rows=[]
        #由新闻中的全部字符串列表构成的列表

    def tableFinder(self):#主过程
        is_in_table=False
        pattern_map=""
        for scanner in range(0,len(self.raw)):
            if (self.raw[scanner]=='1' and (not is_in_table) and self.newTable(scanner)[0]!=0):#获得第一行，开始处理表
                while (newRow(self)):
                    self.rows.append(self.rows)#只要能够加入一行，就算是成功找到一张表
            else:
                None
        return tableMaker(self)#将新闻全部录入表

    def tableMaker(self):
        all_table=[]#三维列表。由新闻中的全部表构成的列表
        for rows in self.all_rows:
            table=[]#二维列表。第一维是当前进入模式的行，第二维是按间隔符切割过之后的块。表示当前填充的表
            for row in self.rows:
                row_elements=[]#表的每一行中各项组成的列表
                for char in pattern_map:
                    break_point=row.find(char)
                    row_elements.append(row[:break_point])
                    row=row[break_point:]
                table.append(row_elements)
            all_table.append(table)
        return all_table

    def newRow(self):#加入新行
        offset=0
        for row in self.rows:
            offset=offset+len(row)#从表中的一号序号开始，到当前需要考察的字符串起点的距离
        target_string=self.raw[scanner+offset:]#只考察未扫描部分
        index_pattern=0#当前已经检查匹配到的pattern_map角标
        index_next=0
        for char in pattern_map:
            break_point=target_string.find(char)
            if (break_point==-1):
                return False#匹配失败
            else:
                index_next=index_next+break_point
                target_string=target_string[break_point:]
                #当pattern_map里面的字符完全匹配后，说明完成了对一行的扫描
            self.rows.append(self.raw[scanner+offset:scanner+offset+index_next])
        return True

    def newTable(self,index_first):
        self.rows=[""]
        if (self.raw[index_first-1]=="（" and self.raw[index_first+1]=="（" and self.raw[index_first+2]==" "):
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
        elif (self.raw[index_first+1]==" " ):
            index_mode=5
            index_second=self.raw[index_first:].find("2 ")
        else:
            index_mode=0

        #寻找第一行的模式
        if (index_mode==-1):#没有2
            index_mode=0
        else:#抽取出模式对象
            self.rows[0]=self.raw[index_first:][:index_second]
            for inner_scanner in range(0,index_second):
                if (self.raw[scanner:][inner_scanner]==' ' or
                    self.raw[scanner:][inner_scanner]=='\u3000' or
                    self.raw[scanner:][inner_scanner]=='\u2003' or
                    self.raw[scanner:][inner_scanner]=='\u2002'):#空格
                    pattern_map=pattern_map+self.raw[scanner:][inner_scanner]
                else:
                    None
        return index_mode
