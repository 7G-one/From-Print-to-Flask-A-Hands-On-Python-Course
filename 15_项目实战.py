# -*- coding: utf-8 -*-
# =============================================
# 第 15 课：项目实战
# =============================================
# 上节课我们学了开发实战入门。
# 这节课我们要做一个完整的项目——学生管理系统！
#
# 综合运用类、文件操作、异常处理等知识，走一遍真实项目的开发流程。

import json
import os

# =============================================
# 第一节：项目需求分析（非常重要！）
# =============================================

"""
【项目名称】学生管理系统

【我们要做什么？】
做一个程序，可以管理学生的信息：
1. 添加学生（姓名、年龄、成绩）
2. 查看所有学生
3. 查找某个学生
4. 修改学生信息
5. 删除学生
6. 统计分析（平均分、最高分、最低分）
7. 保存到文件（这样关闭程序后数据还在）
8. 从文件加载（打开程序时恢复数据）

【技术要点】
1. 用"类"来组织代码（Student 类、StudentManager 类）
2. 用"字典"存储学生信息
3. 用"文件"保存数据
4. 用"异常处理"保证程序稳定

【开发步骤】
1. 先设计 Student 类（存储单个学生的信息）
2. 再设计 StudentManager 类（管理所有学生）
3. 最后写主程序（菜单交互）
"""


# =============================================
# 第二节：设计 Student 类（单个学生）
# =============================================

"""
【设计思路】

一个学生需要哪些信息？
- 姓名（字符串）
- 年龄（整数）
- 成绩（浮点数）

这些信息用什么数据结构？
- 用"类"最合适！
- 把数据（属性）和操作数据的方法放在一起

【类的设计】
class Student:
    属性：name, age, score
    方法：to_dict() - 转换成字典（方便保存到文件）
    方法：from_dict() - 从字典创建（方便从文件加载）
"""


class Student:
    """
    学生类

    【作用】
    存储单个学生的信息

    【属性】
    - name: 字符串，学生姓名
    - age: 整数，学生年龄
    - score: 浮点数，学生成绩

    【方法】
    - to_dict(): 转换成字典
    - from_dict(): 从字典创建学生对象
    """

    def __init__(self, name, age, score):
        """
        初始化方法

        【作用】
        创建学生对象时，设置姓名、年龄、成绩

        【参数】
        - name: 字符串，学生姓名
        - age: 整数，学生年龄
        - score: 浮点数，学生成绩

        【调用示例】
        student = Student("小明", 18, 85.5)
        """

        # 把参数保存到对象的属性中
        self.name = name      # 姓名
        self.age = age        # 年龄
        self.score = score    # 成绩

    def to_dict(self):
        """
        转换成字典

        【作用】
        把学生对象转换成字典，方便保存到 JSON 文件

        【参数】无

        【返回值】
        字典，包含 name, age, score

        【调用示例】
        student = Student("小明", 18, 85.5)
        data = student.to_dict()
        # data = {"name": "小明", "age": 18, "score": 85.5}
        """

        return {
            "name": self.name,      # 姓名
            "age": self.age,        # 年龄
            "score": self.score     # 成绩
        }

    @classmethod
    def from_dict(cls, data):
        """
        从字典创建学生对象（类方法）

        【作用】
        从 JSON 文件读取的字典数据，创建学生对象

        【参数】
        - data: 字典，包含 name, age, score

        【返回值】
        Student 对象

        【调用示例】
        data = {"name": "小明", "age": 18, "score": 85.5}
        student = Student.from_dict(data)
        """

        # cls 就是 Student 类本身
        # 调用 cls() 就是调用 Student()
        return cls(data["name"], data["age"], data["score"])

    def __str__(self):
        """
        字符串表示

        【作用】
        当用 print() 打印学生对象时，显示的内容

        【调用示例】
        student = Student("小明", 18, 85.5)
        print(student)  # 输出：小明, 18岁, 85.5分
        """

        return f"{self.name}, {self.age}岁, {self.score}分"


# =============================================
# 第三节：设计 StudentManager 类（管理所有学生）
# =============================================

