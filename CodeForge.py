import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import webbrowser

BG_COLOR = "#1e1e2f"
FG_COLOR = "#ffffff"
ACCENT_COLOR = "#4CAF50"
BUTTON_COLOR = "#2e2e3e"
HOVER_COLOR = "#3e3e5e"

root = tk.Tk()
root.title("CodeForge v2.0 - EXE Builder by Mr.SenihX")
root.geometry("780x560")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

selected_file = tk.StringVar()

def on_enter(e, widget, color=HOVER_COLOR):
    widget['bg'] = color

def on_leave(e, widget, color=BUTTON_COLOR):
    widget['bg'] = color

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Desteklenen Dosyalar", "*.py *.c *.cpp *.js")]
    )
    if file_path:
        selected_file.set(file_path)

def convert_to_exe():
    file_path = selected_file.get()
    if not file_path:
        messagebox.showerror("Hata", "Lütfen bir dosya seçin.")
        return

    ext = os.path.splitext(file_path)[1]

    if ext == ".py":
        try:
            subprocess.run(["pyinstaller", "--onefile", "--noconsole", "--clean", file_path], check=True)
            exe_name = os.path.splitext(os.path.basename(file_path))[0] + ".exe"
            exe_path = os.path.abspath(os.path.join("dist", exe_name))
            messagebox.showinfo("Başarılı", f".exe dosyası başarıyla oluşturuldu!\n\n📁 Konum:\n{exe_path}")
        except subprocess.CalledProcessError:
            messagebox.showerror("Hata", ".exe oluşturulamadı. PyInstaller kurulu mu?")
    else:
        messagebox.showwarning("Desteklenmeyen", f"{ext} uzantısı şu an desteklenmiyor.")

def create_button(text, command):
    btn = tk.Button(
        root,
        text=text,
        command=command,
        font=("Segoe UI", 10, "bold"),
        bg=BUTTON_COLOR,
        fg=FG_COLOR,
        activebackground=HOVER_COLOR,
        activeforeground="white",
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2"
    )
    btn.bind("<Enter>", lambda e: on_enter(e, btn))
    btn.bind("<Leave>", lambda e: on_leave(e, btn))
    return btn

tk.Label(
    root,
    text="⚙️ CodeForge v2.0",
    font=("Segoe UI", 22, "bold"),
    fg=FG_COLOR,
    bg=BG_COLOR
).pack(pady=20)

tk.Label(
    root,
    text="Kodlarını tek tıkla .exe dosyasına dönüştür!",
    font=("Segoe UI", 11),
    fg="lightgray",
    bg=BG_COLOR
).pack()

create_button("📂 Dosya Seç", select_file).pack(pady=20)

tk.Label(
    root,
    textvariable=selected_file,
    font=("Segoe UI", 9),
    bg=BG_COLOR,
    fg="lightgray"
).pack()

create_button("🚀 EXE'ye Dönüştür", convert_to_exe).pack(pady=30)

def open_link(url):
    webbrowser.open_new(url)

footer = tk.Frame(root, bg=BG_COLOR)
footer.pack(side="bottom", pady=10)

tk.Label(
    footer,
    text="📌 Mr.SenihX tarafından tasarlanmıştır",
    font=("Segoe UI", 8),
    fg="gray",
    bg=BG_COLOR
).pack()

links = {
    "🌐 GitHub": "https://github.com/SenihX",
    "🛡️ TryHackMe": "https://tryhackme.com/p/Mr.SenihX",
    "𝕏 Twitter": "https://x.com/SenihX_"
}

for name, url in links.items():
    link = tk.Label(
        footer,
        text=name,
        font=("Segoe UI", 9, "underline"),
        fg="#00bfff",
        bg=BG_COLOR,
        cursor="hand2"
    )
    link.pack(side="left", padx=8)
    link.bind("<Button-1>", lambda e, u=url: open_link(u))

root.mainloop()
