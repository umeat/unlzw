# unlzw
Python decompression module for .Z files compressed using Unix compress utility

This is a purely Python adaptation of Mark Adler's 'unlzw' C function. Which can be found [here](http://mathematica.stackexchange.com/questions/60531/how-can-i-read-compressed-z-file-automatically-by-mathematica/60879#60879) on Stackoverflow. If you don't have any specific requirement to execute this as Python code, then I recommend using [subprocess](https://docs.python.org/2/library/subprocess.html) to call uncompress, gzip, or something similar to decompress your file. Python will be much slower than using any compiled utility for the same purpose. Note: there are currently no Python modules which provide this functionality (the gzip system utility does - but the gzip Python module does not).

I adapted this function so that it could be used in AWS Lambda scripts to avoid convoluted [virtualenv](http://www.perrygeo.com/running-python-with-compiled-code-on-aws-lambda.html) setups. Though it could probably also be done by wrapping the C code using something like Cython. Currently my application use case is not incredibly time critical, and I expect submission of .Z files will slowly decrease. Though out of personal interest, I would like to minimaize the execution time.

### Usage

This function takes compressed data as any type which can be converted to a bytearray (generally a string), and returns a UTF-8 decoded string containing the decompressed data.

```
f = open('file.Z', 'r')
compressed_data = f.read()
uncompressed_data = unlzw(compressed_data)
```
