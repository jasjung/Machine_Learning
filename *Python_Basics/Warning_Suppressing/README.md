# Supress Warning

```py
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

warnings.simplefilter('always', category=UserWarning)
```

## sklearn 

https://stackoverflow.com/questions/54197853/how-to-ignore-settingwithcopywarning-using-warnings-simplefilter

```py
import warnings
from pandas.core.common import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
```