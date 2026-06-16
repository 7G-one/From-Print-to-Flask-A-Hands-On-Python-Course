# -*- coding: utf-8 -*-
# =============================================
# 第 05 课：字典与集合（函数重构版）
# =============================================
# 上节课我们学了列表和元组。
# 这节课我们要学习字典和集合——两种超级有用的数据容器。
#
# 字典用键值对存储数据，集合自动去重，各有各的用武之地。


# =============================================
# 第一节：什么是字典？
# =============================================

# 【字典的特点】
# 1. 有"键"和"值"两部分
# 2. 键是唯一的（不能重复）
# 3. 通过键来查找值
# 4. 没有顺序（Python 3.7+ 保持插入顺序）

def demo_dict_create():
    # 演示如何创建字典

    print("=== 创建字典 ===")

    # 【创建字典】
    # 用大括号 {} 包起来
    # 键和值用冒号 : 分隔
    # 每对键值用逗号 , 分隔

    # 空字典
    empty_dict = {}
    print(f"空字典：{empty_dict}")

    # 带初始值的字典
    student = {
        "name": "小明",
        "age": 18,
        "grade": "高三",
        "scores": [85, 92, 78]
    }
    print(f"学生信息：{student}")

    # 【键和值的类型】
    # 键：通常是字符串，也可以是数字、元组（不可变类型）
    # 值：可以是任何类型


# =============================================
# 第二节：字典访问（查找值）
# =============================================

def demo_dict_access():
    # 演示如何访问字典中的值

    print("\n=== 字典访问 ===")

    student = {
        "name": "小明",
        "age": 18,
        "grade": "高三"
    }

    # 【方法1：方括号 []】
    print(f"student['name'] = {student['name']}")
    print(f"student['age'] = {student['age']}")

    # 【注意】
    # 如果键不存在，会报错！
    # student['phone']  # KeyError!

    # 【方法2：get() 方法（推荐！）】
    # 如果键不存在，返回 None 或默认值
    print(f"\nstudent.get('name') = {student.get('name')}")
    print(f"student.get('phone') = {student.get('phone')}")        # None
    print(f"student.get('phone', '无') = {student.get('phone', '无')}")  # 默认值

    # 【判断键是否存在】
    print(f"\n'name' in student: {'name' in student}")      # True
    print(f"'phone' in student: {'phone' in student}")    # False


# =============================================
# 第三节：字典修改（增删改）
# =============================================

def demo_dict_modify():
    # 演示如何增删改字典

    print("\n=== 字典修改 ===")

    student = {
        "name": "小明",
        "age": 18
    }
    print(f"原字典：{student}")

    # 【添加/修改键值对】
    # 如果键存在就修改，不存在就添加
    student["age"] = 19           # 修改已存在的键
    student["city"] = "北京"      # 添加新键
    print(f"修改后：{student}")

    # 【删除键值对】
    # del 删除指定键
    del student["city"]
    print(f"\ndel city：{student}")

    # pop() 删除并返回值
    age = student.pop("age")
    print(f"pop('age')：{student}，删除了：{age}")

    # 【update() 批量更新】
    student = {"name": "小明", "age": 18}
    student.update({"age": 20, "city": "北京", "grade": "高三"})
    print(f"\nupdate()：{student}")


# =============================================
# 第四节：字典常用方法
# =============================================

def demo_dict_methods():
    # 演示字典的常用方法

    print("\n=== 字典常用方法 ===")

    student = {
        "name": "小明",
        "age": 18,
        "city": "北京"
    }
    print(f"字典：{student}")

    # 【获取所有键】
    keys = student.keys()
    print(f"\nkeys()：{keys}")
    print(f"转为列表：{list(keys)}")

    # 【获取所有值】
    values = student.values()
    print(f"\nvalues()：{values}")
    print(f"转为列表：{list(values)}")

    # 【获取所有键值对】
    items = student.items()
    print(f"\nitems()：{items}")
    print(f"转为列表：{list(items)}")

    # 【遍历字典】
    print(f"\n遍历字典：")
    for key, value in student.items():
        print(f"  {key}: {value}")

    # 【获取字典长度】
    print(f"\nlen()：{len(student)}")


# =============================================
# 第五节：字典推导式
# =============================================

