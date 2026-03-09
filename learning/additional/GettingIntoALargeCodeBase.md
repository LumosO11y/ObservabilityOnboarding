# The Beginning after the End
Entering a large, established codebase can feel like being dropped in the middle of an  
ocean without a boat.  
It’s overwhelming, but the key is to stop trying to   
travel across the sea in one go, and start by getting to the nearest island.

Here is a collection of tips, tricks and advice to navigating and getting to know a new large codebase to tide you over  
(get it? because of the ocean metaphor? Okay I'll stop now haha).

## Taking your first step:
- Start by finding the ``main`` and the ``projectRunner()``.  
Go over the initialized variables, the method names, and see if you can recognize where the core logic of the application occurs.
- Before writing any code or changing any logic, ensure you can actually run the thing.
Try to run the project locally and see what you can gather.

## Going Deeper: 
- Try to recognize the main flow of the application. Which method calls what? In what order?  
Why? What variables do these functions use? How do the objects interact and relate to each other?
- Go through the pom.xml and take a look at the dependencies used in the project.  
Which do you recognize? How are they used? What are they used for?  
What can they tell you about the build of the project?
What can they tell you about the way it handles data or processing?

## From Source to Destination:
- Locate the Source and Destination of information; They might be able to tell you something about the type and structure of data flowing through the project.
Do they use a specific format, or have special requirements that  
could explain some of the transformations data goes through in the program?
- Look at the project's configuration files. Can you glean more information about the components in use and their relationship?
  
