import json
import numpy as np
from sklearn.metrics import cohen_kappa_score

def read_annotations(file):
    """
    读取需要文档的标注结果

    :param file: 标注结果的jsonl文件路径
    :type file: str
    :return: 两个标注员的标注结果
    :rtype: tuple[list[list[int]], list[list[int]]]
    """
    labels = []  # A标注员的标注结果
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            label = [0] * len(data['text'])
            for span in data['label']:
                for i in range(span[0], span[1]):
                    label[i] = 1
            labels.append(label)
    return labels


def check_sublist_lengths(list1, list2):
    """
    Checks if sublists in two lists have the same length.
    Args:
        list1 (list): The first list to be checked.
        list2 (list): The second list to be checked.

    Returns:
        bool: True if all corresponding sublists have the same length, False otherwise.
    """
    if len(list1) != len(list2):
        print("The two lists have different lengths.")
        return False
    for i in range(len(list1)):
        if len(list1[i]) != len(list2[i]):
            print("The two lists have different lengths.")
            return False
    print("The two lists have the same lengths.")
    return True


def compute_cohen_kappa(y1, y2):
    """
    Computes the average Cohen's kappa coefficient across multiple samples.
    Args:
        y1 (list): A list of lists, containing the labels assigned by the first annotator.
        y2 (list): A list of lists, containing the labels assigned by the second annotator.
    Returns:
        float: The average Cohen's kappa coefficient across all samples.
    """
    kappas = []
    for i in range(len(y1)):
        sample1 = y1[i]
        sample2 = y2[i]
        kappa = cohen_kappa_score(sample1, sample2)
        kappas.append(kappa)
    return np.mean(kappas)


# 测试代码
A_files = './annotation/hanlu_325_424.jsonl'
B_files = './annotation/zhouqixiang_325_424.jsonl'
A_labels = read_annotations(A_files)
B_labels = read_annotations(B_files)

# print(A_labels)
# print(B_labels)

# check_sublist_lengths(A_labels, B_labels)

#计算Kappa系数

kappa_score = compute_cohen_kappa(A_labels, B_labels)

print("Kappa系数为:", kappa_score)