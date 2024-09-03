from PIL import Image

flag = 'technovate{shades_of_fun_2024}'

colors = list() 
pixels = list()

img = Image.new('RGB', (len(flag)//3, 1))

for i in range(0, len(flag), 3):
    color = (ord(flag[i]), ord(flag[i+1]), ord(flag[i+2]))
    print(color)
    colors.append(color)

img.putdata(colors)
img.save('test.png')
