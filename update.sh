#!/bin/bash
# Check GitHub for newer version and update if available
REPO="https://api.github.com/repos/studio-justin-braun/BTtoAUX"
LOCAL_VERSION=$(git rev-parse HEAD)
REMOTE_VERSION=$(curl -s $REPO/commits/main | grep sha | head -n 1 | cut -d '"' -f4)

echo "Local version: $LOCAL_VERSION"
echo "Remote version: $REMOTE_VERSION"

if [ "$LOCAL_VERSION" != "$REMOTE_VERSION" ]; then
    echo "Updating to latest version..."
    git pull --rebase origin main
    echo "Update finished."
else
    echo "Already up to date."
fi
