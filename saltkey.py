#!/usr/bin/env python3
"""WordPress Salt Key Updater

A utility script to automatically fetch and update WordPress security keys/salts
in wp-config.php file.

Features:
    - Fetches fresh security keys from WordPress.org API
    - Creates backup of existing wp-config.php
    - Updates all security keys while preserving file structure
    - Handles cleanup of temporary files

Usage:
    Place script in WordPress root directory and run:
    python3 saltkey.py

Requirements:
    - Python 3.x
    - wp-config.php file in same directory
    - Internet connection to access WordPress.org API

Author: Percio Andrade
Email: percio@zendev.com.br
Version: 1.0
"""

import os
import re
import urllib.request

# Get the absolute path of the script file
script_directory = os.path.dirname(os.path.abspath(__file__))
wp_config_file_path = os.path.join(script_directory, "wp-config.php")

# Check if wp-config.php file exists
if not os.path.exists(wp_config_file_path):
    print("The wp-config.php file was not found. The script will exit.")
    exit(1)

# Fetch values from the URL and save them in key.txt
url = "https://api.wordpress.org/secret-key/1.1/salt/"
response = urllib.request.urlopen(url)
keys_content = response.read().decode("utf-8")

with open("key.txt", "w") as key_file:
    key_file.write(keys_content)

# Create a backup of the original wp-config.php file
os.rename(wp_config_file_path, "wp-config.php.bak")

# Update the wp-config.php file with the new keys
key_dict = {}
with open("key.txt", "r") as key_file:
    for line in key_file:
        match = re.search(r"define\('([^']*)',\s*'([^']*)'\);", line)
        if match:
            key, value = match.groups()
            key_dict[key] = f"define('{key}', '{value}');"

with open("wp-config.php.bak", "r") as wp_config_file:
    wp_config_content = wp_config_file.read()

for key, value in key_dict.items():
    wp_config_content = re.sub(r"define\('" + key + r"',\s*'.*'\);", value, wp_config_content)

with open("wp-config.php", "w") as wp_config_file:
    wp_config_file.write(wp_config_content)

# Remove the temporary key.txt file
os.remove("key.txt")

print("The keys have been updated in the wp-config.php file")