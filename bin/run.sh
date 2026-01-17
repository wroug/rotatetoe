#!/usr/bin/env bash

LOCAL_SHARE="$HOME/.local/share/rotatetoe"

case "$1" in
    --uninstall)
        "$LOCAL_SHARE/bin/uninstall.sh"
        exit 0
        ;;
    --update)
        "$LOCAL_SHARE/bin/initupdate.sh"





cd "$HOME/.local/share/rotatetoe"

#if ! command -v python3 &> /dev/null; then
#    echo "Python3 not found. Please be kind and install it."
#    exit 1
#fi

if [ -f "venv/bin/activate" ]; then
    . venv/bin/activate
else
    echo "Warning! Virtual environment not found. Please check if you have properly ran install.sh."
    while true; do
        read -p "Run install.sh? (y/n) " answer

        case "$answer" in
            [Yy]* )
                echo "Making install.sh executable..."
                cd "$LOCAL_SHARE/bin"
                chmod +x install.sh
                echo "Running install.sh..."
                ./install.sh
                echo "Done!"
                exec "$0" "$@"
                break
                ;;
            [Nn]* )
                echo Continuing.
                break
                ;;
            * )
                echo "Invalid input"
                ;;
        esac
    done
fi

echo "Tip: Resize your terminal now if needed; it's harder to change later. (enter to continue)"
read

cd "$LOCAL_SHARE/game"


python3 main.py
deactivate
echo "If you encountered any problems, feel free to make an issue at https://github.com/wroug/rotatetoe/issues"
echo "We hope you had fun! Press enter to close"

read
