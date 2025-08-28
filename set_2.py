'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # We need to convert the user's letter input first into a number to apply the shift.
    # By using the ASCII system, it's mapped out now for us that we can use the ord and chr functions.
    ascii_code = ord (letter)
    # If the user inputs a single space, the output should also be a single space. This is done earlier on to immediately terminate if said condition is met.
    if ascii_code == 32:
        shift_letter = chr (32)
        return shift_letter
    # If it's not a space, however, we can proceed to applying the shift.
    # But to ensure that our code handles more than one alphabet cycle, we're going to subtract 65 to make A 0.
    base = ascii_code - 65
    # Then, we apply the shift.
    ascii_shifted = base + shift
    # But what if the user inputs a larger shift more than 26?
    # Modulo or the percent that you see is there to check for the surplus.
    # For example, if the ascii_number_shifted equates to 28, 28 % 26  would give you 2.
    # It basically divides your first number, and the second number, and gets the remainder.
    # So for our example, it is exactly 0 wraps around the alphabet, but has a remainder of 2, which we add.
    # This is seen as a similar example of a LeetCode challenge three years ago that also consisted of shifting letters.
    wrap_ascii = ascii_shifted % 26
    # We need to convert it back to ascii.
    wrapped_ascii = 65 + wrap_ascii
    # Then, we can translate this back into it's corresponding letter.
    shifted_letter = chr (wrapped_ascii)
        
    return shifted_letter

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    import string
    alphabet = string.ascii_uppercase
    # We're going to start from the value and take on the rest of the list, plus the remainder of the alphabet.
    # Recall indexing which slices individual characters starting by default from 0.
    # Also recall concantenation which concantenates two strings together.
    # But let's say the shift is stated as 27, this is where the code fails.
    # So let's apply modulo again.
    shift_number = shift % 26
    shifted_alphabet = alphabet[shift_number:] + alphabet [:shift_number]
    # This is to map it out.
    table = str.maketrans(alphabet, shifted_alphabet)

    encrypted = message.translate(table)
    return encrypted

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    ascii_code_letter = ord (letter)
    ascii_code_shift = ord (letter_shift)
    if ascii_code_letter == 32:
        shift_letter = chr (32)
        return shift_letter
    base_letter = ascii_code_letter - 65
    base_shift = ascii_code_shift - 65
    ascii_shifted = base_letter + base_shift
    wrap_ascii = ascii_shifted % 26
    wrapped_ascii = 65 + wrap_ascii
    shifted_letter = chr (wrapped_ascii)
        
    return shifted_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the key is extended to match the length of the message.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Since this is pretty complex and builds upon our previous examples, let's apply the concept of building it's key parts separately first.
    # Step 1. Mapping.
    # To be 0-25.
    def letter_to_num (letter):
        return ord (letter) - ord ("A")
    # Add back what was undone. Mod to take into account wrap around.
    def num_to_letter (number):
        return chr ((number % 26) + ord ("A"))
    # Step 2. Matching length of key to message.
    def match_key (message, key):
        # define variables that will be used
        extended_key = "" # We don't know how long it will be. Starts w/ an empty string until filled in. An accumulator variable.
        key_index = 0 # Which letter of the key we are on.
        # we loop through each character using a for loop until extended_key gets filled.
        for i in range (len(message)): # for every i in the range generated by the length of the message, we loop until match
            extended_key = extended_key + key[key_index] # we add whatever is currently in extended, and add the current key_index which starts from 0
            key_index = (key_index + 1) % len (key) # this updates the value stored in our key_index variable
        return extended_key
    # Step 3. Encrypting the message by the matched key.
    # We'll be using the same principle that we applied by matching.
    matched_key = match_key (message, key)
    encrypted_text = "" # We don't know how long it will be. Starts w/ an empty string until filled in. An accumulator variable.
    # we loop through each character using a for loop until the ciphered_text gets fully translated.
    for i in range (len(message)): # for every i in the range generated by the length of the message, we loop until every is encrypted
        # define variables that will be used
        pmsg = message[i] # which current letter of the message we are on
        pkey = matched_key[i] # matching
        if pmsg == " ":
            encrypted_text = encrypted_text + " "
            continue # move to the next character without making the space an ascii
        
        M = letter_to_num (pmsg) # convert message to number
        K = letter_to_num (pkey) # convert key for the shift

        vigenere_num = (M + K) % 26 # add the shift of the key letter to the message letter, then mod 26 to wrap
        encrypted_text = encrypted_text + num_to_letter(vigenere_num) # convert back to letter until all done
        
    return encrypted_text

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # We have been given a fairly followable flow to interpret in code.
    # Step 1. Take a message to be encoded and a "shift" number. For this example, we will use "INFORMATION_AGE" as the message and 3 as the shift.
    # Step 2. Check if the length of the message is a multiple of the shift. If it is not, add additional underscores to the end of the message until it is.
    length = len (message)
    if length % shift != 0: # Instead of doing a full conditional, since python reads l by l, you can instead update the value if and only if it's not a multiple yet.
        underscore_add = shift - (length % shift) 
        message = message + "_"*underscore_add
    
    # Step 3. Determining how large the grid is.
    nrows = shift # rows determined by shift, the multiple we're trying to adjust to 
    ncolumns = len (message) // shift # since we ensured earlier that the message is a multiple, we can divide (int) the message each with a column of their own
    
    # Step 4. Laying the characters down onto a grid.
    grid = [] # We define our accumulator variable, row, to be the variable where we put our letters in
    start = 0 # Where we start slicing (again, 0 is 1)
    
    for row in range (nrows): # for every row in the range of how many n rows we have, we loop until each has been assigned to a position on the grid
        end = start + ncolumns # this basically entrails that the end is dictated by where the start was ended last loop (ncolumns determine how many letters per row)
        # take into account INFORMATION_AGE being a multiple of 3, since it has 5 columns, when you start at index 0 it ends at index 5 (since you have 5 columns)
        grid.append (message [start:end]) # append stores the info into the grid acc variable
        start = end # to define new start for next set of letters
    
    # Step 5. Read by column top to down, the move on to the next. 
    encoded_text = [] # we start again with an accumulator variable since we'll pick one by one 
    
    for column in range (ncolumns): # for every column in the range of how many n columns we have, we loop until we have gone through every column
        for row in range (nrows): # for every row in the range of how many n rows we have, we loop until we have gone through every row
    # these two basically says, hey let's pick a column, and we go through each row in that column  
            encoded_text.append(grid[row][column])
    return ''.join(encoded_text) # we're saying to the function, join these strings, using no space '' between them.


def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # Step 1. Rebuild the grid that was used to encrypt the message.
    length = len (message)
    
    nrows = shift 
    ncolumns = len (message) // shift

    grid = [] 
    for row in range (nrows):
        grid.append ([''] * ncolumns) # empty spaces multiplied by how many columns there are to be placed in each row

    # Step 2. Placing the message back into the grid. Left to right. Top to bottom. Place each into empty position.
    message_i = 0
    for column in range (ncolumns): #pick column
        for row in range (nrows): # pick row, and top to bottom
            grid[row][column] = message[message_i] # put the letter sliced, and store that into the current column, and into the current grid pointer
            message_i = message_i + 1 # move on to next until loop finish

    # Step 3. Read row by row from left to right.
    decoded_message = ''.join (''.join (row) for row in grid) # for each row in the grid, join them together by row, then by all, no need for i since all in one go

    return decoded_message