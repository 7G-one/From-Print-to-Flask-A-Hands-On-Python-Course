# -*- coding: utf-8 -*-
# =============================================
# 第 03 课：字符串操作
# =============================================
# 上节课我们学了运算符和表达式。
# 这节课我们要学习字符串操作——处理文字的核心技能。
#
# 字符串是编程中最常用的数据类型，几乎每个程序都会用到。
# 比如：用户输入的名字、网页上的文字、文件里的内容……全都是字符串。
# 学好字符串操作，是写 Python 程序的基本功。


# =============================================
# 第一节：什么是字符串？
# =============================================

def demo_string_basics():
    # 字符串就像一串珠子：
    # - 每颗珠子是一个字符（字母、数字、符号）
    # - 珠子串在一起形成一串
    # - 你可以数珠子、找珠子、替换珠子

    # 用引号包起来：单引号 ' ' 或双引号 " "
    name1 = '小明'
    name2 = "小红"
    print("=== 字符串基础 ===")
    print("单引号：", name1)
    print("双引号：", name2)

    # 如果字符串里有单引号，就用双引号包起来
    text1 = "It's a dog"
    # 如果字符串里有双引号，就用单引号包起来
    text2 = 'He said "hello"'
    print(f"含单引号的字符串：{text1}")
    print(f'含双引号的字符串：{text2}')

    # 多行字符串：用三个引号（单引号或双引号）
    text3 = '''这是
一个多行
字符串'''
    text4 = """这也是
一个多行
字符串"""
    print("多行字符串（三单引号）：")
    print(text3)
    print("多行字符串（三双引号）：")
    print(text4)


# =============================================
# 第二节：字符串的长度
# =============================================

def demo_string_length():
    # 使用 len() 函数获取字符串长度
    # len() 会告诉你字符串里有多少个字符

    print("\n=== 字符串的长度 ===")

    text = "Hello Python"
    print(f"字符串：{text}")
    print(f"长度：{len(text)}")  # 12（包含空格，空格也算一个字符）

    name = "小明"
    print(f"名字：{name}，长度：{len(name)}")  # 2

    # 空字符串：一个字符都没有，长度为 0
    empty = ""
    print(f"空字符串：'{empty}'，长度：{len(empty)}")  # 0

    # 只有一个空格的字符串：长度为 1
    # 注意！空格也是一个字符
    space = " "
    print(f"空格：'{space}'，长度：{len(space)}")  # 1


# =============================================
# 第三节：字符串索引（找位置）
# =============================================

def demo_string_index():
    # 索引就是"位置编号"
    # 就像排队时的号码牌——每个人都有一个号码
    #
    # 重要规则：Python 的索引从 0 开始！不是从 1 开始！
    # 第一个字符的索引是 0，第二个是 1，以此类推...

    print("\n=== 字符串索引 ===")

    text = "Python"
    print(f"字符串：{text}")
    print(f"长度：{len(text)}")

    # 正向索引（从左到右，从 0 开始）
    # P  y  t  h  o  n
    # 0  1  2  3  4  5   <- 正向索引
    print(f"\n正向索引：")
    print(f"text[0] = '{text[0]}'")  # P（第1个字符）
    print(f"text[1] = '{text[1]}'")  # y（第2个字符）
    print(f"text[2] = '{text[2]}'")  # t（第3个字符）
    print(f"text[3] = '{text[3]}'")  # h（第4个字符）
    print(f"text[4] = '{text[4]}'")  # o（第5个字符）
    print(f"text[5] = '{text[5]}'")  # n（第6个字符）

    # 反向索引（从右到左，从 -1 开始）
    # P   y   t   h   o   n
    # -6 -5  -4  -3  -2  -1  <- 反向索引
    print(f"\n反向索引：")
    print(f"text[-1] = '{text[-1]}'")  # n（最后一个字符）
    print(f"text[-2] = '{text[-2]}'")  # o（倒数第2个）
    print(f"text[-3] = '{text[-3]}'")  # h（倒数第3个）
    print(f"text[-4] = '{text[-4]}'")  # t（倒数第4个）
    print(f"text[-5] = '{text[-5]}'")  # y（倒数第5个）
    print(f"text[-6] = '{text[-6]}'")  # P（倒数第6个，也就是第1个）

    # 索引图总结：
    # 正向：  0   1   2   3   4   5
    #         P   y   t   h   o   n
    # 反向： -6  -5  -4  -3  -2  -1

    # 索引超出范围会报错！
    # text[6]   -> IndexError，因为只有索引 0 到 5
    # text[-7]  -> IndexError，因为只有索引 -1 到 -6
    # 试试取消下面两行的注释，看看报错信息：
    # print(text[6])
    # print(text[-7])


