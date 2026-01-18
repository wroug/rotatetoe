if "%~1"=="--version" (
    type "%LOCALAPPDATA%\rotatetoe\version.txt"
    exit /b
)

if "%~1"=="--uninstall" (
    "%LOCALAPPDATA%\rotatetoe\bin\windows\uninstall.bat"
    exit /b
)

if "%~1"=="--update" (
    echo Updates are currently unavailable for windows users.
    echo If you wish to update, reinstall the latest version from github.
    exit /b
)

cd /d "%LOCALAPPDATA%\rotatetoe\game"

echo If you encounter any problems, please make an issue at https://github.com/wroug/rotatetoe/issues
echo Resize and zoom terminal to your preferred size now, as it cannot be done later.
pause

python -u main.py
