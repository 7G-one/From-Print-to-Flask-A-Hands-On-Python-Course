# -*- coding: utf-8 -*-
# =============================================
# 第 16 课：Web 开发入门
# =============================================
# 上节课我们学了项目实战。
# 这节课我们要学习 Web 开发——让程序在浏览器中运行。
#
# 用 Flask 框架搭建 Web 应用，理解路由、模板、表单和 RESTful API。

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# =============================================
# 第一节：什么是 Web 开发？
# =============================================

# 【生活类比：去餐厅吃饭】
# 想象你去餐厅吃饭：
#   1. 你（用户）坐在餐桌前（浏览器）
#   2. 服务员（前端）给你看菜单
#   3. 你点菜（发送请求）
#   4. 厨师（后端）做菜（处理请求）
#   5. 服务员把菜端给你（返回响应）

# 【Web 开发就是这样运作的】
#   1. 用户在浏览器输入网址（比如 http://localhost:5000/）
#   2. 浏览器把请求发送给服务器
#   3. 服务器上的 Python 程序收到请求
#   4. Python 程序处理请求，准备好数据
#   5. Python 程序把结果返回给浏览器
#   6. 浏览器把结果显示给用户

# 【两个重要概念：前端 vs 后端】
# 前端（Frontend）：用户看到和操作的部分
#   - HTML：页面的骨架（文字、图片、按钮）
#   - CSS：页面的样式（颜色、大小、布局）
#   - JavaScript：页面的行为（点击按钮后做什么）
#
# 后端（Backend）：服务器上运行的程序
#   - Python：处理业务逻辑
#   - 数据库：存储数据
#   - API：前后端之间的桥梁

# 【HTTP 请求的种类】
# GET：获取数据（比如查看网页、查看商品列表）
# POST：提交数据（比如提交表单、上传文件）
# PUT：更新数据（比如修改个人信息）
# DELETE：删除数据（比如删除一条记录）

# 【我们要学什么？】
# - Flask：一个轻量级的 Python Web 框架
# - 用它来创建网站和 API
# - 最后用 http.server 做一个可直接运行的演示


# =============================================
# 第二节：安装 Flask
# =============================================

# 【安装 Flask】
# 在命令行（终端）中输入：
#   pip install flask
#
# 【验证安装】
#   pip show flask
#
# 【如果安装失败？】
# 1. 检查网络连接
# 2. 使用国内镜像：
#    pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
#
# 【什么是 Flask？】
# Flask 是 Python 最流行的轻量级 Web 框架之一。
# "框架"就是别人写好的工具包，你不需要从零开始，
# 只需要告诉框架"当用户访问某个网址时，做什么事情"。

print("=" * 50)
print("第二小节：安装 Flask")
print("=" * 50)
print()
print("请在命令行中执行：pip install flask")
print("安装完成后，就可以运行本课后面的 Flask 示例了。")
print()


# =============================================
# 第三节：第一个 Flask 程序
# =============================================

# 【需求】
# 创建一个最简单的网站：访问首页，显示 "Hello, World!"
#
# 【代码结构】
# 1. 导入 Flask
# 2. 创建 Flask 应用
# 3. 定义路由（URL 和函数的对应关系）
# 4. 运行应用
#
# 【解释每一行】
# from flask import Flask     → 导入 Flask 类
# app = Flask(__name__)       → 创建一个 Flask 应用对象
# @app.route('/')             → 当用户访问首页（/）时
# def hello():                → 执行这个函数
#     return 'Hello!'         → 返回内容给浏览器
# app.run()                   → 启动服务器，开始监听请求

print("=" * 50)
print("第三小节：第一个 Flask 程序")
print("=" * 50)
print()

# 注意：下面的代码需要安装 Flask 才能运行
# 我们用 print() 展示代码内容，让你了解写法

flask_hello = '''
# 文件名：hello.py
# 这是最简单的 Flask 程序

from flask import Flask

# 创建 Flask 应用
# __name__ 是当前模块的名称，Flask 用它来定位资源文件
app = Flask(__name__)

# 定义路由
# @app.route('/') 的意思是：
#   当用户访问首页（URL 是 /）时，执行下面的函数
@app.route('/')
def hello():
    return 'Hello, World!'

# 启动服务器
# debug=True 表示调试模式（修改代码后自动重启，方便开发）
if __name__ == '__main__':
    app.run(debug=True)

# 运行方式：
#   1. 在终端执行：python hello.py
#   2. 在浏览器打开：http://localhost:5000/
#   3. 你会看到页面上显示：Hello, World!
'''

