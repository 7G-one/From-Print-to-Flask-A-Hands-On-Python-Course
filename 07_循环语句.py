# -*- coding: utf-8 -*-
# =============================================
# 第 07 课：循环语句
# =============================================
# 上节课我们学了条件语句。
# 这节课我们要学习循环语句——让程序重复做事情。
#
# for 循环遍历已知序列，while 循环在条件满足时持续执行。

# =============================================
# 第一节：什么是循环？
# =============================================

# 【循环的作用】
# 让程序重复做某件事情
# 就像流水线上的工人，重复同样的动作

# 【循环的两种形式】
# 1. for 循环：知道要重复多少次
# 2. while 循环：不知道要重复多少次，直到条件不满足


# =============================================
# 第二节：for 循环（遍历）
# =============================================

# 【for 循环的语法】
# for 变量 in 可迭代对象:
#     循环体
#
# "可迭代对象"就是可以一个一个拿出来的东西：
# - 列表
# - 字符串
# - range() 生成的数字

def demo_for_loop():
    # 演示 for 循环的基本用法

    # 【示例1：遍历列表】
    print("=== 遍历列表 ===")
    fruits = ["苹果", "香蕉", "橘子"]
    print("我喜欢的水果：")
    for fruit in fruits:
        print(f"  {fruit}")  # 注意缩进！

    # 【示例2：遍历字符串】
    print("\n=== 遍历字符串 ===")
    for char in "Python":
        print(f"  {char}")

    # 【示例3：遍历字典】
    print("\n=== 遍历字典 ===")
    student = {"name": "小明", "age": 18, "city": "北京"}
    for key, value in student.items():
        print(f"  {key}: {value}")


# =============================================
# 第三节：range() 函数（生成数字序列）
# =============================================

# 【range() 是什么？】
# range() 生成一个数字序列
# 常用于 for 循环中
#
# 三种用法：
# range(stop)           -> 从 0 到 stop-1
# range(start, stop)    -> 从 start 到 stop-1
# range(start, stop, step) -> 从 start 到 stop-1，每次增加 step

def demo_range():
    # 演示 range() 函数的用法

    print("=== range() 函数 ===")

    # 【range(stop)】
    print(f"range(5) = {list(range(5))}")  # [0, 1, 2, 3, 4]

    # 【range(start, stop)】
    print(f"range(2, 7) = {list(range(2, 7))}")  # [2, 3, 4, 5, 6]

    # 【range(start, stop, step)】
    print(f"range(0, 10, 2) = {list(range(0, 10, 2))}")  # [0, 2, 4, 6, 8]
    print(f"range(10, 0, -1) = {list(range(10, 0, -1))}")  # [10, 9, 8, ..., 1]

    # 【示例：循环5次】
    print("\n循环5次：")
    for i in range(5):
        print(f"  第 {i+1} 次循环")

    # 【示例：计算1到10的和】
    print("\n计算1到10的和：")
    total = 0
    for i in range(1, 11):  # 1到10
        total += i
    print(f"  1+2+3+...+10 = {total}")


# =============================================
# 第四节：while 循环（条件循环）
# =============================================

# 【while 循环的语法】
# while 条件:
#     循环体
#
# 只要条件为 True，就一直循环
# 直到条件为 False，才停止
#
# 注意：一定要更新条件变量，否则会死循环！

def demo_while_loop():
    # 演示 while 循环的基本用法

    print("=== while 循环 ===")

    # 【示例1：简单计数】
    print("简单计数：")
    count = 1
    while count <= 5:
        print(f"  count = {count}")
        count += 1  # 别忘了更新条件！

    # 【示例2：模拟输入验证】
    print("\n模拟输入验证（假设用户前两次输错，第三次正确）：")
    password = ""
    attempts = 0
    correct_password = "123456"

    while password != correct_password and attempts < 3:
        # 模拟用户输入
        if attempts == 0:
            password = "wrong1"
        elif attempts == 1:
            password = "wrong2"
        else:
            password = "123456"

        attempts += 1
        print(f"  第{attempts}次尝试：{'成功' if password == correct_password else '失败'}")

    if password == correct_password:
        print("  登录成功！")
    else:
        print("  次数用完，账户锁定")

    # 【示例3：猜数字游戏】
    print("\n猜数字游戏（答案是42）：")
    secret = 42
    guesses = [50, 30, 45, 42]  # 模拟猜测序列

    for guess in guesses:
        if guess > secret:
            print(f"  猜 {guess} → 大了")
        elif guess < secret:
            print(f"  猜 {guess} → 小了")
        else:
            print(f"  猜 {guess} → 恭喜，猜对了！")
            break


# =============================================
# 第五节：break 和 continue
# =============================================

# 【break：立即跳出循环】
# 就像"我不干了！"

# 【continue：跳过这一次，继续下一次】
# 就像"这个不要，下一个"

def demo_break_continue():
    # 演示 break 和 continue 的用法

    print("=== break 和 continue ===")

    # 【break 示例】
    print("break 示例（遇到5就停止）：")
    for i in range(1, 10):
        if i == 5:
            print(f"  遇到 {i}，跳出循环")
            break
        print(f"  i = {i}")

    # 【continue 示例】
    print("\ncontinue 示例（跳过3）：")
    for i in range(1, 6):
        if i == 3:
            print(f"  跳过 {i}")
            continue
        print(f"  i = {i}")

    # 【实际应用：找第一个偶数】
    print("\n找第一个偶数：")
    numbers = [1, 3, 5, 8, 9, 10]
    for num in numbers:
        if num % 2 == 0:
            print(f"  找到第一个偶数：{num}")
            break


