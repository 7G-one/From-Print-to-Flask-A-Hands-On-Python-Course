# -*- coding: utf-8 -*-
# =============================================
# 第 11 课：异常处理
# =============================================
# 上节课我们学了面向对象编程。
# 这节课我们要学习异常处理——让程序出错时不会直接崩溃。
#
# 用 try-except 捕获错误，用 finally 清理资源，用自定义异常表达业务错误。

# =============================================
# 第一节：什么是异常？
# =============================================

"""
【什么是异常？】
异常就是程序运行时发生的错误
如果不处理，程序会崩溃

【常见的异常类型】

| 异常类型 | 说明 | 示例 |
|---------|------|------|
| ValueError | 值错误 | int("abc") |
| TypeError | 类型错误 | "a" + 1 |
| NameError | 变量未定义 | print(x) |
| IndexError | 索引越界 | [1,2][5] |
| KeyError | 键不存在 | {"a":1}["b"] |
| FileNotFoundError | 文件不存在 | open("xxx.txt") |
| ZeroDivisionError | 除以零 | 10 / 0 |
"""


print("=== 常见异常示例 ===")

# 示例1：除以零
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError：除数不能为零！")

# 示例2：类型转换
try:
    num = int("abc")
except ValueError:
    print("ValueError：无法将 'abc' 转换为整数！")

# 示例3：变量未定义
try:
    print(undefined_variable)
except NameError:
    print("NameError：变量未定义！")

# 示例4：索引越界
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("IndexError：索引超出范围！")

# 示例5：键不存在
try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    print("KeyError：键 'b' 不存在！")


# =============================================
# 第二节：try-except 语句
# =============================================

"""
【try-except 的作用】
尝试执行代码，如果出错就处理

【基本语法】
try:
    可能出错的代码
except 异常类型:
    处理错误的代码
"""


print("\n=== try-except 语句 ===")

# 示例1：处理除以零
try:
    result = 10 / 0
    print(f"结果：{result}")
except ZeroDivisionError:
    print("错误：除数不能为零！")

# 示例2：处理类型转换
try:
    num_str = "42"
    num = int(num_str)
    print(f"转换成功：{num}")
except ValueError:
    print("错误：无法转换为整数！")

# 示例3：处理文件不存在
try:
    with open("不存在的文件.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("错误：文件不存在！")


# =============================================
# 第三节：捕获多种异常
# =============================================

"""
【捕获多种异常】
可以有多个 except 块
"""


print("\n=== 捕获多种异常 ===")

# 示例1：多个 except 块
try:
    num_str = "abc"
    num = int(num_str)
    result = 10 / num
except ValueError:
    print("错误：输入的不是数字！")
except ZeroDivisionError:
    print("错误：除数不能为零！")

# 示例2：一个 except 捕获多种异常
try:
    num_str = "abc"
    num = int(num_str)
    result = 10 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"错误：{e}")

# 示例3：获取异常信息
try:
    num = int("abc")
except ValueError as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常信息：{e}")


# =============================================
# 第四节：else 和 finally
# =============================================

"""
【else】
没有异常时执行

【finally】
无论是否异常都执行
"""


print("\n=== else 和 finally ===")

# 示例1：else
try:
    num = int("42")
except ValueError:
    print("输入无效")
else:
    print(f"转换成功：{num}")  # 只有没有异常时才执行

# 示例2：finally
try:
    num = int("42")
    result = 100 / num
except ValueError:
    print("输入无效")
except ZeroDivisionError:
    print("除数为零")
else:
    print(f"计算成功：{result}")
finally:
    print("finally：总是执行（清理工作）")

# 示例3：实际应用
def read_file(filename):
    """
    安全读取文件

    【参数】
    - filename: 字符串，文件路径

    【返回值】
    字符串，文件内容或错误信息
    """

    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        return "文件不存在"
    finally:
        if f:
            f.close()
            print("文件已关闭")

content = read_file("test.txt")
print(f"文件内容：{content}")


# =============================================
# 第五节：with 语句（推荐方式）
# =============================================

