# -*- coding: utf-8 -*-
# =============================================
# 第 08 课：闭包与装饰器
# =============================================
# 上节课我们学了循环语句。
# 这节课我们要学习闭包和装饰器——Python 最优雅的"魔法"特性。
#
# 闭包让函数能"记住"状态，装饰器不修改原函数却能给函数添加额外功能。

import time
import functools


# =============================================
# 第一节：函数回顾
# =============================================

# 【函数的基本结构】
# def 函数名(参数):
#     函数体
#     return 返回值
#
# 函数把代码封装成可复用的单元，接收参数、返回结果。
# 详细的函数知识请回顾第 02 课。

def demo_function_review():
    # 简要回顾函数的核心概念

    print("=== 函数回顾 ===")

    # 定义和调用
    def greet(name):
        # 带参数的函数
        return f"你好，{name}！"

    print(greet("小明"))
    print(greet("小红"))

    # 返回多个值
    def min_max(numbers):
        # 返回最小值和最大值
        return min(numbers), max(numbers)

    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    lo, hi = min_max(nums)
    print(f"列表 {nums} 的最小值: {lo}, 最大值: {hi}")

    # lambda 匿名函数
    # 适合一次性的小逻辑
    double = lambda x: x * 2
    print(f"double(5) = {double(5)}")

    add = lambda a, b: a + b
    print(f"add(3, 5) = {add(3, 5)}")


# =============================================
# 第二节：闭包基础
# =============================================

# 【什么是闭包？】
# 闭包 = 内部函数 + 引用了外部函数的变量
#
# 打个比方：
# - 外部函数像一个"工厂"，生产出内部函数
# - 内部函数像一个"背包"，里面装着外部函数留下的变量
# - 即使外部函数已经执行完毕，内部函数依然能使用那些变量
#
# 【为什么要学闭包？】
# 1. 闭包是装饰器的基础，不学闭包后面会一脸懵
# 2. 闭包可以"记住"状态，不用全局变量也能保存数据
# 3. 很多 Python 高级特性都依赖闭包

def demo_closure_basic():
    # 演示最基本的闭包

    print("=== 闭包基础 ===")

    # 最基本的闭包
    def outer():
        # 外部函数
        x = 10  # 这是外部函数的局部变量

        def inner():
            # 内部函数引用了外部函数的变量 x
            # 这就构成了闭包！
            return x

        # 返回内部函数（注意：没有括号，是返回函数本身）
        return inner

    # 调用 outer()，得到的是 inner 函数
    fn = outer()

    # fn 就是 inner，它"记住"了 x = 10
    print(f"闭包调用：{fn()}")  # 输出 10

    # 验证：outer() 已经执行完了，但 x 还活着
    print(f"函数类型：{type(fn)}")
    print(f"闭包变量：{fn.__closure__[0].cell_contents}")


def demo_closure_counter():
    # 用闭包实现计数器——闭包的实际应用

    print("\n=== 闭包实现计数器 ===")

    # 【nonlocal 关键字】
    # 内部函数默认只能"读取"外部变量，不能"修改"
    # 如果要修改，必须用 nonlocal 声明

    def make_counter():
        # 计数器工厂：用闭包实现状态保存
        count = 0

        def counter():
            nonlocal count  # 声明 count 是外部函数的变量
            count += 1
            return count

        return counter

    # 每次调用 make_counter() 都会创建一个新的计数器
    counter = make_counter()
    print(f"计数：{counter()}")  # 1
    print(f"计数：{counter()}")  # 2
    print(f"计数：{counter()}")  # 3

    # 创建另一个独立的计数器（互不影响）
    counter2 = make_counter()
    print(f"计数器2：{counter2()}")  # 1（从头开始）


def demo_closure_factory():
    # 用闭包实现函数工厂

    print("\n=== 闭包作为配置器 ===")

    def multiplier(factor):
        # 乘法器工厂：用闭包"记住"配置参数
        def multiply(x):
            return x * factor  # factor 被"记住"了
        return multiply

    # 用同一个工厂，生产不同的函数
    double = multiplier(2)
    triple = multiplier(3)
    ten_times = multiplier(10)

    print(f"double(5) = {double(5)}")        # 10
    print(f"triple(5) = {triple(5)}")        # 15
    print(f"ten_times(5) = {ten_times(5)}")  # 50


