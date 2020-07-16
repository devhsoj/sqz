# sqz

sqz is a unique python3 based png compression algorithm for compressing plain text

#### Setup
```sh
pip3 install Pillow
```

#### Example

```python
from sqz import sqz,ring

data_to_compress = 'Random Data' * 10000
img = sqz(data_to_compress,filename='output.png',verbose=True)
decompressed_data = ring('output.png',verbose=True)

print(f'Lossless Compression?: {data_to_compress == decompressed_data}')
```

**NOTE** sqz only works for plain text data!
