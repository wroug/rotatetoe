#!/usr/bin/env bash

GAME_NAME="rotatetoe"
LOCAL_SHARE="$HOME/.local/share/$GAME_NAME"
LOCAL_BIN="$HOME/.local/bin/$GAME_NAME"




echo "This will completely remove $GAME_NAME from your system."
read -p "Are you sure? (y/n) " answer

case "$answer" in
    [Yy]* )
        echo "Removing symlink..."
        rm -f "$LOCAL_BIN"
        echo "Removing game folder..."
        rm -rf "$LOCAL_SHARE"


        echo "Uninstall complete!"
        exit 0
        ;;
    [Nn]* )
        echo "Aborted."
        exit 0
        ;;
    * )
        echo "Invalid input. Aborted."
        exit 1
        ;;
esac