print("【第一个 Flask 程序的代码】")
print(flask_hello)


# =============================================
# 第四节：多个页面（路由）
# =============================================

# 【需求】
# 创建多个页面：
#   - 首页 /
#   - 关于页面 /about
#   - 联系页面 /contact
#
# 【路由是什么？】
# 路由就是"URL 到函数的映射"。
# 每个 URL 对应一个函数，用户访问不同的 URL，
# 就会执行不同的函数，看到不同的页面。
#
# 【调用流程】
# 用户访问 /about
#   → Flask 在路由表里查找 /about
#   → 找到 about() 函数
#   → 执行 about() 函数
#   → 把返回值发给浏览器
#   → 浏览器显示 "这是关于页面"

print("=" * 50)
print("第四小节：多个页面（路由）")
print("=" * 50)
print()

flask_routes = '''
# 文件名：routes.py

from flask import Flask

app = Flask(__name__)

# 首页
@app.route('/')
def index():
    return '欢迎来到首页！'

# 关于页面
@app.route('/about')
def about():
    return '这是关于页面'

# 联系页面
@app.route('/contact')
def contact():
    return '这是联系页面'

if __name__ == '__main__':
    app.run(debug=True)

# 运行后试试：
#   http://localhost:5000/        → 欢迎来到首页！
#   http://localhost:5000/about   → 这是关于页面
#   http://localhost:5000/contact → 这是联系页面
'''

print("【多个路由的代码】")
print(flask_routes)


# =============================================
# 第五节：带参数的路由
# =============================================

# 【需求】
# 创建一个页面，可以显示不同用户的信息：
#   - /user/小明 → 显示 "你好，小明！"
#   - /user/小红 → 显示 "你好，小红！"
#
# 【怎么实现？】
# 在路由中使用 <参数名> 作为占位符。
# Flask 会自动把 URL 中的值提取出来，传给函数。
#
# 【调用流程】
# 用户访问 /user/小明
#   → Flask 提取参数 name = "小明"
#   → 执行 user(name="小明") 函数
#   → 返回 "你好，小明！"

print("=" * 50)
print("第五小节：带参数的路由")
print("=" * 50)
print()

flask_params = '''
# 文件名：user.py

from flask import Flask

app = Flask(__name__)

# <name> 是 URL 参数
# 比如访问 /user/小明，name 的值就是 "小明"
@app.route('/user/<name>')
def user(name):
    return f'你好，{name}！'

# 还可以指定参数类型
# <int:id> 表示参数必须是整数
@app.route('/article/<int:article_id>')
def article(article_id):
    return f'你正在阅读第 {article_id} 篇文章'

if __name__ == '__main__':
    app.run(debug=True)

# 运行后试试：
#   http://localhost:5000/user/小明    → 你好，小明！
#   http://localhost:5000/user/小红    → 你好，小红！
#   http://localhost:5000/article/1    → 你正在阅读第 1 篇文章
'''

print("【带参数的路由代码】")
print(flask_params)


# =============================================
# 第六节：返回 HTML 页面
# =============================================

# 【需求】
# 之前返回的都是纯文本，现在返回完整的 HTML 页面。
# HTML 是网页的骨架，浏览器会把它渲染成漂亮的页面。
#
# 【怎么做？】
# 在函数中返回 HTML 字符串即可。
# Flask 会自动设置正确的响应头，告诉浏览器这是 HTML。

print("=" * 50)
print("第六小节：返回 HTML 页面")
print("=" * 50)
print()

flask_html = '''
# 文件名：html_page.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # 返回完整的 HTML 页面
    # 用三引号写多行字符串
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>我的网站</title>
    </head>
    <body>
        <h1>欢迎来到我的网站</h1>
        <p>这是一个 Flask 示例</p>
        <a href="/about">关于</a>
    </body>
    </html>
    """
    return html

@app.route('/about')
def about():
    return """
    <h1>关于</h1>
    <p>这是关于页面</p>
    <a href="/">返回首页</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
'''

print("【返回 HTML 页面的代码】")
print(flask_html)


# =============================================
# 第七节：模板引擎（Jinja2）
# =============================================

# 【什么是模板引擎？】
# 想象一下"填空题"：
#   HTML 模板就像一张有空位的试卷 {{ 变量 }}
#   Python 变量就像答案
#   模板引擎就是帮你把答案填进去的工具
#
# 【Jinja2 模板语法】
# {{ 变量 }}        → 显示变量的值
# {% for item in items %}  → 循环
# {% if 条件 %}     → 条件判断
#
# 【文件结构】
# 项目/
#   ├── app.py            ← Python 代码
#   └── templates/        ← 模板文件夹（必须叫这个名字）
#       └── index.html    ← HTML 模板
#
# 【为什么要用模板？】
# 如果用 f-string 拼接 HTML，代码会非常乱。
# 模板引擎让你把 Python 代码和 HTML 分开，各管各的。

