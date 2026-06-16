# -*- coding: utf-8 -*-
# =============================================
# 第 12 课：模块与包
# =============================================
# 上节课我们学了异常处理。
# 这节课我们要学习模块与包——把代码组织成可复用的"工具箱"。
#
# 用 import 导入标准库和第三方包，用 pip 管理依赖，用虚拟环境隔离项目。
"""

# =============================================
# 第一节：导入模块的方式
# =============================================

【导入模块的方式】

| 方式 | 语法 | 说明 |
|------|------|------|
| 导入整个模块 | import 模块名 | 使用时需要模块名前缀 |
| 导入特定内容 | from 模块 import 名称 | 直接使用名称 |
| 导入并重命名 | import 模块 as 别名 | 用别名代替模块名 |
| 导入并重命名 | from 模块 import 名称 as 别名 | 用别名代替名称 |
"""


print("=== 导入模块的方式 ===")

# ========== 方式1：导入整个模块 ==========
import math

# 使用时需要模块名前缀
print(f"圆周率: {math.pi}")
print(f"平方根: {math.sqrt(16)}")


# ========== 方式2：导入特定内容 ==========
from math import pi, sqrt

# 直接使用名称
print(f"圆周率: {pi}")
print(f"平方根: {sqrt(25)}")


# ========== 方式3：导入并重命名 ==========
from math import factorial as fact

# 用别名代替名称
print(f"5! = {fact(5)}")


# ========== 方式4：导入模块并重命名 ==========
import datetime as dt

# 用别名代替模块名
now = dt.datetime.now()
print(f"当前时间: {now}")


# =============================================
# 第二节：常用标准库模块
# =============================================

"""
【Python 内置了很多有用的模块】

| 模块 | 用途 |
|------|------|
| math | 数学运算 |
| random | 随机数 |
| datetime | 日期时间 |
| os | 操作系统 |
| json | JSON 处理 |
| collections | 高级数据结构 |
| itertools | 迭代器工具 |
| functools | 函数工具 |
"""


print("\n=== 常用标准库模块 ===")

# ========== math 数学模块 ==========
import math

print("math 模块：")
print(f"  圆周率：{math.pi}")
print(f"  自然常数：{math.e}")
print(f"  平方根：{math.sqrt(16)}")
print(f"  幂运算：{math.pow(2, 3)}")
print(f"  向上取整：{math.ceil(3.2)}")
print(f"  向下取整：{math.floor(3.8)}")


# ========== random 随机数模块 ==========
import random

print("\nrandom 模块：")
print(f"  随机整数(1-10)：{random.randint(1, 10)}")
print(f"  随机浮点数：{random.random():.4f}")
print(f"  随机选择：{random.choice(['苹果', '香蕉', '橘子'])}")
print(f"  随机打乱：{random.sample([1,2,3,4,5], 3)}")


# ========== datetime 日期时间模块 ==========
from datetime import datetime, timedelta

print("\ndatetime 模块：")
now = datetime.now()
print(f"  当前时间：{now}")
print(f"  格式化：{now.strftime('%Y-%m-%d %H:%M:%S')}")
tomorrow = now + timedelta(days=1)
print(f"  明天：{tomorrow.strftime('%Y-%m-%d')}")


# ========== os 操作系统模块 ==========
import os

print("\nos 模块：")
print(f"  当前目录：{os.getcwd()}")
print(f"  目录列表：{os.listdir('.')[:5]}...")


# ========== json 模块 ==========
import json

print("\njson 模块：")
data = {"name": "小明", "age": 18}
json_str = json.dumps(data, ensure_ascii=False)
print(f"  转为JSON：{json_str}")
parsed = json.loads(json_str)
print(f"  解析JSON：{parsed}")


# =============================================
# 第三节：创建自己的模块
# =============================================

"""
【怎么创建模块？】
就是创建一个 .py 文件

【示例】
假设我们创建了 mymath.py 文件：

# mymath.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

【使用自己的模块】
import mymath
print(mymath.add(3, 5))

或者
from mymath import add, PI
print(add(3, 5))
"""


print("\n=== 创建自己的模块 ===")

