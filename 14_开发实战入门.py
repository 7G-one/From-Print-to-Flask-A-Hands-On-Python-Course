# -*- coding: utf-8 -*-
# =============================================
# 第 14 课：开发实战入门
# =============================================
# 前面的课程你已经学会了 Python 的各种语法。
# 这节课教你如何把学到的知识"组合"起来，做出真正有用的程序。
#
# 从需求分析到设计、编码、测试，走一遍完整的开发流程。

# =============================================
# 第一节：开发的基本思路（非常重要！）
# =============================================

"""
【开发的基本思路】

做任何项目，都要遵循这个步骤：

1. 明确需求（我要做什么？）
   - 问自己：这个程序要解决什么问题？
   - 问自己：用户会怎么使用这个程序？
   - 问自己：需要哪些功能？

2. 设计思路（怎么做？）
   - 把大问题拆成小问题
   - 想清楚用什么数据结构
   - 想清楚函数怎么分工

3. 编写代码（动手写）
   - 一个功能一个功能地写
   - 写一点，测试一点
   - 不要一次写太多

4. 测试调试（检查对不对）
   - 正常情况能用吗？
   - 异常情况会崩溃吗？
   - 用户输入错误怎么办？

5. 优化完善（做得更好）
   - 代码能不能更简洁？
   - 用户体验能不能更好？
   - 有没有遗漏的功能？

【比喻】
就像盖房子：
1. 先想好要盖什么样的房子（需求）
2. 画出设计图（设计）
3. 开始施工（编码）
4. 检查质量（测试）
5. 装修完善（优化）
"""

# =============================================
# 第二节：第一个项目 - 简易计算器
# =============================================

print("="*50)
print("项目1：简易计算器")
print("="*50)

"""
【需求分析】
我们要做一个计算器，功能：
1. 能做加法
2. 能做减法
3. 能做乘法
4. 能做除法
5. 能退出程序

【设计思路】
1. 显示菜单（让用户选择做什么运算）
2. 用户输入选择（1-5）
3. 如果选择1-4：
   a. 让用户输入两个数字
   b. 根据选择做计算
   c. 显示结果
4. 如果选择5：
   a. 退出程序
5. 循环回到步骤1

【调用思路】
main() 主函数
    → 显示菜单
    → 获取用户选择
    → 调用 calculate() 做计算
    → 显示结果
    → 循环
"""

def calculator():
    """
    简易计算器函数

    【函数说明】
    这个函数实现了一个简单的计算器：
    - 用户可以选择加减乘除
    - 输入两个数字
    - 程序计算并显示结果
    - 用户可以随时退出

    【参数】无

    【返回值】无

    【调用示例】
    calculator()  # 启动计算器
    """

    # 无限循环，直到用户选择退出
    while True:

        # ========== 显示菜单 ==========
        # \n 表示换行，让界面更清晰
        print("\n" + "="*30)
        print("简易计算器")
        print("="*30)
        print("1. 加法")      # 选项1
        print("2. 减法")      # 选项2
        print("3. 乘法")      # 选项3
        print("4. 除法")      # 选项4
        print("5. 退出")      # 选项5
        print("="*30)

        # ========== 获取用户选择 ==========
        # input() 会等待用户输入
        # 用户输入的内容会存到 choice 变量里
        choice = input("请选择(1-5): ")

        # ========== 处理退出 ==========
        # 如果用户输入 "5"，就退出程序
        if choice == "5":
            print("感谢使用，再见！")
            break  # break 会跳出循环

        # ========== 验证选择是否有效 ==========
        # 如果用户输入的不是 1、2、3、4、5，提示错误
        if choice not in ["1", "2", "3", "4", "5"]:
            print("无效选择，请重试！")
            continue  # continue 会跳过本次循环，回到循环开头

        # ========== 获取用户输入的数字 ==========
        # 用 try-except 防止用户输入非数字
        try:
            # float() 把字符串转换成小数
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))
        except ValueError:
            # 如果用户输入的不是数字，会进入这里
            print("输入的不是有效数字！")
            continue  # 跳过本次循环

        # ========== 根据选择做计算 ==========
        # 用 if-elif 判断用户选择了什么运算
        if choice == "1":
            # 加法
            result = num1 + num2
            op = "+"
        elif choice == "2":
            # 减法
            result = num1 - num2
            op = "-"
        elif choice == "3":
            # 乘法
            result = num1 * num2
            op = "×"
        elif choice == "4":
            # 除法
            # 注意：除数不能为0！
            if num2 == 0:
                print("错误：除数不能为零！")
                continue
            result = num1 / num2
            op = "÷"

        # ========== 显示结果 ==========
        # 用 f-string 格式化输出
        print(f"\n计算结果: {num1} {op} {num2} = {result}")


