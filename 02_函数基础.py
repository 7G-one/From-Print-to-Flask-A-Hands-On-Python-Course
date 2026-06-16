# -*- coding: utf-8 -*-
# =============================================
# 第 02 课：函数基础
# =============================================
# 上节课我们学了变量和数据类型。
# 这节课我们要学习函数——把代码"包起来"的工具。
#
# 学完这节课，你将能够：
# 1. 定义和调用函数
# 2. 使用参数和返回值
# 3. 理解变量作用域

# =============================================
# 第一节：什么是函数
# =============================================

# 【生活中的函数】
# 想象你有一份菜谱："番茄炒蛋"
# - 输入：番茄 2 个、鸡蛋 3 个、盐少许
# - 步骤：打蛋 → 切番茄 → 炒蛋 → 炒番茄 → 合在一起
# - 输出：一盘番茄炒蛋
#
# 函数就是代码世界的"菜谱"！
# - 输入：参数（番茄、鸡蛋）
# - 步骤：函数体（那些操作步骤）
# - 输出：返回值（做好的菜）
#
# 再比如工厂里的机器：
# - 投入原材料（参数）
# - 机器加工（函数体）
# - 吐出成品（返回值）
#
# 【为什么需要函数？】
# 假设你要在程序里 10 次打印"你好，xxx！"
# 没有函数：每次都要写 print("你好，xxx！")，10 行重复代码
# 有函数：写一次 greet("xxx")，调用 10 次就行了
#
# 函数的好处：
# 1. 代码复用——写一次，用多次
# 2. 逻辑清晰——给代码块起个名字，一看就知道干什么
# 3. 易于调试——出问题了，只需要检查函数里的代码

# =============================================
# 第二节：定义函数
# =============================================

# 【定义函数的语法】
#
# def 函数名(参数):
#     函数体
#
# 逐个解释：
# - def：告诉 Python"我要定义一个函数"（define 的缩写）
# - 函数名：给函数起名字（和变量命名规则一样）
# - 参数：函数需要的输入，可以没有（但括号不能省）
# - 冒号 :：表示"接下来是函数体了"
# - 缩进：函数体里的代码必须缩进（通常是 4 个空格）

# ---------- 最简单的函数 ----------

def say_hello():
    # 这个函数没有参数，也没有返回值
    # 它只做一件事：打印一句话
    # 注意：函数体必须缩进！
    print("你好，Python！")


# ---------- 带参数的函数 ----------

def greet(name):
    # 这个函数有一个参数 name
    # 调用时传入名字，它就会打招呼
    print(f"你好，{name}！")


# ---------- 带多个参数的函数 ----------

def introduce(name, age):
    # 这个函数有两个参数：name 和 age
    print(f"我叫{name}，今年{age}岁。")


# ---------- 带返回值的函数 ----------

def add(a, b):
    # 这个函数计算 a + b，并把结果"返回"给调用者
    # return 就是"把结果交出去"
    return a + b


# =============================================
# 第三节：调用函数
# =============================================

# 【调用函数的语法】
#
# 函数名(参数)
#
# 关键点：
# - 函数名后面必须加括号 ()！
# - 不加括号只是"提到"函数，不是"调用"函数
# - 就像你拿着菜谱看（不加括号）vs 真的去做菜（加括号）

print("=== 调用函数 ===")

# 调用无参数函数
say_hello()  # 输出：你好，Python！
say_hello()  # 可以调用多次，每次都会执行

# 调用带参数的函数
greet("小明")   # 输出：你好，小明！
greet("小红")   # 输出：你好，小红！

# 调用带多个参数的函数
introduce("小明", 18)  # 输出：我叫小明，今年18岁。
introduce("小红", 20)  # 输出：我叫小红，今年20岁。

# 调用带返回值的函数
result = add(3, 5)  # add(3, 5) 返回 8，存到 result 里
print(f"3 + 5 = {result}")  # 输出：3 + 5 = 8

# 也可以直接用返回值，不存变量
print(f"10 + 20 = {add(10, 20)}")  # 输出：10 + 20 = 30

# 【常见错误演示】
# 如果只写函数名不加括号：
print(f"\n不加括号会怎样？")
print(f"say_hello 的类型：{type(say_hello)}")
# 输出：<class 'function'>
# Python 会告诉你"这是一个函数"，但不会执行它！
# 就像你拿着菜谱说"这是菜谱"，但没有真的去做菜


