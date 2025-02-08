
import tkinter as tk
from controller import on_search_button_click, load_default_image

def main():
    global entry_name, character_image

    window = tk.Tk()
    window.title("MapleStory Character Search")
    window.geometry("500x500")

    tk.Label(window, text="캐릭터 이름").pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    image = load_default_image()
    character_image = tk.Label(window, image=image)
    character_image.pack()

    btn = tk.Label(window, text="캐릭터 이미지")
    btn.pack()

    tk.Label(window, text="이름").pack()
    label_name = tk.Label(window,text="None")
    label_name.pack()

    tk.Label(window, text="월드").pack()
    label_world = tk.Label(window, text="None")
    label_world.pack()

    tk.Label(window, text="성별").pack()
    label_gender = tk.Label(window, text="None")
    label_gender.pack()

    tk.Label(window, text="직업").pack()
    label_class = tk.Label(window, text="None")
    label_class.pack()

    tk.Label(window, text="레벨").pack()
    label_level = tk.Label(window, text="None")
    label_level.pack()

    tk.Label(window, text="상태")
    state_label = tk.Label(window, text="상태")
    state_label.pack()

    entry_name.bind("<Return>", lambda event: on_search_button_click(entry_name,character_image, label_name, label_world, label_gender, label_class, label_level, state_label))

    window.mainloop()