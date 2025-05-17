import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import webbrowser

# Ana pencere
root = tk.Tk()
root.title("CodeForge EXE Builder - by Mr.SenihX")
root.state("zoomed")  # Tam ekran
root.configure(bg="#1e1e1e")

selected_file = tk.StringVar()
output_path = tk.StringVar()

# ------------------ Fonksiyonlar ------------------ #

def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Supported Files", "*.py *.c *.cpp *.js")]
    )
    if file_path:
        selected_file.set(file_path)
        output_path.set("")  # Önceki sonucu temizle

def convert_to_exe():
    file_path = selected_file.get()
    if not file_path:
        messagebox.showerror("Hata", "Lütfen bir dosya seçin.")
        return

    ext = os.path.splitext(file_path)[1]

    if ext == ".py":
        try:
            subprocess.run(["pyinstaller", "--onefile", file_path], check=True)
            dist_path = os.path.join(os.getcwd(), "dist", os.path.basename(file_path).replace(".py", ".exe"))
            if os.path.exists(dist_path):
                output_path.set(f"✅ EXE Kaydedildi: {dist_path}")
                messagebox.showinfo("Başarılı", f".exe dosyası oluşturuldu:\n{dist_path}")
            else:
                output_path.set("⚠️ EXE oluşturuldu ama dosya bulunamadı.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Hata", ".exe oluşturulamadı. PyInstaller kurulu mu?")
    else:
        messagebox.showwarning("Desteklenmeyen", f"{ext} uzantısı şu an desteklenmiyor.")

def open_link(url):
    webbrowser.open_new_tab(url)

# ------------------ Stil Fonksiyonu ------------------ #
def style_button(btn, normal_bg, hover_bg):
    def on_enter(e): btn["bg"] = hover_bg
    def on_leave(e): btn["bg"] = normal_bg
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ------------------ Arayüz ------------------ #
title = tk.Label(
    root,
    text="CodeForge EXE Builder",
    font=("Segoe UI", 36, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=30)

subtitle = tk.Label(
    root,
    text="📦 Kodlarını tek tıklamayla .exe dosyasına dönüştür!",
    font=("Segoe UI", 16),
    fg="gray",
    bg="#1e1e1e"
)
subtitle.pack()

select_btn = tk.Button(
    root,
    text="📂 Dosya Seç",
    command=select_file,
    font=("Segoe UI", 12),
    bg="#0078D7",
    fg="white",
    padx=15,
    pady=7,
    relief="flat",
    activebackground="#005a9e"
)
select_btn.pack(pady=25)
style_button(select_btn, "#0078D7", "#005a9e")

file_label = tk.Label(
    root,
    textvariable=selected_file,
    font=("Segoe UI", 11),
    bg="#1e1e1e",
    fg="white"
)
file_label.pack()

convert_btn = tk.Button(
    root,
    text="⚙️ EXE'ye Dönüştür",
    command=convert_to_exe,
    font=("Segoe UI", 14, "bold"),
    bg="#28a745",
    fg="white",
    padx=20,
    pady=10,
    relief="flat",
    activebackground="#1c7c35"
)
convert_btn.pack(pady=30)
style_button(convert_btn, "#28a745", "#1c7c35")

output_label = tk.Label(
    root,
    textvariable=output_path,
    font=("Segoe UI", 12),
    bg="#1e1e1e",
    fg="#00ffcc"
)
output_label.pack(pady=10)

# ------------------ Tıklanabilir Sosyal Medya Linkleri ------------------ #
social_frame = tk.Frame(root, bg="#1e1e1e")
social_frame.pack(pady=50)

links = [
    ("🌐 GitHub", "https://github.com/SenihX"),
    ("🛡️ TryHackMe", "https://tryhackme.com/p/Mr.SenihX"),
    ("𝕏 Twitter", "https://x.com/SenihX_")
]

for text, url in links:
    link_label = tk.Label(
        social_frame,
        text=text,
        font=("Segoe UI", 10, "underline"),
        fg="#1e90ff",
        bg="#1e1e1e",
        cursor="hand2"
    )
    link_label.pack(side="left", padx=20)
    link_label.bind("<Button-1>", lambda e, url=url: open_link(url))
    style_button(link_label, "#1e1e1e", "#2e2e2e")

# ------------------ Alt Bilgi ------------------ #
footer = tk.Label(
    root,
    text="Mr.SenihX tarafından tasarlanmıştır • 2025",
    font=("Segoe UI", 9),
    fg="gray",
    bg="#1e1e1e"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
