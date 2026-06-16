# -*- coding: utf-8 -*-
# =============================================
# 第 13 课：生成器与迭代器
# =============================================
# 上节课我们学了装饰器。
# 这节课我们要学习生成器——用 yield 实现"按需生成"。
#
# 生成器不一次性创建所有数据，用到哪个才生成哪个，处理大数据不吃内存。

import sys
import time

# =============================================
# 第一节：什么是生成器？
# =============================================

"""
【生成器的作用】
1. 惰性生成值：用到时才计算
2. 节省内存：不一次性存储所有值
3. 保持状态：记住上次执行的位置

【生成器的两种创建方式】
1. 生成器函数（使用 yield）
2. 生成器表达式（类似列表推导式）
"""


print("=== 什么是生成器 ===")


# =============================================
# 第二节：迭代器协议
# =============================================

"""
【迭代器协议】
迭代器是生成器的底层原理，理解它才能真正理解 yield。

迭代器是一个能记住"当前位置"的对象：
- 每次调用 next()，返回下一个值，然后位置后移
- 就像翻书：每次翻一页，记住读到哪里了

任何实现了 __iter__() 和 __next__() 的对象都是迭代器：
- __iter__() 返回迭代器自身（让 for 循环能用）
- __next__() 返回下一个值，没有更多元素时抛出 StopIteration
"""


print("\n=== 迭代器协议 ===")


# ========== 手动实现一个迭代器 ==========

class CountDown:
    """
    倒计时迭代器

    【作用】
    演示迭代器协议的两个核心方法：
    - __iter__(): 返回自身
    - __next__(): 返回下一个值，到 0 时停止
    """

    def __init__(self, start):
        """
        初始化

        【参数】
        - start: 整数，从哪个数开始倒计时
        """
        self.current = start

    def __iter__(self):
        """
        返回迭代器自身

        【作用】
        for 循环会先调用 __iter__() 获取迭代器
        返回 self 就表示"我自己就是迭代器"
        """
        return self

    def __next__(self):
        """
        返回下一个值

        【逻辑】
        1. 如果 current <= 0，没有更多值了，抛出 StopIteration
        2. 否则 current 减 1，返回减之前的值

        【StopIteration】
        这是迭代器的"结束信号"
        for 循环捕获到它就知道遍历结束了
        """
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


# 使用：for 循环自动调用 __iter__() 和 __next__()
print("倒计时：")
for num in CountDown(5):
    print(f"  {num}")


# ========== for 循环的本质 ==========

"""
【for 循环的本质】
for 循环并不是魔法，它的底层逻辑是：

    iterator = iter(iterable)    # 调用 __iter__()
    while True:
        try:
            item = next(iterator)  # 调用 __next__()
        except StopIteration:      # 没有更多值了
            break
        # 循环体 ...

手动模拟 for 循环：
"""

print("\n手动模拟 for 循环：")
cd = CountDown(3)
iterator = iter(cd)       # 等价于 cd.__iter__()
while True:
    try:
        item = next(iterator)  # 等价于 iterator.__next__()
    except StopIteration:
        break
    print(f"  手动取出：{item}")


# ========== 生成器就是迭代器 ==========

"""
【生成器就是迭代器】
生成器函数用 yield 创建的对象，自动实现了 __iter__() 和 __next__()。
所以生成器可以直接用 for 循环遍历，也可以用 next() 取值。

生成器帮你省去了手写 __iter__ 和 __next__ 的麻烦，
只需要用 yield 标记"在哪里暂停、返回什么值"就行了。
"""

def simple_gen():
    """一个简单的生成器，自动实现迭代器协议"""
    yield 1
    yield 2
    yield 3

g = simple_gen()
print(f"\n生成器有 __iter__：{hasattr(g, '__iter__')}")
print(f"生成器有 __next__：{hasattr(g, '__next__')}")
print(f"iter(g) 就是 g：{iter(g) is g}")

# 用 next() 逐个取值，和 CountDown 一样
print(f"next(g)：{next(g)}")
print(f"next(g)：{next(g)}")
print(f"next(g)：{next(g)}")

# 下面这行会抛出 StopIteration，因为值已经取完了
# print(next(g))  # 取消注释会报错


# =============================================
# 第三节：生成器函数（yield）
# =============================================

"""
【yield 是什么？】
yield 就像"暂停"按钮
函数执行到 yield 时会暂停，返回值
下次调用时，从暂停的地方继续

【对比普通函数】
- 普通函数：执行完所有代码，返回一个值
- 生成器函数：每次 yield 一个值，暂停，下次继续
"""


