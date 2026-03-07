# Rotatetoe

Rotatetoe is a game like tic-tac-toe, but with more strategic planning as the board moves.

## Installation

### Linux:

1. Download the latest installer binary.
2. Run it.  

### Windows:

1. Download the latest .zip release.
2. Extract it.
3. Go to the `bin\windows` directory and run the installer.
(rotatetoe has not been really tested on windows so expect bugs)

Install command:
```cmd
curl -LO https://github.com/wroug/rotatetoe/archive/refs/tags/v1.0.1.zip
powershell -Command "Expand-Archive 'v1.0.1.zip'"
rotatetoe-1.0.1\bin\windows\install.bat
```

### Running without installation: (if other steps failed)

You can also run the game directly without installing:

1. Extract the downloaded file.
2. Enter the directory
-# create a python venv if it neccessary for your device
4. `pip install -r requirements.txt`
5. `cd game`
6. `python main.py`

### If you encounter any problems during installation feel free to make an issue!

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