print("=" * 50)
print("第七小节：模板引擎（Jinja2）")
print("=" * 50)
print()

flask_template_app = '''
# 文件名：app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 准备数据（变量）
    title = '我的网站'
    items = ['Python', 'Flask', 'Web开发']

    # 渲染模板
    # render_template() 会自动在 templates 文件夹中查找文件
    # 把变量 title 和 items 传给模板
    return render_template('index.html',
                           title=title,
                           items=items)

if __name__ == '__main__':
    app.run(debug=True)
'''

flask_template_html = '''
<!-- 文件名：templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>

    <h2>学习内容：</h2>
    <ul>
        <!-- for 循环：遍历 items 列表 -->
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>

    <!-- if 条件判断 -->
    {% if items %}
        <p>共 {{ items|length }} 项</p>
    {% else %}
        <p>暂无内容</p>
    {% endif %}
</body>
</html>
'''

print("【app.py 的代码】")
print(flask_template_app)
print()
print("【templates/index.html 的代码】")
print(flask_template_html)


# =============================================
# 第八节：处理表单
# =============================================

# 【需求】
# 用户在网页上填写表单，Python 程序处理数据。
# 比如：用户注册、搜索框、评论等。
#
# 【怎么实现？】
# 1. 创建一个显示表单的页面（GET 请求）
# 2. 用户填写表单，点击提交（POST 请求）
# 3. Python 程序用 request.form 获取表单数据
#
# 【调用流程】
# 用户访问 /（GET 请求）
#   → 显示表单页面
# 用户填写表单，点击提交
#   → 浏览器发送 POST 请求到 /submit
#   → Python 程序获取表单数据
#   → 返回处理结果

print("=" * 50)
print("第八小节：处理表单")
print("=" * 50)
print()

flask_form = '''
# 文件名：form.py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # 显示表单
    # 注意：表单的 method 是 POST，action 是 /submit
    return """
    <h1>用户注册</h1>
    <form method="POST" action="/submit">
        <p>姓名: <input type="text" name="name"></p>
        <p>年龄: <input type="number" name="age"></p>
        <p><input type="submit" value="提交"></p>
    </form>
    """

@app.route('/submit', methods=['POST'])
def submit():
    # 获取表单数据
    # request.form 是一个字典，存储了表单里所有的字段
    name = request.form['name']    # 获取姓名
    age = request.form['age']      # 获取年龄

    # 返回结果
    return f"""
    <h1>注册成功</h1>
    <p>姓名: {name}</p>
    <p>年龄: {age}</p>
    <a href="/">返回</a>
    """

if __name__ == '__main__':
    app.run(debug=True)

# 运行后试试：
#   1. 打开 http://localhost:5000/
#   2. 填写姓名和年龄
#   3. 点击提交
#   4. 看到 "注册成功" 页面
'''

print("【处理表单的代码】")
print(flask_form)


# =============================================
# 第九节：RESTful API
# =============================================

# 【什么是 API？】
# API（Application Programming Interface）是程序之间的接口。
# 就像餐厅的菜单：你不用知道菜是怎么做的，
# 只需要告诉服务员"我要这个菜"，就能得到结果。
#
# 【什么是 RESTful API？】
# 一种 API 设计风格，用 HTTP 方法表示操作：
#   GET    /api/users     → 获取所有用户（读取）
#   GET    /api/users/1   → 获取 ID 为 1 的用户
#   POST   /api/users     → 创建一个新用户
#   PUT    /api/users/1   → 更新 ID 为 1 的用户
#   DELETE /api/users/1   → 删除 ID 为 1 的用户
#
# 【为什么用 JSON？】
# JSON 是一种轻量级的数据格式，前后端都认识。
# 就像一种"通用语言"，Python 把数据转成 JSON，
# 前端收到 JSON 后，就能解析成自己需要的格式。

print("=" * 50)
print("第九小节：RESTful API")
print("=" * 50)
print()

