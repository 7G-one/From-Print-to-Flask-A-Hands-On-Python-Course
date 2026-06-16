# -*- coding: utf-8 -*-
# =============================================
# 第 04 课：列表与元组
# =============================================
# 上节课我们学了字符串操作。
# 这节课我们要学习列表和元组——Python 中最重要的数据结构。
# 列表可以增删改查，元组不可变，两者都支持索引和切片。


# =============================================
# 第一节：什么是列表？
# =============================================

def demo_list_basics():
    # 列表就像一个购物车：
    # - 可以装很多东西（元素）
    # - 东西有顺序（第一个、第二个...）
    # - 可以添加、删除、修改东西
    #
    # 用方括号 [] 包起来，元素用逗号 , 分隔

    print("=== 第一节：创建列表 ===")

    # 空列表
    empty_list = []
    print(f"空列表：{empty_list}")

    # 带元素的列表
    fruits = ["苹果", "香蕉", "橘子", "葡萄"]
    print(f"水果列表：{fruits}")

    numbers = [1, 2, 3, 4, 5]
    print(f"数字列表：{numbers}")

    # 可以混合不同类型
    mixed = [1, "hello", 3.14, True]
    print(f"混合列表：{mixed}")

    # 列表里可以有列表（嵌套列表）
    nested = [[1, 2], [3, 4], [5, 6]]
    print(f"嵌套列表：{nested}")


# =============================================
# 第二节：列表索引（找位置）
# =============================================

def demo_list_index():
    # 列表索引和字符串一样！从 0 开始，可以是负数。
    #
    # 索引图：
    # 苹果    香蕉    橘子    葡萄
    #  0       1       2       3    <- 正向索引
    # -4      -3      -2      -1    <- 反向索引

    print("\n=== 第二节：列表索引 ===")

    fruits = ["苹果", "香蕉", "橘子", "葡萄"]
    print(f"水果列表：{fruits}")
    print(f"长度：{len(fruits)}")

    # 正向索引（从左到右，从 0 开始）
    print(f"\n正向索引：")
    print(f"fruits[0] = {fruits[0]}")   # 苹果（第 1 个）
    print(f"fruits[1] = {fruits[1]}")   # 香蕉（第 2 个）
    print(f"fruits[2] = {fruits[2]}")   # 橘子（第 3 个）
    print(f"fruits[3] = {fruits[3]}")   # 葡萄（第 4 个）

    # 反向索引（从右到左，从 -1 开始）
    print(f"\n反向索引：")
    print(f"fruits[-1] = {fruits[-1]}")  # 葡萄（最后一个）
    print(f"fruits[-2] = {fruits[-2]}")  # 橘子（倒数第 2 个）
    print(f"fruits[-3] = {fruits[-3]}")  # 香蕉（倒数第 3 个）
    print(f"fruits[-4] = {fruits[-4]}")  # 苹果（倒数第 4 个）


# =============================================
# 第三节：列表切片（截取一部分）
# =============================================

def demo_list_slice():
    # 切片和字符串一样！
    # 列表[开始:结束]，包含开始，不包含结束

    print("\n=== 第三节：列表切片 ===")

    colors = ["红", "橙", "黄", "绿", "蓝", "靛", "紫"]
    print(f"颜色列表：{colors}")

    # 基本切片
    print(f"\ncolors[0:3] = {colors[0:3]}")    # ['红', '橙', '黄']
    print(f"colors[1:4] = {colors[1:4]}")      # ['橙', '黄', '绿']

    # 省略开始或结束
    print(f"\ncolors[:3] = {colors[:3]}")      # ['红', '橙', '黄']（从开头截取）
    print(f"colors[4:] = {colors[4:]}")        # ['蓝', '靛', '紫']（截取到结尾）
    print(f"colors[:] = {colors[:]}")          # 完整复制一份

    # 带步长
    print(f"\ncolors[::2] = {colors[::2]}")    # 隔一个取一个
    print(f"colors[::-1] = {colors[::-1]}")    # 反转列表


# =============================================
# 第四节：列表修改（增删改）
# =============================================

