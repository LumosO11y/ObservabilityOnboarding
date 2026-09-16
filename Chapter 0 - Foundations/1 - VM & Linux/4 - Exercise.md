# The Linux Manipulation Exercise
**Goal**: Find "hidden" information about the computer using *only* the terminal.  
**Scenario**: "You have been given a mystery server. You need to identify its 'DNA' (hardware), its 'Health' (processes), and its 'Security' (permissions)."  
**Additional Instructions**: Note down the commands you used 
## Be on Your Way!
1. **The Version Check**: Find out exactly which version of the Linux Kernel is running.
2. **The Heartbeat**: View the CPU information. Is it an Intel, AMD, or ARM chip?
3. **The Long Way Home**: Navigate to the ``/var/log`` directory. List all files, but show the "long" version so you can see who owns the files.
4. **The Content Hunt**: Find the file named ``syslog`` or ``messages``. Use a command to read only the last 20 lines of that file to see what the system is doing right now.
5. **Create a Secret**: Create a new folder in your home directory called ``SecretProject``.
6. **Lock the Door**: Change the permissions so that only you (the owner) can read and write to it, and no one else in the "world" can even see it's there.  
6.1 Then **Verify**; Run ``ls -ld`` to prove the permissions changed.
7. **The Birth of a File**: Create an empty file named notes.txt without opening an editor.
8. **The Poet**: Write "Hello World!(:" into the file.
9. **The Clone**: Create an exact copy of ``notes.txt`` and call it ``backup_notes.txt``.
10. **The Relocation**: Create a directory called ``Archive`` and move the backup file into it.
11. **The Search Party**: Find every file in the current directory that ends in ``.txt``.
12. **The Cleanup**: Remove the original ``notes.txt`` file.
13. **The "Nuke" (Use with Caution)**: Delete the ``Archive`` directory and everything inside it at once.
  

