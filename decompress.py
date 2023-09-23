import lzma

fileName = str(input('Enter File Name with (xz) format: '))
outputFileName = str(input('Enter Out Put file name: '))

with lzma.open(filename=fileName, mode='rb') as f_in, open(outputFileName, 'rb') as f_out:
    f_out.write(f_in.read())

