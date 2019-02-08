**Instructions on how to use the tachycardia.py module:**
Enter the repository with the tachycardia.py code, and run ‘python3 tachycardia.py’ from the command line. The module will ask the user to enter a word. Once the word is entered:
* ’The answer is True’ will be printed as output if the word contains ‘tachycardic’ in it, regardless of capitalization, leading or trailing spaces or punctuation
* ‘The answer is False’ will be printed as output if the word does not contain ‘tachycardic’ in it

**Instructions on how to use the testing script for tachycardia.py module:**
To run unit testing on the tachycardia.py module, the user should execute ‘pytest -v’ from the terminal. This will return ‘PASSED’ or ‘FAILED’ for each unit test. 

**Notes on how the tachycardia.py module works:**
The main function calls for the user to input a word. The main function then calls the is_tachycardic function, which makes the input string lowercase to prevent issues with capitalization. It then searches for ‘tachycardic’ within the input, and prints that the answer is either True or False depending on whether or not tachycardic exists in the input. 

**Notes on how the testing script for the tachycardia.py module works:**
The test_tachycardia.py script uses the parametrized utility of pytest in order to perform unit testing on the is_tachycardic function. It consists of a parametrized test with 6 test cases and a single non-parametrized unit test. The test cases include both expected True and expected False cases, with a mix of differing capitalization and extra spacing and punctuation to robustly test the function.

**Notes about the assignment:**
* I accidentally committed and pushed my __pycache__ and .venv folders, but removed them from GitHub and they no longer are in the master branch
*I enabled travis CI and ensured that my scripts passed the travis CI testing, including following pep8 standards


