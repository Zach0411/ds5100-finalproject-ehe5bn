# **Montecarlo Simulation- ds5100-finalproject-ehe5bn**

Montecarlo is a Python Module for simulating dice being rolled along with being able to see descriptive statistics. Montecarlo contains three classes, *Die* (to create the Die objects), *Game* (to roll Die objects), and *Analyzer* (to view statistics of each game).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo.

```bash
pip install montecarlo
```
Import the three classes
```bash
from montecarlo.montecarlo import Die, Game, Analyzer
```
<u>Required packages</u>:
*pandas
*numpy

## Usage

```python
import montecarlo

# create a 'die' object using numpy arrays
Die1.Die(array1, array2)

# specify weights of each 'face/side'
Die1.change_weight(face, new_weight)

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