def demo_list_modify():
    # 列表是可变的！可以修改、添加、删除元素。

    print("\n=== 第四节：列表修改（增删改） ===")

    # --- 修改元素 ---
    fruits = ["苹果", "香蕉", "橘子"]
    print(f"原列表：{fruits}")
    fruits[0] = "葡萄"  # 把第一个元素改成葡萄
    print(f"修改后：{fruits}")

    # --- 添加元素 ---
    # append() - 在末尾添加一个元素
    fruits.append("西瓜")
    print(f"\nappend('西瓜')：{fruits}")

    # insert(位置, 值) - 在指定位置插入
    fruits.insert(1, "芒果")  # 在索引 1 的位置插入
    print(f"insert(1, '芒果')：{fruits}")

    # extend() - 把另一个列表的元素逐个添加进来
    fruits.extend(["草莓", "樱桃"])
    print(f"extend(['草莓', '樱桃'])：{fruits}")

    # --- 删除元素 ---
    # remove(值) - 删除第一个匹配的元素
    fruits.remove("香蕉")
    print(f"\nremove('香蕉')：{fruits}")

    # pop() - 删除指定位置的元素，默认删除最后一个，并返回被删除的值
    popped = fruits.pop()
    print(f"pop()：{fruits}，删除了：{popped}")

    popped = fruits.pop(0)  # 删除第一个
    print(f"pop(0)：{fruits}，删除了：{popped}")

    # del - 删除指定位置的元素
    del fruits[0]
    print(f"del fruits[0]：{fruits}")


# =============================================
# 第五节：列表常用方法
# =============================================

def demo_list_methods():
    print("\n=== 第五节：列表常用方法 ===")

    # --- 排序 ---
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"原列表：{numbers}")

    # sort() - 原地排序（直接修改原列表）
    numbers.sort()
    print(f"sort()：{numbers}")

    # sorted() - 返回一个新的排序列表，不修改原列表
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    new_numbers = sorted(numbers)
    print(f"sorted()：{new_numbers}")
    print(f"原列表不变：{numbers}")

    # 降序排序
    numbers.sort(reverse=True)
    print(f"sort(reverse=True)：{numbers}")

    # --- 反转 ---
    numbers = [1, 2, 3, 4, 5]
    numbers.reverse()
    print(f"\nreverse()：{numbers}")

    # --- 查找和统计 ---
    numbers = [1, 2, 3, 4, 5]
    print(f"\n列表：{numbers}")
    print(f"len()：{len(numbers)}")        # 长度
    print(f"count(3)：{numbers.count(3)}")  # 3 出现的次数
    print(f"index(3)：{numbers.index(3)}")  # 3 第一次出现的位置

    # --- 判断元素是否存在 ---
    print(f"\n3 in numbers：{3 in numbers}")  # True
    print(f"6 in numbers：{6 in numbers}")    # False


# =============================================
# 第六节：列表推导式（快速创建列表）
# =============================================

def demo_list_comprehension():
    # 列表推导式就是用一行代码创建列表的快捷方式。
    # 语法：[表达式 for 变量 in 可迭代对象 if 条件]

    print("\n=== 第六节：列表推导式 ===")

    # 创建 1-5 的平方
    squares = [x**2 for x in range(1, 6)]
    print(f"1-5 的平方：{squares}")

    # 创建偶数列表（带条件过滤）
    evens = [x for x in range(1, 11) if x % 2 == 0]
    print(f"1-10 的偶数：{evens}")

    # 字符串处理：把每个单词转成大写
    words = ["hello", "python", "world"]
    upper_words = [w.upper() for w in words]
    print(f"转大写：{upper_words}")

    # 实际应用：过滤出 80 分以上的成绩
    scores = [85, 92, 78, 95, 88, 76, 90]
    passed = [s for s in scores if s >= 80]
    print(f"\n所有成绩：{scores}")
    print(f"80 分以上：{passed}")


# =============================================
# 第七节：元组（不可变的列表）
# =============================================

