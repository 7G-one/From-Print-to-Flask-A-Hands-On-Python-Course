# -*- coding: utf-8 -*-
# =============================================
# 第 09 课：文件操作
# =============================================
# 上节课我们学了函数。
# 这节课我们要学习文件操作——让程序能读写文件。
#
# 用 with 语句安全地操作文件，掌握 CSV 和 JSON 两种常见数据格式。

import os
import json

# =============================================
# 第一节：文件的打开和关闭
# =============================================

"""
【文件操作的基本步骤】
1. 打开文件
2. 读取或写入
3. 关闭文件

【打开文件的方式】
推荐使用 with 语句（自动关闭文件）
"""


# ========== 创建测试目录 ==========
test_dir = "test_files"
os.makedirs(test_dir, exist_ok=True)


# ========== 使用 with 语句 ==========

print("=== with 语句 ===")

# with 会自动关闭文件，不用担心忘记
# 语法：with open("文件路径", "模式") as 变量:

# 写入文件
with open(f"{test_dir}/hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("这是第二行\n")
    f.write("这是第三行\n")

print("文件写入成功！")


# =============================================
# 第二节：文件打开模式
# =============================================

"""
【文件打开模式】

| 模式 | 说明 |
|------|------|
| 'r'  | 只读（默认），文件必须存在 |
| 'w'  | 写入，文件不存在则创建，存在则覆盖 |
| 'a'  | 追加，文件不存在则创建 |
| 'x'  | 创建新文件，文件已存在则报错 |
| 'b'  | 二进制模式 |
| 't'  | 文本模式（默认） |
| '+'  | 读写模式 |
"""


print("\n=== 文件打开模式 ===")

# ========== 只读模式 'r' ==========
# 文件必须存在，否则报错
try:
    with open(f"{test_dir}/hello.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"读取内容：{content}")
except FileNotFoundError:
    print("文件不存在！")


# ========== 写入模式 'w' ==========
# 文件不存在则创建，存在则覆盖
with open(f"{test_dir}/write.txt", "w", encoding="utf-8") as f:
    f.write("这是写入的内容\n")
print("写入模式完成")


# ========== 追加模式 'a' ==========
# 文件不存在则创建，存在则在末尾追加
with open(f"{test_dir}/write.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的内容\n")
print("追加模式完成")


# =============================================
# 第三节：读取文件
# =============================================

"""
【读取文件的方法】

| 方法 | 说明 |
|------|------|
| read() | 读取全部内容 |
| readline() | 读取一行 |
| readlines() | 读取所有行（返回列表）|
| 逐行遍历 | 用 for 循环 |
"""


print("\n=== 读取文件 ===")

# ========== read() 读取全部内容 ==========
with open(f"{test_dir}/hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"read() 全部内容：\n{content}")


# ========== readline() 读取一行 ==========
with open(f"{test_dir}/hello.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"readline() 第一行：{line1.strip()}")
    print(f"readline() 第二行：{line2.strip()}")


# ========== readlines() 读取所有行 ==========
with open(f"{test_dir}/hello.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"readlines() 行列表：{lines}")


# ========== 逐行遍历（推荐！）==========
print("\n逐行遍历：")
with open(f"{test_dir}/hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"  {line.strip()}")


# =============================================
# 第四节：写入文件
# =============================================

"""
【写入文件的方法】

| 方法 | 说明 |
|------|------|
| write() | 写入字符串 |
| writelines() | 写入列表 |
"""


print("\n=== 写入文件 ===")

# ========== write() 写入字符串 ==========
with open(f"{test_dir}/output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.write("第三行\n")
print("write() 写入完成")


# ========== writelines() 写入列表 ==========
lines = ["苹果\n", "香蕉\n", "橘子\n"]
with open(f"{test_dir}/fruits.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
print("writelines() 写入完成")


# =============================================
# 第五节：CSV 文件操作
# =============================================

"""
【什么是 CSV？】
CSV = Comma Separated Values（逗号分隔值）
就是用逗号分隔的数据文件

示例：
姓名,年龄,城市
小明,18,北京
小红,19,上海
"""

import csv

print("\n=== CSV 文件操作 ===")

# ========== 写入 CSV ==========
csv_file = f"{test_dir}/students.csv"
students = [
    ["姓名", "年龄", "城市"],
    ["小明", 18, "北京"],
    ["小红", 19, "上海"],
    ["小刚", 20, "广州"]
]

with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(students)
print("CSV 写入完成")


# ========== 读取 CSV ==========
print("\n读取 CSV：")
with open(csv_file, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")


# =============================================
# 第六节：JSON 文件操作
# =============================================

"""
【什么是 JSON？】
JSON = JavaScript Object Notation
一种轻量级的数据交换格式
常用于配置文件和数据传输

示例：
{
    "name": "小明",
    "age": 18,
    "hobbies": ["编程", "阅读"]
}
"""

print("\n=== JSON 文件操作 ===")

# ========== 写入 JSON ==========
data = {
    "name": "小明",
    "age": 18,
    "hobbies": ["编程", "阅读", "运动"],
    "address": {
        "city": "北京",
        "district": "海淀区"
    }
}

json_file = f"{test_dir}/data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("JSON 写入完成")


# ========== 读取 JSON ==========
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print(f"\n读取 JSON：{loaded_data}")
print(f"姓名：{loaded_data['name']}")
print(f"爱好：{loaded_data['hobbies']}")


# =============================================
# 第七节：路径操作
# =============================================

"""
【路径操作】
用 os.path 模块处理文件路径
"""

print("\n=== 路径操作 ===")

# 获取当前目录
print(f"当前目录：{os.getcwd()}")

# 路径拼接
path = os.path.join("folder", "subfolder", "file.txt")
print(f"路径拼接：{path}")

# 获取文件名和扩展名
file_path = "test_files/data.json"
print(f"文件名：{os.path.basename(file_path)}")
print(f"目录名：{os.path.dirname(file_path)}")
print(f"扩展名：{os.path.splitext(file_path)[1]}")

# 判断路径
print(f"\n路径存在：{os.path.exists(file_path)}")
print(f"是文件：{os.path.isfile(file_path)}")
print(f"是目录：{os.path.isdir('test_files')}")


# =============================================
# 第八节：实战案例
# =============================================

print("\n=== 实战案例 ===")


# ========== 案例1：成绩管理 ==========
print("\n--- 案例1：成绩管理 ---")

def add_score(name, score):
    """
    添加成绩到文件

    【参数】
    - name: 字符串，学生姓名
    - score: 整数，成绩

    【调用示例】
    add_score("小明", 85)
    """

    with open(f"{test_dir}/scores.txt", "a", encoding="utf-8") as f:
        f.write(f"{name},{score}\n")

def get_scores():
    """
    读取所有成绩

    【返回值】
    字典，{姓名: 成绩}

    【调用示例】
    scores = get_scores()
    """

    scores = {}
    try:
        with open(f"{test_dir}/scores.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, score = line.strip().split(",")
                scores[name] = int(score)
    except FileNotFoundError:
        pass
    return scores

# 添加成绩
add_score("小明", 85)
add_score("小红", 92)
add_score("小刚", 78)

# 读取成绩
scores = get_scores()
print(f"成绩：{scores}")
print(f"平均分：{sum(scores.values()) / len(scores):.1f}")


# ========== 案例2：配置文件管理 ==========
print("\n--- 案例2：配置文件管理 ---")

class ConfigManager:
    """
    配置管理类

    【作用】
    管理 JSON 配置文件

    【方法】
    - load(): 加载配置
    - save(): 保存配置
    - get(key): 获取配置项
    - set(key, value): 设置配置项
    """

    def __init__(self, filename):
        """初始化"""
        self.filename = filename
        self.config = {}

    def load(self):
        """加载配置"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}

    def save(self):
        """保存配置"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def get(self, key, default=None):
        """获取配置项"""
        return self.config.get(key, default)

    def set(self, key, value):
        """设置配置项"""
        self.config[key] = value

# 使用
config = ConfigManager(f"{test_dir}/config.json")
config.set("app_name", "MyApp")
config.set("version", "1.0")
config.save()
print(f"配置已保存")

config2 = ConfigManager(f"{test_dir}/config.json")
config2.load()
print(f"应用名：{config2.get('app_name')}")
print(f"版本：{config2.get('version')}")


# ========== 案例3：日志系统 ==========
print("\n--- 案例3：日志系统 ---")

from datetime import datetime

def log(message, level="INFO"):
    """
    写入日志

    【参数】
    - message: 字符串，日志内容
    - level: 字符串，日志级别

    【调用示例】
    log("程序启动")
    log("发生错误", "ERROR")
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{level}] {message}"
    print(log_line)
    with open(f"{test_dir}/app.log", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

log("程序启动")
log("用户登录", "INFO")
log("数据库错误", "ERROR")


# =============================================
# 清理测试文件
# =============================================

import shutil
shutil.rmtree(test_dir, ignore_errors=True)
print("\n测试文件已清理")


# =============================================
# 【练习题】
# =============================================

# 【练习1：读写文本文件】
# 编写一个函数，演示文件的写入和读取操作
# 1. 创建一个文本文件，写入 3 行内容
# 2. 读取并打印文件内容
# 3. 最后删除临时文件
# 提示：
#   1. 用 with open(文件名, "w", encoding="utf-8") 写入
#   2. 用 with open(文件名, "r", encoding="utf-8") 读取
#   3. 用 os.remove(文件名) 删除文件

# 【练习2：词频统计】
# 编写一个函数，统计一段文本中每个单词出现的次数
# 例如：输入 "hello python hello world python hello"
#       返回 {"hello": 3, "python": 2, "world": 1}
# 提示：
#   1. 定义函数 word_count(text)，返回字典 {单词: 次数}
#   2. 用 text.lower() 统一转小写，避免大小写不同算两个词
#   3. 用 text.split() 按空格分割成单词列表
#   4. 用 for 循环遍历，用字典的 get(key, 0) 方法计数

# 【练习3：文件复制】
# 编写一个函数，将一个文件的内容复制到另一个文件
# 提示：
#   1. 定义函数 copy_file(src, dst)，参数是源文件路径和目标文件路径
#   2. 先用 with open 打开源文件读取内容
#   3. 再用 with open 打开目标文件写入内容
#   4. 测试时先创建一个源文件，复制后再清理临时文件

# =============================================
# 练习参考答案
# =============================================
print("\n" + "="*50)
print("练习参考答案")
print("="*50 + "\n")

# 练习1 参考
print("--- 练习1 参考 ---")

def read_write_demo():
    """读写文本文件演示"""

    # 写入
    with open("demo.txt", "w", encoding="utf-8") as f:
        f.write("Hello\n")
        f.write("Python\n")
        f.write("World\n")

    # 读取
    with open("demo.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"内容：{content}")

    # 清理
    os.remove("demo.txt")

read_write_demo()


# 练习2：词频统计
print("\n--- 练习2 参考 ---")

def word_count(text):
    """
    统计词频

    【参数】
    - text: 字符串

    【返回值】
    字典，{单词: 次数}
    """

    words = text.lower().split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

text = "hello python hello world python hello"
result = word_count(text)
print(f"词频：{result}")


# 练习3：文件复制
print("\n--- 练习3 参考 ---")

def copy_file(src, dst):
    """
    复制文件

    【参数】
    - src: 源文件路径
    - dst: 目标文件路径
    """

    with open(src, "r", encoding="utf-8") as f_src:
        content = f_src.read()

    with open(dst, "w", encoding="utf-8") as f_dst:
        f_dst.write(content)

    print(f"复制完成：{src} → {dst}")

# 测试
with open("source.txt", "w") as f:
    f.write("测试内容")
copy_file("source.txt", "dest.txt")

# 清理
os.remove("source.txt")
os.remove("dest.txt")


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- with open() as f 是操作文件的标准写法，自动关闭文件不怕忘记
- CSV 用 csv 模块读写表格数据，JSON 用 json 模块读写结构化数据
- os.path 和 pathlib 处理文件路径，跨平台兼容比手拼字符串安全

常见陷阱：
- 用 "r" 模式打开不存在的文件会 FileNotFoundError，先用 os.path.exists() 检查
- 写文件用 "w" 模式会覆盖原有内容，想追加要用 "a" 模式
- JSON 只能序列化基本类型，自定义对象需要自定义 encoder 或转成字典

下节课预告：
- 下节课学面向对象编程，用"类"和"对象"组织更复杂的代码
"""
