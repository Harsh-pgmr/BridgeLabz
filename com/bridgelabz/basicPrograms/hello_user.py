"""
 ******************************************************************************
 *  Purpose: Prints the Hello world message
 *
 *  @author  Harhad B
 *  @version 3.8
 *  @since   17/12/2020
 ******************************************************************************
"""
name = input("Enter User Name")  # Takes users input
if len(name) > 3:  # Checks for input length
    print("Hello", name, "How are you")
else:
    print("User name should be minimum three characters")