pre_file=open("e://workplace/train/input.temp",mode="r",encoding="utf-8")
ch_file=open("e://workplace/train/ch_input.temp",mode="w",encoding="utf-8")
content=str(pre_file.read())
for char in content:
    if  ((char>=u'\u4e00' and char<=u'\u9fa5') #or (char.isdigit())#汉语或数字
         or (char=='；' or char=='。' or char=='！' or char=='\n')):#保留符号
         ch_file.write(char)
    else:
         ch_file.write(' ')#其余的一律空格，切割句子
pre_file.close()
ch_file.close()