flask_api = '''
# 文件名：api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟数据（实际项目中会用数据库）
users = [
    {"id": 1, "name": "小明", "age": 18},
    {"id": 2, "name": "小红", "age": 20},
]

# GET /api/users → 获取所有用户
@app.route('/api/users', methods=['GET'])
def get_users():
    # jsonify 把 Python 字典/列表转成 JSON 格式
    return jsonify(users)

# GET /api/users/1 → 获取单个用户
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 在列表中查找指定 ID 的用户
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    # 找不到就返回 404 错误
    return jsonify({"error": "用户不存在"}), 404

# POST /api/users → 创建新用户
@app.route('/api/users', methods=['POST'])
def create_user():
    # 获取前端发来的 JSON 数据
    data = request.get_json()
    # 创建新用户
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }
    users.append(new_user)
    # 返回新用户，201 表示"创建成功"
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)

# 测试 API（用 curl 命令）：
# 获取所有用户：curl http://localhost:5000/api/users
# 创建新用户：
#   curl -X POST -H "Content-Type: application/json" \\
#        -d '{"name": "小刚", "age": 22}' \\
#        http://localhost:5000/api/users
'''

print("【RESTful API 的代码】")
print(flask_api)


# =============================================
# 第十节：完整示例 - 待办事项 API
# =============================================

# 【需求】
# 做一个待办事项（Todo List）的 API：
#   GET    /api/todos     → 获取所有待办
#   POST   /api/todos     → 创建待办
#   PUT    /api/todos/1   → 更新待办
#   DELETE /api/todos/1   → 删除待办
#
# 【设计思路】
# 1. 用列表存储待办事项
# 2. 每个待办是一个字典 {id, title, done}
# 3. 用 jsonify 返回 JSON 数据
#
# 【为什么选待办事项？】
# 它涵盖了最常见的 CRUD 操作（Create/Read/Update/Delete），
# 学会了这个，你就能做任何管理系统了。

print("=" * 50)
print("第十小节：完整示例 - 待办事项 API")
print("=" * 50)
print()

flask_todo = '''
# 文件名：todo_api.py

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# 数据存储（实际项目中会用数据库）
todos = []
next_id = 1

# GET /api/todos → 获取所有待办
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# POST /api/todos → 创建待办
@app.route('/api/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()

    todo = {
        "id": next_id,
        "title": data["title"],
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    todos.append(todo)
    next_id += 1

    return jsonify(todo), 201

# PUT /api/todos/1 → 更新待办
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    # 查找待办
    for todo in todos:
        if todo["id"] == todo_id:
            data = request.get_json()
            if "title" in data:
                todo["title"] = data["title"]
            if "done" in data:
                todo["done"] = data["done"]
            return jsonify(todo)

    return jsonify({"error": "任务不存在"}), 404

# DELETE /api/todos/1 → 删除待办
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "已删除"})

if __name__ == '__main__':
    app.run(debug=True)

# 测试命令：
# 获取所有：curl http://localhost:5000/api/todos
# 创建待办：curl -X POST -H "Content-Type: application/json" \\
#               -d '{"title": "学习Python"}' http://localhost:5000/api/todos
# 更新待办：curl -X PUT -H "Content-Type: application/json" \\
#               -d '{"done": true}' http://localhost:5000/api/todos/1
# 删除待办：curl -X DELETE http://localhost:5000/api/todos/1
'''

print("【待办事项 API 的代码】")
print(flask_todo)


# =============================================
# 第十一节：可运行演示（http.server）
# =============================================

# 上面的代码都需要安装 Flask 才能运行。
# 下面用 Python 标准库 http.server 做一个可直接运行的演示，
# 让你在不安装 Flask 的情况下，也能体验 Web 开发的基本流程！
#
# http.server 是 Python 自带的，不需要安装任何东西。

print("=" * 50)
print("第十一小节：可运行演示（http.server）")
print("=" * 50)
print()


# ========== 1. 定义请求处理器 ==========

