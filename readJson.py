import pandas as pd
import json
import csv
file_path = 'output1.csv'
file_conll = 'output1.conll'
import pandas as pd
import re

# 读取conll2003文件
def read_conll(file_path):
    df = pd.read_csv(file_path, sep=' ', header=None)
    return df

def read_file(file_name):
    csv_file = open(file_name, encoding="utf-8")
    csv_reader_lines = csv.reader(csv_file)
    raw_date = []
    for i, line in enumerate(csv_reader_lines):
        raw_date.append(line)
    return raw_date

def read_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    print(data)
    text = data['data']['text']
    print(text)
    annotations = data['annotations']

    print('Text:', text)
    print('Labels:')
    for ann in annotations:
        result = ann['result']
        for r in result:
            if 'labels' in r['value']:
                print(r['value']['labels'][0])


if __name__ == '__main__':
    data = read_file(file_path)
    features = []
    label = []
    for e in data[1]:
        match_text = re.search(r'"text": "(.*)"', e.strip())
        match_label = re.search(r'"labels": \["(\w+)"\]',e.strip())
        if match_text:
            features.append(match_text.group(1).strip())
        if match_label:
            label.append(match_label.group(1).strip())
    res = [[]]
    for e1,e2 in zip(features,label):
        cur = []
        cur.append(e1)
        cur.append(e2)
        res.append(cur)
        print(e1+":"+e2)
