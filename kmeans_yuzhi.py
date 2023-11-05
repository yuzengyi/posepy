import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
def read_json_file(i, folder="output_jsons"):
    # 使用字符串格式化来生成文件名
    filename = f"{folder}/video_{i:012d}_keypoints.json"
    # 读取文件内容并返回
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
# 输入帧数和第几个人
i = int(input("请输入帧数："))
j = int(input("请输入第几个人：（从0开始）"))
# 例如，如果你想读取第1个文件（i=0）:
data = read_json_file(i)
df_combined = pd.DataFrame(columns=["x坐标", "y坐标", "confidence"])
# 设置全局字体
plt.rcParams["font.family"] = "Times New Roman"


if j < len(data["people"]):  # 仅处理第j个人的数据
    person = data["people"][j]
    pose_keypoints_2d = person['pose_keypoints_2d']
else:
    pose_keypoints_2d = [-1] * 75


# 从JSON数据中提取关键点数据
keypoints = pose_keypoints_2d[:75]  # 只保留前75个值

# 将关键点数据重塑为25行3列的矩阵
keypoints_matrix = np.reshape(keypoints, (25, 3))
print(keypoints_matrix)
# 提取置信度
confidences = [kp[2] for kp in keypoints_matrix if kp[2] != 0]

# 使数据为二维
confidences_reshape = np.array(confidences).reshape(-1, 1)

# 使用KMeans进行聚类，假设我们想要分为两类
kmeans = KMeans(n_clusters=2, random_state=0).fit(confidences_reshape)

# 找到阈值（两个聚类中心的平均值）
threshold = np.mean(kmeans.cluster_centers_)
print("阈值：")
print(threshold)
# 绘制直方图
plt.hist(confidences_reshape, bins=30, alpha=0.7, label='Confidence values', color='gray')
centers = kmeans.cluster_centers_
# 绘制聚类中心
for center in centers:
    plt.axvline(x=center[0], color='red', linestyle='--', label=f'Cluster Center {center[0]:.3f}')

# 显示图形
# plt.title("KMeans Clustering of Confidence Values")
plt.xlabel("Confidence Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()