def demo_nonlocal():
    # 演示 nonlocal 的用法和常见错误

    print("\n=== nonlocal 详解 ===")

    # 对比三种变量：
    # 1. 局部变量：在函数内部直接赋值
    # 2. 全局变量：用 global 声明
    # 3. 外部变量：用 nonlocal 声明

    def demo():
        value = "外部原始值"

        def inner():
            # 如果不加 nonlocal，下面的赋值会创建一个新的局部变量 value
            # 加了 nonlocal，才是修改外部函数的 value
            nonlocal value
            value = "被内部函数修改了"

        print(f"修改前：{value}")
        inner()
        print(f"修改后：{value}")

    demo()


# =============================================
# 第三节：lambda 匿名函数
# =============================================

# 【什么是 lambda？】
# lambda 是没有名字的函数，用于简单的、一次性的操作
#
# 【语法】
# lambda 参数: 表达式
#
# 与普通函数的区别：
# 1. lambda 只能写一行表达式
# 2. lambda 自动返回结果，不需要 return
# 3. lambda 没有名字，适合临时使用

def demo_lambda():
    # 演示 lambda 匿名函数的用法

    print("=== lambda 匿名函数 ===")

    # 基本用法：普通函数 vs lambda
    def double(x):
        return x * 2

    double_lambda = lambda x: x * 2

    print(f"double(5) = {double(5)}")
    print(f"double_lambda(5) = {double_lambda(5)}")

    # 多参数
    add = lambda a, b: a + b
    print(f"add(3, 5) = {add(3, 5)}")

    # 实际应用：排序
    students = [("小明", 85), ("小红", 92), ("小刚", 78)]
    students.sort(key=lambda s: s[1])  # 按成绩排序
    print(f"按成绩排序: {students}")


# =============================================
# 第四节：函数作为参数（高阶函数）
# =============================================

# 【什么是高阶函数？】
# 接收函数作为参数，或者返回函数的函数
# map()、filter()、sorted() 都是高阶函数

def demo_higher_order():
    # 演示高阶函数的用法

    print("=== 函数作为参数 ===")

    numbers = [1, 2, 3, 4, 5]

    # map()：对每个元素应用函数
    squared = list(map(lambda x: x**2, numbers))
    print(f"map 平方: {squared}")

    # filter()：过滤元素
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter 偶数: {evens}")

    # sorted()：自定义排序
    words = ["banana", "apple", "cherry"]
    by_length = sorted(words, key=len)
    print(f"按长度排序: {by_length}")


# =============================================
# 第五节：装饰器基础
# =============================================

# 【装饰器的本质】
# 装饰器是一个函数，它接受一个函数作为参数，返回一个新的函数
#
# 【基本语法】
# def 装饰器名(原函数):
#     def 新函数(*args, **kwargs):
#         # 额外功能（前）
#         result = 原函数(*args, **kwargs)
#         # 额外功能（后）
#         return result
#     return 新函数
#
# 【使用方式】
# @装饰器名
# def 被装饰的函数():
#     pass
#
# @语法 等价于：被装饰的函数 = 装饰器名(被装饰的函数)

def demo_decorator_basic():
    # 演示最简单的装饰器

    print("=== 装饰器基础 ===")

    # 最简单的装饰器
    def my_decorator(func):
        def wrapper():
            print("函数执行前")
            func()  # 调用原函数
            print("函数执行后")
        return wrapper

    # 方式1：手动装饰（理解原理）
    def say_hello():
        print("Hello!")

    say_hello = my_decorator(say_hello)
    say_hello()

    print()

    # 方式2：@ 语法（推荐！）
    @my_decorator
    def say_goodbye():
        print("Goodbye!")

    say_goodbye()


