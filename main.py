from art import logo

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # Adjust shift_amount for decoding
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position after shifting
            new_position = (position + shift_amount) % 26
            # Append the new character to the end_text
            end_text += alphabet[new_position]
        else:
            # Append non-alphabetic characters unchanged
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