# =============================================
# 第四节：参数详解
# =============================================

# 参数是函数的"输入"，让函数更灵活。
# 同一个函数，传入不同的参数，就能做不同的事。

# ---------- 位置参数 ----------
# 最基本的参数类型，按位置顺序传入

print("\n=== 位置参数 ===")

def power(base, exponent):
    # 计算 base 的 exponent 次方
    # base 在第 1 个位置，exponent 在第 2 个位置
    return base ** exponent

# 按位置传参：第 1 个给 base，第 2 个给 exponent
print(f"2 的 10 次方 = {power(2, 10)}")   # 1024
print(f"3 的 3 次方 = {power(3, 3)}")     # 27

# 如果顺序搞反了，结果就错了！
print(f"power(2, 10) = {power(2, 10)}")   # 1024（正确）
print(f"power(10, 2) = {power(10, 2)}")   # 100（10的2次方，不是2的10次方）


# ---------- 默认值 ----------
# 给参数一个"默认值"，调用时可以不传这个参数

print("\n=== 默认值 ===")

def greet_with_title(name, title="同学"):
    # title 有默认值 "同学"
    # 如果调用时不传 title，就用默认值
    print(f"你好，{title}{name}！")

greet_with_title("小明")              # 用默认值：你好，同学小明！
greet_with_title("小明", "老师")      # 传入新值：你好，老师小明！
greet_with_title("小红")              # 用默认值：你好，同学小红！
greet_with_title("小红", "教授")      # 传入新值：你好，教授小红！

# 默认值的好处：常用的值设为默认，特殊情况下才需要传入


# ---------- 关键字参数 ----------
# 调用时用 参数名=值 的方式传参，不用记顺序

print("\n=== 关键字参数 ===")

def create_profile(name, age, city):
    # 创建个人资料
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

# 位置参数：按顺序传
create_profile("小明", 18, "北京")

# 关键字参数：用名字传，顺序无所谓
create_profile(city="上海", name="小红", age=20)

# 位置参数和关键字参数可以混用
# 但位置参数必须在关键字参数前面
create_profile("小刚", age=22, city="广州")

# 【什么时候用关键字参数？】
# 1. 参数多的时候，避免记错顺序
# 2. 提高代码可读性，一看就知道每个值是什么意思


# =============================================
# 第五节：返回值
# =============================================

# return 关键字把函数的计算结果"交出去"
# 调用者可以用变量接收这个结果

print("\n=== 返回值 ===")

# ---------- 基本返回值 ----------

def square(n):
    # 计算 n 的平方，并返回结果
    return n * n

result = square(5)
print(f"5 的平方 = {result}")  # 25

# 返回值可以参与运算
print(f"3 的平方 + 4 的平方 = {square(3) + square(4)}")  # 9 + 16 = 25


# ---------- 返回多个值 ----------

def min_max(numbers):
    # 返回一个列表中的最小值和最大值
    # Python 可以一次返回多个值（本质是返回一个元组）
    return min(numbers), max(numbers)

scores = [85, 92, 78, 95, 88]
lowest, highest = min_max(scores)  # 用两个变量接收
print(f"最低分：{lowest}，最高分：{highest}")  # 最低分：78，最高分：95


# ---------- 没有 return 的函数 ----------

def print_info(name):
    # 这个函数只打印，不返回任何东西
    print(f"名字是：{name}")
    # 没有 return 语句

result = print_info("小明")  # 打印：名字是：小明
print(f"返回值是：{result}")  # 输出：返回值是：None

# 【重要】
# 没有 return 的函数，默认返回 None
# None 是 Python 里表示"没有值"的特殊对象
# 不要把 None 和 0 搞混——0 是数字，None 是"空"


# ---------- return 终止函数 ----------

def check_age(age):
    # return 还有一个作用：立刻结束函数
    if age < 0:
        print("年龄不能是负数！")
        return  # 遇到 return，函数立刻结束，后面的代码不执行

    if age >= 18:
        print(f"年龄 {age}，已成年")
    else:
        print(f"年龄 {age}，未成年")

check_age(20)    # 年龄 20，已成年
check_age(15)    # 年龄 15，未成年
check_age(-1)    # 年龄不能是负数！


