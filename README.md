# 📸 PhotoGrabber

> **Secretly collect and backup your precious memories** — silently, safely, and smartly.

---

## 🕵️ What is PhotoGrabber?

**PhotoGrabber** is a lightweight Python tool that **secretly scans your main picture directory**, finds all `.png` and `.jpg` image files, and **moves them to a safe backup spot** — without interrupting your workflow.

Whether you want to:
- Backup all your photos before formatting your PC
- Collect images from a specific folder (even subfolders!)
- Create a silent, automated backup system

**PhotoGrabber does it quietly and efficiently.**

---

## ⚠️ Important Note

This tool is designed for **ethical and personal use only**.  
Use it responsibly — only on your own files or with explicit permission.

The name "secretly" refers to the **non-intrusive background operation**, not malicious intent. 😎

---

## 🚀 Features

- ✅ Automatically finds `.png` and `.jpg` files in your **Pictures** folder (including all subfolders)
- ✅ Copies files to a local `backup` folder (where the script is running)
- ✅ Creates the backup folder automatically if it doesn't exist
- ✅ Handles errors gracefully (missing files, permission issues, etc.)
- ✅ **Fully customizable** — you control the source, destination, and file formats

---

## 🛠️ How It Works

1. Detects your Windows `Pictures` folder automatically using `USERPROFILE`
2. Scans recursively for all `.png` and `.jpg` files
3. Creates a `backup` folder next to the script
4. Copies every found image to that backup folder using `shutil.copy2` (preserves metadata)

---

##🔧 Customization Guide
You can easily change source, destination, and file formats by editing a few lines in the script.

##📂 Change Source Folder (where to grab from)
Find this line:

```python
source_dir = os.path.join(user_profile, "Pictures")
```
Change it to any path you want. Examples:

```python
# Grab from Desktop instead
source_dir = os.path.join(user_profile, "Desktop")

# Grab from a custom folder like D:\MyImages
source_dir = r"D:\MyImages"

# Grab from Downloads folder
source_dir = os.path.join(user_profile, "Downloads")
```

##🖼️ Change File Formats (which extensions to grab)
Find these lines:

```python
picture_files = glob.glob(os.path.join(source_dir, "**", "*.png"), recursive=True)
picture_files.extend(glob.glob(os.path.join(source_dir, "**", "*.jpg"), recursive=True))
```

##Add or remove extensions as you like. Examples:

```python
# Grab only .png files
picture_files = glob.glob(os.path.join(source_dir, "**", "*.png"), recursive=True)

# Grab .png, .jpg, .jpeg, .gif, .bmp
picture_files = glob.glob(os.path.join(source_dir, "**", "*.png"), recursive=True)
picture_files.extend(glob.glob(os.path.join(source_dir, "**", "*.jpg"), recursive=True))
picture_files.extend(glob.glob(os.path.join(source_dir, "**", "*.jpeg"), recursive=True))
picture_files.extend(glob.glob(os.path.join(source_dir, "**", "*.gif"), recursive=True))
picture_files.extend(glob.glob(os.path.join(source_dir, "**", "*.bmp"), recursive=True))

# Grab only .jpg (no subfolders) — remove recursive=True
picture_files = glob.glob(os.path.join(source_dir, "*.jpg"))
```
