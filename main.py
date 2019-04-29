
from PIL import Image
from PIL import ImageSequence


original = Image.open("originals/image1.jpg")
print(original.format, original.size, original.mode)
resized = original.resize((150, 150))
resized.save("resized/resize1.jpg")


original = Image.open("originals/image3.gif")
print(original.format, original.size, original.mode)
frames = [frame.copy().resize((150, 150)) for frame in ImageSequence.Iterator(original)]
x = frames.pop(0)
x.save("resized/resize3.gif", save_all=True, append_images=frames)


original = Image.open("originals/image4.png")
# red, green, blue, alpha = original.split()
print(original.format, original.size, original.mode)
resized = original.resize((150, 150))
# resized.putalpha(alpha)
resized.save("resized/resize4.png")

original = Image.open("originals/image5.png")
# red, green, blue, alpha = original.split()
print(original.format, original.size, original.mode)
resized = original.resize((150, 150))
# resized.putalpha(alpha)
resized.save("resized/resize5.png")
