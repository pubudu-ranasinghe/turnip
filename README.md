# 🥦 Turnip

Turnip is a fancy GUI for [Beets](http://beets.io/) — A media library management system for obsessive-compulsive music geeks.

## Contribution

### Setup

You need **Python 3.6** to run turnip (Does not work with later versions)

Clone repository

```
git clone https://github.com/pubudu-ranasinghe/turnip.git
```

Create a virtual environment inside the directory

```
cd turnip
python -m venv venv
```

Activate the virtual environment

```
# On Mac/Linux:
source venv/bin/activate
# On Windows Powershell:
.\venv\Scripts\Activate.ps1
```

Install the required libraries

```
pip install fbs PyQt5 beets
```

Run

```
fbs run
# or
python src/main/python/turnip/main.py
```