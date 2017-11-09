com_file=open("e://workplace/test/com.file",mode="r",encoding ="utf-8")
ner_file=open("e://workplace/try/ner.file",mode="r",encoding ="utf-8")
new_file=open("e://workplace/test/new.file",mode="w",encoding ="utf-8")
com_line=str(com_file.readline())
ner_line=str(ner_file.readline())
while com_line:
    new_line=ner_line[:len(ner_line)-1]+' '+com_line
    new_file.write(new_line)
    com_line=str(com_file.readline())
    ner_line=str(ner_file.readline())
com_file.close()
ner_file.close()