# =============================================
# 第六节：变量作用域
# =============================================

# 【什么是作用域？】
# 作用域就是变量"能被看到的范围"
#
# 就像你在家里的说话声：
# - 在自己房间里说话（局部变量）——只有房间里的人能听到
# - 在客厅里说话（全局变量）——整个家都能听到
#
# Python 的规则：
# - 函数内部定义的变量是"局部变量"，只能在函数内使用
# - 函数外部定义的变量是"全局变量"，在哪里都能用

print("\n=== 变量作用域 ===")

# ---------- 局部变量 ----------

def my_function():
    # message 是局部变量，只在这个函数里存在
    message = "我在函数内部"
    print(f"函数内：{message}")

my_function()  # 输出：函数内：我在函数内部

# 如果在函数外访问 message，会报错！
# 取消下面这行的注释会报错：
# print(message)  # NameError: name 'message' is not defined
# 因为 message 只在 my_function 里存在，外面看不到它


# ---------- 全局变量 ----------

# 在函数外面定义的变量是全局变量
greeting = "你好"  # 全局变量

def say_hi():
    # 函数内部可以"读取"全局变量
    print(f"{greeting}，世界！")

say_hi()  # 输出：你好，世界！
print(f"函数外：{greeting}")  # 输出：函数外：你好


# ---------- 局部变量和全局变量同名 ----------

print("\n--- 同名变量演示 ---")

name = "全局的小明"  # 全局变量

def test_scope():
    # 函数内部创建了一个同名的局部变量
    # 这个局部变量和外面的全局变量是两个独立的变量！
    name = "局部的小红"
    print(f"函数内：{name}")  # 输出：局部的小红

test_scope()
print(f"函数外：{name}")  # 输出：全局的小明（全局变量没被影响）


# ---------- 修改全局变量 ----------

print("\n--- 修改全局变量 ---")

count = 0  # 全局变量

def increment():
    # 如果要在函数内部修改全局变量，必须用 global 关键字声明
    global count
    count += 1
    print(f"函数内 count = {count}")

increment()  # 函数内 count = 1
increment()  # 函数内 count = 2
increment()  # 函数内 count = 3
print(f"函数外 count = {count}")  # 函数外 count = 3

# 【建议】
# 尽量少用 global，因为全局变量任何地方都能修改，容易出 bug
# 优先用参数传入、用 return 返回，这样更安全


# =============================================
# 第七节：函数的好处
# =============================================

# ---------- 代码复用 ----------

print("\n=== 代码复用 ===")

# 没有函数：重复代码
print("-" * 30)
print("欢迎来到 Python 世界")
print("-" * 30)

print("-" * 30)
print("今天学习函数")
print("-" * 30)

print("-" * 30)
print("加油！")
print("-" * 30)

# 有函数：写一次，用多次
def print_banner(text):
    # 打印带装饰线的文字
    print("-" * 30)
    print(text)
    print("-" * 30)

print()
print_banner("欢迎来到 Python 世界")
print_banner("今天学习函数")
print_banner("加油！")


# ---------- 逻辑清晰 ----------

print("\n=== 逻辑清晰 ===")

# 没有函数：一堆代码，看不出在干什么
# temperature = 36.5
# if temperature >= 37.5:
#     print("发烧了！")
# elif temperature >= 37.0:
#     print("低烧，注意休息")
# else:
#     print("体温正常")

# 有函数：名字就是注释，一看就懂
def check_temperature(temp):
    # 检查体温是否正常
    if temp >= 37.5:
        print(f"体温 {temp}°C，发烧了！")
    elif temp >= 37.0:
        print(f"体温 {temp}°C，低烧，注意休息")
    else:
        print(f"体温 {temp}°C，体温正常")

check_temperature(36.5)  # 体温正常
check_temperature(37.2)  # 低烧
check_temperature(38.5)  # 发烧


# ---------- 易于调试 ----------

print("\n=== 易于调试 ===")

# 如果程序出了问题，有函数的话：
# 1. 可以单独测试每个函数，找出哪个函数有问题
# 2. 不用从几百行代码里大海捞针
#
# 比如你发现计算结果不对，可以单独测试 add 函数：
def add_debug(a, b):
    # 调试版本：打印输入输出，方便排查问题
    result = a + b
    print(f"  [调试] add({a}, {b}) = {result}")
    return result

