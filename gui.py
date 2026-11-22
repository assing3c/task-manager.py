import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

file_name = "taskApp.json"

def create_app():
    root = tk.Tk()
    root.title ("Менеджер задач вась")
    root.geometry ("900x600")
    
    tasks = []
    
    def save_task():
        with open (file_name, "w", encoding="UTF-8") as file:
            json.dump (tasks, file, ensure_ascii=False, indent=4)
        
    def load_task ():
        if os.path.exists(file_name):
            with open (file_name, "r", encoding="UTF-8") as file:
                tasks.extend (json.load(file))
        
    def refresh_list():
        listbox.delete (0, tk.END)
        for task in tasks:
            line = f"[{task['status']}] {task['title']} | дата вась:{task['deadline']} |важность вась:{task['priority']}"
            listbox.insert (tk.END, line)
            if task["status"] == "выполнена вась":
                listbox.itemconfig(tk.END, fg = "#0A9E2D")
            else:
                listbox.itemconfig(tk.END, fg = "#A10505")
        
    def add_task ():
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
            "status": "не готова вась"
        })
        title_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
        save_task()
        refresh_list()
        
    def mark_done():
        selected = listbox.curselection()
        if not selected:
            messagebox.showerror("опущен кодом вась", "задачу надо из списка выбрать вась")
            return
        if selected:
            messagebox.showerror("опущен кодом вась","уже готовая вась")
        index = selected[0]
        tasks [index] ["status"]= "выполнена вась"
        save_task()
        refresh_list()
        
    def delete_task():
        selected = listbox.curselection()
        if not selected:
            messagebox.showerror("опущен кодом вась", "выбери задачу для удаления вась")
            return
        if selected:
            ok1 = messagebox.askokcancel("опущен кодом васьь","уверен вась?")
            if ok1:
                ok2 = messagebox.askokcancel("опущен кодом вась","ты точно уверен вась??")
                if ok2:
                    ok3 = messagebox.askokcancel("опущен кодом вась","ну прям наверняка вась???")
                    if ok3:
                        ok4 = messagebox.askokcancel("опущен кодом вась","а я вот чет не уверен а ты как вась????")
                        if ok4:
                            ok5 = messagebox.askokcancel("опущен кодом вась","ну прям на все 100% вась?????")
                            if ok5:
                                ok6 = messagebox.askokcancel("опущен кодом вась","все так же газ хочешь вась?????")
                                if ok6:
                                    ok7 = messagebox.askokcancel("опущен кодом вась","прям все газик уверенный вась???????")
                                    if ok7:
                                        ok8 = messagebox.askokcancel("опущен кодом вась","ну лан клацай давай вась")
                                        if ok8:
                                            ok9 = messagebox.askokcancel("опущен кодом вась","ну или не совсем реди вась")
                                            if ok9:
                                                ok10 = messagebox.askokcancel("опущен кодом вась","ну лан ща все будет вась")
                                                index = selected[0]
                                                tasks.pop(index)
                                                save_task()
                                                refresh_list()

    tk.Label(root, text = "название задачи вась:").pack(pady = (10,0))
    title_entry = tk.Entry(root, width=50)
    title_entry.pack()

    tk.Label(root, text ="важность вась").pack(pady= (5,0))
    priority_var = tk.StringVar(value="среднячоук вась")
    tk.OptionMenu(root, priority_var, "наивысший вась", "такой сложноватый вась","среднячоук вась","карликовый вась").pack()

    tk.Label(root, text="срок cдачи вась:").pack(pady=(5,0))
    deadline_entry = tk.Entry(root, width=50)
    deadline_entry.pack

    tk.Button(root, text="добавить задачу вась", command=add_task, width=20).pack(pady=12)

    listbox = tk.Listbox(root, width=100, height=20)
    listbox.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    
    tk.Button(btn_frame, text="отметить выполненой вась", command=mark_done).pack(padx=10)

    tk.Button(btn_frame, text="удалить задачу вась",command=delete_task).pack(side=tk.LEFT,padx=10)
    
    listbox.bind("<Delete>", lambda event: delete_task())
    
    load_task()
    return root