"""
【设计思路】

需要管理多个学生，需要哪些功能？
1. 添加学生
2. 查看所有学生
3. 查找学生
4. 修改学生信息
5. 删除学生
6. 统计分析
7. 保存到文件
8. 从文件加载

【数据结构】
用列表存储所有学生：[Student1, Student2, ...]

【类的设计】
class StudentManager:
    属性：students（学生列表）
    属性：filename（保存文件名）
    方法：add_student() - 添加
    方法：show_all() - 查看所有
    方法：find_student() - 查找
    方法：update_student() - 修改
    方法：delete_student() - 删除
    方法：get_statistics() - 统计
    方法：save() - 保存
    方法：load() - 加载
"""


class StudentManager:
    """
    学生管理系统类

    【作用】
    管理所有学生的增删改查

    【属性】
    - students: 列表，存储所有 Student 对象
    - filename: 字符串，保存数据的文件名

    【方法】
    - add_student(name, age, score): 添加学生
    - show_all(): 显示所有学生
    - find_student(name): 查找学生
    - update_student(name, new_age, new_score): 修改学生
    - delete_student(name): 删除学生
    - get_statistics(): 统计分析
    - save(): 保存到文件
    - load(): 从文件加载
    """

    def __init__(self, filename="students.json"):
        """
        初始化方法

        【作用】
        创建学生管理系统时：
        1. 初始化空的学生列表
        2. 设置保存文件名
        3. 尝试从文件加载数据

        【参数】
        - filename: 字符串，保存数据的文件名（默认 "students.json"）

        【调用示例】
        manager = StudentManager()  # 使用默认文件名
        manager = StudentManager("my_students.json")  # 使用自定义文件名
        """

        self.students = []           # 空列表，存储所有学生
        self.filename = filename     # 保存文件名
        self.load()                  # 启动时自动加载数据

    def add_student(self, name, age, score):
        """
        添加学生

        【作用】
        创建一个新的 Student 对象，添加到学生列表中

        【参数】
        - name: 字符串，学生姓名
        - age: 整数，学生年龄
        - score: 浮点数，学生成绩

        【返回值】无

        【调用流程】
        1. 创建 Student 对象
        2. 添加到 self.students 列表
        3. 打印成功提示
        4. 自动保存到文件

        【调用示例】
        manager.add_student("小明", 18, 85.5)
        """

        # 创建学生对象
        student = Student(name, age, score)

        # 添加到列表
        self.students.append(student)

        # 打印提示
        print(f"✓ 已添加: {student}")

        # 自动保存
        self.save()

    def show_all(self):
        """
        显示所有学生

        【作用】
        遍历所有学生，格式化输出

        【参数】无

        【返回值】无

        【调用流程】
        1. 检查是否有学生数据
        2. 打印表头
        3. 遍历所有学生，打印信息
        4. 打印学生总数

        【调用示例】
        manager.show_all()
        """

        # 检查是否有数据
        if not self.students:
            print("暂无学生数据！")
            return

        # 打印表头
        print("\n" + "="*60)
        print(f"{'序号':<6}{'姓名':<12}{'年龄':<8}{'成绩':<8}")
        print("="*60)

        # 遍历所有学生
        # enumerate() 同时获取索引和值
        # start=1 让序号从1开始
        for i, student in enumerate(self.students, 1):
            print(f"{i:<6}{student.name:<12}{student.age:<8}{student.score:<8}")

        # 打印表尾
        print("="*60)
        print(f"共 {len(self.students)} 名学生")

    def find_student(self, name):
        """
        查找学生

        【作用】
        根据姓名查找学生

        【参数】
        - name: 字符串，要查找的学生姓名

        【返回值】
        - 如果找到，返回 Student 对象
        - 如果没找到，返回 None

        【调用流程】
        1. 遍历所有学生
        2. 比较姓名
        3. 找到就返回，没找到返回 None

        【调用示例】
        student = manager.find_student("小明")
        if student:
            print(f"找到: {student}")
        else:
            print("未找到")
        """

        # 遍历所有学生
        for student in self.students:
            # 比较姓名
            if student.name == name:
                return student  # 找到了

        return None  # 没找到

    def update_student(self, name, new_age=None, new_score=None):
        """
        修改学生信息

        【作用】
        根据姓名找到学生，修改年龄或成绩

        【参数】
        - name: 字符串，要修改的学生姓名
        - new_age: 整数（可选），新的年龄
        - new_score: 浮点数（可选），新的成绩

        【返回值】
        - True: 修改成功
        - False: 未找到学生

        【调用流程】
        1. 查找学生
        2. 如果找到，修改信息
        3. 保存到文件

        【调用示例】
        manager.update_student("小明", new_age=19)  # 只改年龄
        manager.update_student("小明", new_score=90)  # 只改成绩
        manager.update_student("小明", new_age=19, new_score=90)  # 都改
        """

        # 查找学生
        student = self.find_student(name)

        if student:
            # 找到了，修改信息
            if new_age is not None:
                student.age = new_age
            if new_score is not None:
                student.score = new_score

            print(f"✓ 已更新: {student}")
            self.save()  # 保存
            return True
        else:
            # 没找到
            print(f"✗ 未找到学生: {name}")
            return False

    def delete_student(self, name):
        """
        删除学生

        【作用】
        根据姓名删除学生

        【参数】
        - name: 字符串，要删除的学生姓名

        【返回值】
        - True: 删除成功
        - False: 未找到学生

        【调用流程】
        1. 查找学生
        2. 如果找到，从列表中移除
        3. 保存到文件

        【调用示例】
        manager.delete_student("小明")
        """

        # 查找学生
        student = self.find_student(name)

        if student:
            # 找到了，从列表中移除
            self.students.remove(student)
            print(f"✓ 已删除: {name}")
            self.save()  # 保存
            return True
        else:
            # 没找到
            print(f"✗ 未找到学生: {name}")
            return False

    def get_statistics(self):
        """
        统计分析

        【作用】
        计算学生总数、平均分、最高分、最低分

        【参数】无

        【返回值】
        字典，包含统计信息：
        - count: 学生总数
        - average: 平均分
        - max: 最高分
        - min: 最低分
        - pass_count: 及格人数（>=60）

        【调用示例】
        stats = manager.get_statistics()
        if stats:
            print(f"平均分: {stats['average']}")
        """

        # 检查是否有数据
        if not self.students:
            return None

        # 收集所有成绩
        scores = [s.score for s in self.students]

        # 计算统计信息
        return {
            "count": len(self.students),                # 学生总数
            "average": sum(scores) / len(scores),       # 平均分
            "max": max(scores),                         # 最高分
            "min": min(scores),                         # 最低分
            "pass_count": len([s for s in scores if s >= 60])  # 及格人数
        }

    def save(self):
        """
        保存到文件

        【作用】
        把学生数据保存到 JSON 文件

        【参数】无

        【返回值】无

        【调用流程】
        1. 把每个 Student 对象转换成字典
        2. 写入 JSON 文件

        【调用示例】
        manager.save()  # 手动保存（通常不需要，因为自动保存）
        """

        # 把所有学生转换成字典列表
        data = [student.to_dict() for student in self.students]

        # 写入 JSON 文件
        # ensure_ascii=False 支持中文
        # indent=2 格式化输出
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        """
        从文件加载

        【作用】
        从 JSON 文件读取学生数据

        【参数】无

        【返回值】无

        【调用流程】
        1. 检查文件是否存在
        2. 读取 JSON 数据
        3. 把字典转换成 Student 对象

        【调用示例】
        manager.load()  # 手动加载（通常不需要，因为自动加载）
        """

        # 检查文件是否存在
        if os.path.exists(self.filename):
            try:
                # 读取 JSON 文件
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # 把字典转换成 Student 对象
                self.students = [Student.from_dict(d) for d in data]
                print(f"已加载 {len(self.students)} 名学生")

            except (json.JSONDecodeError, KeyError) as e:
                # 文件格式错误
                print(f"数据文件格式错误: {e}")
                self.students = []
        else:
            # 文件不存在
            self.students = []