"""
【with 语句】
自动管理资源（自动关闭文件）
比 try-finally 更简洁
"""


print("\n=== with 语句 ===")

# 创建测试文件（使用 tempfile 避免受限目录权限问题）
import tempfile
test_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8')
with test_file as f:
    f.write("Hello, Python!")

# 读取文件（使用 with）
try:
    with open(test_file.name, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"文件内容：{content}")
except FileNotFoundError:
    print("文件不存在")
# 离开 with 块后，文件自动关闭


# =============================================
# 第六节：raise 主动抛出异常
# =============================================

"""
【raise 的作用】
主动抛出异常
用于检查参数是否合法
"""


print("\n=== raise 主动抛出异常 ===")

def divide(a, b):
    """
    除法函数

    【参数】
    - a: 数字，被除数
    - b: 数字，除数

    【返回值】
    数字，a / b

    【异常】
    如果 b == 0，抛出 ValueError
    """

    if b == 0:
        raise ValueError("除数不能为零！")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"捕获异常：{e}")


# =============================================
# 第七节：自定义异常
# =============================================

"""
【自定义异常】
继承 Exception 类
"""


print("\n=== 自定义异常 ===")

class AgeError(Exception):
    """
    年龄错误异常

    【继承自】Exception

    【属性】
    - age: 输入的年龄
    - message: 错误信息
    """

    def __init__(self, age, message="年龄必须在 0-150 之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}，输入的年龄：{self.age}"


def set_age(age):
    """
    设置年龄

    【参数】
    - age: 整数，年龄

    【异常】
    如果年龄不在 0-150 之间，抛出 AgeError
    """

    if not 0 <= age <= 150:
        raise AgeError(age)
    return age

try:
    set_age(200)
except AgeError as e:
    print(f"捕获自定义异常：{e}")


# =============================================
# 第八节：实战案例
# =============================================

print("\n=== 实战案例 ===")


# ========== 案例1：安全除法 ==========
print("\n--- 案例1：安全除法 ---")

def safe_divide(a, b):
    """
    安全除法

    【参数】
    - a: 数字
    - b: 数字

    【返回值】
    数字或错误信息
    """

    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except TypeError:
        return "错误：输入必须是数字"

print(f"10 / 3 = {safe_divide(10, 3)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"'10' / 3 = {safe_divide('10', 3)}")


# ========== 案例2：输入验证 ==========
print("\n--- 案例2：输入验证 ---")

def get_valid_number(prompt):
    """
    获取有效数字

    【参数】
    - prompt: 字符串，提示信息

    【返回值】
    数字

    【逻辑】
    循环询问直到输入有效数字
    """

    while True:
        try:
            # 模拟用户输入
            user_input = "42"  # 实际应用中用 input()
            return int(user_input)
        except ValueError:
            print("输入无效，请输入数字！")

num = get_valid_number("请输入数字：")
print(f"有效数字：{num}")


# ========== 案例3：重试机制 ==========
print("\n--- 案例3：重试机制 ---")

import time

def retry(max_attempts=3, delay=1):
    """
    重试装饰器（装饰器工厂模式）

    【参数】
    - max_attempts: 整数，最大尝试次数
    - delay: 整数，重试间隔（秒）

    【返回值】
    装饰器函数

    【用法】
    @retry(max_attempts=3, delay=1)
    def unstable():
        ...
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"尝试 {attempt + 1} 失败：{e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            raise last_error
        return wrapper
    return decorator

@retry()
def unstable_function():
    """不稳定的函数"""
    import random
    if random.random() < 0.7:
        raise ValueError("随机失败")
    return "成功！"

try:
    result = unstable_function()
    print(f"结果：{result}")
except ValueError as e:
    print(f"最终失败：{e}")




# =============================================
# 【练习题】
# =============================================

# 【练习1：安全除法】
# 编写一个安全的除法函数，处理各种可能的异常情况
# 正常情况返回计算结果，异常情况返回友好的错误信息
# 提示：
#   1. 定义函数 safe_divide(a, b)
#   2. 用 try-except 捕获 ZeroDivisionError（除以零）
#   3. 用 try-except 捕获 TypeError（输入不是数字）
#   4. 测试用例：10/3 正常计算，10/0 捕获除零错误

# 【练习2：邮箱验证】
# 编写一个邮箱验证函数，检查邮箱格式是否正确
# 规则：必须包含 @ 和 .，且 @ 前后都有内容
# 提示：
#   1. 定义函数 validate_email(email)，返回 (是否有效, 提示信息) 的元组
#   2. 用 "if '@' not in email" 检查是否包含 @
#   3. 用 "if '.' not in email" 检查是否包含 .
#   4. 用 email.split("@") 分割后，检查 @ 前后是否都有内容
#   5. 测试用例："test@example.com" 有效，"invalid" 无效

# 【练习3：重试机制】
# 编写一个重试装饰器，让函数失败时自动重试
# 如果函数抛出异常，则重试指定次数，直到成功或用完重试次数
# 提示：
#   1. 定义装饰器函数 retry(func, max_attempts=3)
#   2. 内部定义 wrapper 函数，用 for 循环尝试最多 max_attempts 次
#   3. 每次尝试用 try-except 捕获异常，失败时记录错误并继续
#   4. 如果所有尝试都失败，用 raise 抛出最后一次的异常
#   5. 用 @retry 语法装饰一个不稳定的函数进行测试

# =============================================
# 练习参考答案
# =============================================
print("\n" + "="*50)
print("练习参考答案")
print("="*50 + "\n")

# 练习1 参考
print("--- 练习1 参考 ---")

def safe_divide2(a, b):
    """
    安全除法

    【参数】
    - a: 数字
    - b: 数字

    【返回值】
    数字或错误信息
    """

    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except TypeError:
        return "错误：输入必须是数字"

print(f"10 / 3 = {safe_divide2(10, 3)}")
print(f"10 / 0 = {safe_divide2(10, 0)}")


# 练习2：邮箱验证
print("\n--- 练习2 参考 ---")

def validate_email(email):
    """
    验证邮箱

    【参数】
    - email: 字符串，邮箱地址

    【返回值】
    布尔值，是否有效

    【逻辑】
    检查是否包含 @ 和 .
    """

    if "@" not in email:
        return False, "邮箱必须包含 @"
    if "." not in email:
        return False, "邮箱必须包含 ."

    parts = email.split("@")
    if len(parts) != 2:
        return False, "邮箱格式不正确"

    if not parts[0] or not parts[1]:
        return False, "邮箱格式不正确"

    return True, "邮箱有效"

emails = ["test@example.com", "invalid", "user@domain.org"]
for email in emails:
    is_valid, message = validate_email(email)
    print(f"'{email}': {message}")


# 练习3：重试机制
print("\n--- 练习3 参考 ---")

def retry(max_attempts=3):
    """
    重试装饰器（装饰器工厂模式）

    【参数】
    - max_attempts: 整数，最大尝试次数

    【返回值】
    装饰器函数
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    print(f"尝试 {attempt + 1} 失败：{e}")
            raise last_error
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable():
    """不稳定的函数"""
    import random
    if random.random() < 0.5:
        raise ValueError("随机失败")
    return "成功！"

try:
    result = unstable()
    print(f"结果：{result}")
except ValueError as e:
    print(f"最终失败：{e}")


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- try-except 捕获异常，else 在无异常时执行，finally 无论如何都执行
- raise 主动抛出异常，自定义异常类让错误信息更贴近业务语义
- with 语句自动管理资源，是 try-finally 的优雅替代

常见陷阱：
- 裸 except: 捕获所有异常（包括 KeyboardInterrupt），会隐藏真正的 bug
- 在 except 里写 pass 忽略错误，问题会悄悄积累，早晚爆炸
- 用异常做流程控制（如用 KeyError 判断键是否存在）比 if 判断慢得多

下节课预告：
- 下节课学模块与包，把代码组织成可复用的"工具箱"
"""
