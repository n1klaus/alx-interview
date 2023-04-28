# Validate utf-8

# Problem
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: `def validUTF8(data)`
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

# Solution
- Iterate the items and in the input data list and for each item perform an evaluation
    - Use the code point of the data to get its number of bits hence getting the number of bytes encoded
    - Use unicode code points to get the binary of the data if the data is not already a unicode code point
    - using the number of bytes check in the binary the most significant bits in each byte if it matches a 
      valid UTF8 binary format and return False if either of the data in the input list does not meet the requiremnets i.e
        - range(0x0000, 0x007F) => ( 0 - 7 bits ) 1 byte => ([0xxxxxxx])
        - range(0x0080, 0x07FF) => ( 8 - 11 bits ) 2 bytes =>  ([110xxxxx 10xxxxxx])
        - range(0x0800, 0xFFFF) => ( 12 - 16 bits ) 3 bytes =>  ([1110xxxx 10xxxxxx 10xxxxxx])
        - range(0x10000, 0x10FFFF) => ( 17 - 21 bits ) 4 bytes => ([11110xxx 10xxxxxx 10xxxxxx 10xxxxxx])
- otherwise return true as all checks passed successfully
