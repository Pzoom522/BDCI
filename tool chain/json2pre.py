import json
import os
input_data=open("e://workplace/test/DATA_TEST.txt",mode="r",encoding="utf-8")
temp_input=open("e://workplace/test/input.temp",mode="w",encoding="utf-8")
line = json.loads(input_data.readline())
while line:
       body=str(line['body']).replace('\n',' ')
       temp_input.write("北航。"+body+"\n")
       line = json.loads(input_data.readline())
input_data.close()
temp_input.close()


