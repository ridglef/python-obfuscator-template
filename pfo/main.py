import ast
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from transformers import IntegerTransformer, Base64Transformer, CompressTransformer

def obfuscate():
    file_path = file_entry.get()
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "File not found!")
        return

    try:
        output_text.insert(tk.END,"Loading " + file_path + "\n")
        with open(file_path, "r") as script:
            src = script.read()
            tree = ast.parse(src, filename=file_path)
            IntegerTransformer.transform(tree)
            transformed = ast.unparse(tree)
            transformed = CompressTransformer.transform(transformed)
            transformed = Base64Transformer.transform(transformed)
            output_file = file_path.replace(".py", "-obf.py")
            with open(output_file, "w") as out:
                out.write(transformed)
            output_text.insert(tk.END, "Wrote to " + output_file + "\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

root = tk.Tk()
root.title("Python Obfuscator Template")

file_label = tk.Label(root, text="Python File Path:")
file_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

output_text = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
output_text.grid(row=1, columnspan=3, padx=5, pady=5)

obfuscate_button = tk.Button(root, text="Obfuscate", command=obfuscate)
obfuscate_button.grid(row=2, columnspan=3, padx=5, pady=5)

root.mainloop()
