from datetime import datetime
import json
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

file_name = "taskApp.json"
bg_image_file = "smert.jpg"

def create_app():
    root = tk.Tk()
    root.title("Менеджер задач вась")
    root.geometry("900x625")

    tasks = []
    selected_index = None

    def save_task():
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)

    def load_task():
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="UTF-8") as file:
                tasks.extend(json.load(file))

    def select_task(index):
        nonlocal selected_index
        selected_index = index
        refresh_list()

    def refresh_list():
        listbox.delete("task_item")
        y = 15
        for i, task in enumerate(tasks):
            line = f"[{task['status']}] {task['title']} | дата вась:{task['deadline']} |важность вась:{task['priority']}"
            color = "#0A9E2D" if task["status"] == "готова вась" else "#A10505"
            if i == selected_index:
                listbox.create_rectangle(
                    5,
                    y - 10,
                    695,
                    y + 12,
                    fill="#E0E0E0",
                    outline="",
                    tags="task_item",
                )
            item_id = listbox.create_text(
                10,
                y,
                anchor="w",
                text=line,
                fill=color,
                font=("Arial", 10, "bold"),
                tags="task_item",
            )
            listbox.tag_bind(item_id, "<Button-1>", lambda e, idx=i: select_task(idx))
            y += 24

    def add_task():
        nonlocal selected_index
        title = title_entry.get().strip()
        today = datetime.now().strftime("%d.%m.%Y")
        deadline = deadline_entry.get().strip() or today
        priority = priority_var.get()

        if not title:
            messagebox.showerror("опущен кодом вась", "надо название а не это вот вась")
            return

        tasks.append({
            "title": title,
            "deadline": deadline,
            "priority": priority,
            "status": "не готова вась",
            })
        title_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        selected_index = None
        save_task()
        refresh_list()

    def mark_done():
        if selected_index is None:
            messagebox.showerror("опущен кодом вась", "задачу надо из списка выбрать вась")
            return

        if tasks[selected_index]["status"] == "готова вась":
            messagebox.showerror("опущен кодом вась", "уже готовая вась")
            return

        tasks[selected_index]["status"] = "готова вась"
        save_task()
        refresh_list()

    def mark_not_done():
        if selected_index is None:
            messagebox.showerror("опущен кодом вась", "задачу надо из списка выбрать вась")
            return

        if tasks[selected_index]["status"] == "не готова вась":
            messagebox.showerror("опущен кодом вась", "уже не готова вась")
            return

        tasks[selected_index]["status"] = "не готова вась"
        save_task()
        refresh_list()

    def delete_task():
        nonlocal selected_index
        if selected_index is None:
            messagebox.showerror("опущен кодом вась", "выбери задачу для удаления вась")
            return

        if selected_index is not None:
            ok1 = messagebox.askokcancel("опущен кодом васьь", "уверен вась?")
            if ok1:
                ok2 = messagebox.askokcancel("опущен кодом вась", "ты точно уверен вась??")
                if ok2:
                    ok3 = messagebox.askokcancel("опущен кодом вась", "ну прям наверняка вась???")
                    if ok3:
                        ok4 = messagebox.askokcancel("опущен кодом вась","а я вот чет не уверен а ты как вась????",)
                        if ok4:
                            ok5 = messagebox.askokcancel("опущен кодом вась","ну прям на все 100% вась?????",)
                            if ok5:
                                ok6 = messagebox.askokcancel("опущен кодом вась","все так же газ хочешь вась?????",)
                                if ok6:
                                    ok7 = messagebox.askokcancel("опущен кодом вась","прям все газик уверенный вась???????",)
                                    if ok7:
                                        ok8 = messagebox.askokcancel("опущен кодом вась","ну лан клацай давай вась",)
                                        if ok8:
                                            ok9 = messagebox.askokcancel(
                                                "опущен кодом вась","ну или не совсем реди вась",)
                                            if ok9:
                                                ok10 = messagebox.askokcancel("опущен кодом вась", "ну лан ща все будет вась",)
                                                if ok10:
                                                    tasks.pop(selected_index)
                                                    selected_index = None
                                                    save_task()
                                                    refresh_list()

    tk.Label(root, text="название задачи вась:").pack(pady=(10, 0))
    title_entry = tk.Entry(root, width=50)
    title_entry.pack()

    tk.Label(root, text="важность вась").pack(pady=(5, 0))
    priority_var = tk.StringVar(value="среднячоук вась")
    tk.OptionMenu(root,priority_var,"наивысший вась","такой сложноватый вась","среднячоук вась","карликовый вась",).pack()

    tk.Label(root, text="срок cдачи вась:").pack(pady=(5, 0))
    deadline_entry = tk.Entry(root, width=50)
    deadline_entry.pack()

    tk.Button(
        root, text="добавить задачу вась", command=add_task, width=20).pack(pady=12)

    listbox = tk.Canvas(root, width=700, height=300, bg="white")
    listbox.pack(pady=10)

    if os.path.exists(bg_image_file):
        img = Image.open(bg_image_file).resize((700, 300))
        bg_photo = ImageTk.PhotoImage(img)
        listbox.create_image(0, 0, anchor="nw", image=bg_photo)
        listbox.bg_photo = bg_photo

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(
        btn_frame, text="удалить задачу вась", command=delete_task).pack(pady=(0, 5))
    tk.Button(
        btn_frame, text="отметить готовой вась", command=mark_done).pack(side=tk.LEFT, padx=5)
    tk.Button(
        btn_frame, text="отметить не готовой вась", command=mark_not_done).pack(side=tk.LEFT, padx=5)

    root.bind("<Delete>", lambda event: delete_task())

    load_task()
    refresh_list()
    return root
