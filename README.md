<div align="center">
    <img src="design/Turnip.png" />
    <p>
        Turnip is a fancy GUI for <a href="http://beets.io/">Beets</a> — A media library management system for obsessive-compulsive music geeks.
    </p>
    <img src="https://travis-ci.org/pubudu-ranasinghe/turnip.svg?branch=master">
    <img src="https://ci.appveyor.com/api/projects/status/05glwcx6bj0morjq?svg=true">
</div>


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
