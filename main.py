user_input = input("\tPress enter to start encrypting messages using a modified Caesar's Cipher. Enter 'quit' to exit the program\n>>> ")
 
while user_input.lower() != "quit":
    encryption_key = int(input("\tEnter encryption key\n>>> "))
    message_original = str(input("\tEnter your message\n>>> "))
 
    message_encrypted = ""
 
    for char in message_original:
        char_unicode_old = ord(char)
       
        # checks if it is an uppercase letter or a lowercase letter or a number
        upper  = char_unicode_old >= 65 and char_unicode_old <=  90
        lower  = char_unicode_old >= 95 and char_unicode_old <= 122
        number = char_unicode_old >= 48 and char_unicode_old <=  57
 
        # does nothing if it the character is not a letter or number
        char_unicode_new = char_unicode_old + (encryption_key * (upper or lower or number))
 
        # makes unicode only be in between 65 - 90 (A - Z) if the original character was an uppercase letter
        char_unicode_new += upper * ((91 - ((65 - char_unicode_new) % 26) - char_unicode_new) * (char_unicode_new < 65))
        char_unicode_new += upper * ( 65 + ((char_unicode_new - 65) % 26) - char_unicode_new) * (char_unicode_new > 90 )
 
        # makes unicode only be in between 97 - 122 (a - z) if the original character was a lowercase letter
        char_unicode_new += lower * (123 - ((97 - char_unicode_new) % 26) - char_unicode_new) * (char_unicode_new < 97 )
        char_unicode_new += lower * (97 +  ((char_unicode_new - 97) % 26) - char_unicode_new) * (char_unicode_new > 122)
       
        # makes unicode only be in between 48 - 57 (0 - 9) if the original character was a number
        char_unicode_new += number * (58 - ((48 - char_unicode_new) % 10) - char_unicode_new) * (char_unicode_new < 48 )
        char_unicode_new += number * (48 + ((char_unicode_new - 48) % 10) - char_unicode_new) * (char_unicode_new > 57 )
 
        message_encrypted += chr(char_unicode_new)
 
    print("Encrypted message : " + message_encrypted)
 
    user_input = input("\tPress enter to continue encrypting messages. Enter 'quit' to exit the program\n>>> ")
    
