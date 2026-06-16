# -*- coding: utf-8 -*-
# =============================================
# 第 10 课：面向对象编程
# =============================================
# 上节课我们学了文件操作。
# 这节课我们要学习面向对象编程——用"类"和"对象"组织代码。
#
# 类是蓝图，对象是实例，继承和多态让代码更灵活、更易扩展。

# =============================================
# 第一节：类和对象
# =============================================

"""
【类和对象的关系】

类（Class）：模板、蓝图
对象（Object）：用模板做出来的东西

比喻：
- 类：饼干模具
- 对象：用模具做出来的饼干

【类的组成部分】
1. 属性（数据）：对象有什么
2. 方法（行为）：对象能做什么
"""


# ========== 定义一个简单的类 ==========

class Dog:
    """
    狗类

    【作用】
    描述狗的特征和行为

    【属性】
    - name: 字符串，狗的名字
    - age: 整数，狗的年龄

    【方法】
    - bark(): 叫
    - show_info(): 显示信息
    """

    # 类属性（所有实例共享）
    species = "犬科"

    def __init__(self, name, age):
        """
        初始化方法（构造函数）

        【作用】
        创建对象时，设置属性

        【参数】
        - name: 字符串，狗的名字
        - age: 整数，狗的年龄

        【调用时机】
        创建对象时自动调用

        【调用示例】
        dog = Dog("旺财", 3)
        """

        # 实例属性（每个实例独有）
        self.name = name
        self.age = age

    def bark(self):
        """
        叫

        【作用】
        打印狗叫的声音

        【调用示例】
        dog.bark()  # 输出: 旺财: 汪汪汪！
        """

        print(f"{self.name}: 汪汪汪！")

    def show_info(self):
        """
        显示信息

        【作用】
        打印狗的名字和年龄

        【调用示例】
        dog.show_info()  # 输出: 旺财，3岁
        """

        print(f"{self.name}，{self.age}岁")


# ========== 创建对象 ==========

print("=== 创建对象 ===")

# 创建对象（实例化）
dog1 = Dog("旺财", 3)
dog2 = Dog("小白", 2)

# 调用方法
dog1.bark()
dog2.bark()

# 访问属性
print(f"dog1 的名字：{dog1.name}")
print(f"dog2 的年龄：{dog2.age}")

# 访问类属性
print(f"物种：{dog1.species}")


# =============================================
# 第二节：self 是什么？
# =============================================

"""
【self 的含义】
self 代表"对象自己"
就像"我"代表说话的人一样

【什么时候用 self？】
在类的方法中，用 self 访问对象自己的属性和方法

【调用过程】
dog1.bark()
→ 等价于 Dog.bark(dog1)
→ self 就是 dog1
"""


class Cat:
    """
    猫类

    【演示 self 的用法】
    """

    def __init__(self, name, color):
        """
        初始化

        【参数】
        - name: 字符串，猫的名字
        - color: 字符串，猫的颜色
        """

        # self.name 是这只猫的名字
        self.name = name
        self.color = color

    def meow(self):
        """
        叫

        【self 代表调用这个方法的猫】
        """

        # self 代表调用这个方法的猫
        return f"{self.name}: 喵~"

    def describe(self):
        """
        描述

        【self.name 和 self.color 是这只猫的属性】
        """

        return f"这是一只{self.color}的{self.name}"


print("\n=== self 的含义 ===")

# 创建两只猫
cat1 = Cat("咪咪", "白色")
cat2 = Cat("花花", "橘色")

# 调用方法时，Python 自动传入 self
print(cat1.meow())    # 等价于 Cat.meow(cat1)
print(cat2.meow())    # 等价于 Cat.meow(cat2)
print(cat1.describe())
print(cat2.describe())


# =============================================
# 第三节：类属性和实例属性
# =============================================

"""
【类属性】
- 所有对象共享的属性
- 定义在类里面，方法外面

【实例属性】
- 每个对象独有的属性
- 定义在 __init__ 方法里
"""


class Student:
    """
    学生类

    【类属性】
    - school: 学校名（所有学生共享）

    【实例属性】
    - name: 姓名
    - age: 年龄
    """

    # 类属性（所有学生共享）
    school = "清华大学"
    total_students = 0

    def __init__(self, name, age):
        """
        初始化

        【参数】
        - name: 字符串，学生姓名
        - age: 整数，学生年龄
        """

        # 实例属性（每个学生独有）
        self.name = name
        self.age = age

        # 修改类属性
        Student.total_students += 1

    def info(self):
        """
        显示信息

        【调用示例】
        student.info()
        """

        return f"{self.name}，{self.age}岁，来自{self.school}"