# 模拟创建模块
class MyMath:
    """数学工具模块"""

    @staticmethod
    def add(a, b):
        """加法"""
        return a + b

    @staticmethod
    def subtract(a, b):
        """减法"""
        return a - b

    @staticmethod
    def multiply(a, b):
        """乘法"""
        return a * b

    @staticmethod
    def divide(a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

    PI = 3.14159

# 使用模块
print(f"add(3, 5) = {MyMath.add(3, 5)}")
print(f"subtract(10, 3) = {MyMath.subtract(10, 3)}")
print(f"multiply(4, 5) = {MyMath.multiply(4, 5)}")
print(f"divide(10, 3) = {MyMath.divide(10, 3):.2f}")
print(f"PI = {MyMath.PI}")


# =============================================
# 第四节：pip 安装第三方包
# =============================================

"""
【什么是 pip？】
pip 是 Python 的包管理器
用来安装、卸载、更新第三方包

【常用命令】

| 命令 | 说明 |
|------|------|
| pip install 包名 | 安装包 |
| pip install 包名==版本 | 安装指定版本 |
| pip install --upgrade 包名 | 升级包 |
| pip uninstall 包名 | 卸载包 |
| pip list | 查看已安装包 |
| pip show 包名 | 查看包信息 |
| pip freeze > requirements.txt | 导出依赖 |
| pip install -r requirements.txt | 从文件安装依赖 |

【使用国内镜像（更快）】
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名
"""


print("\n=== pip 安装第三方包 ===")

# 常用第三方包
packages = {
    "数据处理": ["pandas", "numpy", "matplotlib"],
    "Web开发": ["flask", "django", "requests"],
    "自动化": ["selenium", "beautifulsoup4", "scrapy"],
    "AI/ML": ["tensorflow", "pytorch", "scikit-learn"],
}

print("常用第三方包：")
for category, pkgs in packages.items():
    print(f"\n  {category}:")
    for pkg in pkgs:
        print(f"    - {pkg}")


# =============================================
# 第五节：虚拟环境
# =============================================

"""
【什么是虚拟环境？】
虚拟环境是一个独立的 Python 环境
每个项目可以有自己的依赖，互不影响

【为什么要用虚拟环境？】
1. 隔离项目依赖
2. 避免版本冲突
3. 便于部署

【创建虚拟环境】
python -m venv myenv

【激活虚拟环境】
# Windows
myenv\Scripts\activate

# Linux/Mac
source myenv/bin/activate

【退出虚拟环境】
deactivate
"""


print("\n=== 虚拟环境 ===")

print("创建虚拟环境：python -m venv myenv")
print("激活虚拟环境：myenv\\Scripts\\activate")
print("退出虚拟环境：deactivate")


# =============================================
# 第六节：if __name__ == "__main__"
# =============================================

"""
【这个是什么？】
每个 Python 文件都有 __name__ 变量
- 直接运行时：__name__ == "__main__"
- 被导入时：__name__ == "模块名"

【为什么要这样写？】
让模块既能被导入，又能直接运行
"""


print("\n=== if __name__ == '__main__' ===")

def main():
    """主函数"""
    print("这是主程序")

# 只在直接运行时执行
if __name__ == "__main__":
    main()
    print("模块被直接运行")
else:
    print("模块被导入")


# =============================================
# 【练习题】
# =============================================
# 先看题目，自己写代码，再看参考答案！

# 【练习1：使用 math 模块】
# 题目描述：导入 math 模块，计算一个半径为 5 的圆的面积和周长，
#          并用 f-string 格式化输出，保留 2 位小数。
# 提示：
#   - 面积公式：π × r²，周长公式：2 × π × r
#   - math.pi 获取圆周率，** 运算符做幂运算
#   - f"{value:.2f}" 可以保留 2 位小数

# 【练习2：使用 random 模块】
# 题目描述：用 random 模块生成 10 个 1~100 之间的随机整数，
#          存入列表，然后找出最大值、最小值和平均值。
# 提示：
#   - random.randint(1, 100) 生成随机整数
#   - 列表推导式 [表达式 for _ in range(10)] 可以快速生成列表
#   - 内置函数 max()、min()、sum() + len() 求最大/最小/平均值

# 【练习3：使用 datetime 模块】
# 题目描述：用 datetime 模块创建两个日期对象（2024-01-01 和 2024-12-31），
#          计算它们之间相差多少天，并用 strftime 格式化输出日期。
# 提示：
#   - from datetime import datetime 导入
#   - datetime(年, 月, 日) 创建日期对象
#   - 两个日期相减得到 timedelta 对象，.days 属性获取天数
#   - .strftime('%Y-%m-%d') 格式化日期

# 【练习4：使用 json 模块】
# 题目描述：创建一个嵌套字典表示应用配置（包含 app_name、version、
#          debug 和 database 信息），用 json.dumps 转为 JSON 字符串
#          （带缩进），再用 json.loads 解析回来，最后取出嵌套字段。
# 提示：
#   - json.dumps(字典, ensure_ascii=False, indent=2) 转为格式化 JSON
#   - json.loads(字符串) 解析 JSON 为 Python 对象
#   - 用 字典['key']['nested_key'] 访问嵌套字段

# 【练习5：创建自己的模块】
# 题目描述：创建一个 StringUtils 类（模拟模块），包含三个静态方法：
#          reverse(反转字符串)、is_palindrome(判断回文)、count_words(统计单词数)，
#          然后分别调用测试。
# 提示：
#   - 用 class + @staticmethod 定义静态方法
#   - s[::-1] 反转字符串
#   - s.split() 按空格拆分单词，len() 计算数量

# =============================================
# 练习参考答案
# =============================================

print("\n" + "="*50)
print("练习参考答案")
print("="*50 + "\n")

# 练习1：使用 math 模块
print("--- 练习1 参考 ---")

import math

# 计算圆的面积和周长
radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"半径：{radius}")
print(f"面积：{area:.2f}")
print(f"周长：{circumference:.2f}")