# =============================================
# 第四节：字符串切片（截取一部分）
# =============================================

def demo_string_slice():
    # 切片就是"截取字符串的一部分"
    # 就像切蛋糕——切出你想要的那一块
    #
    # 切片语法：字符串[开始:结束]
    # 重要规则：包含"开始"位置，不包含"结束"位置（左闭右开）

    print("\n=== 字符串切片 ===")

    text = "Hello Python"
    print(f"字符串：{text}")
    print(f"索引：   0  1  2  3  4  5  6  7  8  9  10 11")
    print(f"字符：   H  e  l  l  o     P  y  t  h  o  n")

    # 基本切片
    # text[0:5] -> 取索引 0, 1, 2, 3, 4（不含索引 5）
    print(f"\ntext[0:5]  = '{text[0:5]}'")    # Hello
    # text[6:12] -> 取索引 6, 7, 8, 9, 10, 11（不含索引 12）
    print(f"text[6:12] = '{text[6:12]}'")     # Python

    # 省略开始或结束
    # 省略开始 -> 从头开始
    print(f"\ntext[:5]  = '{text[:5]}'")      # Hello（从开头到索引 4）
    # 省略结束 -> 到末尾结束
    print(f"text[6:]  = '{text[6:]}'")        # Python（从索引 6 到末尾）
    # 都省略 -> 完整复制
    print(f"text[:]   = '{text[:]}'")         # Hello Python（完整复制）

    # 带步长的切片
    # 语法：字符串[开始:结束:步长]
    # 步长 = 每次跳几个字符
    print(f"\ntext[::2]   = '{text[::2]}'")   # HloPto（每隔1个取1个）
    print(f"text[::3]   = '{text[::3]}'")     # Hl yh（每隔2个取1个）

    # 反转字符串
    # 步长为 -1 表示从右往左取，效果就是反转
    print(f"\ntext[::-1]  = '{text[::-1]}'")   # nohtyP olleH（反转！）

    # 切片图示：
    #  H  e  l  l  o     P  y  t  h  o  n
    #  0  1  2  3  4  5  6  7  8  9 10 11
    #  |<- text[0:5] ->|  |<- text[6:12] ->|


# =============================================
# 第五节：字符串方法（常用操作）
# =============================================