def demo_tuple():
    # 元组就像列表，但是不能修改！
    # 就像一个密封的盒子，装好就不能动了。
    # 用小括号 () 创建。

    print("\n=== 第七节：元组 ===")

    # 创建元组
    colors = ("红", "绿", "蓝")
    print(f"元组：{colors}")

    # 单个元素的元组（注意：必须加逗号！）
    single = (1,)
    print(f"单元素元组：{single}")

    # 没有逗号就不是元组，只是一个普通括号表达式
    not_tuple = (1)
    print(f"不是元组：{not_tuple}，类型：{type(not_tuple)}")

    # 元组索引（和列表一样）
    print(f"\ncolors[0] = {colors[0]}")
    print(f"colors[-1] = {colors[-1]}")

    # 元组不能修改！取消下面这行的注释会报错：
    # colors[0] = "黄"  # TypeError: 'tuple' object does not support item assignment

    # 元组解包：把元组的元素一次性赋给多个变量
    name, age, city = ("小明", 18, "北京")
    print(f"\n解包结果 -> 姓名：{name}，年龄：{age}，城市：{city}")

    # 元组的优点：
    # 1. 比列表更快（内存占用更小）
    # 2. 安全（不会被意外修改）
    # 3. 可以作为字典的键（列表不行）


# =============================================
# 第八节：列表 vs 元组
# =============================================

def demo_list_vs_tuple():
    print("\n=== 第八节：列表 vs 元组 ===")

    # 列表：可以修改
    my_list = [1, 2, 3]
    my_list[0] = 10
    print(f"列表可以修改：{my_list}")

    # 元组：不能修改
    my_tuple = (1, 2, 3)
    # my_tuple[0] = 10  # 报错！
    print(f"元组不能修改：{my_tuple}")

    # 什么时候用列表？
    # - 需要修改、添加、删除元素时
    # - 数据会变化时（比如购物车、待办事项）
    #
    # 什么时候用元组？
    # - 数据不应该被修改时（比如坐标、RGB颜色值）
    # - 需要保护数据时
    # - 需要用作字典的键时


# =============================================
# 实战小项目：学生成绩统计器
# =============================================
print("\n" + "=" * 50)
print("实战小项目：学生成绩统计器")
print("=" * 50)

def score_analyzer(scores):
    """分析成绩列表，返回统计信息"""
    if not scores:
        return {"平均分": 0, "最高分": 0, "最低分": 0, "及格人数": 0}

    avg = sum(scores) / len(scores)
    passed = sum(1 for s in scores if s >= 60)

    return {
        "平均分": round(avg, 1),
        "最高分": max(scores),
        "最低分": min(scores),
        "及格人数": passed,
        "及格率": f"{passed / len(scores) * 100:.1f}%"
    }

# 测试
scores = [85, 92, 58, 76, 95, 43, 88, 72, 61, 90]
result = score_analyzer(scores)
print(f"成绩列表：{scores}")
for key, value in result.items():
    print(f"  {key}：{value}")


# =============================================
# 第九节：实战练习（函数版）
# =============================================
#
# 练习1：写一个 list_operations() 函数，演示列表增删改操作
# 练习2：写一个 multiples_of_3(n) 函数，生成 1-n 中所有 3 的倍数
# 练习3：写一个 score_stats(scores) 函数，统计成绩
# 练习4：写一个 unpack_tuple(info) 函数，解包元组
# 练习5：写一个 transpose(matrix) 函数，矩阵转置
# 练习6：写一个 shopping_cart(items) 函数，计算购物车总价

# --- 练习1：列表操作 ---
def list_operations():
    # 对列表依次进行 append、remove、sort、reverse 操作
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"原列表：{nums}")

    nums.append(5)
    print(f"append(5)：{nums}")

    nums.remove(1)  # remove(1) 只删除第一个匹配的 1
    print(f"remove(1)：{nums}")

    nums.sort()
    print(f"sort()：{nums}")

    nums.reverse()
    print(f"reverse()：{nums}")