class SimpleWebHandler(BaseHTTPRequestHandler):
    """
    简易 Web 请求处理器

    【作用】
    处理浏览器发来的请求，返回 HTML 或 JSON

    【类比 Flask】
    - do_GET()  对应  @app.route('/xxx', methods=['GET'])
    - do_POST() 对应  @app.route('/xxx', methods=['POST'])
    - self.path 对应  请求的 URL 路径
    """

    # 模拟数据（相当于 Flask 应用里的全局变量）
    todos = [
        {"id": 1, "title": "学习 Python", "done": False},
        {"id": 2, "title": "学习 Web 开发", "done": False},
        {"id": 3, "title": "做项目实战", "done": True},
    ]

    def do_GET(self):
        """
        处理 GET 请求（用户在浏览器输入网址，或点击链接）

        【类比 Flask】
        @app.route('/')
        def index():
            return 'Hello!'
        """

        # ---------- 路由：首页 ----------
        if self.path == "/" or self.path == "/index":
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>首页</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }
                    a { display: block; margin: 10px 0; font-size: 18px; }
                    h1 { color: #333; }
                </style>
            </head>
            <body>
                <h1>欢迎来到首页！</h1>
                <p>这是一个用 Python http.server 搭建的简易网站。</p>
                <a href="/about">关于页面</a>
                <a href="/api/todos">查看待办事项（JSON API）</a>
                <a href="/form">添加待办事项</a>
                <a href="/hello/小明">带参数的路由示例</a>
            </body>
            </html>
            """
            self.send_html(html)

        # ---------- 路由：关于页面 ----------
        elif self.path == "/about":
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>关于</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }
                    a { font-size: 18px; }
                </style>
            </head>
            <body>
                <h1>关于本项目</h1>
                <p>这是一个用 Python 标准库 http.server 搭建的演示网站。</p>
                <p>它展示了 Web 开发的基本概念：</p>
                <ul>
                    <li>路由（URL 到函数的映射）</li>
                    <li>返回 HTML 页面</li>
                    <li>返回 JSON 数据（API）</li>
                    <li>处理表单提交</li>
                    <li>带参数的路由</li>
                </ul>
                <a href="/">返回首页</a>
            </body>
            </html>
            """
            self.send_html(html)

        # ---------- 带参数的路由 ----------
        elif self.path.startswith("/hello/"):
            # 从 URL 中提取名字
            name = self.path[7:]  # 去掉 "/hello/" 前缀
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>问候</title>
                <style>
                    body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }}
                </style>
            </head>
            <body>
                <h1>你好，{name}！</h1>
                <p>这是一个带参数的路由示例。</p>
                <p>URL: /hello/{name} → 提取参数 name = "{name}"</p>
                <a href="/">返回首页</a>
            </body>
            </html>
            """
            self.send_html(html)

        # ---------- API：返回 JSON 数据 ----------
        elif self.path == "/api/todos":
            self.send_json(self.todos)

        # ---------- 路由：表单页面 ----------
        elif self.path == "/form":
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>添加待办</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }
                    input[type="text"] { padding: 8px; width: 100%%; box-sizing: border-box; }
                    input[type="submit"] {
                        background: #4CAF50; color: white; border: none;
                        padding: 10px 20px; cursor: pointer; margin-top: 10px;
                    }
                </style>
            </head>
            <body>
                <h1>添加待办事项</h1>
                <form method="POST" action="/add_todo">
                    <p>任务名称：</p>
                    <input type="text" name="title" placeholder="请输入任务...">
                    <p><input type="submit" value="添加"></p>
                </form>
                <a href="/">返回首页</a>
            </body>
            </html>
            """
            self.send_html(html)

        # ---------- 404 页面 ----------
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = "<h1>404 - 页面不存在</h1><a href='/'>返回首页</a>"
            self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        """
        处理 POST 请求（用户提交表单）

        【类比 Flask】
        @app.route('/add_todo', methods=['POST'])
        def add_todo():
            title = request.form['title']
            ...
        """

        if self.path == "/add_todo":
            # 读取请求体（表单数据）
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            # parse_qs 把 "title=学习Python" 解析成 {"title": ["学习Python"]}
            params = parse_qs(body)

            title = params.get("title", [""])[0]

            if title:
                # 添加到待办列表
                new_id = max((t["id"] for t in self.todos), default=0) + 1
                self.todos.append({
                    "id": new_id,
                    "title": title,
                    "done": False
                })

                html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>添加成功</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }}
                        a {{ display: block; margin: 10px 0; font-size: 18px; }}
                    </style>
                </head>
                <body>
                    <h1>添加成功！</h1>
                    <p>已添加任务：{title}</p>
                    <a href="/api/todos">查看所有待办</a>
                    <a href="/form">继续添加</a>
                    <a href="/">返回首页</a>
                </body>
                </html>
                """
                self.send_html(html)
            else:
                self.send_html("<h1>任务名称不能为空！</h1><a href='/form'>返回</a>")

        else:
            self.send_response(404)
            self.end_headers()

    def send_html(self, html):
        """发送 HTML 响应"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def send_json(self, data):
        """发送 JSON 响应（类似 Flask 的 jsonify）"""
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        self.wfile.write(json_str.encode("utf-8"))

    def log_message(self, format, *args):
        """自定义日志格式（让输出更清晰）"""
        print(f"  [请求] {args[0]}")


