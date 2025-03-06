# Developed by Fernanda Battig
# March 6 2025

import os
import subprocess
import argparse
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS

# ==========================
# Command-Line Arguments
# ==========================
parser = argparse.ArgumentParser(description="Generate a video from an image with FFmpeg and Pillow.")
parser.add_argument("--image", type=str, default="Fox.png", help="Path to the input image file.")
parser.add_argument("--music", type=str, default="backgroundMusic.mp3", help="Path to the background music file.")
parser.add_argument("--caption", type=str, default="This is a fox in the wild. It has a bushy tail, sharp eyes, and a thick coat.", help="Caption text for the image.")
parser.add_argument("--voiceover", type=str, default="This is a fox in the wild. It has a bushy tail, sharp eyes, and a thick coat.", help="Voiceover text.")
parser.add_argument("--duration", type=int, default=10, help="Duration of the video in seconds (default: 10).")
parser.add_argument("--rotate", type=int, choices=[0, 90, 180, 270], default=0, help="Rotate the image by 90, 180, or 270 degrees.")
args = parser.parse_args()

# ==========================
# Configurations
# ==========================
image_path = args.image
music_file = args.music
output_image = "transformed_image.jpg"
output_video = "output_video.mp4"
captions = args.caption
voiceover_text = args.voiceover
video_duration = args.duration

# ==========================
# Check if Files Exist
# ==========================
for file in [image_path, music_file]:
    if not os.path.exists(file):
        print(f"Error: '{file}' not found.")
        exit()

# ==========================
# Process Image
# ==========================
image = Image.open(image_path)
image = image.convert("L")  # Grayscale transformation

# Rotate the image if requested
if args.rotate in [90, 180, 270]:
    image = image.rotate(args.rotate, expand=True)

# Ensure even dimensions for FFmpeg compatibility
new_width = image.width if image.width % 2 == 0 else image.width - 1
new_height = image.height if image.height % 2 == 0 else image.height - 1
image = image.resize((new_width, new_height))

# Add text overlay
draw = ImageDraw.Draw(image)
try:
    font = ImageFont.truetype("arial.ttf", 36)
except IOError:
    font = ImageFont.load_default()
draw.text((50, 50), captions, font=font, fill="white")
image.save(output_image)

# ==========================
# Create Voiceover
# ==========================
voiceover = gTTS(text=voiceover_text, lang='en')
voiceover.save("voiceover.mp3")

# ==========================
# Generate Video with FFmpeg
# ==========================
result = subprocess.run([
    "ffmpeg", "-y", "-loop", "1", "-i", output_image,
    "-i", "voiceover.mp3", "-i", music_file,
    "-filter_complex", "[1:a][2:a]amix=inputs=2:duration=shortest[a]",
    "-map", "0:v", "-map", "[a]",
    "-vf", f"drawtext=text='{captions}':fontcolor=white:fontsize=36:x=(w-text_w)/2:y=h-100",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-t", str(video_duration),
    "-c:a", "aac", output_video
], capture_output=True, text=True)

# Check for errors
if result.returncode != 0:
    print("FFmpeg error:", result.stderr)
else:
    print("Video generated successfully!")
