import json


def read_json_file(i, folder="output_jsons"):
    # 使用字符串格式化来生成文件名
    filename = f"{folder}/video_{i:012d}_keypoints.json"

    # 读取文件内容并返回
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


# 例如，如果你想读取第1个文件（i=0）:
data = read_json_file(0)
print(data)

# 如果你想读取第2个文件（i=1）:
data = read_json_file(1)
print(data)