print("\n=== 生成器函数 ===")


# ========== 普通函数 vs 生成器函数 ==========

def normal_function():
    """
    普通函数

    【返回值】
    列表，包含所有值
    """

    return [1, 2, 3, 4, 5]


def generator_function():
    """
    生成器函数

    【yield】
    暂停，返回值，下次继续

    【返回值】
    生成器对象
    """

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# 普通函数返回列表
result = normal_function()
print(f"普通函数：{result}")
print(f"类型：{type(result)}")

# 生成器函数返回生成器对象
gen = generator_function()
print(f"\n生成器：{gen}")
print(f"类型：{type(gen)}")

# 使用 next() 获取值
print(f"\nnext：{next(gen)}")  # 1
print(f"next：{next(gen)}")  # 2
print(f"next：{next(gen)}")  # 3

# 使用 for 循环遍历
print("\nfor 循环遍历：")
gen = generator_function()
for value in gen:
    print(f"  {value}")


# =============================================
# 第四节：yield 的工作原理
# =============================================

"""
【yield 的工作原理】
1. 函数执行到 yield 时暂停
2. 返回 yield 后面的值
3. 保存函数的状态
4. 下次调用时，从暂停的地方继续

【比喻】
就像看书：
- 看到第 10 页，夹个书签（yield）
- 合上书（暂停）
- 下次打开，从第 11 页继续
"""


print("\n=== yield 的工作原理 ===")


def countdown(n):
    """
    倒计时生成器

    【参数】
    - n: 整数，起始数字

    【yield】
    每次返回当前数字，然后暂停
    """

    print("开始倒计时...")
    while n > 0:
        yield n  # 暂停，返回值，保存状态
        n -= 1
        print(f"继续执行，n={n}")
    print("倒计时结束！")


# 创建生成器（不执行代码）
gen = countdown(5)
print("生成器已创建")

# 第一次调用 next() 开始执行
print("\n第一次 next()：")
value = next(gen)
print(f"得到值：{value}")

print("\n第二次 next()：")
value = next(gen)
print(f"得到值：{value}")

print("\n第三次 next()：")
value = next(gen)
print(f"得到值：{value}")


# =============================================
# 第五节：生成器的优势：节省内存
# =============================================

"""
【生成器的优势】
生成器只在需要时才生成值
处理大数据时非常有用！

【对比】
- 列表：一次性生成所有值，占用内存
- 生成器：按需生成，节省内存
"""


print("\n=== 内存对比 ===")


# 列表：存储所有值
def get_list(n):
    """返回列表"""
    return list(range(n))


# 生成器：不存储值
def get_generator(n):
    """返回生成器"""
    for i in range(n):
        yield i


# 内存对比
n = 1000000

list_result = get_list(n)
gen_result = get_generator(n)

print(f"列表大小：{sys.getsizeof(list_result) / 1024 / 1024:.2f} MB")
print(f"生成器大小：{sys.getsizeof(gen_result)} 字节")

# 生成器只在需要时才生成值
# 处理大数据时非常有用！


# =============================================
# 第六节：生成器表达式
# =============================================

"""
【生成器表达式】
类似列表推导式，但用小括号 ()

【对比】
- 列表推导式：[表达式 for 变量 in 可迭代对象]
- 生成器表达式：(表达式 for 变量 in 可迭代对象)
"""


print("\n=== 生成器表达式 ===")


# 列表推导式：一次性生成所有值
squares_list = [x**2 for x in range(10)]
print(f"列表推导式：{squares_list}")
print(f"类型：{type(squares_list)}")

# 生成器表达式：惰性生成值
squares_gen = (x**2 for x in range(10))
print(f"\n生成器表达式：{squares_gen}")
print(f"类型：{type(squares_gen)}")

# 转换为列表查看内容
print(f"转为列表：{list(squares_gen)}")

# 生成器表达式在 sum()、max() 等函数中很有用
total = sum(x**2 for x in range(1000000))
print(f"\n1到1000000的平方和：{total}")


# =============================================
# 第七节：生成器的实际应用
# =============================================

"""
【实际应用场景】
1. 读取大文件
2. 无限序列
3. 斐波那契数列
4. 数据流处理
"""


print("\n=== 实际应用 ===")


