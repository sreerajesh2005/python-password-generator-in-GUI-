Password Generator
This is a simple password generator application built using PySimpleGUI. The application allows users to specify the number of uppercase letters, lowercase letters, digits, and symbols to include in the generated password.

Features
User-friendly interface with inputs for specifying the number of each type of character in the password.
Generates a random password based on user inputs.
Displays the generated password in a read-only text box.
Requirements
Python 3.x
PySimpleGUI
Installation
Install Python 3 from python.org.
Install the PySimpleGUI package using pip:
bash
Copy code
pip install PySimpleGUI
Usage
Run the script:
bash
Copy code
python password_generator.py
Enter the desired number of uppercase letters, lowercase letters, digits, and symbols.
Click the 'Ok' button to generate the password.
The generated password will be displayed in the read-only text box.
Click the 'Cancel' button to close the application.
Example
When you run the application, you'll see a window with fields to input the number of uppercase letters, lowercase letters, digits, and symbols you want in your password. After entering the values and clicking 'Ok', the generated password will be shown in the text box.


# Enhanced Password Generator

This is a powerful and user-friendly password generator application built with PySimpleGUI. It allows users to create secure passwords with customizable character types and advanced options.

## Key Features

1. **Customizable Character Sets**:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Digits (0-9)
   - Symbols (!@#$%, etc.)

2. **Visual Character Count Controls**:
   - Intuitive sliders to select the number of each character type (0-8 each)
   - Real-time display of selected character counts

3. **Advanced Security Options**:
   - Exclude similar characters (i, l, 1, L, o, 0, O) to prevent confusion
   - Exclude ambiguous symbols to improve readability and security

4. **Password Strength Assessment**:
   - Visual strength meter with progress bar
   - Percentage-based strength rating
   - Algorithm that considers both length and character diversity

5. **User-Friendly Interface**:
   - Clean, dark theme for reduced eye strain
   - Clearly organized sections with separators
   - Responsive layout with intuitive controls

6. **Convenience Features**:
   - One-click copy to clipboard functionality
   - Password length display
   - Status bar for system feedback

## How It Works

1. Adjust the sliders to select how many of each character type you want in your password
2. Toggle the advanced options based on your security needs
3. Click "Generate" to create a new random password
4. The strength meter will show how secure your password is
5. Click "Copy" to easily transfer the password to your clipboard

## Security Benefits

- Excluding similar characters prevents visual confusion that could lead to entry errors
- Eliminating ambiguous symbols creates passwords that are easier to read and type correctly
- The strength algorithm ensures your passwords have both complexity and length
- True randomization using Python's secure random number generation

This application is perfect for anyone who needs to create secure, memorable passwords for various online accounts and services.
