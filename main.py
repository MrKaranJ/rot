def rot(text, rotNumber):
    """
    Take an input string 'text' and ROT Algorithm number 'n' and encode 
    the string using ROT n algorithm.
    
    USAGE:

    print(rot("ABCD", 2))

    OUTPUT:

    CDEF
    """
    # ASCII Values for 'A' and 'Z'
    startIndex = 65
    endIndex = 90
    # Initializing empty string for encoding
    codedText = ""
    # Process one character at a time
    for char in text:
        # Only process capital alphabet
        if (ord(char) >= startIndex and ord(char) <= endIndex):
            uncoded = ord(char) - startIndex
            # Encode based on the cipher number
            coded = uncoded + rotNumber
            # In case of invalid ASCII value consider the remainder
            if coded >= (endIndex - startIndex + 1):
                coded = coded % int(endIndex - startIndex + 1)
            coded = coded + startIndex
        else:
            coded = ord(char)
        # Concatenate to the output string
        codedText = codedText + chr(coded)
    return codedText

def derot(text, rotNumber):
    """
    Take an input string 'text' and ROT Algorithm number 'n' and decode 
    the string using ROT n algorithm.
    
    USAGE:

    print(derot("CDEF", 2))

    OUTPUT:

    ABCD
    """
    # ASCII Values for 'A' and 'Z'
    startIndex = 65
    endIndex = 90
    decodedText = ""
    # Process one character at a time
    for char in text:
        # Only process capital alphabet
        if (ord(char) >= startIndex and ord(char) <= endIndex):
            coded = ord(char) - startIndex
            # Decode based on the cipher number
            decoded = coded - rotNumber
            # In case of invalid ASCII value add the alphabet length
            if decoded < 0:
                decoded = decoded + (endIndex - startIndex + 1)
            decoded = decoded + startIndex
        else:
            decoded = ord(char)
        # Concatenate to the output string
        decodedText = decodedText + chr(decoded)
    return decodedText

# Take the input text and convert to upper for easier processing
text = input("Enter Text String:\n")
text = text.upper()
# Get input ROT Cipher number
rotNumber = int(input("Enter ROT Cipher Number:\n"))

# Check validity of ROT Cipher number and process
# Else throw error
if isinstance(rotNumber, int) and rotNumber > 0 and rotNumber < 26:
    print("Unencoded String: {0}".format(text))
    print("Rotation Cipher Number: {0}".format(rotNumber))
    print("Coded Text: {0}".format(rot(text, rotNumber)))
    print("Decoded Text: {0}".format(derot(rot(text, rotNumber), rotNumber)))
else:
    print("Invalide ROT Number. Please try again with a number between 1 and 25")