# ========== 2. 启动服务器 ==========

def run_demo_server(port=8080):
    """
    启动简易 Web 服务器

    【参数】
    - port: 端口号（默认 8080）

    【启动后】
    在浏览器中访问 http://localhost:8080/
    """
    server = HTTPServer(("127.0.0.1", port), SimpleWebHandler)
    print(f"\n服务器已启动！请在浏览器中访问：")
    print(f"  http://localhost:{port}/")
    print(f"\n可用页面：")
    print(f"  /              → 首页")
    print(f"  /about         → 关于页面")
    print(f"  /hello/你的名字 → 带参数的路由")
    print(f"  /api/todos     → 待办事项 API（JSON）")
    print(f"  /form          → 添加待办的表单")
    print(f"\n按 Ctrl+C 停止服务器")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        server.server_close()


# ========== 3. 运行 ==========

# 取消下面这行的注释，就可以启动服务器
# run_demo_server()

print("【提示】取消最后一行 run_demo_server() 的注释，")
print("然后运行此文件，即可在浏览器中体验 Web 开发！")
print("（启动后在浏览器访问 http://localhost:8080/ ）")
print()


# =============================================
# 【练习题】
# =============================================

print("=" * 50)
print("练习题")
print("=" * 50)
print()


# ----- 练习 1：个人博客 -----
print("--- 练习 1：个人博客 ---")
print("""
需求：
  用 Flask 创建一个个人博客：
  - 首页显示文章列表
  - 点击文章标题，进入文章详情页
  - 有一个"关于"页面

提示：
  1. 用列表存储文章，每篇文章是字典 {title, content, date}
  2. 创建路由 /（首页）、/article/<id>（详情）、/about（关于）
  3. 用模板引擎渲染 HTML

调用流程：
  用户访问首页 → 显示文章列表 → 点击标题 → 显示文章详情
""")
print()


# ----- 练习 2：留言板 -----
print("--- 练习 2：留言板 ---")
print("""
需求：
  用 Flask 创建一个留言板：
  - 用户可以填写昵称和留言内容
  - 提交后显示所有留言
  - 支持回复（给某条留言添加回复）

提示：
  1. 用列表存储留言，每条留言是字典 {name, message, time, replies}
  2. 创建路由 /（显示留言+处理新留言）、/reply/<id>（处理回复）
  3. 用 request.method 区分 GET（显示页面）和 POST（处理提交）

调用流程：
  用户访问 / → 看到留言列表和表单 → 填写留言 → 提交 → 页面刷新显示新留言
""")
print()


# ----- 练习 3：天气查询 -----
print("--- 练习 3：天气查询 ---")
print("""
需求：
  用 Flask 创建一个天气查询页面：
  - 输入城市名
  - 显示该城市的天气信息（可以用模拟数据）

提示：
  1. 用字典存储天气数据，如 {'北京': {'temp': 5, 'weather': '晴'}}
  2. 创建路由 /（显示查询表单）、/weather（查询结果）
  3. 用 request.form 获取用户输入的城市名

调用流程：
  用户访问 / → 输入城市名 → 提交 → 显示天气信息
""")
print()


# ----- 练习 4：计算器 Web 版 -----
print("--- 练习 4：计算器 Web 版 ---")
print("""
需求：
  用 Flask 创建一个 Web 计算器：
  - 显示两个输入框和运算符选择
  - 点击计算按钮，显示结果
  - 保存计算历史

提示：
  1. 前端用 JavaScript 的 fetch() 发送 POST 请求
  2. 后端用 request.get_json() 获取数据
  3. 用 jsonify() 返回结果
  4. 用列表保存计算历史

调用流程：
  用户输入数字 → 点击计算 → JavaScript 发送请求 → Python 计算 → 返回结果
""")
print()


# ----- 练习 5：文件管理器 -----
print("--- 练习 5：文件管理器 ---")
print("""
需求：
  用 Flask 创建一个简易文件管理器：
  - 显示服务器上的文件列表
  - 支持上传文件
  - 支持下载文件
  - 支持删除文件

提示：
  1. 用 os.listdir() 获取文件列表
  2. 用 request.files 获取上传的文件
  3. 用 send_file() 返回下载文件
  4. 用 os.remove() 删除文件

调用流程：
  用户访问 / → 看到文件列表 → 上传/下载/删除操作
""")
print()


# =============================================
# 练习参考答案
# =============================================

print("=" * 50)
print("练习参考答案")
print("=" * 50)
print()


