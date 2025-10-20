import matplotlib.pyplot as plt
import numpy as np

def HeadTailEncod(message):
    '''
    Convert message into binary string with conditional padding.
    Characters with ASCII < 69 are padded with '0', others are raw.
    '''
    st = ""
    for i in message:
        if ord(i) < 69:
            st += bin(ord(i)).replace('b', '0')
        else:
            st += bin(ord(i)).replace('b', '')
    return st

def Encodemessage(st):
    '''
    Encode binary string using symbolic Heads and Tails blocks.
    Each '1' becomes Heads, each '0' becomes Tails.
    '''
    Heads = ''.join(bin(ord(i)).replace('0b', '') for i in "Heads")
    Tails = ''.join(bin(ord(i)).replace('0b', '') for i in "Tails")
    message = ""
    for i in st:
        message += Heads if i == "1" else Tails
    return message

def Decodemessage(message):
    '''
    Decode symbolic Heads/Tails blocks back into binary string,
    then decode binary string into original text.
    '''
    Heads = ''.join(bin(ord(i)).replace('0b', '') for i in "Heads")
    block_size = len(Heads)

    # Step 1: Decode symbolic blocks
    binary = ""
    j = 1
    while len(message) >= block_size * j:
        block = message[(j - 1) * block_size : j * block_size]
        binary += "1" if block == Heads else "0"
        j += 1

    # Step 2: Ensure byte alignment
    if len(binary) % 8 != 0:
        print(f"⚠️ Warning: Binary stream not byte-aligned ({len(binary)} bits). Truncating excess.")
        binary = binary[:len(binary) - (len(binary) % 8)]

    # Step 3: Decode binary to text
    origin = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        origin += chr(int(byte, 2))
    print("✅ Original Message:", origin)
    return origin

def decode_conditional_binary(binary_stream):
    '''
    Decode raw binary stream (from HeadTailEncod) back to text.
    '''
    message = ""
    for i in range(0, len(binary_stream), 8):
        byte = binary_stream[i:i+8]
        if len(byte) < 8:
            continue
        try:
            message += chr(int(byte, 2))
        except ValueError:
            message += "�"
    print("✅ Decoded from binary stream:", message)
    return message

def drawmessage(binary_stream):
    '''
    Visualize binary stream as RGB image.
    Each 3 bytes form one pixel.
    '''
    RGB = []
    Img = []
    for j in range(0, len(binary_stream), 8):
        byte = binary_stream[j:j+8]
        if len(byte) < 8:
            break
        RGB.append(int(byte, 2))
        if len(RGB) == 3:
            Img.append(RGB)
            RGB = []

    # Pad incomplete pixel
    if RGB:
        while len(RGB) < 3:
            RGB.append(0)
        Img.append(RGB)

    # Pad image to square
    total_pixels = len(Img)
    side = int(np.ceil(np.sqrt(total_pixels)))
    while len(Img) < side * side:
        Img.append([0, 0, 0])

    Img_Nump = np.array(Img, dtype=np.uint8).reshape((side, side, 3))
    plt.imshow(Img_Nump)
    plt.axis('off')
    plt.title("Encoded Message Visualization")
    plt.show()



# Example usage
if __name__ == "__main__":
    testmessage = "can you fix this draw image function def HeadTailEncod(message): '''" \
" Heads = 0100 1000 0100 0101 0100 0001 0100 0100 0101 0011 Tails  0101 0100 0100 0001 " \
"0100 1001 0100 1100 0101 0011 ''' Heads   ''.join((bin(ord(i))) for i in "'Heads'")"\
".replace('b','') Tails =  ''.join((bin(ord(i))) for i in "'Tails'").replace('b','')"
    binary = HeadTailEncod(testmessage)
    encoded = Encodemessage(binary)
    decoded = Decodemessage(encoded)
    drawmessage(binary)