def demo_decorator_with_args():
    # 演示装饰带参数的函数

    print("\n=== 装饰带参数的函数 ===")

    # 用 *args 和 **kwargs 接收任意参数
    def log_args(func):
        def wrapper(*args, **kwargs):
            print(f"调用 {func.__name__}，参数：{args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"返回值：{result}")
            return result
        return wrapper

    @log_args
    def add(a, b):
        return a + b

    @log_args
    def greet(name, greeting="你好"):
        return f"{greeting}, {name}!"

    add(3, 5)
    greet("小明", greeting="早上好")


# =============================================
# 第六节：带参数装饰器（装饰器工厂）
# =============================================

# 【问题】
# 装饰器本身也需要参数怎么办？
#
# 【解决】
# 用三层函数：装饰器工厂 → 装饰器 → 包装函数
#
# def 装饰器工厂(参数):        # 第一层：接收装饰器的参数
#     def 装饰器(函数):        # 第二层：接收被装饰的函数
#         def 包装(*args):     # 第三层：实际执行
#             ...
#         return 包装
#     return 装饰器

def demo_decorator_factory():
    # 演示带参数的装饰器

    print("=== 带参数装饰器 ===")

    def repeat(times):
        # 让函数执行多次的装饰器工厂
        def decorator(func):
            def wrapper(*args, **kwargs):
                results = []
                for _ in range(times):
                    result = func(*args, **kwargs)
                    results.append(result)
                return results
            return wrapper
        return decorator

    @repeat(times=3)
    def say_hi(name):
        print(f"Hi, {name}!")
        return f"Hi {name}"

    results = say_hi("小明")
    print(f"结果：{results}")


# =============================================
# 第七节：实用装饰器
# =============================================

# 【实用装饰器】
# timer  - 测量函数执行时间
# cache  - 缓存函数结果
# retry  - 失败自动重试
# log    - 记录函数调用日志

def demo_timer():
    # 计时装饰器——测量函数执行时间

    print("=== 计时装饰器 ===")

    def timer(func):
        # 测量函数执行时间
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} 执行时间：{end - start:.4f}秒")
            return result
        return wrapper

    @timer
    def slow_function():
        time.sleep(0.1)
        return "完成"

    result = slow_function()
    print(f"结果：{result}")


def demo_cache():
    # 缓存装饰器——避免重复计算

    print("\n=== 缓存装饰器 ===")

    def cache(func):
        # 缓存函数结果
        cached_results = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args not in cached_results:
                cached_results[args] = func(*args)
            return cached_results[args]
        return wrapper

    @cache
    def fibonacci(n):
        # 计算斐波那契数列
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    start = time.time()
    result = fibonacci(30)
    end = time.time()
    print(f"fibonacci(30) = {result}")
    print(f"计算时间：{end - start:.4f}秒")


def demo_retry():
    # 重试装饰器——失败自动重试

    print("\n=== 重试装饰器 ===")

    def retry(max_attempts=3, delay=0.1):
        # 重试装饰器工厂
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_error = None
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_error = e
                        print(f"  尝试 {attempt + 1} 失败：{e}")
                        if attempt < max_attempts - 1:
                            time.sleep(delay)
                raise last_error
            return wrapper
        return decorator

    call_count = 0

    @retry(max_attempts=3, delay=0.1)
    def unstable_function():
        # 模拟一个不稳定的函数：前两次失败，第三次成功
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ValueError("随机失败")
        return "成功！"

    try:
        result = unstable_function()
        print(f"结果：{result}")
    except ValueError as e:
        print(f"最终失败：{e}")


def demo_log():
    # 日志装饰器——记录函数调用

    print("\n=== 日志装饰器 ===")

    def log(level="INFO"):
        # 日志装饰器工厂
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{level}] 调用 {func.__name__}")
                result = func(*args, **kwargs)
                print(f"[{level}] {func.__name__} 返回 {result}")
                return result
            return wrapper
        return decorator

    @log(level="DEBUG")
    def calculate(x, y):
        return x + y

    calculate(3, 5)


# =============================================
# 第八节：functools.wraps 保留原函数信息
# =============================================