print("\n=== 类属性和实例属性 ===")

# 创建学生
s1 = Student("小明", 18)
s2 = Student("小红", 19)

print(s1.info())
print(s2.info())
print(f"学校：{Student.school}")
print(f"学生总数：{Student.total_students}")


# =============================================
# 第四节：方法详解
# =============================================

"""
【方法的类型】

1. 实例方法：第一个参数是 self
2. 类方法：用 @classmethod，第一个参数是 cls
3. 静态方法：用 @staticmethod，没有 self 或 cls
"""


class Calculator:
    """
    计算器类

    【演示三种方法】
    """

    # 类属性
    pi = 3.14159

    def __init__(self, value=0):
        """初始化"""
        self.value = value

    def add(self, n):
        """
        实例方法

        【作用】
        给当前值加上 n

        【参数】
        - n: 数字

        【调用方式】
        calc.add(10)
        """

        self.value += n
        return self

    @classmethod
    def circle_area(cls, radius):
        """
        类方法

        【作用】
        计算圆的面积

        【参数】
        - radius: 数字，半径

        【返回值】
        数字，圆的面积

        【调用方式】
        Calculator.circle_area(5)
        """

        return cls.pi * radius ** 2

    @staticmethod
    def add_numbers(a, b):
        """
        静态方法

        【作用】
        计算两个数的和

        【参数】
        - a: 数字
        - b: 数字

        【返回值】
        数字，a + b

        【调用方式】
        Calculator.add_numbers(3, 5)
        """

        return a + b


print("\n=== 方法详解 ===")

# 实例方法
calc = Calculator(10)
calc.add(5)
print(f"实例方法：{calc.value}")

# 类方法
area = Calculator.circle_area(5)
print(f"类方法：圆面积 = {area:.2f}")

# 静态方法
result = Calculator.add_numbers(3, 5)
print(f"静态方法：3 + 5 = {result}")


# =============================================
# 第五节：继承
# =============================================

"""
【什么是继承？】
就像孩子继承父母的特征
子类可以继承父类的属性和方法

【继承的好处】
1. 代码复用：不需要重复写相同的代码
2. 扩展功能：在父类基础上添加新功能

【语法】
class 子类名(父类名):
    子类的内容
"""


class Animal:
    """
    动物类（父类）

    【属性】
    - name: 名字
    - age: 年龄

    【方法】
    - speak(): 叫
    - show_info(): 显示信息
    """

    def __init__(self, name, sound):
        """
        初始化

        【参数】
        - name: 字符串，名字
        - sound: 字符串，叫声
        """

        self.name = name
        self.sound = sound

    def speak(self):
        """
        叫

        【调用示例】
        animal.speak()
        """

        print(f"{self.name}: {self.sound}")

    def show_info(self):
        """
        显示信息

        【调用示例】
        animal.show_info()
        """

        print(f"{self.name}")


class Bird(Animal):
    """
    鸟类（子类）

    【继承自】Animal

    【新增属性】
    - color: 颜色

    【新增方法】
    - fly(): 飞翔
    """

    def __init__(self, name, color):
        """
        初始化

        【调用父类的 __init__】
        """

        # 调用父类的 __init__
        super().__init__(name, "叽叽喳喳")
        self.color = color

    def fly(self):
        """
        飞翔

        【调用示例】
        bird.fly()
        """

        print(f"{self.name}展翅高飞！")


class Fish(Animal):
    """
    鱼类（子类）

    【继承自】Animal

    【新增属性】
    - color: 颜色

    【新增方法】
    - swim(): 游泳
    """

    def __init__(self, name, color):
        """
        初始化

        【调用父类的 __init__】
        """

        super().__init__(name, "咕噜咕噜")
        self.color = color

    def swim(self):
        """
        游泳

        【调用示例】
        fish.swim()
        """

        print(f"{self.name}: 自在地游来游去~")


print("\n=== 继承 ===")

# 创建对象
fish = Fish("小丑鱼", "橙色")
bird = Bird("小燕子", "棕色")

# 调用继承的方法
fish.speak()    # 继承自 Animal
bird.speak()    # 继承自 Animal