# ========== 调用计算器 ==========
# 取消下面这行的注释，就可以运行计算器
# calculator()


# =============================================
# 第三节：第二个项目 - 文件批量重命名工具
# =============================================

print("\n" + "="*50)
print("项目2：文件批量重命名工具")
print("="*50)

"""
【需求分析】
整理文件夹时，经常需要批量修改文件名。这个工具的功能：
1. 查看目录下所有文件
2. 按规则批量重命名（加前缀、加后缀、替换文字）
3. 预览重命名效果（不直接改，先看看）
4. 确认后执行重命名

【设计思路】
1. 用 os.listdir() 获取文件列表
2. 用 os.path.splitext() 分离文件名和扩展名
3. 创建一个类来管理重命名规则
4. 提供 preview() 预览和 execute() 执行

【调用思路】
创建 FileRenamer 对象
    → 调用 load_files() 加载文件
    → 调用 add_prefix() / replace_text() 设置规则
    → 调用 preview() 预览效果
    → 调用 execute() 执行重命名
"""


class FileRenamer:
    """
    文件批量重命名工具

    【类的作用】
    把文件列表和重命名逻辑封装在一起，
    支持预览后再执行，避免误操作。

    【属性】
    - directory: 字符串，目标目录路径
    - files: 列表，目录下的文件名
    - rename_rules: 列表，重命名规则

    【方法】
    - load_files(): 加载目录下的文件
    - add_prefix(prefix): 给所有文件名加前缀
    - add_suffix(suffix): 给所有文件名加后缀（在扩展名之前）
    - replace_text(old, new): 替换文件名中的文字
    - preview(): 预览重命名效果
    - execute(): 执行重命名
    """

    def __init__(self, directory="."):
        """
        初始化文件重命名器

        【参数】
        - directory: 字符串，目标目录路径，默认为当前目录
        """
        self.directory = directory
        self.files = []         # 原始文件名列表
        self.new_names = []     # 重命名后的文件名列表

    def load_files(self):
        """
        加载目录下的所有文件

        【逻辑】
        1. 用 os.listdir() 获取目录下所有条目
        2. 只保留文件（排除目录）
        3. 初始化 new_names 为 files 的副本
        """
        import os

        all_items = os.listdir(self.directory)
        # 只保留文件，排除子目录
        self.files = [f for f in all_items
                      if os.path.isfile(os.path.join(self.directory, f))]
        # 初始时新文件名和原文件名相同
        self.new_names = self.files.copy()
        print(f"已加载 {len(self.files)} 个文件")

    def add_prefix(self, prefix):
        """
        给所有文件名加前缀

        【参数】
        - prefix: 字符串，要添加的前缀

        【逻辑】
        photo.jpg → vacation_photo.jpg
        """
        import os
        self.new_names = []
        for f in self.files:
            name, ext = os.path.splitext(f)
            self.new_names.append(f"{prefix}{name}{ext}")
        print(f"已添加前缀: '{prefix}'")

    def add_suffix(self, suffix):
        """
        给所有文件名加后缀（在扩展名之前）

        【参数】
        - suffix: 字符串，要添加的后缀

        【逻辑】
        photo.jpg → photo_2024.jpg
        """
        import os
        self.new_names = []
        for f in self.files:
            name, ext = os.path.splitext(f)
            self.new_names.append(f"{name}{suffix}{ext}")
        print(f"已添加后缀: '{suffix}'")

    def replace_text(self, old_text, new_text):
        """
        替换文件名中的文字

        【参数】
        - old_text: 字符串，要被替换的文字
        - new_text: 字符串，替换后的文字

        【逻辑】
        IMG_001.jpg → photo_001.jpg（old_text="IMG_", new_text="photo_"）
        """
        import os
        self.new_names = []
        for f in self.files:
            name, ext = os.path.splitext(f)
            new_name = name.replace(old_text, new_text)
            self.new_names.append(f"{new_name}{ext}")
        print(f"已替换: '{old_text}' → '{new_text}'")

    def preview(self):
        """
        预览重命名效果（不实际执行）

        【参数】无
        【返回值】无

        【逻辑】
        对比显示 原文件名 → 新文件名
        标注哪些会改变，哪些不变
        """
        print("\n" + "-"*55)
        print(f"{'原文件名':<25}{'→':^5}{'新文件名':<25}")
        print("-"*55)

        change_count = 0
        for old, new in zip(self.files, self.new_names):
            if old != new:
                marker = ""  # 有变化
                change_count += 1
            else:
                marker = "（不变）"
            print(f"{old:<25}{'→':^5}{new:<25}{marker}")

        print("-"*55)
        print(f"共 {len(self.files)} 个文件，{change_count} 个将被重命名")

    def execute(self):
        """
        执行重命名

        【逻辑】
        遍历文件列表，用 os.rename() 执行重命名
        """
        import os

        if not self.files:
            print("没有文件可以重命名！")
            return

        success = 0
        for old, new in zip(self.files, self.new_names):
            if old == new:
                continue  # 文件名没变，跳过

            old_path = os.path.join(self.directory, old)
            new_path = os.path.join(self.directory, new)

            # 检查目标文件是否已存在
            if os.path.exists(new_path):
                print(f"跳过 '{old}'：目标 '{new}' 已存在")
                continue

            os.rename(old_path, new_path)
            success += 1

        print(f"\n重命名完成！成功 {success} 个")


