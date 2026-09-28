# Getting Into a Large Codebase

Entering a large, established codebase can feel like being dropped in the middle of an  
ocean without a boat.  
It’s overwhelming, but the key is to stop trying to
travel across the sea in one go, and start by getting to the nearest island.

Here is a collection of tips, tricks and advice for navigating and getting to know a new large codebase to tide you over  
(get it? because of the ocean metaphor? Okay I'll stop now haha).

## Taking your first step

- Start by finding the entry point (the ``main`` method) and whatever it hands off to to start the application.  
Go over the initialized variables, the method names, and see if you can recognize where the core logic of the application occurs.
- Before writing any code or changing any logic, ensure you can actually run the thing.
Try to run the project locally and see what you can gather.

## Going Deeper

- Try to recognize the main flow of the application. Which method calls what? In what order?  
Why? What variables do these functions use? How do the objects interact and relate to each other?
- Go through the project's build file (e.g. ``go.mod`` in a Go project, ``pom.xml`` in a Java project) and take a look at the dependencies used in the project.  
Which do you recognize? How are they used? What are they used for?  
What can they tell you about the build of the project?
What can they tell you about the way it handles data or processing?

## From Source to Destination

- Locate the Source and Destination of information; they might be able to tell you something about the type and structure of data flowing through the project.
Do they use a specific format, or have special requirements that  
could explain some of the transformations data goes through in the program?
- Look at the project's configuration files. Can you glean more information about the components in use and their relationship?
  
## Don't Sweat the Small Stuff

- Use breakpoints strategically while running code to get a more in-depth look at things that look complicated (your IDE's debugger, or [Delve](https://github.com/go-delve/delve) for Go).
- Use scratch files to run methods in isolation in order to understand them better.  
  You can also use them to test out and manipulate code logic.
- Read the tests. They're usually the most honest documentation of how a piece of code is meant to be called and what it's expected to return.
- Use ``git log`` and ``git blame`` on a confusing piece of code: the commit message and linked merge request often explain *why* it looks the way it does.

- **Also, don't hesitate to ask other members of the team for advice and additional explanations about the code structure and logic!**

## Your Turn

Ask your mentor to pick one of our repositories for you. Using the tips above:

1. Get it building and running locally (or its tests passing, if it can't run standalone).
2. Draw a diagram of how data flows through it: where it comes in, the main components it passes through, and where it goes out.
3. Write down 3 things you still don't understand, and go over the diagram and the questions with your mentor.
