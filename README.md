markdown

# YouTube Video Downloader (macOS Style)

![App Screenshot](screenshot.png)

A modern macOS-style YouTube video downloader application built with Python and Tkinter. Supports video quality selection and audio-only downloads.

## Features ✨

- **macOS-like GUI**: Native-looking interface using `ttkbootstrap`
- **Multiple Quality Options**: 
  - Best Quality (auto-select)
  - HD 1080p
  - HD 720p
  - Audio Only (MP3)
- **Progress Tracking**: Real-time progress bar with percentage
- **Path Selection**: Choose save location with directory picker
- **Error Handling**: Clean error messages for invalid URLs/paths

## Requirements 📦

- Python 3.7+
- macOS (for native look) or Windows/Linux

## Installation 🛠️

1. Install required packages:

pip install yt-dlp ttkbootstrap

2. Clone the repository:

git clone https://github.com/bimo5851/vidtub.git

## Usage 🚀
Run the application:


python main.py
Interface guide:

Paste YouTube URL in the input field

Choose save location (default: Desktop)

Select desired quality

Click "Download Video"

Usage Demo

## Technical Stack 💻
Python 3 - Base language

yt-dlp - YouTube content downloader

Tkinter - GUI framework

ttkbootstrap - Modern UI components

Threading - Background downloads

## Customization 🎨
Modify the theme by changing the Style parameter:

python
Copy
self.style = Style(theme='litera')  # Options: 'minty', 'sandstone', 'cosmo'
Add quality presets by editing the combobox values:

python

self.quality = ttk.Combobox(quality_frame, 
                          values=["4K", "1440p", "480p", ...])
## Disclaimer ⚠️
This project is intended for educational purposes only. Please:

Respect YouTube's Terms of Service

Only download content you have rights to

Do not use for piracy

##License 📄
MIT License - Free for personal and educational use

Copy

---

**Note:** For actual use, you should:
1. Replace `yourusername` in the clone URL
2. Add actual screenshots/demo GIF
3. Modify license if needed
4. Add proper error handling documentation
5. Include contributor guidelines if open-sourcing

Would you like me to create any specific section in more detail? 😊