# --- 练习2：列表推导式 ---
def multiples_of_3(n):
    # 用列表推导式生成 1-n 中所有 3 的倍数
    return [x for x in range(1, n + 1) if x % 3 == 0]


def extract_upper(s):
    # 从字符串中提取所有大写字母
    return [c for c in s if c.isupper()]


# --- 练习3：成绩统计 ---
def score_stats(scores):
    # 统计平均分、最高分、最低分、90分以上人数
    return {
        "平均分": sum(scores) / len(scores),
        "最高分": max(scores),
        "最低分": min(scores),
        "90分以上": len([s for s in scores if s >= 90])
    }


# --- 练习4：元组解包 ---
def unpack_tuple(info):
    # 将元组解包为单独的变量并打印
    name, age, city, job = info
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    print(f"城市：{city}")
    print(f"职业：{job}")


# --- 练习5：矩阵转置 ---
def transpose(matrix):
    # 将矩阵转置（行变列，列变行）
    # 把第 i 列变成第 i 行
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# --- 练习6：购物车 ---
def shopping_cart(items):
    # 计算购物车总价
    # items 是列表，每个元素是字典 {"name": ..., "price": ..., "quantity": ...}
    total = sum(item["price"] * item["quantity"] for item in items)
    print("购物车：")
    for item in items:
        print(f"  {item['name']}: ¥{item['price']} x {item['quantity']}")
    print(f"总计：¥{total}")
    return total


# =============================================
# 主程序入口
# =============================================

if __name__ == "__main__":
    # 第一节到第八节：教学演示
    demo_list_basics()
    demo_list_index()
    demo_list_slice()
    demo_list_modify()
    demo_list_methods()
    demo_list_comprehension()
    demo_tuple()
    demo_list_vs_tuple()

    # 第九节：实战练习
    print("\n" + "=" * 50)
    print("实战练习")
    print("=" * 50)

    # 练习1：列表操作
    print("\n--- 练习1 参考 ---")
    list_operations()

    # 练习2：列表推导式
    print("\n--- 练习2 参考 ---")
    print(f"3 的倍数（1-20）：{multiples_of_3(20)}")
    print(f"大写字母：{extract_upper('Hello World')}")

    # 练习3：成绩统计
    print("\n--- 练习3 参考 ---")
    scores = [85, 92, 78, 95, 88, 76, 90]
    print(f"成绩：{scores}")
    stats = score_stats(scores)
    for key, value in stats.items():
        if key == "平均分":
            print(f"  {key}：{value:.1f}")
        else:
            print(f"  {key}：{value}")

    # 练习4：元组解包
    print("\n--- 练习4 参考 ---")
    info = ("小明", 18, "北京", "工程师")
    unpack_tuple(info)

    # 练习5：矩阵转置
    print("\n--- 练习5 参考 ---")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"原矩阵：{matrix}")
    print(f"转置后：{transpose(matrix)}")

    # 练习6：购物车
    print("\n--- 练习6 参考 ---")
    cart = [
        {"name": "苹果", "price": 8.5, "quantity": 3},
        {"name": "牛奶", "price": 12, "quantity": 2},
        {"name": "面包", "price": 6, "quantity": 1}
    ]
    shopping_cart(cart)

    # 课程总结
    print("\n" + "=" * 50)
    print("课程总结")
    print("=" * 50)
    # 核心收获：
    # - 列表用 append() 加元素、remove() 删元素、索引取值，是最灵活的容器
    # - 列表推导式 [表达式 for x in 列表 if 条件] 一行代码搞定筛选和转换
    # - 元组用 () 创建，不可修改，适合存储不该被改动的数据如坐标 (x, y)
    #
    # 常见陷阱：
    # - 列表是可变对象：a = b 不会复制，改 b 会同时改 a，要用 b = a.copy()
    # - append() 和 extend() 的区别：
    #     append 把参数当一个元素整体加入，extend 拆开逐个添加
    # - 元组只有一个元素时要加逗号：(1) 是整数，(1,) 才是元组
    #
    # 下节课预告：
    # - 下节课学字典与集合，用"键值对"和"无重复集"解决更多数据问题
