import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkbootstrap import Style
import yt_dlp
import threading

class MacStyleDownloader:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme='litera')
        self.setup_window()
        self.create_widgets()
        self.ydl_opts = {
            'outtmpl': '',
            'quiet': True,
            'progress_hooks': [self.update_progress],
        }

    def setup_window(self):
        self.root.title("YouTube Downloader")
        self.root.geometry("680x420")
        self.root.resizable(False, False)
        self.root.iconbitmap('')  # ضع أيقونة .icns هنا إذا كنت على ماك

    def create_widgets(self):
        # الإطار الرئيسي
        main_frame = ttk.Frame(self.root, padding=(30, 20))
        main_frame.pack(fill=tk.BOTH, expand=True)

        # العنوان
        title = ttk.Label(main_frame, 
                         text="YouTube Video Downloader",
                         font=('Helvetica', 20, 'bold'),
                         foreground='#1d1d1d')
        title.pack(pady=(0, 25))

        # حقل إدخال الرابط
        url_frame = ttk.Frame(main_frame)
        url_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(url_frame, text="Video URL:", font=('Helvetica', 12)).pack(side=tk.LEFT, padx=(0, 10))
        self.url_entry = ttk.Entry(url_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # تحديد المسار
        path_frame = ttk.Frame(main_frame)
        path_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(path_frame, text="Save Location:", font=('Helvetica', 12)).pack(side=tk.LEFT, padx=(0, 10))
        self.path_label = ttk.Label(path_frame, text="Desktop", foreground='#666666')
        self.path_label.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        ttk.Button(path_frame, 
                  text="Change", 
                  command=self.select_path,
                  style='primary.TButton').pack(side=tk.LEFT)

        # إعدادات الجودة
        quality_frame = ttk.Frame(main_frame)
        quality_frame.pack(fill=tk.X, pady=15)
        
        ttk.Label(quality_frame, text="Quality:", font=('Helvetica', 12)).pack(side=tk.LEFT)
        self.quality = ttk.Combobox(quality_frame, 
                                  values=["Best Quality", "HD 1080p", "HD 720p", "Audio Only"],
                                  state='readonly',
                                  width=15)
        self.quality.current(0)
        self.quality.pack(side=tk.LEFT, padx=10)

        # شريط التقدم
        self.progress = ttk.Progressbar(main_frame, 
                                      orient=tk.HORIZONTAL,
                                      length=500,
                                      mode='determinate')
        self.progress.pack(pady=20)

        # زر التحميل
        self.download_btn = ttk.Button(main_frame,
                                      text="Download Video",
                                      command=self.start_download,
                                      style='success.TButton')
        self.download_btn.pack(pady=10)

    def select_path(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_label.config(text=folder)

    def update_progress(self, d):
        if d['status'] == 'downloading':
            percent = float(d['_percent_str'].replace('%', ''))
            self.progress['value'] = percent
            self.root.title(f"Downloading ({percent:.1f}%)...")

    def start_download(self):
        if not self.url_entry.get():
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return

        quality_map = {
            "Best Quality": "best",
            "HD 1080p": "bestvideo[height<=1080]+bestaudio",
            "HD 720p": "bestvideo[height<=720]+bestaudio",
            "Audio Only": "bestaudio"
        }
        
        self.ydl_opts['outtmpl'] = f'{self.path_label.cget("text")}/%(title)s.%(ext)s'
        self.ydl_opts['format'] = quality_map[self.quality.get()]

        self.download_btn.config(state=tk.DISABLED)
        threading.Thread(target=self.download_video, daemon=True).start()

    def download_video(self):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url_entry.get()])
            messagebox.showinfo("Success", "Download completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")
        finally:
            self.root.title("YouTube Downloader")
            self.progress['value'] = 0
            self.download_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = MacStyleDownloader(root)
    root.mainloop()