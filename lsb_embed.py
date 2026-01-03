from PIL import Image

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def embed_lsb(image_path, output_path, message):
    img = Image.open(image_path)
    pixels = img.load()

    binary = text_to_bits(message) + '1111111111111110'
    idx = 0

    for y in range(img.height):
        for x in range(img.width):
            if idx < len(binary):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary[idx])
                pixels[x, y] = (r, g, b)
                idx += 1

    img.save(output_path)

embed_lsb("examples/original.png", "examples/stego.png", "CTF{LSB_HIDDEN}")
