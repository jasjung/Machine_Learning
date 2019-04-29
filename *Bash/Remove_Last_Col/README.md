# Remove Last Column	

Say you have a csv or txt file as an output from a process. But I now want to remove one of the columns, say the last one. I could rerun the process but what if the process is computationally expensive? Thus, I want to find a solution in bash. 

## Keep First n Columns for CSV

- https://stackoverflow.com/questions/14418511/bash-method-to-remove-last-4-columns-from-csv-file


where n = 4 

```bash
cut -d',' -f -4 tmp.csv > out.csv
```
