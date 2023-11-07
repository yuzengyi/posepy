import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
# print(data)
# 使用os.path.abspath()将相对路径转换为绝对路径
# json_folder = os.path.abspath('./output_jsons')

# 获取文件夹中的所有JSON文件
# json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]
# 初始化一个空的DataFrame
df_combined = pd.DataFrame(columns=["x坐标", "y坐标", "confidence"])



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

# 从数据中提取x和y坐标
x_coords = [point[0] for point in keypoints_matrix]
y_coords = [point[1] for point in keypoints_matrix]
# 设置默认字体为"Linux Biolinum O"
plt.rcParams['font.family'] = 'Times new roman'
# # 绘制散点图
# plt.figure(figsize=(10, 10))
# plt.scatter(x_coords, y_coords)
#
# # 设置坐标轴的方向和标签
# # plt.gca().invert_yaxis()  # 使得(0,0)在左上角
# # 将x轴移动到图的上方
# plt.xaxis.tick_top()
# plt.xaxis.set_label_position('top')
#
# # 设置坐标轴的方向和标签
# plt.invert_yaxis()  # 使得(0,0)在左上角
# plt.xlabel('x')
# plt.ylabel('y')
# # plt.title('Scatter plot of x and y coordinates')
#
# # 显示图形
# plt.show()
# 绘制散点图
fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(x_coords, y_coords)

# 将x轴移动到图的上方
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')

# 设置坐标轴的方向和标签
ax.invert_yaxis()  # 使得(0,0)在左上角
ax.set_xlabel('x')
ax.set_ylabel('y')
# ax.set_title('Scatter plot of x and y coordinates')

# 显示图形
plt.show()
# 将数据添加到整合后的DataFrame中
df_person = pd.DataFrame(keypoints_matrix, columns=["x坐标", "y坐标", "confidence"])
df_combined = pd.concat([df_combined, df_person], ignore_index=True)

# 设置行名为特征0到24的对应索引
df_combined.index = range(25)

# 将DataFrame保存为xlsx文件
output_file = 'output2.xlsx'
df_combined.to_excel(output_file, index=True)
print(f"DataFrame已保存为{output_file}文件。")
# openpose(i,j): output:矩阵

# 遍历所有JSON文件并整合数据
# for frame_num, json_file in enumerate(json_files):
#     if frame_num + 1 == i:  # 仅处理第i帧的数据
#         with open(os.path.join(json_folder, json_file), 'r') as f:
#             data = json.load(f)
#
#         if j < len(data["people"]):  # 仅处理第j个人的数据
#             person = data["people"][j]
#             pose_keypoints_2d = person['pose_keypoints_2d']
#
#             # 从JSON数据中提取关键点数据
#             keypoints = pose_keypoints_2d[:75]  # 只保留前75个值
#
#             # 将关键点数据重塑为25行3列的矩阵
#             keypoints_matrix = np.reshape(keypoints, (25, 3))
#
#             # 将数据添加到整合后的DataFrame中
#             df_person = pd.DataFrame(keypoints_matrix, columns=["x坐标", "y坐标", "confidence"])
#             df_combined = pd.concat([df_combined, df_person], ignore_index=True)
#
# # 设置行名为特征0到24的对应索引
# df_combined.index = range(25)
#
# # 将DataFrame保存为xlsx文件
# output_file = 'output.xlsx'
# df_combined.to_excel(output_file, index=True)

# print(f"DataFrame已保存为{output_file}文件。")