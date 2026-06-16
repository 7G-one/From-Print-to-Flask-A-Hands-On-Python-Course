# -*- coding: utf-8 -*-
# =============================================
# 第 06 课：条件语句（函数重构版）
# =============================================
# 上节课我们学了字典和集合。
# 这节课我们要学习条件语句的进阶用法。
#
# 包括嵌套 if、三元表达式、match-case 结构和实际应用场景。


# =============================================
# 第一节：嵌套 if 语句
# =============================================

# 【什么是嵌套？】
# 就是在 if 里面再放一个 if，一层套一层
# 就像俄罗斯套娃，大娃娃里面装小娃娃
#
# 【语法】
# if 条件1:
#     条件1满足时执行的代码
#     if 条件2:
#         条件1和条件2都满足时执行的代码
#     else:
#         条件1满足但条件2不满足时执行的代码
# else:
#     条件1不满足时执行的代码

def demo_nested_if():
    # 演示嵌套 if 语句

    print("=== 嵌套 if 语句 ===")

    # 【示例1：判断是否可以开车】
    # 逻辑：必须成年 + 有驾照 才能开车
    age = 25
    has_license = True

    print(f"年龄：{age}")
    print(f"有驾照：{has_license}")

    if age >= 18:
        print("已成年 [OK]")
        if has_license:
            print("可以开车 [car]")
        else:
            print("需要先考驾照")
    else:
        print("未成年，不能开车 [X]")

    # 【示例2：购物折扣系统】
    # 逻辑：VIP 和普通用户有不同的折扣规则
    print("\n--- 购物折扣系统 ---")
    is_vip = True
    total = 500

    print(f"是否VIP：{is_vip}")
    print(f"消费金额：{total}元")

    if is_vip:
        # VIP 用户
        if total >= 300:
            discount = 0.7    # 7折
            print("VIP消费满300，打7折")
        else:
            discount = 0.8    # 8折
            print("VIP消费不满300，打8折")
    else:
        # 普通用户
        if total >= 500:
            discount = 0.9    # 9折
            print("普通用户消费满500，打9折")
        else:
            discount = 1.0    # 无折扣
            print("普通用户无折扣")

    final = total * discount
    print(f"应付金额：{final}元")

    # 【示例3：成绩评级（多层嵌套）】
    print("\n--- 成绩评级系统 ---")
    score = 85
    is_makeup = False  # 是否补考

    print(f"分数：{score}")
    print(f"是否补考：{is_makeup}")

    if score >= 60:
        # 及格
        if is_makeup:
            # 补考及格，最高只能 C
            if score >= 80:
                grade = "C"
            elif score >= 70:
                grade = "C"
            else:
                grade = "D"
            print(f"补考及格，等级：{grade}")
        else:
            # 正常考试
            if score >= 90:
                grade = "A"
            elif score >= 80:
                grade = "B"
            else:
                grade = "C"
            print(f"正常及格，等级：{grade}")
    else:
        # 不及格
        grade = "F"
        print(f"不及格，等级：{grade}")

    # 【嵌套 if 的注意事项】
    # 1. 嵌套不要太深（建议不超过 3 层），否则代码难以阅读
    # 2. 可以用 and/or 合并条件来减少嵌套


# =============================================
# 第二节：三元表达式（简洁写法）
# =============================================

def demo_ternary():
    # 演示三元表达式的用法

    print("\n=== 三元表达式 ===")

    # 【什么是三元表达式？】
    # 就是用一行代码写 if-else
    # 语法：值1 if 条件 else 值2
    #
    # 等价于：
    # if 条件:
    #     结果 = 值1
    # else:
    #     结果 = 值2

    # 【基本用法】
    age = 20
    status = "成年" if age >= 18 else "未成年"
    print(f"age = {age}, status = {status}")

    # 【更多示例】
    score = 85
    result = "及格" if score >= 60 else "不及格"
    print(f"score = {score}, result = {result}")

    num = 7
    parity = "偶数" if num % 2 == 0 else "奇数"
    print(f"num = {num}, parity = {parity}")

    # 【在 print 中直接使用】
    x = 10
    print(f"{x} 是 {'正数' if x > 0 else '负数'}")

    # 【在列表推导式中使用】
    numbers = [1, -2, 3, -4, 5, -6]
    labels = ["正" if n > 0 else "负" for n in numbers]
    print(f"\n数字：{numbers}")
    print(f"标签：{labels}")

    # 【三元表达式嵌套（不推荐太复杂）】
    # 可以嵌套，但可读性会变差
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
    print(f"\nscore = {score}, grade = {grade}")

    # 【最佳实践】
    # 简单的二选一 -> 用三元表达式
    # 复杂的多条件 -> 用完整的 if-elif-else