# 调用子类特有的方法
fish.swim()     # Fish 特有
bird.fly()      # Bird 特有


# =============================================
# 第六节：多态
# =============================================

"""
【什么是多态？】
同样的方法，不同的行为
就像"叫"这个动作，猫和狗叫的声音不同

【多态的好处】
代码更灵活，更容易扩展
"""


print("\n=== 多态 ===")

# 创建不同的动物
animals = [Fish("小丑鱼", "橙色"), Bird("小燕子", "棕色")]

# 同样是调用 speak()，但行为不同
for animal in animals:
    animal.speak()


# =============================================
# 第七节：魔术方法
# =============================================

"""
【什么是魔术方法？】
以 __ 开头和结尾的特殊方法
Python 在特定情况下会自动调用

常用的魔术方法：
- __init__: 创建对象时调用
- __str__: 用 print() 打印时调用
- __repr__: 调试时的表示
- __len__: 用 len() 时调用
"""


class Point:
    """
    点类

    【演示魔术方法】
    """

    def __init__(self, x, y):
        """初始化"""
        self.x = x
        self.y = y

    def __str__(self):
        """
        字符串表示（用户友好）

        【调用时机】
        用 print() 打印时
        """

        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """
        调试表示

        【调用时机】
        在交互式环境中显示
        """

        return f"Point(x={self.x!r}, y={self.y!r})"

    def __add__(self, other):
        """
        加法运算符

        【调用时机】
        用 + 运算符时
        """

        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """
        等于运算符

        【调用时机】
        用 == 运算符时
        """

        return self.x == other.x and self.y == other.y


print("\n=== 魔术方法 ===")

p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 + p2 = {p1 + p2}")
print(f"p1 == p2: {p1 == p2}")


# =============================================
# 第八节：实战案例
# =============================================

print("\n=== 实战案例 ===")


# ========== 案例1：学生管理 ==========
print("\n--- 案例1：学生管理 ---")

class StudentManager:
    """
    学生管理类

    【作用】
    管理多个学生

    【方法】
    - add_student(student): 添加学生
    - show_all(): 显示所有学生
    - get_average(): 获取平均分
    """

    def __init__(self):
        """初始化"""
        self.students = []

    def add_student(self, student):
        """
        添加学生

        【参数】
        - student: Student 对象
        """

        self.students.append(student)

    def show_all(self):
        """显示所有学生"""

        for student in self.students:
            print(f"  {student.name}: {student.score}分")

    def get_average(self):
        """
        获取平均分

        【返回值】
        浮点数，平均分
        """

        if not self.students:
            return 0
        total = sum(s.score for s in self.students)
        return total / len(self.students)


# 创建学生类
class GraduateStudent:
    """研究生类"""

    def __init__(self, name, score):
        self.name = name
        self.score = score


# 使用
manager = StudentManager()
manager.add_student(GraduateStudent("小明", 85))
manager.add_student(GraduateStudent("小红", 92))
manager.add_student(GraduateStudent("小刚", 78))

manager.show_all()
print(f"平均分: {manager.get_average():.1f}")


# ========== 案例2：银行账户 ==========
print("\n--- 案例2：银行账户 ---")

class BankAccount:
    """
    银行账户类

    【属性】
    - owner: 户主
    - balance: 余额

    【方法】
    - deposit(amount): 存款
    - withdraw(amount): 取款
    - show_balance(): 显示余额
    """

    def __init__(self, owner, balance=0):
        """
        初始化

        【参数】
        - owner: 字符串，户主
        - balance: 数字，初始余额
        """

        self.owner = owner
        self.__balance = balance  # 私有属性

    def deposit(self, amount):
        """
        存款

        【参数】
        - amount: 数字，存款金额

        【返回值】
        self（支持链式调用）
        """

        if amount <= 0:
            raise ValueError("存款金额必须为正数")
        self.__balance += amount
        print(f"存入{amount}元")
        return self

    def withdraw(self, amount):
        """
        取款

        【参数】
        - amount: 数字，取款金额

        【返回值】
        self（支持链式调用）
        """

        if amount > self.__balance:
            raise ValueError("余额不足")
        self.__balance -= amount
        print(f"取出{amount}元")
        return self

    @property
    def balance(self):
        """
        获取余额

        【返回值】
        数字，当前余额
        """

        return self.__balance

    def show_balance(self):
        """显示余额"""

        print(f"{self.owner}的余额：{self.__balance}元")