# ========== 1. 读取大文件 ==========
def read_large_file(file_path):
    """
    逐行读取大文件

    【参数】
    - file_path: 字符串，文件路径

    【返回值】
    生成器，每次 yield 一行

    【优势】
    不一次性加载整个文件到内存
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()


# ========== 2. 无限序列 ==========
def infinite_counter(start=0):
    """
    无限计数器

    【参数】
    - start: 整数，起始数字

    【返回值】
    生成器，无限生成数字

    【注意】
    无限序列不能直接转为列表！
    """

    n = start
    while True:
        yield n
        n += 1


# 使用 take 获取前 N 个
def take(n, generator):
    """
    从生成器取前 n 个值

    【参数】
    - n: 整数，取几个
    - generator: 生成器

    【返回值】
    生成器，前 n 个值
    """

    for _ in range(n):
        yield next(generator)


counter = infinite_counter(1)
first_ten = list(take(10, counter))
print(f"前10个数：{first_ten}")


# ========== 3. 斐波那契数列 ==========
def fibonacci():
    """
    无限斐波那契数列

    【返回值】
    生成器，无限生成斐波那契数
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# 取前20个
fib = fibonacci()
first_20 = list(take(20, fib))
print(f"斐波那契前20：{first_20}")


# =============================================
# 第八节：yield from（委派生成器）
# =============================================

"""
【yield from 的作用】
将迭代操作委派给另一个生成器

【比喻】
就像经理把任务分配给员工
"""


print("\n=== yield from ===")


# 链接多个可迭代对象
def chain(*iterables):
    """
    链接多个可迭代对象

    【参数】
    - *iterables: 任意个可迭代对象

    【返回值】
    生成器，所有元素
    """

    for iterable in iterables:
        yield from iterable  # 委派给子生成器


result = list(chain([1, 2], [3, 4], [5, 6]))
print(f"链接结果：{result}")


# 递归生成器
def flatten(nested):
    """
    展平嵌套列表

    【参数】
    - nested: 嵌套列表

    【返回值】
    生成器，所有元素
    """

    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)  # 递归展平
        else:
            yield item


nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"展平结果：{list(flatten(nested))}")


# =============================================
# 第九节：itertools 标准库
# =============================================

"""
【itertools 模块】
提供了很多有用的迭代器工具
"""


print("\n=== itertools ===")

import itertools

# 无限迭代器
print("count：", list(itertools.islice(itertools.count(10), 5)))
print("cycle：", list(itertools.islice(itertools.cycle([1, 2, 3]), 7)))
print("repeat：", list(itertools.repeat("hello", 3)))

# 组合迭代器
print("chain：", list(itertools.chain([1, 2], [3, 4])))
print("islice：", list(itertools.islice(range(10), 2, 7, 2)))

# 组合数学
print("product：", list(itertools.product("AB", "12")))
print("permutations：", list(itertools.permutations("ABC", 2)))
print("combinations：", list(itertools.combinations("ABC", 2)))


# =============================================
# 【练习题】
# =============================================
# 先看题目，自己写代码，再看参考答案！

# 【练习1：基础生成器——偶数序列】
# 题目描述：编写一个生成器函数 even_numbers(n)，用 yield 逐个生成
#          前 n 个偶数（0, 2, 4, ...），然后用 list() 转为列表打印。
# 提示：
#   - 生成器函数用 def + yield，不是 return
#   - for i in range(n) 循环 n 次，每次 yield i * 2
#   - list(生成器) 可以把所有值收集到列表中

# 【练习2：无限生成器——2的幂次】
# 题目描述：编写一个无限生成器 powers_of_two()，依次生成 2 的幂次
#          （1, 2, 4, 8, 16, ...），用 while True + yield 实现。
#          然后配合 take(n, gen) 函数取出前 8 个值。
# 提示：
#   - 无限生成器用 while True 循环，不会自动停止
#   - 用变量 n=1 开始，每次 yield n 后 n *= 2
#   - 前面课程中定义了 take(n, generator) 函数可复用

# 【练习3：文件处理生成器】
# 题目描述：创建一个测试文件 numbers.txt（内容为 1~10 每行一个数字），
#          编写生成器函数 read_numbers(filename) 逐行读取并转为整数，
#          最后用 sum() 计算总和。读取完成后清理测试文件。
# 提示：
#   - with open(filename, "r") as f 打开文件
#   - for line in f 逐行迭代，line.strip() 去换行符，int() 转整数
#   - yield 每行的整数值
#   - os.makedirs("test_files", exist_ok=True) 创建目录
#   - shutil.rmtree("test_files", ignore_errors=True) 清理目录

