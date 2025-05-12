AmazonifyTracks is a simple Python-based tool that reads a list of liked songs from a .txt file and automatically imports them into your Amazon Music library using browser automation.

🚀 Features
Import songs from a plain text file

Automate Amazon Music searches and library additions

Lightweight and easy to use

Built with Python and Selenium

📄 Input Format
The input file should be a plain .txt file with each line formatted like:
      Artist Name - Song Title
      Taylor Swift - Blank Space
      Imagine Dragons - Believer
🔧 Requirements
Python 3.7+
Google Chrome
ChromeDriver (matching your Chrome version)

Amazon Music account

🛠️ Installation
Clone the repo
git clone https://github.com/yourusername/text2tunes.git
cd text2tunes
Install dependencies

pip install -r requirements.txt
Download ChromeDriver

Visit: https://chromedriver.chromium.org/downloads

Make sure it matches your Chrome version

Place the chromedriver executable in your system PATH or in the project root

⚙️ Usage
Create a text file named songs.txt in the project directory with your liked songs.

Run the script:

python import_songs.py
Log in to your Amazon Music account when prompted.

The script will search for each song and add it to your library.

💡 Pro Tip: Run the script in headless mode by editing the Selenium options if you don’t want the browser window to appear.

🧠 How It Works
Uses Selenium to automate the Chrome browser

Logs into Amazon Music

Searches for each song in the list

Clicks the "Add to Library" button if found

📌 Notes
This tool is for personal use only and is not affiliated with Amazon.

Excessive automation may trigger Amazon's anti-bot measures. Use responsibly.
