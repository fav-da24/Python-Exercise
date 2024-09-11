# Music Streaming Web App

To create a music streaming web app from your Android phone using Termux and Python, you can use Flask to serve the music files over HTTP. Flask will allow you to create a simple web server, and HTML5 can handle audio streaming that continues to play even when your phone's screen is locked or when the app is not in the foreground. 

Here's a step-by-step guide to help you set this up:

## 1. Install Termux and Necessary Packages
First, ensure that you have Termux installed on your Android device. Then, open Termux and run the following commands to update the package list and install Python and Flask

## 2. Set Up Flask App
Next, create a Python script that will serve as your Flask app. You can create this script using a text editor like nano or vim.

## 3. Write the Flask App Code
Write simple Flask app that will stream your music files

## 4. Modify the MUSIC_DIR Path
Replace "/path/to/your/music" with the actual path to the directory where your music files are stored. 

## 5. Run the Flask App
Save and exit the file (Ctrl + X, then Y and Enter in nano).

## 6. Access the Web App
Now, open a web browser on your phone or another device connected to the same Wi-Fi network, and navigate to http://<your_phone_ip>:5000. You should see a list of your music files with audio players.

## 7. Keep the Stream Playing When Screen is Locked or App is Backgrounded
HTML5 audio playback should continue even if the screen is locked or the browser is backgrounded. However, some Android browsers or device settings might stop background audio playback. Here are some tips:

  - Use Chrome or Firefox: These browsers generally support background audio playback well.
  - Battery Optimization Settings: Ensure that battery optimization is disabled for your browser app to prevent it from being paused when in the background.
  - Lock Screen Controls: Some browsers also offer lock screen media controls.
