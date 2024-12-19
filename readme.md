# WordPress Salt Key Updater 🔑

## About 📝
A Python utility script that automatically fetches and updates WordPress security keys/salts in wp-config.php file.

- Author 👨‍💻
- Percio Andrade
- Email: percio@zendev.com.br
- Website: Zendev : https://zendev.com.br

## Features ✨
- Fetches fresh security keys from WordPress.org API 🔄
- Creates backup of existing wp-config.php 💾
- Updates all security keys while preserving file structure 🔐
- Handles cleanup of temporary files 🧹

## Requirements 📋
- Python 3.x
- wp-config.php file in same directory
- Internet connection to access WordPress.org API

## Usage 🚀
1. Place script in WordPress root directory
2. Run:
```bash
python3 saltkey.py
```

# Safety Features 🛡️
- Automatically creates wp-config.php.bak backup
- Validates wp-config.php existence
- Cleans up temporary files
- Preserves original file structure

# Notes 📌
- Always backup your WordPress files before running
- Ensure proper file permissions
- Run from WordPress root directory