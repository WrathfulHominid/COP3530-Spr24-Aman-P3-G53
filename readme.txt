Here are the steps to run the frontend

1. cd into request - COP3530-Spr24-Aman-P3-G53\request
2. run: python request.py
3. On a new terminal cd into frontend - COP3530-Spr24-Aman-P3-G53\frontend
4. run the following to install dependencies: npm install
5. run: npm start 
6. A browser should open with the webpage

UPDATE:

Since the code was transferred to S3 cloud storage to be able to use 100k files, there is now another step for the code to work

1. Create a file called config.json within the root folder (take a look at directory.png to see where the file should be placed)
2. Inside config.json copy what you see in keys.png 
3. The reason for this is that git does not let you push important information like these keys, so they cannot be hardcoded
4. After you have created the config.json file you can run the program like usual with the first 6 steps

