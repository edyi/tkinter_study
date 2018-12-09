import tkinter as tk

def pushed(self):
    self["text"] = "押されたよ"

root = tk.Tk()
root.title("検索")
root.geometry("300x400")

label = tk.Label(root, text="テスト中")
# label.grid()

button = tk.Button(root, text="ボタン", command= lambda : pushed(button))
button.pack()

root.mainloop()