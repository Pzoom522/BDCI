import json
import os
input_data=open("e://DATA_T.txt",mode="r",encoding="utf-8")
temp_input=open("e://input.temp",mode="a",encoding="utf-8")
line = json.loads(input_data.readline())
while line:
       temp_input.write("北航。"+str(line['body'])+"\n")
       line = json.loads(input_data.readline())
input_data.close()
temp_input.close()


