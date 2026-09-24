# Color Blindness Test GUI 👁️🎨

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)
![Pillow](https://img.shields.io/badge/Images-Pillow-yellow.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

## Overview

**Color Blindness Test** is a Python-based desktop application that provides an interactive, digital version of color vision deficiency assessments (similar to the Ishihara test). It features a modern Graphical User Interface (GUI) built with Tkinter, guiding users through a seamless testing experience.

The application automatically randomizes a set of test plates, collects the user's responses, evaluates them in real-time, and provides a final diagnostic score out of 15.

## Key Features

* **Modern GUI Design:** Custom-styled Tkinter interface with background imaging, icon integration, and a clean login/entry screen.
* **Randomized Testing Sequence:** Dynamically loads and shuffles test images from a local data directory, ensuring the test is different every time.
* **Automated Scoring:** Compares user input directly against the embedded answers (derived from filenames) and tallies correct responses.
* **Input Validation & Progression:** Guides the user through a welcome screen, rules explanation, a 15-question test loop, and a final results dashboard.

## Tech Stack

* **Language:** Python
* **GUI Framework:** Tkinter (Standard GUI library for Python)
* **Image Processing:** Pillow (PIL) for resizing and rendering background assets, icons, and test plates.

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/martynaswitula/Color-Blindness-Test.git
   cd Color-Blindness-Test
   ```

2. Install the required image-processing dependency:
   ```bash
   pip install -r requirements.txt
   ```

3. **Data Folder Setup:** 
   Ensure there is a folder named `dane` in the root directory. This folder should contain the test images (e.g., Ishihara plates). 
   *Note on naming convention:* The application evaluates answers based on the filename. If the image shows the number 12, the file **must** be named `12.jpg` (or `.png`).

4. Run the application:
   ```bash
   python aplikacja_PAZIG.py
   ```

## Usage Guide

1. **Login Screen:** Enter your email address to begin.
2. **Rules:** Read the test instructions carefully.
3. **Test Phase:** 15 randomized images will be displayed sequentially. Type the number you see in the image and click **"Dalej"** (Next). If you cannot see a number, leave it blank or guess, and proceed.
4. **Results:** After 15 images, your final score will be displayed on the screen.

## Project Structure
* `aplikacja_PAZIG.py` - Main application logic and GUI definitions.
* `tlo.png`, `logowanie.jpg`, `mail.jpg`, `mail2.jpg` - UI assets and icons.
* `dane/` - Directory containing the clinical test images (not included in repo by default to prevent cheating).