# =============================================
# 第三节：match-case 结构（Python 3.10+）
# =============================================

def demo_match_case():
    # 演示 match-case 结构的用法

    print("\n=== match-case 结构 ===")

    # 【什么是 match-case？】
    # Python 3.10 引入的新语法，类似其他语言的 switch-case
    # 但它更强大！可以匹配值、类型、甚至解构数据
    #
    # 【语法】
    # match 变量:
    #     case 值1:
    #         匹配值1时执行
    #     case 值2:
    #         匹配值2时执行
    #     case _:    # _ 是通配符，匹配所有其他情况
    #         以上都不匹配时执行

    import sys
    print(f"当前 Python 版本：{sys.version.split()[0]}")

    # 【检查版本是否支持】
    major, minor = sys.version_info[:2]
    if major < 3 or (major == 3 and minor < 10):
        print("当前 Python 版本不支持 match-case（需要 3.10+）")
        print("以下代码仅作展示，实际运行需要升级 Python")
        return

    # ---------- 示例1：基本匹配 ----------
    print("\n--- 示例1：基本匹配 ---")

    command = "quit"

    match command:
        case "quit" | "exit" | "q":
            # | 表示"或"，多个值匹配同一个分支
            print("退出程序")
        case "help" | "h":
            print("显示帮助")
        case "start" | "run":
            print("启动程序")
        case _:    # 通配符，匹配所有其他情况
            print(f"未知命令：{command}")

    # ---------- 示例2：匹配数字 ----------
    print("\n--- 示例2：匹配数字 ---")

    status_code = 404

    match status_code:
        case 200:
            print("请求成功")
        case 301:
            print("重定向")
        case 404:
            print("页面未找到")
        case 500:
            print("服务器错误")
        case _:    # 其他状态码
            print(f"未知状态码：{status_code}")

    # ---------- 示例3：使用 guard（条件守卫）----------
    print("\n--- 示例3：条件守卫 ---")

    score = 85

    match score:
        case s if s >= 90:
            print(f"分数{s}，等级A（优秀）")
        case s if s >= 80:
            print(f"分数{s}，等级B（良好）")
        case s if s >= 70:
            print(f"分数{s}，等级C（中等）")
        case s if s >= 60:
            print(f"分数{s}，等级D（及格）")
        case s:
            print(f"分数{s}，等级F（不及格）")

    # ---------- 示例4：解构匹配 ----------
    print("\n--- 示例4：解构匹配 ---")

    # 匹配元组
    point = (3, 4)

    match point:
        case (0, 0):
            print("原点")
        case (x, 0):
            print(f"在X轴上，x = {x}")
        case (0, y):
            print(f"在Y轴上，y = {y}")
        case (x, y):
            print(f"普通点：({x}, {y})")

    # 匹配列表
    data = [1, 2, 3]

    match data:
        case []:
            print("空列表")
        case [x]:
            print(f"只有一个元素：{x}")
        case [x, y]:
            print(f"两个元素：{x}, {y}")
        case [x, *rest]:
            print(f"第一个元素：{x}，剩余：{rest}")

    # ---------- 示例5：匹配字典 ----------
    print("\n--- 示例5：匹配字典 ---")

    user = {"role": "admin", "name": "Alice"}

    match user:
        case {"role": "admin", "name": name}:
            print(f"管理员 {name}，拥有全部权限")
        case {"role": "editor", "name": name}:
            print(f"编辑 {name}，拥有编辑权限")
        case {"role": "viewer", "name": name}:
            print(f"访客 {name}，只有查看权限")
        case {"name": name}:
            print(f"用户 {name}，角色未知")
        case _:
            print("未知用户")


# =============================================
# 第四节：条件表达式的实际应用
# =============================================

def demo_input_validation():
    # 应用1：输入验证

    print("\n--- 应用1：输入验证 ---")

    test_ages = [25, -5, 200, "abc"]
    for age in test_ages:
        is_valid, message = validate_age(age)
        print(f"  年龄 {str(age):>5} -> {'[OK]' if is_valid else '[X]'} {message}")


def validate_age(age):
    # 验证年龄是否合法

    # 先判断类型
    if not isinstance(age, int):
        return False, "年龄必须是整数"
    elif age < 0:
        return False, "年龄不能为负数"
    elif age > 150:
        return False, "年龄不能超过150"
    else:
        return True, "年龄合法"