def demo_dict_comprehension():
    # 演示字典推导式的用法

    print("\n=== 字典推导式 ===")

    # 【基本语法】
    # {键表达式: 值表达式 for 变量 in 可迭代对象}

    # 创建数字平方字典
    squares = {x: x**2 for x in range(1, 6)}
    print(f"数字平方：{squares}")

    # 带条件的字典推导式
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"偶数平方：{even_squares}")

    # 【实际应用】
    # 将两个列表合并成字典
    names = ["小明", "小红", "小刚"]
    scores = [85, 92, 78]
    student_scores = {name: score for name, score in zip(names, scores)}
    print(f"\n学生成绩：{student_scores}")


# =============================================
# 第六节：什么是集合？
# =============================================

def demo_set_create():
    # 演示如何创建集合

    print("\n=== 创建集合 ===")

    # 【集合的特点】
    # 1. 元素唯一（不能重复）
    # 2. 没有顺序
    # 3. 可以用来去重
    # 4. 可以做集合运算（交集、并集、差集）

    # 【创建集合】
    # 用大括号 {} 包起来（注意：空集合要用 set()）

    # 空集合（不能用 {}，那是空字典）
    empty_set = set()
    print(f"空集合：{empty_set}")

    # 带初始值的集合
    fruits = {"苹果", "香蕉", "橘子", "苹果"}  # 重复的会被去重
    print(f"水果集合：{fruits}")  # 只有3个，苹果只出现一次

    # 从列表创建集合
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = set(numbers)
    print(f"\n原列表：{numbers}")
    print(f"去重后：{unique_numbers}")


# =============================================
# 第七节：集合常用操作
# =============================================

def demo_set_operations():
    # 演示集合的增删查操作

    print("\n=== 集合常用操作 ===")

    fruits = {"苹果", "香蕉", "橘子"}
    print(f"原集合：{fruits}")

    # 【添加元素】
    fruits.add("葡萄")
    print(f"\nadd('葡萄')：{fruits}")

    # 【删除元素】
    # remove() - 删除指定元素（不存在会报错）
    fruits.remove("香蕉")
    print(f"remove('香蕉')：{fruits}")

    # discard() - 删除指定元素（不存在不报错）
    fruits.discard("西瓜")  # 不存在也不报错
    print(f"discard('西瓜')：{fruits}")

    # 【集合长度】
    print(f"\nlen()：{len(fruits)}")

    # 【判断元素是否存在】
    print(f"\n'苹果' in fruits：{'苹果' in fruits}")
    print(f"'西瓜' in fruits：{'西瓜' in fruits}")


# =============================================
# 第八节：集合运算（交集、并集、差集）
# =============================================

def demo_set_math():
    # 演示集合的数学运算

    print("\n=== 集合运算 ===")

    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}

    print(f"A = {a}")
    print(f"B = {b}")

    # 【交集（共同的元素）】
    intersection = a & b
    print(f"\nA & B（交集）：{intersection}")  # {3, 4, 5}

    # 【并集（所有的元素）】
    union = a | b
    print(f"A | B（并集）：{union}")  # {1, 2, 3, 4, 5, 6, 7}

    # 【差集（A有B没有）】
    difference = a - b
    print(f"A - B（差集）：{difference}")  # {1, 2}

    # 【对称差集（不共同的元素）】
    symmetric_difference = a ^ b
    print(f"A ^ B（对称差集）：{symmetric_difference}")  # {1, 2, 6, 7}

    # 【实际应用：找共同好友】
    my_friends = {"Alice", "Bob", "Charlie", "David"}
    your_friends = {"Bob", "David", "Eve", "Frank"}

    common = my_friends & your_friends
    print(f"\n我的好友：{my_friends}")
    print(f"你的好友：{your_friends}")
    print(f"共同好友：{common}")


# =============================================
# 实战小项目：词频统计器
# =============================================
print("\n" + "=" * 50)
print("实战小项目：词频统计器")
print("=" * 50)

def word_counter(text):
    """统计文本中每个词出现的次数"""
    words = text.lower().split()
    count = {}
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            count[word] = count.get(word, 0) + 1
    return count

def top_words(count_dict, n=5):
    """返回出现次数最多的 n 个词"""
    sorted_words = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

# 测试
text = "Python is great and Python is easy to learn. Python is powerful and Python is fun."
result = word_counter(text)
print(f"原文：{text}")
print(f"\n词频统计：")
for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}次")
print(f"\nTop 5：")
for word, count in top_words(result):
    print(f"  {word}: {count}次")


# =============================================
# 第九节：实战练习
# =============================================

