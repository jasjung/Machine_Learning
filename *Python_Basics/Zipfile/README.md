# Zipfile

It is unnecessary to upload raw csv files to github. Thus, let's compress them and find out how to read it. 

```
import zipfile 

zip_file = zipfile.ZipFile('data.csv.zip', 'r')
df = pd.read_csv(zip_file.open('data.csv'))
```

