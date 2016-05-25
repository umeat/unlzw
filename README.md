# unlzw
Python decompression module for .Z files compressed using Unix compress utility

This is a purely Python adaptation of Mark Adler's 'unlzw' C function. Which can be found [here](http://mathematica.stackexchange.com/questions/60531/how-can-i-read-compressed-z-file-automatically-by-mathematica/60879#60879) on Stackoverflow. 

### Usage

This funciton takes compressed data as any type which can be converted to a bytearray - string is generally the easiest - and returns a UTF-8 decoded string containing decompressed data.

```
f = open('file.Z', 'r')
compressed_data = f.read()
decompressed_data = unlzw(compressed_data)
```