# ========== 测试文件批量重命名工具 ==========
# 注意：以下测试使用模拟数据，不会真正修改文件

import os
import tempfile

# 创建临时目录和测试文件
temp_dir = tempfile.mkdtemp()
test_files = ["photo_001.jpg", "photo_002.jpg", "document.txt", "notes.txt"]
for fname in test_files:
    with open(os.path.join(temp_dir, fname), "w") as f:
        f.write("test")

# 创建重命名器
renamer = FileRenamer(temp_dir)
renamer.load_files()

# 测试1：加前缀
print("\n--- 测试1：加前缀 'vacation_' ---")
renamer.add_prefix("vacation_")
renamer.preview()

# 测试2：替换文字
print("\n--- 测试2：把 'photo' 替换为 'img' ---")
renamer.replace_text("photo", "img")
renamer.preview()

# 测试3：加后缀
print("\n--- 测试3：加后缀 '_2024' ---")
renamer.add_suffix("_2024")
renamer.preview()

# 清理临时文件
import shutil
shutil.rmtree(temp_dir)


# =============================================
# 第四节：第三个项目 - 待办清单
# =============================================

print("\n" + "="*50)
print("项目3：待办清单")
print("="*50)

"""
【需求分析】
管理待办事项，功能：
1. 添加任务
2. 完成任务
3. 查看所有任务
4. 查看未完成任务

【设计思路】
1. 用列表存储任务
2. 每个任务是一个字典 {任务名, 是否完成}
3. 创建一个类来管理任务

【调用思路】
创建 TodoList 对象
    → 调用 add_task() 添加任务
    → 调用 complete_task() 完成任务
    → 调用 show_tasks() 查看任务
"""


