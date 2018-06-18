# Big File 

If you cannot read your entire data into your work environment. 

[Reference](https://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python)

```
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


f = open('really_big_file.dat')
for piece in read_in_chunks(f):
    process_data(piece)
```

If the file is line-based, the file object is already a lazy generator of lines:

```
for line in open('really_big_file.dat'):
    process_data(line)
```

## Loading Chunks 
[Reference](https://stackoverflow.com/questions/5832856/how-to-read-file-n-lines-at-a-time-in-python)

```
from itertools import islice
with open(filename, 'r') as infile:
    lines_gen = islice(infile, N)
```
