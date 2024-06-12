def split_64bit_to_8bit_chunks(n):
    chunks = [(n >> (8 * i)) & 0xFF for i in range(8)]
    chunks.reverse() 
    return chunks

def circular_left_shift_8bit(value, shift_amount):
    shift_amount %= 8
    shifted_left = (value << shift_amount) & 0xFF
    shifted_right = value >> (8 - shift_amount)
    return (shifted_left | shifted_right) & 0xFF

def process_chunks(bits):
    chunks = split_64bit_to_8bit_chunks(bits)
    processed_chunks = []
    for k in range(8):
        prev_k = 7 if k == 0 else k - 1
        xor_value = circular_left_shift_8bit(chunks[prev_k], k + 1)
        processed_chunks.append(chunks[k] ^ xor_value)
    
    concatenated_hex = ''.join(f'{part:02x}' for part in processed_chunks)
    
    single_number = int(concatenated_hex, 16)
    
    return single_number