# 使用
account = BankAccount("小明", 1000)
account.deposit(500)
account.withdraw(200)
account.show_balance()


# =============================================
# 【练习题】
# =============================================

# 【练习1：矩形类】
# 定义一个 Rectangle 类，表示矩形
# 属性：width（宽度）、height（高度）
# 方法：area() 计算面积、perimeter() 计算周长
# 提示：
#   1. 在 __init__ 中接收 width 和 height 参数
#   2. 面积 = width × height
#   3. 周长 = 2 × (width + height)
#   4. 创建一个 10×20 的矩形，测试面积和周长

# 【练习2：计数器类】
# 定义一个 Counter 类，实现计数器功能
# 属性：count（当前计数值）
# 方法：increment() 加 1、decrement() 减 1、reset() 重置为 0
# 提示：
#   1. 在 __init__ 中将 count 初始化为 0
#   2. increment() 让 count 加 1
#   3. decrement() 让 count 减 1
#   4. reset() 将 count 设为 0
#   5. 可选：实现 __str__ 方法，打印时显示 "Counter(count=数值)"

# 【练习3：形状继承】
# 定义一个 Shape 基类和两个子类 Circle（圆形）、Square（正方形）
# Shape 基类：定义 area() 和 perimeter() 方法（抛出 NotImplementedError）
# Circle 子类：属性 radius（半径），实现面积和周长计算
# Square 子类：属性 side（边长），实现面积和周长计算
# 提示：
#   1. 圆面积 = π × r²，圆周长 = 2 × π × r（用 math.pi）
#   2. 正方形面积 = side²，正方形周长 = 4 × side
#   3. 创建一个圆形和一个正方形，放入列表，用 for 循环调用 area() 和 perimeter()
#   4. 这就是多态：同一个方法名，不同类有不同的实现

# =============================================
# 练习参考答案
# =============================================
print("\n" + "="*50)
print("练习参考答案")
print("="*50 + "\n")

# 练习1 参考
print("--- 练习1 参考 ---")

class Rectangle:
    """
    矩形类

    【属性】
    - width: 宽度
    - height: 高度

    【方法】
    - area(): 面积
    - perimeter(): 周长
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """计算面积"""
        return self.width * self.height

    def perimeter(self):
        """计算周长"""
        return 2 * (self.width + self.height)


rect = Rectangle(10, 20)
print(f"面积: {rect.area()}")
print(f"周长: {rect.perimeter()}")


# 练习2：计数器类
print("\n--- 练习2 参考 ---")

class Counter:
    """
    计数器类

    【属性】
    - count: 计数

    【方法】
    - increment(): 增加
    - decrement(): 减少
    - reset(): 重置
    """

    def __init__(self):
        self.count = 0

    def increment(self):
        """增加"""
        self.count += 1

    def decrement(self):
        """减少"""
        self.count -= 1

    def reset(self):
        """重置"""
        self.count = 0

    def __str__(self):
        """字符串表示"""
        return f"Counter(count={self.count})"


counter = Counter()
counter.increment()
counter.increment()
counter.increment()
print(f"计数器: {counter}")
counter.decrement()
print(f"计数器: {counter}")


# 练习3：形状继承
print("\n--- 练习3 参考 ---")

import math

class Shape:
    """形状基类"""

    def area(self):
        """面积（子类实现）"""
        raise NotImplementedError

    def perimeter(self):
        """周长（子类实现）"""
        raise NotImplementedError


class Circle(Shape):
    """圆形"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    """正方形"""

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


shapes = [Circle(5), Square(6)]
for shape in shapes:
    print(f"{type(shape).__name__}: 面积={shape.area():.2f}, 周长={shape.perimeter():.2f}")


# =============================================
# 课程总结
# =============================================
"""
核心收获：
- 类用 class 定义，self 代表实例本身，__init__ 是构造方法
- 继承让子类复用父类代码，多态让不同子类对同一方法有不同实现
- 魔术方法如 __str__、__len__、__eq__ 让自定义类像内置类型一样好用

常见陷阱：
- 忘记在方法的第一个参数写 self，调用时会报"缺少参数"的错误
- 类属性是所有实例共享的，修改类属性会影响所有实例，实例属性才各是各的
- 多继承时方法解析顺序（MRO）可能不符合直觉，尽量用单继承加组合

下节课预告：
- 下节课学异常处理，让程序出错时不会直接崩溃
"""