def demo_string_methods():
    # 方法就是"字符串能做的事情"
    # 就像人能走路、说话、吃饭一样
    # 字符串也能做很多事情：变大写、找内容、去掉空格……
    # 调用方法的语法：字符串.方法名()

    print("\n=== 字符串方法 ===")

    # --- 去除空白 ---
    # strip()  - 去掉两边的空白
    # lstrip() - 只去掉左边的空白
    # rstrip() - 只去掉右边的空白
    # "空白"包括：空格、制表符(\t)、换行符(\n)
    text = "  Hello Python World  "
    print(f"原字符串：'{text}'")
    print(f"strip()  ：'{text.strip()}'")     # 去掉两边空格
    print(f"lstrip() ：'{text.lstrip()}'")    # 只去左边空格
    print(f"rstrip() ：'{text.rstrip()}'")    # 只去右边空格
    # 为什么要去空白？
    # 用户输入的内容经常带多余的空格
    # 比如用户输入 "  小明  "，实际想要的是 "小明"
    # 所以处理输入时，strip() 是标配操作

    # --- 大小写转换 ---
    text = "Hello Python"
    print(f"\n原字符串：{text}")
    print(f"upper()      ：{text.upper()}")        # HELLO PYTHON（全部大写）
    print(f"lower()      ：{text.lower()}")        # hello python（全部小写）
    print(f"title()      ：{text.title()}")        # Hello Python（每个单词首字母大写）
    print(f"capitalize() ：{text.capitalize()}")   # Hello python（只有句首大写）
    # 实际用途：比较用户输入时，不区分大小写
    # if user_input.lower() == "yes":
    #     print("用户确认了")

    # --- 查找和替换 ---
    text = "Hello Python World"
    print(f"\n原字符串：{text}")
    # find() 查找子字符串，返回第一次出现的位置
    pos = text.find("Python")
    print(f"find('Python')  = {pos}")     # 6（从索引 6 开始）
    # 找不到返回 -1
    pos = text.find("Java")
    print(f"find('Java')    = {pos}")     # -1（找不到）
    # replace() 替换子字符串（返回新字符串，不修改原字符串）
    new_text = text.replace("Python", "Java")
    print(f"replace 后：{new_text}")       # Hello Java World
    # count() 统计出现次数
    text2 = "Hello Hello Hello"
    count = text2.count("Hello")
    print(f"\n'{text2}' 中 'Hello' 出现 {count} 次")

    # --- 判断方法（返回 True 或 False） ---
    text = "Hello123"
    print(f"\n原字符串：{text}")
    print(f"isalpha()            ：{text.isalpha()}")      # False（是否全是字母）
    print(f"isdigit()            ：{text.isdigit()}")      # False（是否全是数字）
    print(f"isalnum()            ：{text.isalnum()}")      # True（是否全是字母或数字）
    print(f"startswith('Hello')  ：{text.startswith('Hello')}")  # True
    print(f"endswith('123')      ：{text.endswith('123')}")      # True
    print(f"\n'abc'.isalpha()      ：{'abc'.isalpha()}")       # True
    print(f"'123'.isdigit()       ：{'123'.isdigit()}")        # True
    print(f"''.isalpha()          ：{''.isalpha()}")           # False（空字符串）


# =============================================
# 第六节：字符串分割和合并
# =============================================

def demo_string_split_join():
    print("\n=== 分割和合并 ===")

    # 分割：split()
    # 把字符串按指定的分隔符拆开，得到一个列表
    # 语法：字符串.split(分隔符)

    # 用逗号分割
    text = "苹果,香蕉,橘子,葡萄"
    fruits = text.split(",")
    print(f"原字符串：{text}")
    print(f"分割后：{fruits}")       # ['苹果', '香蕉', '橘子', '葡萄']
    print(f"分割后有 {len(fruits)} 个元素")

    # 用空格分割（不传参数默认按空格、制表符、换行符分割）
    text = "Hello Python World"
    words = text.split()
    print(f"\n原字符串：{text}")
    print(f"分割后：{words}")       # ['Hello', 'Python', 'World']

    # 用指定的分隔符分割
    data = "2024-01-15"
    parts = data.split("-")
    print(f"\n日期字符串：{data}")
    print(f"分割后：{parts}")       # ['2024', '01', '15']
    print(f"年：{parts[0]}，月：{parts[1]}，日：{parts[2]}")

    # 合并：join()
    # 把列表里的字符串用指定的分隔符连起来
    # 语法：分隔符.join(列表)
    fruits = ["苹果", "香蕉", "橘子", "葡萄"]
    result = ",".join(fruits)
    print(f"\n列表：{fruits}")
    print(f"用逗号合并：{result}")          # 苹果,香蕉,橘子,葡萄
    result = " | ".join(fruits)
    print(f"用竖线合并：{result}")          # 苹果 | 香蕉 | 橘子 | 葡萄
    result = "".join(fruits)
    print(f"直接合并：{result}")            # 苹果香蕉橘子葡萄
    # split 和 join 是一对反操作：
    # split 把字符串拆成列表
    # join 把列表拼成字符串


