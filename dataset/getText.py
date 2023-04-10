
import pandas as pd

# 读取csv文件
df = pd.read_csv('promise_nfr_review.csv',sep=';')

# 选择指定列
selected_column = df['RequirementText']
Text_0_254 = selected_column[0:224]  #hanlu
Text_255_424 = selected_column[225:424]  #一起标的，用来达成共识
Text_325_424 = selected_column[325:424]  #hanlu和zhouqixiang分别标的，用来计算一致性
Text_425_624 = selected_column[425:624]  #zhouqixiang

Text_0_254.to_csv('Text_0_224.txt',index=False, header=False)
Text_255_424.to_csv('Text_225_424.txt',index=False, header=False)
Text_325_424.to_csv('Text_325_424.txt',index=False, header=False)
Text_425_624.to_csv('Text_425_624.txt',index=False, header=False)
#
# # 将指定列写入新的txt文件
# selected_column.to_csv('RequirementText.txt', index=False, header=False)