def demo_permission_control():
    # 应用2：权限控制

    print("\n--- 应用2：权限控制 ---")

    permissions = {
        "admin": ["read", "write", "delete", "manage"],
        "editor": ["read", "write"],
        "viewer": ["read"],
    }

    users = [
        ("admin", "delete"),
        ("editor", "delete"),
        ("viewer", "write"),
        ("guest", "read"),
    ]

    for role, action in users:
        allowed = permissions.get(role, [])
        if action in allowed:
            has_perm = True
        else:
            has_perm = False
        status = "允许" if has_perm else "拒绝"
        print(f"  {role:>8} 执行 {action:>6} -> {status}")


def demo_bmi_classification():
    # 应用3：数据分类（BMI 计算）

    print("\n--- 应用3：数据分类 ---")

    weights = [50, 65, 80, 95]
    height = 1.75

    for w in weights:
        bmi = w / (height ** 2)
        if bmi < 18.5:
            category = "偏瘦"
            advice = "建议增加营养摄入"
        elif bmi < 24:
            category = "正常"
            advice = "继续保持"
        elif bmi < 28:
            category = "偏胖"
            advice = "建议适当运动"
        else:
            category = "肥胖"
            advice = "建议就医咨询"
        print(f"  体重{w}kg, BMI={bmi:.1f} -> {category}，{advice}")


def demo_config_parsing():
    # 应用4：配置解析

    print("\n--- 应用4：配置解析 ---")

    levels = ["DEBUG", "info", "WARNING", "error", "unknown"]
    for lvl in levels:
        level = lvl.lower()
        if level == "debug":
            num = 10
            desc = "调试"
        elif level == "info":
            num = 20
            desc = "信息"
        elif level == "warning":
            num = 30
            desc = "警告"
        elif level == "error":
            num = 40
            desc = "错误"
        elif level == "critical":
            num = 50
            desc = "严重"
        else:
            num = 0
            desc = "未知"
        print(f"  '{lvl}' -> 级别{num} ({desc})")


def demo_calculator():
    # 应用5：简易计算器

    print("\n--- 应用5：简易计算器 ---")

    operations = [
        (10, "+", 3),
        (10, "-", 3),
        (10, "*", 3),
        (10, "/", 3),
        (10, "/", 0),
        (10, "**", 3),
        (10, "%", 3),
    ]

    for a, op, b in operations:
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                result = "错误：除数不能为0"
            else:
                result = a / b
        elif op == "//":
            if b == 0:
                result = "错误：除数不能为0"
            else:
                result = a // b
        elif op == "%":
            if b == 0:
                result = "错误：除数不能为0"
            else:
                result = a % b
        elif op == "**":
            result = a ** b
        else:
            result = f"错误：不支持的运算符 '{op}'"
        print(f"  {a} {op} {b} = {result}")


def demo_weekday_check():
    # 应用6：日期星期判断

    print("\n--- 应用6：日期星期判断 ---")

    days = ["周一", "周三", "周五", "周六", "周日", "节日"]
    for day in days:
        if day in ["周一", "周二", "周三", "周四", "周五"]:
            day_type = "工作日"
        elif day in ["周六", "周日"]:
            day_type = "周末"
        else:
            day_type = "无效日期"
        emoji = "[work]" if day_type == "工作日" else "[party]" if day_type == "周末" else "[?]"
        print(f"  {day} -> {day_type} {emoji}")


# =============================================
# 实战小项目：猜数字游戏（简化版）
# =============================================
print("\n" + "=" * 50)
print("实战小项目：猜数字游戏")
print("=" * 50)

def guess_number_game(target, guesses):
    """模拟猜数字游戏，根据猜测列表返回结果"""
    results = []
    for guess in guesses:
        if guess == target:
            results.append(f"  猜 {guess} → 恭喜，猜对了！")
            break
        elif guess < target:
            results.append(f"  猜 {guess} → 太小了")
        else:
            results.append(f"  猜 {guess} → 太大了")
    return results

# 模拟游戏
target = 42
guesses = [50, 25, 38, 42]
print(f"目标数字：{target}")
print(f"猜测记录：")
for line in guess_number_game(target, guesses):
    print(line)


# =============================================
# 第五节：实战练习
# =============================================

def exercise_password_strength():
    # 练习1：密码强度检查
    # 检查密码的强度：长度>=8、含大写、含小写、含数字

    print("\n--- 练习1：密码强度检查 ---")
    password = "Python123"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    is_long = len(password) >= 8

    print(f"密码：{password}")
    print(f"  长度>=8：{is_long}")
    print(f"  包含大写：{has_upper}")
    print(f"  包含小写：{has_lower}")
    print(f"  包含数字：{has_digit}")

    if is_long and has_upper and has_lower and has_digit:
        strength = "强"
    elif len(password) >= 6:
        strength = "中"
    else:
        strength = "弱"
    print(f"  强度：{strength}")