# ----- 练习 1 参考答案 -----
print("--- 练习 1 参考答案：个人博客 ---")
print()

answer_blog_app = '''
# 文件名：blog_app.py

from flask import Flask, render_template

app = Flask(__name__)

# 模拟文章数据
articles = [
    {"id": 0, "title": "第一篇文章", "content": "这是我的第一篇博客！", "date": "2024-01-15"},
    {"id": 1, "title": "学习Python", "content": "Python 真的很好学。", "date": "2024-01-16"},
    {"id": 2, "title": "Web开发入门", "content": "Flask 让 Web 开发变得简单。", "date": "2024-01-17"},
]

@app.route('/')
def index():
    """首页：显示文章列表"""
    return render_template('blog_index.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    """文章详情页"""
    if 0 <= id < len(articles):
        return render_template('blog_article.html', article=articles[id])
    return '<h1>文章不存在</h1><a href="/">返回首页</a>'

@app.route('/about')
def about():
    """关于页面"""
    return render_template('blog_about.html')

if __name__ == '__main__':
    app.run(debug=True)
'''

answer_blog_index = '''
<!-- templates/blog_index.html -->
<h1>我的博客</h1>
{% for article in articles %}
    <h2><a href="/article/{{ article.id }}">{{ article.title }}</a></h2>
    <p>{{ article.date }}</p>
{% endfor %}
<a href="/about">关于</a>
'''

answer_blog_article = '''
<!-- templates/blog_article.html -->
<h1>{{ article.title }}</h1>
<p>日期: {{ article.date }}</p>
<hr>
<p>{{ article.content }}</p>
<a href="/">返回首页</a>
'''

print("app.py:")
print(answer_blog_app)
print("templates/blog_index.html:")
print(answer_blog_index)
print("templates/blog_article.html:")
print(answer_blog_article)


# ----- 练习 2 参考答案 -----
print("--- 练习 2 参考答案：留言板 ---")
print()

answer_message_app = '''
# 文件名：message_app.py

from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    """首页：显示留言 + 处理新留言"""
    if request.method == 'POST':
        name = request.form.get('name', '匿名')
        message = request.form.get('message', '')
        if message:
            messages.append({
                'name': name,
                'message': message,
                'time': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'replies': []
            })
    return render_template('message_board.html', messages=messages)

@app.route('/reply/<int:msg_id>', methods=['POST'])
def reply(msg_id):
    """处理回复"""
    if 0 <= msg_id < len(messages):
        reply_text = request.form.get('reply', '')
        if reply_text:
            messages[msg_id]['replies'].append(reply_text)
    return render_template('message_board.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
'''

answer_message_html = '''
<!-- templates/message_board.html -->
<h1>留言板</h1>
<form method="POST">
    <p>昵称: <input type="text" name="name" placeholder="匿名"></p>
    <p><textarea name="message" placeholder="写下你的留言..."></textarea></p>
    <p><input type="submit" value="提交留言"></p>
</form>
<hr>
{% for i in range(messages|length) %}
    {% set msg = messages[i] %}
    <h3>{{ msg.name }} ({{ msg.time }})</h3>
    <p>{{ msg.message }}</p>
    {% for reply in msg.replies %}
        <p style="margin-left:30px">回复: {{ reply }}</p>
    {% endfor %}
    <form method="POST" action="/reply/{{ i }}" style="margin-left:30px">
        <input type="text" name="reply" placeholder="回复...">
        <input type="submit" value="回复">
    </form>
    <hr>
{% endfor %}
'''

print("app.py:")
print(answer_message_app)
print("templates/message_board.html:")
print(answer_message_html)


# ----- 练习 3 参考答案 -----
print("--- 练习 3 参考答案：天气查询 ---")
print()

answer_weather_app = '''
# 文件名：weather_app.py

from flask import Flask, request, render_template

app = Flask(__name__)

# 模拟天气数据（实际项目中可调用天气 API）
weather_data = {
    '北京': {'temp': 5, 'weather': '晴', 'humidity': 30},
    '上海': {'temp': 12, 'weather': '多云', 'humidity': 65},
    '广州': {'temp': 22, 'weather': '小雨', 'humidity': 80},
    '深圳': {'temp': 24, 'weather': '阴', 'humidity': 70},
}

@app.route('/')
def index():
    """首页：显示查询表单"""
    return render_template('weather_form.html')

@app.route('/weather', methods=['POST'])
def weather():
    """查询天气"""
    city = request.form.get('city', '')
    data = weather_data.get(city)
    return render_template('weather_result.html', city=city, data=data)

if __name__ == '__main__':
    app.run(debug=True)
'''

