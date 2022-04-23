"""Interstellar Intcode Program"""

# Test cases
prompt_code = [1,9,10,3,2,3,11,0,99,30,40,50]
short_code1 = [1,0,0,0,99]
short_code2 = [2,3,0,3,99]
short_code3 = [2,4,4,5,99,0]
short_code4 = [1,1,1,4,99,5,6,0,99]
gravity_assist = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,9,23,27,2,27,6,31,1,5,31,35,2,9,35,39,2,6,39,43,2,43,13,47,2,13,47,51,1,10,51,55,1,9,55,59,1,6,59,63,2,63,9,67,1,67,6,71,1,71,13,75,1,6,75,79,1,9,79,83,2,9,83,87,1,87,6,91,1,91,13,95,2,6,95,99,1,10,99,103,2,103,9,107,1,6,107,111,1,10,111,115,2,6,115,119,1,5,119,123,1,123,13,127,1,127,5,131,1,6,131,135,2,135,13,139,1,139,2,143,1,143,10,0,99,2,0,14,0]

def update_intcodes(intcodes):
    """
    An Intcode Program is a list of comma-separated integers, like [1,0,0,3,99].
    To run one:
    Step 1:  Look at integer at index 0 to find the "opcode". If opcode is... 
        1 = Add integer at indices 1 & 2 and store the result at the index denoted by integer at index 3
        2 = Same as opcode1 but multiply the integers instead
        99 = End program
        Unknown code = Something went wrong! 
    Step 2: Move to the next sequence by stepping forward 4 positions (so if you previously started at Index0, you should start the next sequence at Index4)
    ---
    Examples: 
    1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
    2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
    2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

    :return: Updated list of intcodes
    """
    
    try: 

        # Do this at every fourth element of the list of intcodes starting at 0
        # Note: The "i" iterable variable represents the same index as positon 0

        for i in range(0, len(intcodes)-1, 4):
    
            # Get the value at the position 0 + 1 index
            num1_index = intcodes[i+1]

            # Get the value at the position 0 + 2 index
            num2_index = intcodes[i+2]

            # Get the index to update based on the value at the position 0 + 3 index
            update_index = intcodes[i+3]
    
            # Add if value at position 0 index == 1
            if intcodes[i] == 1:
                sum = intcodes[num1_index] + intcodes[num2_index]
                intcodes[update_index] = sum
    
            # Multiply if value at position 0 index == 2
            elif intcodes[i] == 2:
                product = intcodes[num1_index] * intcodes[num2_index]  
                intcodes[update_index] = product
    
            # Print terminated message if value at positon 0 index == 99 
            elif intcodes[i] == 99:
                print("Program terminated.")
                break
    
            # In all other cases, print error message
            else: 
                print("Something went wrong. Invalid code.")
                
        # Return the updated list of intcodes 
        return intcodes

    # Handle IndexErrors    
    except IndexError:
        return intcodes


# Call the test cases
print(update_intcodes(prompt_code))
print(update_intcodes(short_code1))
print(update_intcodes(short_code2))
print(update_intcodes(short_code3))
print(update_intcodes(short_code4))
print(update_intcodes(gravity_assist))