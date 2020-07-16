from sys import getsizeof
from PIL import Image
from time import time


def sqz(data,filename='data.png',verbose=False):
    start = time()
    size_before = sys.getsizeof(data)

    if verbose:
        print(f'[sqz] Size of data before compression: {round(size_before / 1000000,3)} mb')
    
    data = [data[i:i + 4] for i in range(0,len(data),4)]

    if verbose:
        print('[sqz] Chunked data into a 2-dimensional array')

    img = Image.new(mode='RGBA',size=(len(data),1))
    pixels = img.load()

    if verbose:
        print('[sqz] Generated new RGBA-PNG image')

    pos = 0
    for chunk in data:
        if len(chunk) < 4:
            chunk += '«' * (4 - len(chunk))
        
        pixels[pos,0] = (ord(chunk[0]),ord(chunk[1]),ord(chunk[2]),ord(chunk[3]))
        pos += 1

    if verbose:
        print('[sqz] Converted data to 4 byte pixels')

    img.save(filename)
    end = time()

    if verbose:
        print(f'[sqz] Finished in {round(end-start,2)} seconds')

        f = open(filename,'rb')
        size_after = sys.getsizeof(f.read())
        f.close()

        print(f'[sqz] Size of data after compression: {round(size_after / 1000000,3)} mb | Ratio {round(size_after/size_before*100,3)}%\n')    

    return img


def ring(filename,verbose=False):
    start = time()
    img = Image.open(filename)

    if verbose:
        print('[sqz] Loaded RGBA-PNG file')

    pixels = img.load()
    data = ''

    if verbose:
        print('[sqz] Loaded pixel data')

    for x in range(img.size[0]):
        pxl = pixels[x,0]
        data += ''.join([chr(i) for i in pxl])

    if verbose:
        print('[sqz] Converted pixel data to plain/text')
    
    end = time()

    if verbose:
        print(f'[sqz] Finished in {round(end-start,2)} seconds')
    
    return data.replace('«','')