class TodoList:
    """
    待办清单类

    【属性】
    - tasks: 列表，存储任务

    【方法】
    - add_task(name): 添加任务
    - complete_task(index): 完成任务
    - show_tasks(): 显示所有任务
    - get_pending(): 获取未完成任务
    """

    def __init__(self):
        """
        初始化待办清单

        【调用时机】
        创建对象时自动调用
        """
        self.tasks = []  # 空列表，存储任务

    def add_task(self, task_name):
        """
        添加任务

        【参数】
        - task_name: 字符串，任务名称

        【返回值】无

        【逻辑】
        创建一个字典 {name: 任务名, done: 是否完成}
        添加到 tasks 列表中

        【调用示例】
        todo.add_task("学习 Python")
        """

        # 创建任务字典
        task = {
            "name": task_name,   # 任务名称
            "done": False        # 是否完成，初始为 False
        }

        # 添加到列表
        self.tasks.append(task)
        print(f"✓ 已添加任务: {task_name}")

    def complete_task(self, index):
        """
        完成任务

        【参数】
        - index: 整数，任务的序号（从0开始）

        【返回值】无

        【逻辑】
        1. 检查索引是否有效
        2. 把任务的 done 设为 True

        【调用示例】
        todo.complete_task(0)  # 完成第一个任务
        """

        # 检查索引是否有效
        if 0 <= index < len(self.tasks):
            # 设置为已完成
            self.tasks[index]["done"] = True
            print(f"✓ 已完成: {self.tasks[index]['name']}")
        else:
            print("无效的任务编号！")

    def show_tasks(self):
        """
        显示所有任务

        【参数】无

        【返回值】无

        【逻辑】
        1. 检查是否有任务
        2. 遍历所有任务
        3. 已完成的显示 ✓，未完成的显示 ○

        【调用示例】
        todo.show_tasks()
        """

        # 检查是否有任务
        if not self.tasks:
            print("暂无任务！")
            return

        print("\n待办清单:")
        print("-"*40)

        # 遍历所有任务
        # enumerate() 同时获取索引和值
        for i, task in enumerate(self.tasks):

            # 根据是否完成选择图标
            if task["done"]:
                status = "✓"  # 已完成
            else:
                status = "○"  # 未完成

            # 打印任务
            # i+1 让序号从1开始
            print(f"{i+1}. [{status}] {task['name']}")

    def get_pending(self):
        """
        获取未完成的任务

        【参数】无

        【返回值】
        列表，包含所有未完成的任务

        【调用示例】
        pending = todo.get_pending()
        print(f"还有 {len(pending)} 个任务未完成")
        """

        # 列表推导式：筛选未完成的任务
        return [t for t in self.tasks if not t["done"]]


# ========== 测试待办清单 ==========

# 创建待办清单
todo = TodoList()

# 添加任务
todo.add_task("学习 Python")
todo.add_task("做练习题")
todo.add_task("复习笔记")

# 显示所有任务
todo.show_tasks()

# 完成第一个任务
todo.complete_task(0)

# 再次显示
todo.show_tasks()

# 获取未完成任务
pending = todo.get_pending()
print(f"\n还有 {len(pending)} 个任务未完成")


# =============================================
# 第五节：开发技巧总结
# =============================================

print("\n" + "="*50)
print("开发技巧总结")
print("="*50)