# =============================================
# 第六节：enumerate() 带索引遍历
# =============================================

# 【enumerate() 是什么？】
# 同时获取索引和值
# 语法：enumerate(可迭代对象, start=0)

def demo_enumerate():
    # 演示 enumerate() 的用法

    print("=== enumerate() ===")

    fruits = ["苹果", "香蕉", "橘子"]

    # 不用 enumerate（不推荐）
    print("不用 enumerate：")
    for i in range(len(fruits)):
        print(f"  {i}: {fruits[i]}")

    # 用 enumerate（推荐！）
    print("\n用 enumerate：")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")

    # 从1开始计数
    print("\n从1开始：")
    for num, fruit in enumerate(fruits, start=1):
        print(f"  {num}. {fruit}")


# =============================================
# 第七节：zip() 并行遍历
# =============================================

# 【zip() 是什么？】
# 同时遍历多个列表
# 长度以最短的为准

def demo_zip():
    # 演示 zip() 的用法

    print("=== zip() ===")

    names = ["小明", "小红", "小刚"]
    scores = [85, 92, 78]
    cities = ["北京", "上海", "广州"]

    print("并行遍历：")
    for name, score, city in zip(names, scores, cities):
        print(f"  {name} 来自 {city}，成绩 {score} 分")

    # 【实际应用：成绩表】
    print("\n成绩表：")
    print("  姓名\t成绩\t城市")
    print("  ----\t----\t----")
    for name, score, city in zip(names, scores, cities):
        print(f"  {name}\t{score}\t{city}")


# =============================================
# 第八节：列表推导式（快速创建列表）
# =============================================

# 【列表推导式是什么？】
# 用一行代码创建列表的快捷方式
# 语法：[表达式 for 变量 in 可迭代对象 if 条件]

def demo_list_comprehension():
    # 演示列表推导式的用法

    print("=== 列表推导式 ===")

    # 创建平方数列表
    squares = [x**2 for x in range(1, 6)]
    print(f"平方数：{squares}")

    # 带条件的列表推导式
    evens = [x for x in range(1, 11) if x % 2 == 0]
    print(f"偶数：{evens}")

    # 字符串处理
    words = ["hello", "python", "world"]
    upper_words = [w.upper() for w in words]
    print(f"转大写：{upper_words}")

    # 【实际应用：过滤及格成绩】
    scores = [85, 92, 78, 95, 88, 76, 90]
    passed = [s for s in scores if s >= 80]
    print(f"\n所有成绩：{scores}")
    print(f"80分以上：{passed}")


# =============================================
# 实战小项目：九九乘法表生成器
# =============================================
print("\n" + "=" * 50)
print("实战小项目：九九乘法表生成器")
print("=" * 50)

def multiplication_table(n=9):
    """生成 n*n 乘法表"""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j:2d}", end="  ")
        print()  # 换行

def multiplication_table_compact(n=9):
    """紧凑版乘法表"""
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(f"{j}×{i}={i*j:2d}")
        print("  ".join(row))

# 测试
print("标准版：")
multiplication_table(9)
print("\n紧凑版：")
multiplication_table_compact(9)


# =============================================
# 练习参考答案
# =============================================

def exercise_1():
    # 练习1：求1到100的和
    print("--- 练习1：求1到100的和 ---")
    total = 0
    for i in range(1, 101):
        total += i
    print(f"1到100的和：{total}")
    print(f"公式验证：{100 * 101 // 2}")


def exercise_2():
    # 练习2：找最大值
    print("\n--- 练习2：找最大值 ---")
    numbers = [34, 67, 12, 89, 45, 23, 78]
    print(f"列表：{numbers}")

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print(f"最大值：{max_num}")
    print(f"验证：{max(numbers)}")


def exercise_3():
    # 练习3：斐波那契数列
    print("\n--- 练习3：斐波那契数列 ---")
    fib = [1, 1]
    for i in range(2, 10):
        fib.append(fib[i-1] + fib[i-2])
    print(f"前10项：{fib}")


def exercise_4():
    # 练习4：九九乘法表
    print("\n--- 练习4：九九乘法表 ---")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j:2}", end="  ")
        print()


def exercise_5():
    # 练习5：打印三角形
    print("\n--- 练习5：打印三角形 ---")
    n = 5
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def exercise_6():
    # 练习6：统计字符
    print("\n--- 练习6：统计字符 ---")
    text = "hello python world"
    char_count = {}
    for char in text:
        if char != " ":  # 忽略空格
            char_count[char] = char_count.get(char, 0) + 1

    print(f"文本：{text}")
    print(f"字符统计：")
    for char, count in sorted(char_count.items()):
        print(f"  '{char}': {count}")


# =============================================
# 主程序入口
# =============================================

if __name__ == "__main__":
    demo_for_loop()
    print()
    demo_range()
    print()
    demo_while_loop()
    print()
    demo_break_continue()
    print()
    demo_enumerate()
    print()
    demo_zip()
    print()
    demo_list_comprehension()

    # 练习参考答案
    print("\n" + "="*50)
    print("练习参考答案")
    print("="*50)

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- for 循环用 range() 控制次数，while 循环用条件控制
- break 立即退出循环，continue 跳过本次迭代
- 列表推导式是 [表达式 for 变量 in 可迭代对象 if 条件] 的简洁写法

常见陷阱：
- for 循环中修改列表会导致意外结果
- while 循环忘记更新条件会死循环
- 列表推导式太复杂时应该改用普通循环

下节课预告：
- 下节课学习闭包和装饰器——函数的"高级玩法"
"""
