@echo off

set "USER_BIN=%USERPROFILE%\bin"
set "LAUNCHER=%USER_BIN%\rotatetoe.bat"

if exist "%LAUNCHER%" (
    echo Removing launcher...
    del /Q "%LAUNCHER%"
    echo Launcher removed.
) else (
    echo No launcher found in %USER_BIN%.
)

set "TARGET=%LOCALAPPDATA%\rotatetoe"

if exist "%TARGET%" (
    echo Removing Rotatetoe files...
    rmdir /S /Q "%TARGET%"
    echo Game files removed.
) else (
    echo No Rotatetoe files found in %LOCALAPPDATA%.
)

echo Uninstallation complete.
pause



REM mrrp purrmeowww