"""
【开发技巧】

1. 先想后写
   - 动手前先想清楚要做什么
   - 画个流程图或写伪代码
   - 不要一上来就写代码

2. 小步快跑
   - 不要一次写太多
   - 写一点，测试一点
   - 确保每一步都正确

3. 善用函数
   - 把重复的代码封装成函数
   - 一个函数只做一件事
   - 函数名要说明功能

4. 使用类
   - 把相关的数据和函数放在一起
   - 让代码更有组织
   - 方便复用和维护

5. 处理异常
   - 不要假设用户会按规矩输入
   - 用 try-except 处理可能的错误
   - 给用户友好的错误提示

6. 写注释
   - 解释代码的用途
   - 说明参数和返回值
   - 方便以后维护

7. 命名规范
   - 变量名要有意义
   - 函数名要说明功能
   - 类名用大驼峰（StudentManager）
"""


# =============================================
# 【练习题】
# =============================================

print("\n" + "="*50)
print("练习题")
print("="*50)

"""
练习1：猜数字游戏
    需求：
    - 程序随机生成1-100的数字
    - 用户循环猜测
    - 提示"大了"或"小了"
    - 猜对后显示尝试次数

    设计：
    1. 用 random.randint() 生成随机数
    2. 用 while 循环让用户猜
    3. 用 if-else 判断大小
    4. 用计数器记录次数

    调用：
    guess_number()  # 启动游戏

练习2：简易记账本
    需求：
    - 记录收入和支出
    - 显示余额
    - 显示收支明细

    设计：
    1. 用列表存储记录
    2. 每条记录是字典 {类型, 金额, 描述}
    3. 创建 AccountBook 类

    调用：
    book = AccountBook()
    book.add_record("income", 10000, "工资")
    book.show_records()

练习3：单词本
    需求：
    - 添加英文单词和中文意思
    - 随机测试
    - 显示正确率

    设计：
    1. 用字典存储 {英文: 中文}
    2. 随机抽取单词
    3. 记录对错

    调用：
    vocab = Vocabulary()
    vocab.add_word("hello", "你好")
    vocab.quiz()
"""


# =============================================
# 练习参考答案
# =============================================

print("\n" + "="*50)
print("练习参考答案")
print("="*50)


# 练习1：猜数字游戏
print("\n--- 练习1 参考 ---")

import random

def guess_number():
    """
    猜数字游戏

    【规则】
    程序随机生成 1-100 的数字，用户循环猜测，
    程序提示"大了"或"小了"，猜对后显示尝试次数。
    """

    # 生成随机数
    answer = random.randint(1, 100)
    attempts = 0  # 计数器

    print("我想了一个 1-100 的数字，猜猜看！")

    while True:
        try:
            guess = int(input("请输入你的猜测: "))
        except ValueError:
            print("请输入有效数字！")
            continue

        attempts += 1  # 每猜一次，计数器加 1

        if guess < answer:
            print("小了！再试试。")
        elif guess > answer:
            print("大了！再试试。")
        else:
            print(f"恭喜你猜对了！答案就是 {answer}")
            print(f"你一共猜了 {attempts} 次")
            break

# 取消注释可运行：
# guess_number()

# 自动演示（不用手动输入）
answer = random.randint(1, 100)
print(f"[自动演示] 答案是 {answer}")
for test_guess in [50, 75, 60, 65]:
    if test_guess < answer:
        print(f"  猜 {test_guess} → 小了")
    elif test_guess > answer:
        print(f"  猜 {test_guess} → 大了")
    else:
        print(f"  猜 {test_guess} → 猜对了！")
        break


# 练习2：简易记账本
print("\n--- 练习2 参考 ---")

