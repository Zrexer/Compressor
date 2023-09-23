import lzma

fileName = str(input('Enter the file name: '))
outputFileName = str(input('Enter the output file name: '))

with open(fileName, 'rb') as f_in, lzma.open(outputFileName, 'wb') as f_out:
    f_out.write(f_in.read())

