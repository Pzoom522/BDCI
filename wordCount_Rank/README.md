# 预处理-一种寻找训练集中的实体规律的方法
**目的:通过将训练集中DATA_T_RESULT.txt中的实体单独分词并找出热词，为寻找实体的工作提供参考**

## 流程：
***DATA_T_RESULT.xlsx***=>导出为.csv并使每个实体用句号间隔=>***all_entities.csv***=>用CoreNLP分词=>***all_entities.csv.json***
=>2all_entities_list.py=>***seg_pos_list.file***=>MapReduce.py & wordcount.py=>***seg_pos.csv***