print("调试 add 函数：")
add_debug(3, 5)
add_debug(10, 20)
add_debug(-1, 1)


# =============================================
# 第八节：实战项目——计算器函数
# =============================================

# 我们要用函数来做一个简单的计算器
# 这个项目会用到本节课学的所有知识点：
# - 定义函数（def）
# - 参数（位置参数、默认值）
# - 返回值（return）
# - 函数调用

print("\n" + "=" * 50)
print("实战项目：计算器函数")
print("=" * 50)


# ---------- 基础运算函数 ----------

def add(a, b):
    # 加法：返回 a + b
    return a + b


def subtract(a, b):
    # 减法：返回 a - b
    return a - b


def multiply(a, b):
    # 乘法：返回 a * b
    return a * b


def divide(a, b):
    # 除法：返回 a / b
    # 注意：除数不能为 0！
    if b == 0:
        print("错误：除数不能为 0！")
        return None  # 返回 None 表示计算失败
    return a / b


# ---------- 测试基础运算 ----------

print("\n--- 基础运算测试 ---")

x = 10
y = 3

print(f"{x} + {y} = {add(x, y)}")        # 13
print(f"{x} - {y} = {subtract(x, y)}")   # 7
print(f"{x} * {y} = {multiply(x, y)}")   # 30
print(f"{x} / {y} = {divide(x, y):.2f}") # 3.33

# 测试除以零
print(f"{x} / 0 = {divide(x, 0)}")       # None


# ---------- 统一计算函数 ----------

def calculate(a, op, b):
    # 根据运算符调用对应的函数
    # 参数：
    #   a: 第一个数字
    #   op: 运算符（字符串：+、-、*、/）
    #   b: 第二个数字
    # 返回值：计算结果，如果运算符无效返回 None

    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        print(f"错误：不支持的运算符 '{op}'")
        return None


# ---------- 测试统一计算 ----------

print("\n--- 统一计算测试 ---")

# 用不同的运算符调用同一个函数
print(f"calculate(10, '+', 3) = {calculate(10, '+', 3)}")  # 13
print(f"calculate(10, '-', 3) = {calculate(10, '-', 3)}")  # 7
print(f"calculate(10, '*', 3) = {calculate(10, '*', 3)}")  # 30
print(f"calculate(10, '/', 3) = {calculate(10, '/', 3):.2f}")  # 3.33
print(f"calculate(10, '/', 0) = {calculate(10, '/', 0)}")  # None
print(f"calculate(10, '%', 3) = {calculate(10, '%', 3)}")  # None


# ---------- 批量计算 ----------

print("\n--- 批量计算 ---")

# 定义一组计算任务
tasks = [
    (100, "+", 200),
    (50, "-", 30),
    (6, "*", 7),
    (100, "/", 4),
    (10, "/", 0),
]

# 用循环批量执行
for a, op, b in tasks:
    result = calculate(a, op, b)
    if result is not None:
        print(f"  {a} {op} {b} = {result}")
    else:
        print(f"  {a} {op} {b} = 计算失败")


# ---------- 带格式的输出函数 ----------

def print_result(a, op, b):
    # 打印格式化的计算结果
    result = calculate(a, op, b)
    if result is not None:
        # 判断结果是不是整数（没有小数部分）
        if isinstance(result, float) and result == int(result):
            print(f"  {a} {op} {b} = {int(result)}")
        else:
            print(f"  {a} {op} {b} = {result}")
    else:
        print(f"  {a} {op} {b} = 计算失败")


print("\n--- 格式化输出 ---")
print_result(10, "+", 5)    # 10 + 5 = 15
print_result(10, "/", 3)    # 10 / 3 = 3.333...
print_result(10, "/", 2)    # 10 / 2 = 5（不是 5.0）


# ---------- main 函数 ----------

