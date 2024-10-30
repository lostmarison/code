import tkinter as tk
from tkinter import messagebox

# 用于存储用户账户信息
user_database = {}


def register_user():
    def complete_registration():
        user_name = user_entry.get()
        user_password = password_entry.get()
        if user_name and user_password:  # 检查用户名和密码是否非空
            user_database[user_name] = user_password  # 存储账户信息
            messagebox.showinfo("注册", "注册成功")
            registration_window.destroy()  # 关闭注册窗口
        else:
            messagebox.showerror("错误", "用户名和密码不能为空")

    registration_window = tk.Toplevel()  # 创建注册窗口
    registration_window.title("用户注册")
    registration_window.geometry("300x150")
    registration_window.resizable(False, False)

    # 设置注册窗口的标签和输入框
    tk.Label(registration_window, text="账号：", font=("黑体", 15)).place(x=30, y=20)
    tk.Label(registration_window, text="密码：", font=("黑体", 15)).place(x=30, y=50)
    user_entry = tk.Entry(registration_window, width=12, font=("黑体", 15))
    user_entry.place(x=100, y=20)
    password_entry = tk.Entry(
        registration_window, width=12, font=("黑体", 15), show="*"
    )  # 增加 show="*" 以隐藏密码
    password_entry.place(x=100, y=50)

    # 设置注册按钮
    tk.Button(
        registration_window,
        command=complete_registration,
        text="注册",
        font=("黑体", 16),
        width=8,
    ).place(x=100, y=80)


# 主窗口的登录功能
def login_user():
    user_name = user_field.get()
    user_password = password_field.get()
    if user_name in user_database and user_database[user_name] == user_password:
        messagebox.showinfo("登录", "登录成功")
    else:
        messagebox.showerror("错误", "账号不存在或密码错误")


# 创建主窗口
main_window = tk.Tk()
main_window.title("用户登录与注册")  # 设置主窗口标题
main_window.geometry("500x300")  # 设置主窗口大小
main_window.resizable(False, False)  # 缩放锁定

# 设置主窗口的标签
tk.Label(main_window, text="账号：", font=("黑体", 26)).place(x=50, y=50)
tk.Label(main_window, text="密码：", font=("黑体", 26)).place(x=50, y=130)

# 创建字符串变量
user_field = tk.StringVar()
password_field = tk.StringVar()

# 设置主窗口输入框
tk.Entry(main_window, textvariable=user_field, width=15, font=("黑体", 26)).place(
    x=150, y=50
)
tk.Entry(
    main_window, textvariable=password_field, width=15, font=("黑体", 26), show="*"
).place(
    x=150, y=130
)  # 增加 show="*" 以隐藏密码

# 设置注册和登录按钮
tk.Button(
    main_window, command=register_user, text="注册新用户", font=("黑体", 26), width=12
).place(
    x=50, y=200
)  # 调整按钮文本和宽度
tk.Button(
    main_window, command=login_user, text="登录", font=("黑体", 26), width=8
).place(x=280, y=200)

# 运行主循环
main_window.mainloop()
