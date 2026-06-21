# 📁 File Organizer

A simple Python GUI application that automatically organizes files into folders based on their file type.

## 🚀 Features

- User-friendly graphical interface
- Select any folder from your computer
- Automatically sorts files into categories
- Creates folders automatically if they don't exist
- Supports multiple file types
- Helps keep folders clean and organized

## 📂 Supported Categories

| Category | Extensions |
|-----------|------------|
| Images | .jpg, .jpeg, .png, .gif, .bmp, .webp |
| Videos | .mp4, .mkv, .avi, .mov, .wmv |
| Documents | .pdf, .docx, .doc, .txt, .pptx, .xlsx |
| Audio | .mp3, .wav, .aac, .flac |
| Archives | .zip, .rar, .7z, .tar |
| Others | Any unsupported file type |

## 🛠 Requirements

- Python 3.x
- Tkinter (included with Python)

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/vishalvivek14332-source/python-mini-tools.git
```

Navigate to the project folder:

```bash
cd python-mini-tools/file_organizer
```

Run the application:

```bash
python main.py
```

## 📋 Example

### Before Organization

```text
Downloads/
├── photo.jpg
├── movie.mp4
├── report.pdf
├── song.mp3
├── project.zip
```

### After Organization

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Videos/
│   └── movie.mp4
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Archives/
│   └── project.zip
```

## 📁 Project Structure

```text
file_organizer/
├── main.py
└── README.md
```

## 🔮 Future Enhancements

- Undo file organization
- Organize files by date
- Duplicate file detection
- Detailed file statistics
- Dark mode interface

## 👨‍💻 Author

Vishal Vivek