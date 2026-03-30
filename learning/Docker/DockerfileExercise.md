# Overview
In this exercise, you'll get hands-on experience with the Dockerfile.    
You will create your own first Dockerfile and use it to run the Python app that is in the DockerFilePythonApp directory. 
Good luck!

## Your first own Dockerfile
Using everything you've learned so far and researched about the composition of Dockerfiles, create your own Dockerfile to run your first containerized app!    
**The Dockerfile should be made according to the following instructions:**
1. Use an official lightweight Python image
2. Set the directory inside the container for our app
3. Copy only the requirements file first (Better for caching). Also, think why it is better for caching!
4. Install the required libraries
5. Copy the rest of our app code
6. Inform Docker the app runs on port 5000
7. Last but not least, add the command to run the app

## Now that you have your Dockerfile
1. Open the terminal in the same folder where you have the app and the Dockerfile
2. Create an image from your Dockerfile
3. Run the container! make sure to map the app to port 8080 on your machine.

## Verification
1. Open a browser and go to http://localhost:8080
2. See if you got the success message!

## More Questions For you My Friend
- Stop the container with ctrl + c, then try to run it again without the port mapping.
1. Is the container still running?
2. Can you still see the website at localhost:8080? Why or why not?