# =============================================
# 第四节：主程序（菜单交互）
# =============================================

"""
【设计思路】

主程序是一个无限循环：
1. 显示菜单
2. 获取用户选择
3. 根据选择执行对应功能
4. 循环回到步骤1
"""


def main():
    """
    主函数

    【作用】
    程序的入口，显示菜单，处理用户选择

    【调用流程】
    1. 创建 StudentManager 对象
    2. 进入无限循环
    3. 显示菜单
    4. 获取用户选择
    5. 根据选择调用对应方法
    """

    # 创建学生管理器
    manager = StudentManager()

    # 无限循环
    while True:

        # ========== 显示菜单 ==========
        print("\n" + "="*40)
        print("      学生管理系统")
        print("="*40)
        print("1. 添加学生")
        print("2. 查看所有学生")
        print("3. 查找学生")
        print("4. 修改学生信息")
        print("5. 删除学生")
        print("6. 统计分析")
        print("7. 退出")
        print("="*40)

        # ========== 获取用户选择 ==========
        choice = input("请选择(1-7): ")

        # ========== 处理选择 ==========

        if choice == "1":
            # ---------- 添加学生 ----------
            print("\n--- 添加学生 ---")

            # 获取姓名
            name = input("姓名: ")

            # 获取年龄（需要转换成整数）
            try:
                age = int(input("年龄: "))
            except ValueError:
                print("年龄必须是数字！")
                continue

            # 获取成绩（需要转换成浮点数）
            try:
                score = float(input("成绩: "))
            except ValueError:
                print("成绩必须是数字！")
                continue

            # 调用管理器添加学生
            manager.add_student(name, age, score)

        elif choice == "2":
            # ---------- 查看所有 ----------
            manager.show_all()

        elif choice == "3":
            # ---------- 查找学生 ----------
            print("\n--- 查找学生 ---")
            name = input("请输入姓名: ")

            student = manager.find_student(name)
            if student:
                print(f"找到: {student}")
            else:
                print("未找到该学生")

        elif choice == "4":
            # ---------- 修改学生 ----------
            print("\n--- 修改学生 ---")
            name = input("请输入要修改的学生姓名: ")

            print("(直接回车跳过不修改)")
            age_str = input("新年龄: ")
            score_str = input("新成绩: ")

            # 转换输入（如果为空则不修改）
            new_age = int(age_str) if age_str else None
            new_score = float(score_str) if score_str else None

            manager.update_student(name, new_age, new_score)

        elif choice == "5":
            # ---------- 删除学生 ----------
            print("\n--- 删除学生 ---")
            name = input("请输入要删除的学生姓名: ")

            # 确认删除
            confirm = input(f"确定要删除 {name} 吗？(y/n): ")
            if confirm.lower() == "y":
                manager.delete_student(name)

        elif choice == "6":
            # ---------- 统计分析 ----------
            stats = manager.get_statistics()
            if stats:
                print("\n" + "="*30)
                print("统计分析")
                print("="*30)
                print(f"学生总数: {stats['count']}")
                print(f"平均分: {stats['average']:.1f}")
                print(f"最高分: {stats['max']}")
                print(f"最低分: {stats['min']}")
                print(f"及格人数: {stats['pass_count']}")
                print(f"及格率: {stats['pass_count']/stats['count']*100:.1f}%")
            else:
                print("暂无数据！")

        elif choice == "7":
            # ---------- 退出 ----------
            print("感谢使用，再见！")
            break

        else:
            print("无效选择，请重试！")


