#!/usr/bin/env bash


GAME_NAME="rotatetoe"
GAME_SRC="$(dirname "$0")/.."
LOCAL_SHARE="$HOME/.local/share/$GAME_NAME"
LOCAL_BIN="$HOME/.local/bin"
RUN_SCRIPT="bin/run.sh"
VENV_DIR="$LOCAL_SHARE/venv"

echo "Starting installation."
echo "If you encounter any problems, feel free to make an issue at https://github.com/wroug/rotatetoe/issues"

if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install it first."
    exit 1
fi

for dire in "$HOME/.local/share" "$HOME/.local/bin"; do
    if [ ! -d "$dire" ]; then
        read -p "Directory ~/.local/$(basename $dire) does not exist. Create it? (y/n) " answer
        case "$answer" in
            [Yy]* ) mkdir -p "$dire"; echo "Created ~/.local/$(basename $dire)";;
            [Nn]* ) echo "Cannot continue without ~/.local/$(basename $dire). Exiting."; exit 1;;
            *     ) echo "Invalid input. Exiting."; exit 1;;
        esac
    fi
done

if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    SHELL_NAME=$(basename "$SHELL")

    case "$SHELL_NAME" in
        bash)
            SHELL_FILE="$HOME/.bashrc"
            ;;
        zsh )
            SHELL_FILE="$HOME/.zshrc"
            ;;
        *   )
            SHELL_FILE=""
            ;;
    esac
    
    if [ -n "$SHELL_FILE" ] && [ -f "$SHELL_FILE" ]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_FILE"
        echo "Added ~/.local/bin to PATH in ~/$(basename $SHELL_FILE)."
    else
        echo ""
        echo "Warning: Could not detect shell config file for $SHELL_NAME."
        echo "Please add this line to your shell config manually:"
        echo 'export PATH="$HOME/.local/bin:$PATH"'
        read -p "Press Enter to continue after adding it, or Ctrl+C to abort."
    fi
fi

echo "Copying game to $LOCAL_SHARE"
rm -rf "$LOCAL_SHARE"
cp -r "$GAME_SRC" "$LOCAL_SHARE"

if [ ! -d  "$VENV_DIR" ]; then
    echo "Creating python virtual environment"
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists, skipping creation"
fi
echo "Installing required Python packages..."
source "$VENV_DIR/bin/activate"
python3 -m pip install --upgrade pip
python3 -m pip install -r "$LOCAL_SHARE/requirements.txt"
deactivate


chmod +x "$LOCAL_SHARE/bin/"*

ln -sf "$LOCAL_SHARE/$RUN_SCRIPT" "$LOCAL_BIN/$GAME_NAME"



echo ""
echo "Installation complete! You can now run the game by typing:"
echo "    $GAME_NAME"
echo ""
echo "You can safely delete the original installer folder if you want."
