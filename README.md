# ImageDownloader


##Basics

This program download image file from urls in csv file.
Before execute, the file 'imageurls.csv' must be in the same directory of the .exe file.
When the program success, two files 'downloaded.csv' and 'log.txt' and a folder 'image' will appear.

1.	imageurls.csv
  Save urls of images to download as 'imageurls.csv'.
  It has to be this name or the program will never recognize the file.
  
2.	downloaded.csv
  When the program runs, 'downloaded.csv' file will be created.
  In this file, the urls in 'imageurls.csv' will be copied with tag added; 'Success' means the image downloaded successfully while 'Fail' means not.
  
3.	image directory
  The images downloaded will be saved in this folder.
  When there is any duplicated file, it will replace it without questioning.

4.	log.txt
  Log file will also be created.


##Description

This program is for windows.
1. Download 'py2exe' from web.
2. Put this command in windows cmd command line.
    > python setup.py py2exe
3. Go to 'dist' and find 'ImageDownloader' exe file and run.