# 【练习4：生成器管道】
# 题目描述：构建一个生成器管道，包含三个环节：
#          numbers(n) 生成 0~n-1 的数字 -> squared() 求平方 ->
#          even_only() 过滤出偶数。将三个生成器串联起来，
#          对 0~9 的数字执行管道，打印最终结果。
# 提示：
#   - 每个环节都是一个生成器函数，接收上一个生成器作为参数
#   - numbers(n) 用 for i in range(n) yield i
#   - squared(nums) 用 for n in nums yield n**2
#   - even_only(nums) 用 for n in nums if n%2==0 yield n
#   - 管道组合：even_only(squared(numbers(10)))

# 【练习5：递归展平生成器】
# 题目描述：编写一个递归生成器 flatten_deep(nested)，将任意深度的
#          嵌套列表展平为一维序列。用 yield from 实现递归委派。
#          测试数据：[1, [2, [3, 4]], [5, [6, [7, 8]]]]
# 提示：
#   - for item in nested 遍历每个元素
#   - isinstance(item, (list, tuple)) 判断是否为嵌套
#   - 如果是嵌套：yield from flatten_deep(item) 递归展平
#   - 如果不是嵌套：yield item 直接返回

# =============================================
# 练习参考答案
# =============================================

print("\n" + "="*50)
print("练习参考答案")
print("="*50 + "\n")

# 练习1：基础生成器
print("--- 练习1 参考 ---")

def even_numbers(n):
    """
    生成前 n 个偶数

    【参数】
    - n: 整数，生成几个

    【返回值】
    生成器，前 n 个偶数
    """

    for i in range(n):
        yield i * 2


print(f"前10个偶数：{list(even_numbers(10))}")


# 练习2：无限生成器
print("\n--- 练习2 参考 ---")

def powers_of_two():
    """
    生成 2 的幂次

    【返回值】
    生成器，2 的幂次
    """

    n = 1
    while True:
        yield n
        n *= 2


print(f"前8个2的幂：{list(take(8, powers_of_two()))}")


# 练习3：文件处理生成器
print("\n--- 练习3 参考 ---")

import os

# 创建测试文件
os.makedirs("test_files", exist_ok=True)
with open("test_files/numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i}\n")


def read_numbers(filename):
    """
    逐行读取数字

    【参数】
    - filename: 字符串，文件路径

    【返回值】
    生成器，每行的数字
    """

    with open(filename, "r") as f:
        for line in f:
            yield int(line.strip())


total = sum(read_numbers("test_files/numbers.txt"))
print(f"数字总和：{total}")

# 清理
import shutil
shutil.rmtree("test_files", ignore_errors=True)


# 练习4：生成器管道
print("\n--- 练习4 参考 ---")

def numbers(n):
    """生成数字"""
    for i in range(n):
        yield i


def squared(numbers):
    """平方"""
    for n in numbers:
        yield n ** 2


def even_only(numbers):
    """过滤偶数"""
    for n in numbers:
        if n % 2 == 0:
            yield n


# 管道：numbers -> squared -> even_only
pipeline = even_only(squared(numbers(10)))
print(f"管道结果：{list(pipeline)}")


# 练习5：展平生成器
print("\n--- 练习5 参考 ---")

def flatten_deep(nested):
    """
    递归展平嵌套列表

    【参数】
    - nested: 嵌套列表

    【返回值】
    生成器，所有元素
    """

    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten_deep(item)
        else:
            yield item


nested = [1, [2, [3, 4]], [5, [6, [7, 8]]]]
print(f"展平：{list(flatten_deep(nested))}")


# =============================================
# 【教授的话】
# =============================================

# =============================================
# 课程总结
# =============================================
"""
核心收获：
- 迭代器协议：__iter__() 返回自身，__next__() 返回下一个值或抛出 StopIteration
- for 循环的本质就是 iter() + next() + StopIteration 的组合
- 生成器函数用 yield 逐个返回值，每次 next() 执行到下一个 yield 就暂停
- 生成器自动实现了迭代器协议，省去了手写 __iter__ 和 __next__ 的麻烦
- 生成器表达式 (x**2 for x in range(10)) 是列表推导式的"懒惰版"，不占内存
- yield from 可以委托子生成器，itertools 模块提供了大量高效迭代工具

常见陷阱：
- 生成器只能遍历一次：遍历完就"空了"，想重复使用要重新创建
- 生成器是惰性的：不调用 next() 就不会执行，调试时看不到中间过程
- 在生成器里 return 会抛出 StopIteration，不是返回值，想返回值用 yield

下节课预告：
- 下节课进入开发实战，学习如何把学到的语法组合起来做真实项目
"""
