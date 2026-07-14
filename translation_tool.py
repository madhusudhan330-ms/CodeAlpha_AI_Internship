import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeAlpha AI - Language Translation Tool")
        self.root.geometry("550x500")
        self.root.configure(bg="#f0f2f5")

        # Supported languages mapping
        self.languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Hindi": "hi",
            "Telugu": "te",
            "Mandarin": "zh-CN",
            "Arabic": "ar"
        }

        self.setup_ui()

    def setup_ui(self):
        # Header Title
        title = tk.Label(self.root, text="Language Translation Tool", font=("Helvetica", 16, "bold"), bg="#f0f2f5", fg="#333")
        title.pack(pady=15)

        # Dropdowns Selection Frame
        lang_frame = tk.Frame(self.root, bg="#f0f2f5")
        lang_frame.pack(pady=10)

        tk.Label(lang_frame, text="Source:", bg="#f0f2f5", font=("Helvetica", 10)).grid(row=0, column=0, padx=5)
        self.src_lang = ttk.Combobox(lang_frame, values=list(self.languages.keys()), state="readonly", width=15)
        self.src_lang.grid(row=0, column=1, padx=10)
        self.src_lang.set("English")

        tk.Label(lang_frame, text="Target:", bg="#f0f2f5", font=("Helvetica", 10)).grid(row=0, column=2, padx=5)
        self.tgt_lang = ttk.Combobox(lang_frame, values=list(self.languages.keys()), state="readonly", width=15)
        self.tgt_lang.grid(row=0, column=3, padx=10)
        self.tgt_lang.set("Spanish")

        # User Text Input area
        tk.Label(self.root, text="Enter Text:", bg="#f0f2f5", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=40)
        self.input_text = tk.Text(self.root, height=6, width=55, font=("Helvetica", 10))
        self.input_text.pack(pady=5)

        # Trigger Translation Button
        self.btn_translate = tk.Button(self.root, text="Translate Text", font=("Helvetica", 11, "bold"), bg="#007bff", fg="white", command=self.translate_text, width=20)
        self.btn_translate.pack(pady=15)

        # Output text field
        tk.Label(self.root, text="Translated Output:", bg="#f0f2f5", font=("Helvetica", 11, "bold")).pack(anchor="w", padx=40)
        self.output_text = tk.Text(self.root, height=6, width=55, font=("Helvetica", 10), bg="#e9ecef")
        self.output_text.pack(pady=5)

        # Action layout for copying text
        action_frame = tk.Frame(self.root, bg="#f0f2f5")
        action_frame.pack(pady=10)
        
        btn_copy = tk.Button(action_frame, text="📋 Copy Translation", font=("Helvetica", 9), command=self.copy_to_clipboard, bg="#28a745", fg="white")
        btn_copy.pack()

    def translate_text(self):
        text_to_translate = self.input_text.get("1.0", tk.END).strip()
        if not text_to_translate:
            messagebox.showwarning("Warning", "Please enter some text to translate.")
            return

        src = self.languages[self.src_lang.get()]
        tgt = self.languages[self.tgt_lang.get()]

        try:
            translated = GoogleTranslator(source=src, target=tgt).translate(text_to_translate)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
        except Exception as e:
            messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

    def copy_to_clipboard(self):
        translated_text = self.output_text.get("1.0", tk.END).strip()
        if translated_text:
            pyperclip.copy(translated_text)
            messagebox.showinfo("Success", "Translation copied to clipboard!")
        else:
            messagebox.showwarning("Empty", "Nothing to copy yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()