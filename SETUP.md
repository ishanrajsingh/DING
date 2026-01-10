🚀 DING Setup Guide

A minimal version control system. Lightweight, educational, and fun.
Get it running in under 5 minutes.

⚡ Quick Setup (No Overthinking)
```git clone https://github.com/opencodeiiita/DING.git```
```cd DING```
```python -m venv venv```
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```pip install -e .```
```ding --help```

If you see help output, you’re good to go. ✅

🧩 Requirements

Before starting, make sure you have: Python 3.14.2

Verify with: ```python --version```
Download from python.org or manage versions using pyenv

Installation Walkthrough
1) Clone the Repository
```git clone https://github.com/opencodeiiita/DING.git```
```cd DING```

2) Create & Activate a Virtual Environment

Using a virtual environment keeps dependencies isolated and avoids global conflicts.

Windows:

```python -m venv venv```
```venv\Scripts\activate```


macOS / Linux:

```python3 -m venv venv```
```source venv/bin/activate```


Once activated, your terminal prompt should start with (venv).

3) Install DING (Editable Mode)
```pip install -e .```
Editable mode means any code changes reflect immediately—no reinstall required.

Confirm Installation -
Run: ```ding --help```

Expected output:
usage: ding [-h] {init,hash,cat-file} ...

If this appears, DING is installed correctly 🎉

🎯 Getting Started with DING
Initialize a Repository
```mkdir demo-project```
```cd demo-project```
```ding init```

This creates a .ding/ directory that stores all internal data.

Hash a File:

```echo "DING is awesome" > sample.txt```
```ding hash sample.txt```

Output will be a hash value, representing the stored content.

View Stored Content:

```ding cat-file <hash>```

This decompresses and prints the original file contents.

🧠 What’s Happening Behind the Scenes (BTS - not the korean boys band)?

ding init - Creates .ding/ and required internal structure

ding hash - Reads file content, Compresses it, Generates a SHA-1 hash, Stores it inside .ding/objects/

ding cat-file - Retrieves data using the hash, Decompresses and displays it

These are the same core ideas used by Git internally.

Common Issues & Fixes - 

```ding: command not found```
Cause: Virtual environment not active or install failed

Fix:
# Activate venv first
```pip install -e .```

ModuleNotFoundError: No module named 'src'
Cause: Command executed outside the project root

Fix:
```cd path/to/DING```
```ding --help```

Python Version Problems
Cause: Wrong Python version being used

Fix:
```python3.14 -m venv venv```
Or use pyenv:
```pyenv install 3.14.2```
``pyenv local 3.14.2```

pip install -e . fails

Fix:
```pip install --upgrade pip setuptools wheel```
```pip install -e .```


Use -v for detailed logs if needed.

Project Layout
DING/
├── setup.py
├── README.md
├── SETUP.md
├── CONTRIBUTING.md
└── src/
    ├── cli.py
    ├── data.py
    ├── base.py

🚀 What to Do Next

Read README.md for project goals
Review CONTRIBUTING.md if you want to help improve DING
Explore src/data.py to understand hashing & storage
Experiment by hashing and modifying files

💡 Helpful Experiments

Hash the same file twice → same hash
Modify file → new hash
Inspect .ding/objects/ to see stored blobs
This is content-addressable storage in action.

❓ FAQs

Q. Do I really need a virtual environment?
Ans. Not mandatory, but strongly recommended.

Q. Can I use older Python versions?
Ans. It may work, but 3.14.2 is the official target.

Q. Is this a Git replacement?
Ans. No. DING is educational—meant to explain how VCS works internally.

🤝 Need Help?

Recheck this guide
Open an issue on GitHub
Ask in community channels
Read CONTRIBUTING.md

🎉 You’re Set

DING is installed, running, and ready to explore.
You now understand the fundamentals behind real-world version control systems.

Go break things. Then fix them. 🔥
