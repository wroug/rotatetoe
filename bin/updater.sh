#!/usr/bin/env bash




set -e

GAME_NAME="rotatetoe"
LOCAL_SHARE="$HOME/.local/share/$GAME_NAME"
TMP_CURRENT="/tmp/rotatetoe-current"
TMP_UPDATE="/tmp/rotatetoe-update"
REPO_URL="https://github.com/wroug/rotatetoe"
RELEASE_ZIP_URL="$REPO_URL/releases/latest/download/rotatetoe-linux.zip"
LOCAL_VERSION=$(<"$LOCAL_SHARE/version.txt")
ORIGIN_VERSION=$(curl -s https://raw.githubusercontent.com/wroug/rotatetoe/main/version.txt | tr -d "\n")

if [ "$LOCAL_VERSION" = "$ORIGIN_VERSION" ]; then
    echo "Already up to date."
    exit 0
fi


trap 'echo; echo "Update interrupted! Your game may be in inconsistent state."; exit 255' INT

echo "Starting updater..."


echo "Downloading latest release..."
rm -rf "$TMP_UPDATE"
mkdir -p "$TMP_UPDATE"
curl -L -o "$TMP_UPDATE/release.zip" "$RELEASE_ZIP_URL"
unzip -q "$TMP_UPDATE/release.zip" -d "$TMP_UPDATE"



echo "Applying update..."
rm -rf "$LOCAL_SHARE/"*
cp -r "$TMP_UPDATE/rotatetoe/"* "$LOCAL_SHARE/"



echo "Restoring persistent files..."
PERSISTENT_LIST="$TMP_CURRENT/game/persistent_files.txt"
if [ -f "$PERSISTENT_LIST" ]; then
    while IFS= read -r file; do
        SRC="$TMP_CURRENT/$file"
        DEST="$LOCAL_SHARE/$file"
        if [ -e "$SRC" ]; then
            mkdir -p "$(dirname "$DEST")"
            cp -r "$SRC" "$DEST"
        fi
    done < "$PERSISTENT_LIST"
fi

python3 -m venv "$LOCAL_SHARE/venv"
source "$LOCAL_SHARE/venv/bin/activate"
python3 -m pip install --upgrade pip
python3 -m pip install -r "$LOCAL_SHARE/requirements.txt"
deactivate

rm -rf "$TMP_CURRENT" "$TMP_UPDATE"
chmod +x "$LOCAL_SHARE/bin/"*
echo "Update done! You can now run the game as usual."