def main():
    # 程序的主入口
    # 把所有演示代码组织在一起

    print("\n" + "=" * 50)
    print("计算器演示")
    print("=" * 50)

    # 演示各种调用方式
    print("\n--- 方式1：直接调用基础函数 ---")
    print(f"  add(100, 200) = {add(100, 200)}")
    print(f"  subtract(100, 200) = {subtract(100, 200)}")

    print("\n--- 方式2：用 calculate 统一调用 ---")
    print(f"  calculate(100, '+', 200) = {calculate(100, '+', 200)}")
    print(f"  calculate(100, '-', 200) = {calculate(100, '-', 200)}")

    print("\n--- 方式3：用 print_result 格式化输出 ---")
    print_result(50, "+", 50)
    print_result(100, "-", 33)
    print_result(12, "*", 12)
    print_result(100, "/", 8)

    print("\n--- 方式4：在表达式中使用返回值 ---")
    # 函数的返回值可以直接参与运算
    total = add(10, 20) + add(30, 40)
    print(f"  add(10,20) + add(30,40) = {total}")  # 100

    # 用返回值做判断
    result = calculate(100, "/", 0)
    if result is None:
        print("  计算失败，可能是除以零了")


# 调用 main 函数，启动程序
main()


# =============================================
# 【练习题】
# =============================================

# 【练习1：基础】
# 写一个 greet(name) 函数，输出"你好，{name}！"
# 然后调用它，传入你自己的名字
# 提示：
#   1. 用 def 定义函数
#   2. 函数体用 print 输出
#   3. 调用时传入一个字符串

# 【练习2：应用】
# 写一个 max_of_three(a, b, c) 函数，返回三个数中的最大值
# 不能用内置的 max() 函数，用 if 语句自己实现
# 提示：
#   1. 先比较 a 和 b，得到较大的那个
#   2. 再用较大的那个和 c 比较
#   3. 用 return 返回最终结果

# 【练习3：进阶】
# 写一个 fibonacci(n) 函数，返回第 n 个斐波那契数
# 斐波那契数列：1, 1, 2, 3, 5, 8, 13, 21, ...
# 规律：第 n 项 = 第 (n-1) 项 + 第 (n-2) 项
# 提示：
#   1. 前两项都是 1（n=1 和 n=2 时返回 1）
#   2. 用循环从第 3 项开始计算
#   3. 每次循环更新"前两项"的值


# =============================================
# 练习参考答案
# =============================================

print("\n" + "=" * 50)
print("练习参考答案")
print("=" * 50 + "\n")


# 练习1 参考
print("--- 练习1 参考 ---")

def greet_exercise(name):
    # 输出问候语
    print(f"你好，{name}！")

greet_exercise("小明")   # 你好，小明！
greet_exercise("Python") # 你好，Python！


# 练习2 参考
print("\n--- 练习2 参考 ---")

def max_of_three(a, b, c):
    # 返回三个数中的最大值
    # 方法：先比较前两个，再和第三个比较
    if a >= b:
        bigger = a
    else:
        bigger = b

    if bigger >= c:
        return bigger
    else:
        return c

print(f"max_of_three(3, 7, 5) = {max_of_three(3, 7, 5)}")   # 7
print(f"max_of_three(10, 2, 8) = {max_of_three(10, 2, 8)}")  # 10
print(f"max_of_three(1, 4, 9) = {max_of_three(1, 4, 9)}")    # 9


# 练习3 参考
print("\n--- 练习3 参考 ---")

def fibonacci(n):
    # 返回第 n 个斐波那契数
    # 第 1 项：1
    # 第 2 项：1
    # 第 n 项 = 第 (n-1) 项 + 第 (n-2) 项

    if n <= 2:
        return 1

    # 用变量记录前两项，避免重复计算
    prev2 = 1  # 第 (i-2) 项
    prev1 = 1  # 第 (i-1) 项

    for i in range(3, n + 1):
        current = prev1 + prev2  # 当前项 = 前两项之和
        prev2 = prev1            # 更新：前两项往后移
        prev1 = current

    return prev1

# 打印前 10 个斐波那契数
print("前 10 个斐波那契数：")
for i in range(1, 11):
    print(f"  第 {i} 项 = {fibonacci(i)}")


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- 函数用 def 定义，用 函数名() 调用
- 参数让函数更灵活，return 让函数有返回值
- 作用域决定变量在哪里能用

常见陷阱：
- 忘记写冒号 : 导致 SyntaxError
- 忘记调用函数（只写函数名不加括号）
- 在函数外访问局部变量会报错

下节课预告：
- 下节课学字符串操作，用函数处理文本
"""
