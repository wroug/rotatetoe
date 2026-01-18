# Rotatetoe

Rotatetoe is a game like tic-tac-toe, but with more strategic planning as the board moves.

## Installation

### Linux:

1. Download the latest tar.gz release.
2. Extract it.
3. Go to the `bin` directory and run the installer.


How to install:
```bash
wget https://github.com/wroug/rotatetoe/archive/refs/tags/v0.1.1.tar.gz
tar -xzf v0.1.1.tar.gz
bash rotatetoe-0.1.1/bin/install.sh
```

### Windows:

1. Download the latest .zip release.
2. Extract it.
3. Go to the `bin\windows` directory and run the installer.
(rotatetoe has not been really tested on windows so expect bugs)

How to install:
```cmd
curl -LO https://github.com/wroug/rotatetoe/archive/refs/tags/v0.1.1.zip
powershell -Command "Expand-Archive 'v0.1.1.zip'"
rotatetoe-0.1.1\bin\windows\install.bat
```

### Running without installation:

You can also run the game directly without installing:

1. Extract the downloaded file.
2. Enter the directory
3. `pip install -r requirements.txt`
4. `cd game`
5. `python main.py`

## Requirements:

Python 3.x  
Pip  
Terminal with proper size.  
A windows or linux computer (as of now, on MacOS you can only play without installation)  

## Usage:

`rotatetoe --version` to check the version  
`rotatetoe --update` to update the game  
`rotatetoe --uninstall` to uninstall the game  

## Licence:

MIT
