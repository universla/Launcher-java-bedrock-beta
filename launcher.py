import os
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk

class MinecraftLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Minecraft Launcher")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        
        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        
        # Título
        title_label = tk.Label(root, text="MINECRAFT LAUNCHER", 
                              font=("Arial", 16, "bold"), 
                              fg="#3498db")
        title_label.pack(pady=20)
        
        # Frame para botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        
        # Botones
        self.java_btn = tk.Button(button_frame, 
                                 text="▶ Iniciar Minecraft Java", 
                                 command=self.launch_java,
                                 bg="#27ae60", 
                                 fg="white",
                                 font=("Arial", 10, "bold"),
                                 width=25,
                                 height=2)
        self.java_btn.pack(pady=5)
        
        self.bedrock_btn = tk.Button(button_frame, 
                                   text="▶ Iniciar Minecraft Bedrock", 
                                   command=self.launch_bedrock,
                                   bg="#e74c3c", 
                                   fg="white",
                                   font=("Arial", 10, "bold"),
                                   width=25,
                                   height=2)
        self.bedrock_btn.pack(pady=5)
        
        # Botón de salir
        exit_btn = tk.Button(root, 
                           text="Salir", 
                           command=root.quit,
                           bg="#7f8c8d", 
                           fg="white",
                           font=("Arial", 9),
                           width=10)
        exit_btn.pack(pady=10)
    
    def launch_java(self):
        # Ruta típica del launcher de Minecraft Java
        java_paths = [
            r"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe",
            r"C:\Program Files\Minecraft Launcher\MinecraftLauncher.exe",
            r"C:\Users\Public\Desktop\Minecraft Launcher.lnk"
        ]
        
        launched = False
        for path in java_paths:
            if os.path.exists(path):
                try:
                    subprocess.Popen([path])
                    messagebox.showinfo("Éxito", "Minecraft Java iniciando...")
                    launched = True
                    break
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo iniciar: {str(e)}")
                    return
        
        if not launched:
            messagebox.showerror("Error", "No se encontró Minecraft Java Edition.\nAsegúrate de tenerlo instalado.")
    
    def launch_bedrock(self):
        # Ruta típica de Minecraft Bedrock (puede variar)
        bedrock_paths = [
            r"C:\Program Files\WindowsApps\Microsoft.MinecraftUWP_*\Minecraft.Windows.exe",
            r"C:\Program Files (x86)\WindowsApps\Microsoft.MinecraftUWP_*\Minecraft.Windows.exe"
        ]
        
        # Alternativa: abrir desde el protocolo
        try:
            subprocess.Popen(["start", "minecraft:"], shell=True)
            messagebox.showinfo("Éxito", "Minecraft Bedrock iniciando...")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar Bedrock: {str(e)}\n\nIntenta abrirlo desde el menú de inicio.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MinecraftLauncher(root)
    root.mainloop()