def exercise_login():
    # 练习2：登录验证（嵌套 if）

    print("\n--- 练习2：登录验证 ---")
    test_cases = [
        ("admin", "123456"),    # 正确
        ("admin", "wrong"),     # 密码错误
        ("unknown", "123456"),  # 用户名错误
        ("", "123456"),         # 用户名为空
    ]

    valid_users = {"admin": "123456", "user1": "password"}

    for username, password in test_cases:
        if not username:
            result = "请输入用户名"
        elif not password:
            result = "请输入密码"
        elif username not in valid_users:
            result = "用户名不存在"
        elif valid_users[username] != password:
            result = "密码错误"
        else:
            result = "登录成功！"
        print(f"  用户'{username}' -> {result}")


def exercise_discount():
    # 练习3：购物车折扣（嵌套 if）

    print("\n--- 练习3：购物车折扣 ---")
    test_orders = [
        (True, 1200),    # VIP，高消费
        (True, 600),     # VIP，中消费
        (True, 200),     # VIP，低消费
        (False, 900),    # 非VIP，高消费
        (False, 300),    # 非VIP，低消费
    ]

    for is_member, total in test_orders:
        if is_member:
            if total >= 1000:
                discount = 0.6
                rule = "会员满1000打6折"
            elif total >= 500:
                discount = 0.7
                rule = "会员满500打7折"
            else:
                discount = 0.8
                rule = "会员打8折"
        else:
            if total >= 800:
                discount = 0.9
                rule = "非会员满800打9折"
            else:
                discount = 1.0
                rule = "无折扣"

        final = total * discount
        member_str = "VIP" if is_member else "普通"
        print(f"  [{member_str}] 消费{total}元 -> {rule} -> 实付{final:.0f}元")


def exercise_ternary():
    # 练习4：三元表达式实战

    print("\n--- 练习4：三元表达式实战 ---")
    numbers = [-3, -1, 0, 2, 5, 8, -7, 10]

    # 用三元表达式分类
    categories = [
        "零" if n == 0 else "正" if n > 0 else "负"
        for n in numbers
    ]
    print(f"数字：{numbers}")
    print(f"分类：{categories}")

    # 用三元表达式取绝对值
    abs_values = [n if n >= 0 else -n for n in numbers]
    print(f"绝对值：{abs_values}")


def exercise_leap_year():
    # 练习5：闰年判断（嵌套逻辑）

    print("\n--- 练习5：闰年判断 ---")
    years = [2000, 1900, 2024, 2023, 2100]

    for year in years:
        # 嵌套写法（更清晰地展示逻辑）
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    is_leap = True   # 能被400整除 -> 闰年
                else:
                    is_leap = False  # 能被100整除但不能被400整除 -> 非闰年
            else:
                is_leap = True       # 能被4整除但不能被100整除 -> 闰年
        else:
            is_leap = False          # 不能被4整除 -> 非闰年

        print(f"  {year}年 -> {'闰年' if is_leap else '平年'}")


# =============================================
# 主程序入口
# =============================================

if __name__ == "__main__":
    # 教学演示
    demo_nested_if()
    demo_ternary()
    demo_match_case()

    # 实际应用
    print("\n=== 条件表达式的实际应用 ===")
    demo_input_validation()
    demo_permission_control()
    demo_bmi_classification()
    demo_config_parsing()
    demo_calculator()
    demo_weekday_check()

    # 练习题
    print("\n" + "=" * 50)
    print("实战练习")
    print("=" * 50)

    exercise_password_strength()
    exercise_login()
    exercise_discount()
    exercise_ternary()
    exercise_leap_year()


# =============================================
# 课程总结
# =============================================

# 核心收获：
# - 嵌套 if 处理多层判断：先判断大类再判断细节，如 VIP 满减的阶梯折扣
# - 三元表达式 "A" if 条件 else "B" 一行搞定简单二选一，适合列表推导式
# - match-case 是 Python 3.10+ 的模式匹配，比长串 elif 更清晰
#
# 常见陷阱：
# - 嵌套太深（超过 3 层）会让代码难读，考虑用函数拆分或字典映射替代
# - 三元表达式里滥用会降低可读性，复杂的逻辑还是用 if-elif-else 更清楚
# - match-case 的 case _ 是通配符，漏写会导致匹配失败却不报错
#
# 下节课预告：
# - 下节课学循环语句，让程序能自动重复执行任务
