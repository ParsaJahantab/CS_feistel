import random
from sub_key import process_chunks
from round_function import round_function


IP = [115, 42, 107, 82, 51, 33, 78, 38, 124, 91, 67, 37, 73, 77, 112, 4, 48, 69, 100, 116, 75, 95, 71, 62, 30, 120, 83, 44, 
      2, 18, 65, 21, 20, 101, 46, 9, 114, 72, 118, 121, 34, 45, 7, 16, 1, 110, 41, 19, 31, 126, 59, 109, 24, 
      10, 64, 50, 99, 103, 35, 106, 3, 90, 6, 127, 104, 36, 12, 63, 85, 55, 70, 57, 27, 89, 5, 68, 88, 117, 
      98, 76, 14, 60, 40, 97, 74, 29, 87, 92, 25, 17, 84, 122, 94, 52, 53, 11, 15, 111, 32, 54, 86, 93, 22, 
      119, 47, 108, 102, 56, 0, 81, 79, 23, 39, 43, 8, 105, 49, 66, 61, 113, 125, 13, 80, 58, 123, 96, 28, 26]
FP = [108, 44, 28, 60, 15, 74, 62, 42, 114, 35, 53, 95, 66, 121, 80, 96, 43, 89, 29, 47, 32, 31, 102, 111, 52, 
      88, 127, 72, 126, 85, 24, 48, 98, 5, 40, 58, 65, 11, 7, 112, 82, 46, 1, 113, 27, 41, 34, 104, 16, 116, 55,
      4, 93, 94, 99, 69, 107, 71, 123, 50, 81, 118, 23, 67, 54, 30, 117, 10, 75, 17, 70, 22, 37, 12, 84, 20, 79,
      13, 6, 110, 122, 109, 3, 26, 90, 68, 100, 86, 76, 73, 61, 9, 87, 101, 92, 21, 125, 83, 78, 56, 18, 33, 106,
      57, 64, 115, 59, 2, 105, 51, 45, 97, 14, 119, 36, 0, 19, 77, 38, 103, 25, 39, 91, 124, 8, 120, 49, 63]


def apply_permutation(block, table):
    return ''.join(block[i] for i in table)


def hex_to_halves(hex_number):
    
    lower=hex_number & 0x0000000000000000FFFFFFFFFFFFFFFF
    upper = (hex_number >> 64) & 0x0000000000000000FFFFFFFFFFFFFFFF
    
    return lower,upper



def feistel(input,key):
    input = int(apply_permutation(f'{input:0128b}', IP),2)
    left,right = hex_to_halves(input)


    prev_left = left
    for i in range(16):
        sub_key=process_chunks(key)
        left = right
        right = round_function(right_chunk=right,left_chunk=prev_left,key=sub_key)
        prev_left=left
        
    output = (right << 64)+ left

    output = int(apply_permutation(f'{output:0128b}', FP),2)
    return output

input = 0x0a900027ab5427a76cdcb3afa3895fd0
key = 0x9994757689a35355
output = feistel(input=input,key=key)

print(hex(output))
