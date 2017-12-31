import sys
from PIL import Image

images = map(Image.open, ['IMG_1325.jpg', 'n_l.jpg', 'generated_image-2.jpg'])
widths, heights = zip(*(i.size for i in images))
#print(images.size)
print(widths)
total_width = sum(widths)
max_height = max(heights)
new_im = Image.new('RGB', (total_width, max_height))
#print(images.size)
x_offset = 0
images = map(Image.open, ['IMG_1325.jpg', 'n_l.jpg', 'generated_image-2.jpg'])
for im in images:
  print("H3")
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test2.jpg')
