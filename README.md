# 🧠 HeadTail Symbolic Encoder & Visualizer

This Python module encodes text messages into symbolic binary streams using custom "Heads" and "Tails" blocks, then visualizes the binary stream as an RGB image. It also supports full decoding back to the original message.

---

## 📦 Features

- 🔢 **Conditional Binary Encoding**: ASCII characters below 69 are padded with `'0'`, others are encoded raw.
- 🪙 **Symbolic Encoding**: Binary digits are replaced with symbolic blocks derived from `"Heads"` and `"Tails"`.
- 🔍 **Full Decoding Pipeline**: Symbolic blocks → binary → original text.
- 🖼️ **Binary Visualization**: Converts binary stream into RGB pixels and displays as an image.
- 🧪 **Byte Alignment Check**: Ensures binary stream is properly aligned before decoding.

<img src="Screenshot 2025-10-19 215702.png" />

---

## 🧬 Encoding Logic

### `HeadTailEncod(message)`
Converts a string into a binary stream. Characters with ASCII `< 69` are padded with `'0'`.

### `Encodemessage(binary)`
Encodes binary stream using symbolic blocks:
- `'1'` → `"Heads"` block
- `'0'` → `"Tails"` block

### `Decodemessage(symbolic)`
Decodes symbolic blocks back to binary, then reconstructs the original message.

### `decode_conditional_binary(binary_stream)`
Decodes raw binary stream (from `HeadTailEncod`) directly into text.

---

## 🎨 Visualizing the Binary Stream

### `drawmessage(binary_stream)`
- Groups every 3 bytes into RGB pixels.
- Pads incomplete pixels and reshapes into a square image.
- Displays the image using `matplotlib`.

---

## 🚀 Example Usage

```python
if __name__ == "__main__":
    testmessage = "can you fix this draw image function def HeadTailEncod(message): '''" \
    " Heads = 0100 1000 0100 0101 0100 0001 0100 0100 0101 0011 Tails  0101 0100 0100 0001 " \
    "0100 1001 0100 1100 0101 0011 ''' Heads   ''.join((bin(ord(i))) for i in \"Heads\")"\
    ".replace('b','') Tails =  ''.join((bin(ord(i))) for i in \"Tails\").replace('b','')"

    binary = HeadTailEncod(testmessage)
    encoded = Encodemessage(binary)
    decoded = Decodemessage(encoded)
    drawmessage(binary)

