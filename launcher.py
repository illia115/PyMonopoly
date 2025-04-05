import customtkinter as ctk
import tkinter
import subprocess
import subprocess


ctk.set_appearance_mode("dark")  # "light", "dark", "system"

# Создание основного окна
app = ctk.CTk()
app.geometry("500x300")
app.title("PyMonopoly launcher")

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="both", expand=True)
def button_callback():
    subprocess.run(["game23.exe"])

button = ctk.CTkButton(frame, text="Launch", command=button_callback)
button.pack(pady=5)

label = ctk.CTkLabel(frame, text="GitHub=url", font=("Arial", 18))
label.pack(pady=10)
label = ctk.CTkLabel(frame, text="Discord=https://discord.gg/CRzm7JrR", font=("Arial", 18))
label.pack(pady=10)


tabview = ctk.CTkTabview(frame)
tab1 = tabview.add("Atikinsons88")
tab3 = tabview.add("Saul Goodman")

ctk.CTkLabel(tab1, text="Telegram=@Atikin").pack(pady=10)
ctk.CTkLabel(tab3, text="Telegram=@heizenberg889").pack(pady=10)


tabview.pack(pady=5, fill="x")

# Запуск приложения
app.mainloop()
