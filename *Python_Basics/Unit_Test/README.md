# Unit Test 

- https://docs.python.org/3/library/unittest.html
- `pytest` - alternative to unittest 
- `unittest.main()` to run the tests 


## IPYNB 

When running in jupyter notebook, you have the run the test like the following. This is because they were noramlly designed to be called from a command line. 

```py 
unittest.main(argv=['first-arg-is-ignored'], exit=False)
```


## Simple format 

```py 
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    # testing your function
    def test_small_list(self):
        actual = your_function([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
``` 


## Corey Schafer

- tutorial: https://www.youtube.com/watch?v=6tNS--WetLI
- make sure tests are isolated 
- https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing


### Calling 

```sh
python test_calc.py # need unittest.main()
python -m unittest test_calc.py # need does not need unittest.main()
```

### setUp and tearDown 


The following code runs in the beginning and the end of the test module 

```py
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

```


The following code runs in the beginning and the end of each test case. 

```py
    def setUd(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')
```