# =============================================
# 第七节：字符串格式化（f-string 详解）
# =============================================

def demo_fstring():
    # f-string 是 Python 3.6+ 最方便的字符串格式化方式
    # 在字符串前面加一个 f，然后用 { } 放变量或表达式
    # 语法：f"文字{变量}文字"

    print("\n=== f-string 详解 ===")

    name = "小明"
    age = 18
    score = 95.678

    # 基本用法
    print(f"我叫{name}，今年{age}岁")

    # 花括号里可以放任何表达式
    print(f"明年{age + 1}岁")
    print(f"名字长度：{len(name)}")
    print(f"成绩：{score:.1f}分")    # 保留 1 位小数 -> 95.7
    print(f"成绩：{score:.2f}分")    # 保留 2 位小数 -> 95.68

    # 对齐和填充
    # < 左对齐，> 右对齐，^ 居中
    print(f"\n对齐演示（宽度 10）：")
    print(f"{'左对齐':<10}|")        # 左对齐，宽度 10
    print(f"{'右对齐':>10}|")        # 右对齐，宽度 10
    print(f"{'居中':^10}|")          # 居中，宽度 10

    # 数字格式化
    num = 42
    print(f"\n数字 {num} 的不同进制：")
    print(f"十进制：{num}")
    print(f"二进制：{num:b}")        # 101010
    print(f"八进制：{num:o}")        # 52
    print(f"十六进制：{num:x}")      # 2a
    print(f"十六进制（大写）：{num:X}")  # 2A

    # 千分位分隔符
    big_num = 1234567890
    print(f"\n千分位：{big_num:,}")  # 1,234,567,890

    # 百分比
    rate = 0.856
    print(f"百分比：{rate:.1%}")     # 85.6%

    # f-string 小总结：
    # {变量}           -> 插入变量值
    # {表达式}         -> 插入计算结果
    # {值:.2f}        -> 保留2位小数
    # {值:<10}        -> 左对齐，宽度10
    # {值:>10}        -> 右对齐，宽度10
    # {值:^10}        -> 居中，宽度10
    # {值:,}          -> 千分位分隔
    # {值:.1%}        -> 百分比格式


# =============================================
# 第八节：实战练习（函数版）
# =============================================
#
# 练习1：写一个 reverse_string(s) 函数，反转字符串
# 练习2：写一个 count_chars(s, ch) 函数，统计字符出现次数
# 练习3：写一个 hide_phone(phone) 函数，隐藏手机号中间4位
# 练习4：写一个 title_words(s) 函数，每个单词首字母大写
# 练习5：写一个 parse_csv(data) 函数，解析 CSV 字符串
# 练习6：写一个 check_password(pwd) 函数，检查密码强度

# --- 练习1：字符串反转 ---
def reverse_string(s):
    # 用切片 [::-1] 反转字符串
    return s[::-1]


# --- 练习2：统计字符 ---
def count_chars(s, ch):
    # 用 count() 方法统计字符出现次数
    return s.count(ch)


# --- 练习3：隐藏手机号 ---
def hide_phone(phone):
    # 取前3位 + "****" + 取后4位
    return phone[:3] + "****" + phone[7:]


# --- 练习4：首字母大写 ---
def title_words(s):
    # 用 title() 方法让每个单词首字母大写
    return s.title()