# =============================================
# 第五节：测试代码
# =============================================

print("="*50)
print("学生管理系统测试")
print("="*50)

# 创建管理器（使用测试文件）
manager = StudentManager("test_students.json")

# 添加学生
manager.add_student("小明", 18, 85)
manager.add_student("小红", 19, 92)
manager.add_student("小刚", 20, 78)
manager.add_student("小丽", 18, 95)

# 显示所有
manager.show_all()

# 查找
print("\n查找小红:")
student = manager.find_student("小红")
if student:
    print(f"找到: {student}")

# 统计
stats = manager.get_statistics()
if stats:
    print(f"\n统计:")
    print(f"  平均分: {stats['average']:.1f}")
    print(f"  最高分: {stats['max']}")
    print(f"  最低分: {stats['min']}")

# 修改
manager.update_student("小明", new_score=90)

# 删除
manager.delete_student("小刚")

# 再次显示
manager.show_all()

# 清理测试文件
os.remove("test_students.json")


# =============================================
# 【练习题】
# =============================================

print("\n" + "="*50)
print("练习题")
print("="*50)

"""
练习1：扩展学生管理系统
    需求：
    - 添加按成绩排序功能
    - 添加按姓名模糊搜索功能
    - 添加导出到CSV文件功能

    设计：
    1. 在 StudentManager 类中添加新方法
    2. 在菜单中添加新选项

    调用：
    manager.sort_by_score()
    results = manager.search_by_name("小")
    manager.export_to_csv("students.csv")

练习2：图书管理系统
    需求：
    - 添加图书（书名、作者、ISBN）
    - 借阅图书
    - 归还图书
    - 查看借阅记录

    设计：
    1. 创建 Book 类
    2. 创建 Library 类
    3. 用字典存储借阅记录

    调用：
    library = Library()
    library.add_book("Python入门", "张三", "978-xxx")
    library.borrow_book("978-xxx", "小明")
    library.return_book("978-xxx")

练习3：任务管理器
    需求：
    - 添加任务（标题、截止日期、优先级）
    - 标记完成
    - 按优先级排序
    - 显示未完成任务

    设计：
    1. 创建 Task 类
    2. 创建 TaskManager 类
    3. 用列表存储任务

    调用：
    manager = TaskManager()
    manager.add_task("学习Python", "2024-01-20", "高")
    manager.complete_task(0)
    manager.show_by_priority()
"""


