### 📄 **README.md** 

```markdown
🎥 FFmpeg-Pillow-Video-Generator

## 📋 Description
This Python script generates a short video from an image using **Pillow** for image processing and **FFmpeg** for video creation. It overlays text onto the image, applies a basic transformation (grayscale or rotation), and adds background music with captions and a voiceover narration.

---

## 🛠️ Requirements

### Install FFmpeg (MacOS)
```bash
brew install ffmpeg
```

### Install Python Libraries
Run the following command inside your virtual environment:
```bash
pip install pillow gtts
```

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/battigfernanda/FFmpeg-Pillow-Video-Generator.git
   cd FFmpeg-Pillow-Video-Generator
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. **Prepare your files:**
   - An image (e.g., `Fox.png`).
   - A background music file (e.g., `backgroundMusic.mp3`).

2. **Run the script:**
   ```bash
   python video_generator.py --image Fox.png --music backgroundMusic.mp3 --caption "This is a fox in the wild." --voiceover "This is a fox in the wild." --duration 5 --rotate 90
   ```

---

## 🔄 Command-Line Options

- `--image`: Path to the input image file. *(Default: Fox.png)*
- `--music`: Path to the background music file. *(Default: backgroundMusic.mp3)*
- `--caption`: Caption text for the image.
- `--voiceover`: Text for the voiceover narration.
- `--duration`: Duration of the video in seconds. *(Default: 10)*
- `--rotate`: Rotate the image by 90, 180, or 270 degrees. *(Default: 0)*

---

## 🖼️ Example Command
```bash
python video_generator.py --image Fox.png --music backgroundMusic.mp3 --caption "A beautiful fox in the forest." --voiceover "A beautiful fox in the forest." --duration 5 --rotate 90
```

---

## 🛠️ Troubleshooting

- **`FileNotFoundError: No such file or directory: 'ffmpeg'`**  
  Ensure FFmpeg is installed and added to your system PATH.

- **`ModuleNotFoundError: No module named 'gtts'`**  
  Run:
  ```bash
  pip install gtts
  ```

---

## 🗂️ Directory Structure
```
FFmpeg-Pillow-Video-Generator/
├── .gitignore
├── Fox.png
├── backgroundMusic.mp3
├── output_video.mp4
├── transformed_image.jpg
├── video_generator.py
├── voiceover.mp3
├── README.md  # ← Add this file
```

---

## 📜 License
This project is developed by **Fernanda Battig** - March 6, 2025.  
Feel free to use and modify it as needed.

---

## ⭐ Acknowledgments
- [FFmpeg](https://ffmpeg.org/)
- [Pillow](https://python-pillow.org/)
- [gTTS](https://pypi.org/project/gTTS/)
```

---

### 🛠️ **How to Upload This README to GitHub:**
1. Create a file named **`README.md`** in your project directory.
2. Paste the above content directly into the file.
3. Save the file.
4. Run these commands to upload it to GitHub:

```bash
git add README.md
git commit -m "Add README.md"
git push -u origin main
```

---

If you need help with anything else, just let me know! 😊