# --- 练习5：CSV 数据处理 ---
def parse_csv(data):
    # 用 split(",") 分割 CSV 字符串，返回字典
    parts = data.split(",")
    return {
        "姓名": parts[0],
        "年龄": parts[1],
        "城市": parts[2],
        "职业": parts[3]
    }


# --- 练习6：密码强度检查 ---
def check_password(pwd):
    # 检查密码是否满足：长度>=8、包含大写、包含小写、包含数字
    has_length = len(pwd) >= 8
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    # any() 函数：只要有一个元素是 True，就返回 True
    # 这里的生成器表达式 (c.isupper() for c in pwd)
    # 会逐个检查密码里的每个字符，只要有一个是大写，any() 就返回 True
    if has_length and has_upper and has_lower and has_digit:
        return "强"
    else:
        return "弱"


# =============================================
# 主程序入口
# =============================================

if __name__ == "__main__":
    # 第一节到第七节：教学演示
    demo_string_basics()
    demo_string_length()
    demo_string_index()
    demo_string_slice()
    demo_string_methods()
    demo_string_split_join()
    demo_fstring()

    # 第八节：实战练习
    print("\n" + "=" * 50)
    print("实战练习")
    print("=" * 50)

    # 练习1：字符串反转
    print("\n--- 练习1：字符串反转 ---")
    text = "Hello World"
    print(f"原字符串：{text}")
    print(f"反转后：{reverse_string(text)}")

    # 练习2：统计字符
    print("\n--- 练习2：统计字符 ---")
    text = "Hello Python"
    print(f"字符串：{text}")
    print(f"长度：{len(text)}")
    print(f"'l' 出现次数：{count_chars(text, 'l')}")
    print(f"'o' 出现次数：{count_chars(text, 'o')}")

    # 练习3：隐藏手机号
    print("\n--- 练习3：隐藏手机号 ---")
    phone = "13812345678"
    print(f"原手机号：{phone}")
    print(f"隐藏后：{hide_phone(phone)}")

    # 练习4：首字母大写
    print("\n--- 练习4：首字母大写 ---")
    text = "hello python world"
    print(f"原字符串：{text}")
    print(f"首字母大写：{title_words(text)}")

    # 练习5：CSV 数据处理
    print("\n--- 练习5：CSV 数据处理 ---")
    data = "张三,25,北京,工程师"
    print(f"原始数据：{data}")
    info = parse_csv(data)
    for key, value in info.items():
        print(f"  {key}：{value}")

    # 练习6：密码强度检查
    print("\n--- 练习6：密码强度检查 ---")
    password = "Python123"
    print(f"密码：{password}")
    print(f"强度：{check_password(password)}")

    # 课程总结
    print("\n" + "=" * 50)
    print("课程总结")
    print("=" * 50)
    # 核心收获：
    # 1. 创建字符串：用单引号 '...' 或双引号 "..."
    # 2. len(字符串) -> 获取长度
    # 3. 字符串[索引] -> 取单个字符（索引从 0 开始，-1 是最后一个）
    # 4. 字符串[开始:结束:步长] -> 切片截取子串
    # 5. 字符串[::-1] -> 反转字符串
    # 6. strip()/upper()/lower()/title() -> 去空白、大小写转换
    # 7. find()/replace()/count() -> 查找、替换、统计
    # 8. split(分隔符) -> 字符串拆成列表
    # 9. 分隔符.join(列表) -> 列表拼成字符串
    # 10. f"文字{变量}" -> 格式化字符串
    #
    # 常见陷阱：
    # - 字符串是不可变的！s[0] = 'X' 会报错，必须创建新字符串
    # - 索引越界：s[10] 在字符串长度不够时会 IndexError
    # - 忘记 strip()：从 input() 或文件读取的字符串常带换行符和空格
    # - 索引从 0 开始，不是从 1 开始
    #
    # 下节课预告：
    # 下节课学列表与元组——Python 最重要的数据容器
    # 列表可以装很多东西，比字符串更灵活！
