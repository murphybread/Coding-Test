#!/bin/bash
export LC_ALL=C.UTF-8  # Set locale explicitly

# Check the number of parameters.
if [ $# -ne 2 ]; then
  echo "Usage: $0 <level> <taken time>"
  echo "Example: $0 silver1 15m"
  exit 1
fi

# Get the level and time parameters
level="$1"
time="$2"

# Stage all changes in the current directory and its subdirectories
git add .
if [ $? -ne 0 ]; then
  echo "Error staging files. Make sure you're in a git repository."
  exit 1
fi

# Get the list of changed files
changed_files=$(git diff --name-only --cached)
if [ $? -ne 0 ]; then
  echo "Error getting changed files. Make sure you have staged changes."
  exit 1
fi

# Extract the category from the path (replace slashes with dashes)
category=$(dirname "$changed_files" | tr '/' '-')

# Extract only the filename from the path
filename=$(basename "$changed_files")

# Create a commit message with the filename, level, category, and time
commit_message="$filename: $level $category $time"

# Debug the commit message
echo "Commit Message: $commit_message"

# Commit with the constructed message
git commit -m "$commit_message"
