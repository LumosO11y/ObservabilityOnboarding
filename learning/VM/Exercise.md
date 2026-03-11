# The Linux Manipulation Exercise
**Goal**: Find "hidden" information about the computer using *only* the terminal.  
**Scenario**: "You have been given a mystery server. You need to identify its 'DNA' (hardware), its 'Health' (processes), and its 'Security' (permissions)."  
**Additional Instructions**: Note down the commands you used 
## Be on Your Way!
- **The Version Check**: Find out exactly which version of the Linux Kernel is running.
- **The Heartbeat**: View the CPU information. Is it an Intel, AMD, or ARM chip?
- **The Long Way Home**: Navigate to the ``/var/log`` directory. List all files, but show the "long" version so you can see who owns the files.
- **The Content Hunt**: Find the file named ``syslog`` or ``messages``. Use a command to read only the last 20 lines of that file to see what the system is doing right now.
- **Create a Secret**: Create a new folder in your home directory called ``SecretProject``.
- **Lock the Door**: Change the permissions so that only you (the owner) can read and write to it, and no one else in the "world" can even see it's there.  
Then **Verify**; Run ls -ld to prove the permissions changed.
- **The Birth of a File**: Create an empty file named notes.txt without opening an editor.
- **The Clone**: Create an exact copy of ``notes.txt`` and call it ``backup_notes.txt``.
- **The Relocation**: Create a directory called ``Archive`` and move the backup file into it.
- **The Search Party**: Find every file in the current directory that ends in ``.txt``.
- **The Cleanup**: Remove the original ``notes.txt`` file.
- **The "Nuke" (Use with Caution)**: Delete the ``Archive`` directory and everything inside it at once.
  