# =============================================
# 练习参考答案
# =============================================

print("\n" + "="*50)
print("练习参考答案")
print("="*50)


# 练习1：扩展学生管理系统（按成绩排序、模糊搜索、导出CSV）
print("\n--- 练习1 参考 ---")

class StudentManagerExtended(StudentManager):
    """
    扩展的学生管理系统

    【新增功能】
    - sort_by_score(): 按成绩排序
    - search_by_name(keyword): 按姓名模糊搜索
    - export_to_csv(filename): 导出到 CSV 文件
    """

    def sort_by_score(self, reverse=True):
        """
        按成绩排序

        【参数】
        - reverse: True 为降序（高分在前），False 为升序
        """
        self.students.sort(key=lambda s: s.score, reverse=reverse)
        print("已按成绩排序")
        self.show_all()

    def search_by_name(self, keyword):
        """
        按姓名模糊搜索

        【参数】
        - keyword: 字符串，搜索关键词

        【返回值】
        列表，包含所有匹配的 Student 对象
        """
        results = [s for s in self.students if keyword in s.name]
        if results:
            print(f"找到 {len(results)} 个匹配结果:")
            for s in results:
                print(f"  {s}")
        else:
            print(f"未找到包含 '{keyword}' 的学生")
        return results

    def export_to_csv(self, filename="students.csv"):
        """
        导出到 CSV 文件

        【参数】
        - filename: 字符串，导出的文件名
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write("姓名,年龄,成绩\n")
            for s in self.students:
                f.write(f"{s.name},{s.age},{s.score}\n")
        print(f"已导出到 {filename}（共 {len(self.students)} 条）")


# 测试扩展功能
ext_manager = StudentManagerExtended("test_extended.json")
ext_manager.add_student("张三", 18, 85)
ext_manager.add_student("李四", 19, 92)
ext_manager.add_student("张小明", 20, 78)
ext_manager.add_student("王五", 18, 95)

print("\n按成绩排序:")
ext_manager.sort_by_score()

print("\n模糊搜索 '张':")
ext_manager.search_by_name("张")

ext_manager.export_to_csv("test_students.csv")

# 清理测试文件
import os
os.remove("test_extended.json")
os.remove("test_students.csv")


# 练习2：图书管理系统
print("\n--- 练习2 参考 ---")

class Book:
    """
    图书类

    【属性】
    - title: 书名
    - author: 作者
    - isbn: ISBN 编号
    - borrowed: 是否被借出
    """

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False  # 默认未借出
        self.borrower = None   # 借阅人

    def __str__(self):
        status = "已借出" if self.borrowed else "可借阅"
        return f"[{status}] {self.title} - {self.author} (ISBN: {self.isbn})"


class Library:
    """
    图书管理类

    【功能】
    - 添加图书
    - 借阅图书
    - 归还图书
    - 查看借阅记录
    """

    def __init__(self):
        self.books = {}       # {isbn: Book}
        self.borrow_log = []  # 借阅记录

    def add_book(self, title, author, isbn):
        """添加图书"""
        if isbn in self.books:
            print(f"ISBN {isbn} 已存在！")
            return
        self.books[isbn] = Book(title, author, isbn)
        print(f"已添加: {title}")

    def borrow_book(self, isbn, borrower):
        """
        借阅图书

        【参数】
        - isbn: 字符串，图书 ISBN
        - borrower: 字符串，借阅人姓名
        """
        if isbn not in self.books:
            print("未找到该图书！")
            return

        book = self.books[isbn]
        if book.borrowed:
            print(f"《{book.title}》已被 {book.borrower} 借出！")
            return

        book.borrowed = True
        book.borrower = borrower
        self.borrow_log.append({
            "isbn": isbn,
            "title": book.title,
            "borrower": borrower,
            "action": "借阅"
        })
        print(f"{borrower} 成功借阅《{book.title}》")

    def return_book(self, isbn):
        """归还图书"""
        if isbn not in self.books:
            print("未找到该图书！")
            return

        book = self.books[isbn]
        if not book.borrowed:
            print(f"《{book.title}》未被借出！")
            return

        borrower = book.borrower
        self.borrow_log.append({
            "isbn": isbn,
            "title": book.title,
            "borrower": borrower,
            "action": "归还"
        })
        book.borrowed = False
        book.borrower = None
        print(f"《{book.title}》已归还")

    def show_books(self):
        """显示所有图书"""
        if not self.books:
            print("图书馆暂无图书！")
            return
        print("\n图书列表:")
        for book in self.books.values():
            print(f"  {book}")

    def show_log(self):
        """显示借阅记录"""
        if not self.borrow_log:
            print("暂无借阅记录！")
            return
        print("\n借阅记录:")
        for log in self.borrow_log:
            print(f"  [{log['action']}] {log['borrower']} - 《{log['title']}》")


# 测试图书管理系统
library = Library()
library.add_book("Python入门", "张三", "978-1")
library.add_book("数据结构", "李四", "978-2")
library.add_book("算法导论", "王五", "978-3")
library.show_books()

library.borrow_book("978-1", "小明")
library.borrow_book("978-2", "小红")
library.show_books()

library.return_book("978-1")
library.show_log()


# 练习3：任务管理器
print("\n--- 练习3 参考 ---")

class Task:
    """
    任务类

    【属性】
    - title: 标题
    - deadline: 截止日期
    - priority: 优先级（高/中/低）
    - done: 是否完成
    """

    def __init__(self, title, deadline, priority="中"):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.done = False

    def __str__(self):
        status = "已完成" if self.done else "未完成"
        return f"[{status}] {self.title} | 截止: {self.deadline} | 优先级: {self.priority}"


class TaskManager:
    """
    任务管理器

    【功能】
    - 添加任务
    - 标记完成
    - 按优先级排序
    - 显示未完成任务
    """

    # 优先级排序用的映射
    PRIORITY_ORDER = {"高": 0, "中": 1, "低": 2}

    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority="中"):
        """添加任务"""
        task = Task(title, deadline, priority)
        self.tasks.append(task)
        print(f"已添加: {title}")

    def complete_task(self, index):
        """标记任务完成"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            print(f"已完成: {self.tasks[index].title}")
        else:
            print("无效的任务编号！")

    def show_by_priority(self):
        """按优先级排序显示"""
        sorted_tasks = sorted(
            self.tasks,
            key=lambda t: self.PRIORITY_ORDER.get(t.priority, 1)
        )
        print("\n按优先级排序:")
        for t in sorted_tasks:
            print(f"  {t}")

    def show_pending(self):
        """显示未完成任务"""
        pending = [t for t in self.tasks if not t.done]
        if not pending:
            print("所有任务已完成！")
            return
        print(f"\n未完成任务（共 {len(pending)} 个）:")
        for t in pending:
            print(f"  {t}")


# 测试任务管理器
tm = TaskManager()
tm.add_task("学习Python", "2024-01-20", "高")
tm.add_task("写作业", "2024-01-18", "中")
tm.add_task("看电影", "2024-01-25", "低")
tm.add_task("复习考试", "2024-01-19", "高")

tm.show_by_priority()
tm.complete_task(0)
tm.show_pending()


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- 完整项目流程：需求分析 → 类设计 → 数据持久化 → 异常处理 → 测试
- 用 JSON 文件保存和加载数据，让程序重启后数据不丢失
- 把大问题拆成小方法，每个方法只做一件事，代码更清晰更易调试

常见陷阱：
- 数据保存失败时没有异常处理，用户操作了一堆数据结果程序崩溃全丢
- 类设计时把所有逻辑塞进一个方法，应该按职责拆分成多个小方法
- 不做边界测试（如空输入、重复数据），上线后用户会遇到各种奇怪问题

下节课预告：
- 下节课学 Web 开发入门，用 Flask 把你的程序搬到浏览器里运行
"""