# 【问题】
# 装饰后，函数的名字和文档会丢失
#
# 【解决】
# 用 @functools.wraps(func) 装饰包装函数
# 它会把原函数的 __name__、__doc__ 等信息复制到包装函数上

def demo_wraps():
    # 演示 functools.wraps 的作用

    print("=== functools.wraps ===")

    # 不用 wraps 的装饰器
    def bad_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    # 用 wraps 的装饰器
    def good_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    @bad_decorator
    def func_a():
        """func_a 的文档"""
        pass

    @good_decorator
    def func_b():
        """func_b 的文档"""
        pass

    print(f"不用 wraps: 函数名={func_a.__name__}, 文档={func_a.__doc__}")
    print(f"使用 wraps: 函数名={func_b.__name__}, 文档={func_b.__doc__}")


# =============================================
# 练习参考答案
# =============================================

def exercise_1():
    # 练习1：基础——写一个 log 装饰器，记录函数调用
    print("--- 练习1：log 装饰器 ---")

    def log_call(func):
        # 记录函数调用的装饰器
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] 调用 {func.__name__}({args}, {kwargs})")
            result = func(*args, **kwargs)
            print(f"[{timestamp}] 返回：{result}")
            return result
        return wrapper

    @log_call
    def multiply(a, b):
        # 乘法
        return a * b

    multiply(3, 5)


def exercise_2():
    # 练习2：应用——写一个 cache 装饰器，缓存函数结果
    print("\n--- 练习2：cache 装饰器 ---")

    def cache(func):
        # 缓存装饰器
        cached = {}

        @functools.wraps(func)
        def wrapper(*args):
            if args not in cached:
                cached[args] = func(*args)
            return cached[args]
        return wrapper

    @cache
    def factorial(n):
        # 计算阶乘
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(f"5! = {factorial(5)}")
    print(f"10! = {factorial(10)}")


def exercise_3():
    # 练习3：进阶——写一个 retry(max_attempts) 带参数装饰器
    print("\n--- 练习3：retry 装饰器 ---")

    def retry(max_attempts=3, delay=0.1):
        # 重试装饰器工厂
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_error = None
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_error = e
                        print(f"  尝试 {attempt + 1} 失败：{e}")
                        if attempt < max_attempts - 1:
                            time.sleep(delay)
                raise last_error
            return wrapper
        return decorator

    call_count = [0]  # 用列表包装，以便在内部函数中修改

    @retry(max_attempts=3, delay=0.1)
    def unreliable_function():
        # 模拟不稳定函数
        call_count[0] += 1
        if call_count[0] < 3:
            raise ValueError("随机失败")
        return "成功！"

    try:
        result = unreliable_function()
        print(f"结果：{result}")
    except ValueError as e:
        print(f"最终失败：{e}")


# =============================================
# 主程序入口
# =============================================

if __name__ == "__main__":
    demo_function_review()
    print()
    demo_closure_basic()
    print()
    demo_closure_counter()
    print()
    demo_closure_factory()
    print()
    demo_nonlocal()
    print()
    demo_lambda()
    print()
    demo_higher_order()
    print()
    demo_decorator_basic()
    print()
    demo_decorator_with_args()
    print()
    demo_decorator_factory()
    print()
    demo_timer()
    print()
    demo_cache()
    print()
    demo_retry()
    print()
    demo_log()
    print()
    demo_wraps()

    # 练习参考答案
    print("\n" + "="*50)
    print("练习参考答案")
    print("="*50)

    exercise_1()
    exercise_2()
    exercise_3()


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- 闭包是内部函数引用外部变量，让函数有了"记忆"
- nonlocal 关键字让内部函数能修改外部变量
- 装饰器是"函数的函数"，用 @ 语法优雅地扩展函数功能

常见陷阱：
- 闭包中修改外部变量必须用 nonlocal，否则会创建新的局部变量
- 装饰器忘记 return 会导致原函数返回 None
- 带参数装饰器是三层嵌套，别搞混了

下节课预告：
- 下节课学习文件操作——让程序读写文件
"""
