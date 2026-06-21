# 🐍 Python Chalkboard-Style Teaching Course

<h3 align="center"><a href="README.md">中文</a> | <a href="README_en.md">English</a></h3>

> From print("Hello World") to building a Flask web application

## What is this?

A beginner-friendly course for people who **want to learn Python but don't know where to start**.

This isn't a "look at the code and figure it out yourself" kind of course — every lesson comes with a **runnable hands-on project, 3 exercises, and real-life analogies**. 17 lessons take you from `print()` all the way to building your own Flask web application.

Functions are taught in lesson 2 (not lesson 8), closures and decorators are combined into one lesson (not split into two), and every lesson has complete code you can run right away. By the end, you'll understand why Python is the best first programming language.

## How do I run it?

```bash
# Navigate to the course directory
cd "d:/VS project/Mimo project/s_python"

# Run any lesson
python 00_零基础入门.py
python 01_变量与数据类型.py
...
python 17_Web开发入门.py
```

## What will I learn?

### Phase 1: Building the Foundation 🏗️
Learn to "talk" to Python first. Variables, functions, strings, lists — the building blocks of all Python code.

| # | What you'll build | What you'll pick up along the way |
|---|-------------------|-----------------------------------|
| 00 | Hello World + personal info card | print, variables, comments |
| 01 | Temperature converter | Data types, f-strings, type conversion |
| 02 | Calculator functions | Function definitions, parameters, return values, scope |
| 03 | Password strength checker | String methods, slicing, split/join |
| 04 | Student grade statistics | Lists, tuples, list comprehensions |
| 05 | Word frequency counter | Dictionaries, sets, dict comprehensions |
| 06 | Number guessing game | if/elif/else, match-case |
| 07 | Multiplication table generator | for/while, break/continue |

### Phase 2: Advanced Skills ⚡
Start writing "advanced" code. Closures, decorators, files, OOP — Python's killer features.

| # | What you'll build | What you'll pick up along the way |
|---|-------------------|-----------------------------------|
| 08 | Closures & decorators | nonlocal, lambda, @syntax, timer/cache/retry |
| 09 | Log analyzer | File I/O, CSV, JSON |
| 10 | Student management system | Classes, inheritance, polymorphism, magic methods |
| 11 | Safe division + retry mechanism | try/except, custom exceptions |
| 12 | Create your own module | import, pip, __name__ |
| 13 | Data pipeline | Generators, yield, itertools |

### Phase 3: Capstone Projects 🎯
Put it all together. From command-line tools to web applications.

| # | What you'll build | What's involved |
|---|-------------------|-----------------|
| 14 | Development intro | Calculator + to-do list |
| 15 | Full student management system | OOP + JSON persistence |
| 16 | Flask web application | Routing + templates + RESTful API |

## What does the file structure look like?

```
s_python/
├── 00_零基础入门.py           ← Start here
├── 01_变量与数据类型.py       ← Temperature converter
├── 02_函数基础.py             ← Functions taught early!
├── 03_字符串操作.py           ← Password strength checker
├── 04_列表与元组.py           ← Student grade statistics
├── 05_字典与集合.py           ← Word frequency counter
├── 06_条件语句.py             ← Number guessing game
├── 07_循环语句.py             ← Multiplication table
├── 08_闭包与装饰器.py         ← timer/cache/retry decorators
├── 09_文件操作.py             ← Log analyzer
├── 10_面向对象编程.py         ← Student management system
├── 11_异常处理.py             ← Safe division
├── 12_模块与包.py             ← Create your own module
├── 13_生成器与迭代器.py       ← Data pipeline
├── 14_开发实战入门.py         ← Calculator + to-do list
├── 15_项目实战.py             ← Full student management system
├── 16_Web开发入门.py          ← Flask API
└── README.md                 ← You're reading this one
```

## A Few Tips

1. **Don't skip lessons** — Later lessons build on earlier ones; skip ahead and you'll be lost
2. **Don't just read** — Run the code directly, change parameters, see how the results change
3. **Do the exercises** — They're not decoration; try writing them yourself before checking the answers
4. **Use functions** — Functions are taught in lesson 2; every lesson after that organizes code with functions
5. **Don't fear errors** — Python's error messages are friendly and readable; take the time to read them

## Requirements

- **Python 3.7+** — Download from [python.org](https://python.org)
- **Editor** — VS Code + Python extension recommended

## Course Highlights

- 🎯 **Real-life analogies** — Every lesson includes them, turning abstract concepts into everyday examples
- 📝 **Line-by-line comments** — Detailed explanations for every line of code
- 🧮 **Hands-on projects** — Not isolated code snippets, but complete programs you can actually run
- ⚠️ **Common pitfalls** — Highlights mistakes beginners often make, so you can avoid them
- 📋 **Exercises** — 3 per lesson, with problem descriptions + hints + reference solutions
- 🔧 **Functions first** — Functions taught in lesson 2, used to organize code in every lesson after

## Learning Roadmap

```
Getting Started (00)
    ↓
Variables + Functions (01-02)    ← Functions taught early!
    ↓
Data Structures (03-05)       ← Strings, lists, dictionaries
    ↓
Control Flow (06-07)          ← Conditionals, loops
    ↓
Advanced Features (08-13)     ← Closures, decorators, OOP, generators
    ↓
Capstone Projects (14-16)     ← Calculator, student management, Flask web
```

---

> "Python is the best first programming language. After finishing this course, you'll be able to solve real problems with code."