def exercise_dict_basics():
    # 练习1：字典基础
    # 创建个人信息字典，练习添加、删除、遍历操作

    print("\n--- 练习1：字典基础 ---")
    my_info = {
        "name": "小明",
        "age": 18,
        "hobbies": ["编程", "阅读", "运动"],
        "city": "北京"
    }
    print(f"我的信息：{my_info}")

    # 添加新键
    my_info["job"] = "学生"
    print(f"添加职业后：{my_info}")

    # 删除键
    del my_info["city"]
    print(f"删除城市后：{my_info}")

    # 遍历
    print(f"\n遍历：")
    for key, value in my_info.items():
        print(f"  {key}: {value}")


def exercise_dict_count():
    # 练习2：字典计数
    # 统计字符串中每个字符出现的次数

    print("\n--- 练习2：字典计数 ---")
    text = "hello python"
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    print(f"字符计数：{char_count}")


def exercise_dict_comprehension():
    # 练习3：字典推导式
    # 用字典推导式创建 {单词: 单词长度} 的字典

    print("\n--- 练习3：字典推导式 ---")
    words = ["apple", "banana", "cherry"]
    word_lengths = {w: len(w) for w in words}
    print(f"单词长度：{word_lengths}")


def exercise_set_operations():
    # 练习4：集合去重与运算
    # 对两个列表求并集、交集、差集

    print("\n--- 练习4：集合去重与运算 ---")
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    set1, set2 = set(list1), set(list2)
    print(f"列表1：{list1}")
    print(f"列表2：{list2}")
    print(f"并集：{set1 | set2}")
    print(f"交集：{set1 & set2}")
    print(f"差集（1有2没有）：{set1 - set2}")


def exercise_score_dict():
    # 练习5：成绩字典
    # 统计最高分学生、90分以上、平均分

    print("\n--- 练习5：成绩字典 ---")
    scores = {"小明": 85, "小红": 92, "小刚": 78, "小丽": 95}

    # 最高分学生
    best_student = max(scores, key=scores.get)
    print(f"成绩：{scores}")
    print(f"最高分学生：{best_student}（{scores[best_student]}分）")

    # 90分以上
    excellent = {name: score for name, score in scores.items() if score >= 90}
    print(f"90分以上：{excellent}")

    # 平均分
    avg = sum(scores.values()) / len(scores)
    print(f"平均分：{avg:.1f}")


def exercise_shopping_cart():
    # 练习6：购物车（字典版）
    # 用嵌套字典实现购物车，计算总价

    print("\n--- 练习6：购物车（字典版） ---")
    cart = {
        "苹果": {"price": 8.5, "quantity": 3},
        "牛奶": {"price": 12, "quantity": 2},
        "面包": {"price": 6, "quantity": 1}
    }

    total = sum(info["price"] * info["quantity"] for info in cart.values())
    print(f"购物车：")
    for name, info in cart.items():
        subtotal = info["price"] * info["quantity"]
        print(f"  {name}: ¥{info['price']} x {info['quantity']} = ¥{subtotal}")
    print(f"总计：¥{total}")


# =============================================
# 主程序入口
# =============================================

if __name__ == "__main__":
    # 教学演示
    demo_dict_create()
    demo_dict_access()
    demo_dict_modify()
    demo_dict_methods()
    demo_dict_comprehension()
    demo_set_create()
    demo_set_operations()
    demo_set_math()

    # 练习题
    print("\n" + "="*50)
    print("实战练习")
    print("="*50)

    exercise_dict_basics()
    exercise_dict_count()
    exercise_dict_comprehension()
    exercise_set_operations()
    exercise_score_dict()
    exercise_shopping_cart()


# =============================================
# 课程总结
# =============================================

# 核心收获：
# - 字典用 d["key"] 取值，用 d.get("key", 默认值) 避免 KeyError
# - 集合天然去重，用 & 交集、| 并集、- 差集做集合运算，性能极佳
# - 字典推导式 {k: v for ...} 和集合推导式 {x for ...} 让数据转换更简洁
#
# 常见陷阱：
# - 字典键不存在时用 d["key"] 会 KeyError，优先用 .get() 方法
# - 集合是无序的：不能用索引访问，也不能指望元素有固定顺序
# - 可变对象（列表、字典）不能做字典的键或集合的元素，会报 TypeError
#
# 下节课预告：
# - 下节课学条件语句，让程序根据情况做不同的事
