# ZPL-Auto-Printer

This software continuously checks a specific folder for files. If the folder doesn't exist, it is created. Whenever files are found, the program sends any text files as ZPL commands to the printer. If no text files are detected, it checks for zip files (the original format downloaded from the logistic site Mercado Livre) and then verifies for text files again.

The program is intended to run on any PC without requiring Python or any of its libraries. To achieve this, it has been compiled into an executable file using PyInstaller.

## Future Improvements

Since it was my first program to go into production, it lacks some features to improve its speed, intuitiveness, and modularity. Here are some points that could be improved in future versions:

- **~~Read the printer IP address from an external file:~~**
  - This allows for easy updates if the printer is installed on another PC, or if the PC's IP address changes, without needing to recompile the program.

- **~~Create functions for checking the folder and sending the ZPL commands to the printer:~~**
  - This will make the code easier to understand and scale.

- **~~Improve user messages' content and layout (line breaks):~~**
  - Enhance the clarity and readability of messages displayed to the user.

- **Treat corrupted zip file errors:**
  - A common error is when a zip file is corrupted. It could ask for user confirmation and then automatically delete the file when that happens, instead of just closing the program without any messages.
 
- **Add logging for printing jobs:**
  - If, for any reason, the program is terminated, either due to an error or the user's actions, a log would provide the opportunity to examine the last files that were printed and their respective times, enabling the printing or downloading of labels based on the last one.
---

Feel free to adjust any specific details to better match your project's requirements.