class AccountBook:
    """
    简易记账本

    【功能】
    - 记录收入和支出
    - 显示余额
    - 显示收支明细
    """

    def __init__(self):
        """初始化空账本"""
        self.records = []  # 存储所有记录

    def add_record(self, r_type, amount, description):
        """
        添加记录

        【参数】
        - r_type: 字符串，"income"（收入）或 "expense"（支出）
        - amount: 数字，金额
        - description: 字符串，描述
        """
        record = {
            "type": r_type,
            "amount": amount,
            "description": description
        }
        self.records.append(record)
        print(f"已记录: {r_type} {amount} 元 - {description}")

    def get_balance(self):
        """
        计算余额

        【逻辑】
        收入加，支出减
        """
        balance = 0
        for r in self.records:
            if r["type"] == "income":
                balance += r["amount"]
            else:
                balance -= r["amount"]
        return balance

    def show_records(self):
        """显示所有记录和余额"""
        if not self.records:
            print("暂无记录！")
            return

        print("\n" + "-"*40)
        print(f"{'类型':<8}{'金额':<10}{'描述':<20}")
        print("-"*40)

        for r in self.records:
            # 收入显示 +，支出显示 -
            sign = "+" if r["type"] == "income" else "-"
            type_name = "收入" if r["type"] == "income" else "支出"
            print(f"{type_name:<8}{sign}{r['amount']:<9}{r['description']:<20}")

        print("-"*40)
        print(f"余额: {self.get_balance()} 元")


# 测试记账本
book = AccountBook()
book.add_record("income", 10000, "工资")
book.add_record("expense", 3000, "房租")
book.add_record("expense", 1500, "伙食费")
book.add_record("income", 2000, "兼职")
book.show_records()


# 练习3：单词本
print("\n--- 练习3 参考 ---")

class Vocabulary:
    """
    单词本

    【功能】
    - 添加英文单词和中文意思
    - 随机抽取单词测试
    - 显示正确率
    """

    def __init__(self):
        """初始化空单词本"""
        self.words = {}  # {英文: 中文}

    def add_word(self, english, chinese):
        """
        添加单词

        【参数】
        - english: 字符串，英文单词
        - chinese: 字符串，中文意思
        """
        self.words[english] = chinese
        print(f"已添加: {english} → {chinese}")

    def quiz(self, num=3):
        """
        随机测试

        【参数】
        - num: 整数，测试的单词数量（默认 3）

        【逻辑】
        1. 随机抽取单词
        2. 显示中文，让用户输入英文
        3. 判断对错
        4. 最后显示正确率
        """
        if not self.words:
            print("单词本为空，请先添加单词！")
            return

        # 随机抽取单词
        import random
        test_words = random.sample(list(self.words.items()), min(num, len(self.words)))

        correct = 0  # 答对的次数

        for eng, chi in test_words:
            print(f"\n中文: {chi}")
            answer = input("请输入对应的英文单词: ").strip().lower()

            if answer == eng.lower():
                print("正确！")
                correct += 1
            else:
                print(f"错误！正确答案是: {eng}")

        # 显示正确率
        total = len(test_words)
        rate = correct / total * 100
        print(f"\n测试结果: {correct}/{total}，正确率 {rate:.0f}%")


# 测试单词本
vocab = Vocabulary()
vocab.add_word("hello", "你好")
vocab.add_word("python", "蟒蛇/编程语言")
vocab.add_word("world", "世界")
vocab.add_word("computer", "电脑")
vocab.add_word("program", "程序")

# 取消注释可运行交互测试：
# vocab.quiz()

# 自动演示（不用手动输入）
print("\n[自动演示] 单词本中已有以下单词:")
for eng, chi in vocab.words.items():
    print(f"  {eng} → {chi}")
print("运行 vocab.quiz() 可以进行交互式测试")


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- 开发流程：需求分析 → 设计类和方法 → 编码实现 → 测试 → 优化
- 先想清楚"这个程序要做什么"再动手写代码，否则会反复返工
- 用类把数据和方法组织在一起，比一堆散落的函数更容易维护

常见陷阱：
- 一上来就写代码，不做需求分析和设计，写到一半发现方向错了
- 试图一次写出"完美"代码，应该先让它能用，再逐步优化
- 不写测试就认为代码没问题，实际运行时各种边界情况会暴露 bug

下节课预告：
- 下节课做完整的项目实战——学生管理系统，综合运用所有学到的知识
"""
