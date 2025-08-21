import PySimpleGUI as sg
import random
import string
import pyperclip

# Set theme and font options
sg.theme('DarkBlack')
sg.set_options(font='Verdana 12')

def generate_password(upper_count, lower_count, digits_count, symbols_count, exclude_similar=True, exclude_ambiguous=True):
    """Generate a password based on specified character types and counts"""
    # Define character pools
    upper_pool = string.ascii_uppercase
    lower_pool = string.ascii_lowercase
    digits_pool = string.digits
    symbols_pool = string.punctuation
    
    # Exclude similar characters if requested (e.g., i, l, 1, L, o, 0, O)
    if exclude_similar:
        similar_chars = 'il1Lo0O'
        upper_pool = ''.join(c for c in upper_pool if c not in similar_chars)
        lower_pool = ''.join(c for c in lower_pool if c not in similar_chars)
        digits_pool = ''.join(c for c in digits_pool if c not in similar_chars)
    
    # Exclude ambiguous symbols if requested
    if exclude_ambiguous:
        ambiguous_symbols = '{}[]()/\'"`~,;:.<>\\'
        symbols_pool = ''.join(c for c in symbols_pool if c not in ambiguous_symbols)
    
    # Generate characters for each category
    upper_chars = random.sample(upper_pool, min(upper_count, len(upper_pool))) if upper_pool else []
    lower_chars = random.sample(lower_pool, min(lower_count, len(lower_pool))) if lower_pool else []
    digits_chars = random.sample(digits_pool, min(digits_count, len(digits_pool))) if digits_pool else []
    symbols_chars = random.sample(symbols_pool, min(symbols_count, len(symbols_pool))) if symbols_pool else []
    
    # Combine and shuffle
    all_chars = upper_chars + lower_chars + digits_chars + symbols_chars
    random.shuffle(all_chars)
    
    return ''.join(all_chars)

def calculate_strength(password):
    """Calculate password strength based on length and character diversity"""
    if not password:
        return 0
    
    strength = 0
    length = len(password)
    
    # Length contributes up to 50 points (max at 20+ chars)
    strength += min(length * 2.5, 50)
    
    # Character diversity
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    
    # Each character type adds points
    type_count = sum([has_upper, has_lower, has_digit, has_symbol])
    strength += (type_count - 1) * 15  # More types = better
    
    return min(int(strength), 100)

# Layout definition
layout = [
    [sg.Text('Password Generator', font='Verdana 16 bold')],
    [sg.HorizontalSeparator()],
    [sg.Text('Character Types:', font='Verdana 13 bold')],
    [
        sg.Text('Uppercase:'), 
        sg.Slider(range=(0, 8), default_value=2, orientation='h', key='-UP-'),
        sg.Text('A-Z', size=(5, 1))
    ],
    [
        sg.Text('Lowercase:'), 
        sg.Slider(range=(0, 8), default_value=2, orientation='h', key='-LOW-'),
        sg.Text('a-z', size=(5, 1))
    ],
    [
        sg.Text('Digits:'), 
        sg.Slider(range=(0, 8), default_value=2, orientation='h', key='-DIG-'),
        sg.Text('0-9', size=(5, 1))
    ],
    [
        sg.Text('Symbols:'), 
        sg.Slider(range=(0, 8), default_value=2, orientation='h', key='-SYM-'),
        sg.Text('!@#$%', size=(5, 1))
    ],
    [sg.HorizontalSeparator()],
    [sg.Text('Options:', font='Verdana 13 bold')],
    [
        sg.Checkbox('Exclude similar characters (i, l, 1, L, o, 0, O)', default=True, key='-EX_SIM-'),
        sg.Checkbox('Exclude ambiguous symbols', default=True, key='-EX_AMB-')
    ],
    [sg.HorizontalSeparator()],
    [
        sg.Button('Generate', size=(10, 1)), 
        sg.Button('Copy', size=(10, 1)), 
        sg.Button('Exit', size=(10, 1))
    ],
    [sg.Text('Password:'), sg.Push(), sg.Text('', key='-PASS_LEN-')],
    [
        sg.Multiline(size=(40, 3), no_scrollbar=True, disabled=True, key='-PASS-', 
                    background_color='black', text_color='white')
    ],
    [sg.Text('Strength:')],
    [
        sg.ProgressBar(100, orientation='h', size=(30, 20), key='-STRENGTH-', 
                      bar_color=('green', 'black')),
        sg.Text('0%', key='-STR_PCT-', size=(5, 1))
    ],
    [sg.StatusBar('Ready', key='-STATUS-')]
]

# Create window
window = sg.Window('Enhanced Password Generator', layout, finalize=True)

# Event loop
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
        
    if event == 'Generate':
        try:
            # Get values from sliders
            u_upper = int(values['-UP-'])
            u_lower = int(values['-LOW-'])
            u_digits = int(values['-DIG-'])
            u_symbols = int(values['-SYM-'])
            
            # Check if at least one character type is selected
            if u_upper + u_lower + u_digits + u_symbols == 0:
                sg.popup_error('Please select at least one character type!')
                continue
                
            # Generate password
            password = generate_password(
                u_upper, u_lower, u_digits, u_symbols,
                values['-EX_SIM-'], values['-EX_AMB-']
            )
            
            # Update UI
            window['-PASS-'].update(password)
            window['-PASS_LEN-'].update(f'{len(password)} chars')
            
            # Calculate and display strength
            strength = calculate_strength(password)
            window['-STRENGTH-'].update(strength)
            window['-STR_PCT-'].update(f'{strength}%')
            
            # Update status
            window['-STATUS-'].update('Password generated successfully')
            
        except Exception as e:
            sg.popup_error(f'Error generating password: {str(e)}')
            window['-STATUS-'].update('Error generating password')
            
    if event == 'Copy':
        password = values['-PASS-']
        if password:
            try:
                pyperclip.copy(password)
                window['-STATUS-'].update('Password copied to clipboard!')
            except Exception as e:
                sg.popup_error(f'Could not copy to clipboard: {str(e)}')
        else:
            sg.popup_error('No password to copy! Generate one first.')

window.close()
