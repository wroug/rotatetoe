#!/usr/bin/env bash

set -e

GAME_NAME="rotatetoe"
LOCAL_SHARE="$HOME/.local/share/$GAME_NAME"
TMP_CURRENT="/tmp/rotatetoe-current"

trap 'echo; echo "Update interrupted! Your game may be in inconsistent state."; exit 255' INT



echo "Preparing updater..."


rm -rf "$TMP_CURRENT"
mkdir -p "$TMP_CURRENT"
cp -r "$LOCAL_SHARE/." "$TMP_CURRENT/"

bash "$TMP_CURRENT/bin/updater.sh" "$@"
