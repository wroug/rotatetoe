@echo off

REM installer thingy, im putting together random commands from the internet so lots of comments so i dont forget qwq


echo This installer is barely tested. If it fails please make an issue at https://github.com/wroug/rotatetoe/issues

where python >nul 2>&1
if errorlevel 1 (
    echo Python was not found in PATH.
    echo Please install Python 3 and make sure 'python' is in your path before running this installer.
    pause
    exit /b
)

where pip >nul 2>&1
if errorlevel 1 (
    echo pip was not found in PATH.
    echo Please install pip before running this installer.
    pause
    exit /b 1
)





REM go to the project root
set "SCRIPT_DIR=%~dp0"

cd /d "%SCRIPT_DIR%\..\.."


set "ROOT_DIR=%CD%"

REM create the appdata directry

set "TARGET=%LOCALAPPDATA%\rotatetoe"
if exist "%TARGET%" (
    echo Removing existing installation...
    rmdir /s /q "%TARGET%"
)
mkdir "%TARGET%"

REM man why is batch so much more complicated than bash
REM copy fikes

echo Copying files...
xcopy /E /I /Y "%ROOT_DIR%\*" "%TARGET%\"


REM install reuwqiremnts

pip install -r "%TARGET%\requirements.txt"

REM meow meow meow meow meow meow nyaaa
REM i want a cola qwq gimme a cola
REM send that thang to da path
set "USER_BIN=%USERPROFILE%\bin"
if not exist "%USER_BIN%" mkdir "%USER_BIN%"
copy /Y "%SCRIPT_DIR%\rotatetoe.bat" "%USER_BIN%"


echo %PATH% | findstr /I /C:"%USER_BIN%" >nul
if errorlevel 1 (
    echo Adding to path...
    setx PATH "%PATH%;%USER_BIN%" >nul
    echo Added to path.
)

echo Restart CMD to use rotatoe.
echo Launch it by typing:
echo     rotatetoe
pause
