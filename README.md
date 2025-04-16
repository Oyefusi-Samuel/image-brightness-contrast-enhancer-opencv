# Image Brightness & Contrast Enhancer 🖼️✨

A simple Python tool that allows you to interactively select an image, enhance its brightness and contrast, and view both the original and adjusted images along with their histograms. Ideal for beginners exploring image processing with OpenCV.

---

## 📌 Features

- Open any image from your computer via a file dialog  
- Apply customizable brightness and contrast adjustments  
- Display original and enhanced images side by side  
- Visualize pixel intensity distribution using histograms (RGB)

---

## 🖥️ Requirements

- Python 3.7+  
- OpenCV  
- NumPy  
- Matplotlib  
- Tkinter (usually comes pre-installed with Python)

---

## 🔧 Setup Instructions

1. **Clone the Repository to your local workspace**  
   ```bash
   git clone https://github.com/Oyefusi-Samuel/image-brightness-contrast-enhancer-opencv.git

  
 2. **Navigate into the Project Directory**
   ```
  cd image-brightness-contrast-enhancer
```

3. **Create a Virtual Environment**
```
python -m venv venv
```

4. **Activate the Virtual Environment from terminal**
   ```
   venv\Scripts\activate
   
   ```

5. **Windows (PowerShell) — you may need to run:**
```
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
6. Then run
```
.\venv\Scripts\Activate.ps1
```

6. **Install Requirements**
```
pip install -r requirements.txt
```
7. **Run the Code**
```
python code.py
```

## 🖼️ What Happens
- A file dialog box appears to let you select an image.

- After selection, two windows will display:

- Original Image

- Adjusted Image (brightened and contrasted)

- Two histograms will also be shown side-by-side in a Matplotlib window.








    