# 练习2：使用 random 模块
print("\n--- 练习2 参考 ---")

import random

# 生成随机数列表
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"随机数列表：{numbers}")
print(f"最大值：{max(numbers)}")
print(f"最小值：{min(numbers)}")
print(f"平均值：{sum(numbers) / len(numbers):.1f}")


# 练习3：使用 datetime 模块
print("\n--- 练习3 参考 ---")

from datetime import datetime

# 计算天数差
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
delta = date2 - date1
print(f"从 {date1.strftime('%Y-%m-%d')} 到 {date2.strftime('%Y-%m-%d')}")
print(f"相差 {delta.days} 天")


# 练习4：使用 json 模块
print("\n--- 练习4 参考 ---")

import json

# 保存配置
config = {
    "app_name": "MyApp",
    "version": "1.0",
    "debug": True,
    "database": {
        "host": "localhost",
        "port": 5432
    }
}

# 转为 JSON 字符串
json_str = json.dumps(config, ensure_ascii=False, indent=2)
print(f"JSON 字符串：\n{json_str}")

# 解析 JSON 字符串
parsed = json.loads(json_str)
print(f"\n解析结果：{parsed}")
print(f"应用名：{parsed['app_name']}")
print(f"数据库端口：{parsed['database']['port']}")


# 练习5：创建自己的模块
print("\n--- 练习5 参考 ---")

class StringUtils:
    """字符串工具模块"""

    @staticmethod
    def reverse(s):
        """反转字符串"""
        return s[::-1]

    @staticmethod
    def is_palindrome(s):
        """判断是否是回文"""
        return s == s[::-1]

    @staticmethod
    def count_words(s):
        """统计单词数"""
        return len(s.split())

# 使用
print(f"reverse('Hello') = {StringUtils.reverse('Hello')}")
print(f"is_palindrome('abcba') = {StringUtils.is_palindrome('abcba')}")
print(f"count_words('Hello Python World') = {StringUtils.count_words('Hello Python World')}")


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- import 导入模块，from ... import ... 导入特定成员，as 给模块起别名
- pip install 安装第三方包，requirements.txt 记录项目依赖，venv 创建虚拟环境
- if __name__ == "__main__" 让模块既可以被导入，也可以直接运行

常见陷阱：
- 循环导入：A 模块导入 B，B 又导入 A，Python 会报 ImportError
- 忘记创建虚拟环境，不同项目的依赖版本冲突，导致各种奇怪错误
- 把所有 import 写在文件开头不如按需导入清晰，但标准惯例还是放顶部

下节课预告：
- 下节课学装饰器详解，Python 最优雅的"魔法"特性之一
"""
