# Youtube_mass_uploader
Selenium bot that uploads up to ~100 videos a day.

Start by adding your chosen video in the 'video' folder.
Then add the email, password of you youtube account and the new video path (in the 'videos' folder), title od the video and description of the video in 'credentials.py'.

If you want to add more emails to choose from, when running the script, add them in the EMAILS array and adjust 'uploader.py'.

When you have added your video/s, you can run 'main.py' in the therminal, choose your email, video, if you want to run the webdriver headless* and then enjoy your videos.

If your youtube account is new, you can probably upload only a few videos, atfer a few das this will increase to ~100.

*headless means that the driver is not getting rendered, so no window will open.