answer_weather_result = '''
<!-- templates/weather_result.html -->
<h1>{{ city }} 的天气</h1>
{% if data %}
    <p>温度: {{ data.temp }} C</p>
    <p>天气: {{ data.weather }}</p>
    <p>湿度: {{ data.humidity }}%</p>
{% else %}
    <p>未找到该城市的天气数据</p>
{% endif %}
<a href="/">返回</a>
'''

print("app.py:")
print(answer_weather_app)
print("templates/weather_result.html:")
print(answer_weather_result)


# ----- 练习 4 参考答案 -----
print("--- 练习 4 参考答案：计算器 Web 版 ---")
print()

answer_calc_app = '''
# 文件名：calc_app.py

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

history = []  # 计算历史

@app.route('/')
def index():
    """显示计算器界面"""
    return render_template('calculator.html', history=history)

@app.route('/calculate', methods=['POST'])
def calculate():
    """处理计算请求"""
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    op = data.get('op', '+')

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = '错误: 除数不能为零' if b == 0 else a / b
    else:
        result = '未知运算符'

    history.append(f'{a} {op} {b} = {result}')
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
'''

answer_calc_html = '''
<!-- templates/calculator.html (核心部分) -->
<h1>Web 计算器</h1>
<input id="a" type="number" value="0">
<select id="op">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="*">*</option>
    <option value="/">/</option>
</select>
<input id="b" type="number" value="0">
<button onclick="calc()">=</button>
<span id="result"></span>

<h3>计算历史</h3>
<ul>
{% for h in history %}
    <li>{{ h }}</li>
{% endfor %}
</ul>

<script>
function calc() {
    fetch('/calculate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            a: parseFloat(document.getElementById('a').value),
            b: parseFloat(document.getElementById('b').value),
            op: document.getElementById('op').value
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').textContent = data.result;
    });
}
</script>
'''

print("app.py:")
print(answer_calc_app)
print("templates/calculator.html:")
print(answer_calc_html)


# ----- 练习 5 参考答案 -----
print("--- 练习 5 参考答案：文件管理器 ---")
print()

answer_file_app = '''
# 文件名：file_manager_app.py

import os
from flask import Flask, request, send_file, render_template, redirect

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """显示文件列表"""
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('file_manager.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    """上传文件"""
    file = request.files.get('file')
    if file and file.filename:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect('/')

@app.route('/download/<filename>')
def download(filename):
    """下载文件"""
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

@app.route('/delete/<filename>')
def delete(filename):
    """删除文件"""
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
'''

answer_file_html = '''
<!-- templates/file_manager.html -->
<h1>文件管理器</h1>
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="上传">
</form>
<ul>
{% for f in files %}
    <li>
        {{ f }}
        <a href="/download/{{ f }}">下载</a>
        <a href="/delete/{{ f }}">删除</a>
    </li>
{% endfor %}
</ul>
'''

print("app.py:")
print(answer_file_app)
print("templates/file_manager.html:")
print(answer_file_html)


# =============================================
# 课程总结
# =============================================

# 核心收获：
#   1. Web 开发的本质是"请求-处理-响应"：浏览器发请求，服务器处理，返回结果
#   2. Flask 用 @app.route() 定义路由，每个路由对应一个视图函数
#   3. RESTful API 用 GET/POST/PUT/DELETE 四种方法对应读取/创建/更新/删除操作
#
# 常见陷阱：
#   1. 忘记设置 methods=['POST']：默认路由只接受 GET 请求，表单提交会报 405 错误
#   2. debug=True 只用于开发：部署到生产环境时必须关闭，否则会暴露源码和错误信息
#   3. 表单数据没有验证就直接使用：可能导致 XSS 注入等安全问题


# =============================================
# 课程完结总结
# =============================================

# 恭喜你完成了 Python 基础课程！
#
# 你已经掌握了：
#   00-07：Python 基础（变量、类型、运算符、字符串、列表、字典、条件、循环）
#   08-13：Python 进阶（闭包与装饰器、文件、OOP、异常、模块与包、生成器与迭代器）
#   14-16：项目实战（开发实战入门、项目实战、Web 开发入门）
#
# 接下来你可以：
#   1. 学习 Django/Flask 深入 Web 开发
#   2. 学习 pandas/numpy 做数据分析
#   3. 学习 requests/BeautifulSoup 做爬虫
#   4. 参与开源项目，在实战中成长
#
# Python 是最好的第一门编程语言。
# 你已经迈出了最重要的一步，继续加油！
