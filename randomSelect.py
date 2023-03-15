import pandas as pd
import random

# 读取csv文件
df = pd.read_csv('func_concerns.csv',sep=';')

# 随机选择50行
sampled_df = df.sample(n=50)
print(sampled_df['RequirementText'].head())
text = sampled_df['RequirementText']
# 保存为新的csv文件
sampled_df.to_csv('textLabel.csv',index=False)
text.to_csv('text.csv', index=False)
