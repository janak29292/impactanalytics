# Assignment


## Installation



```bash
git clone https://github.com/janak29292/impactanalytics.git
cd impactanalytics
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

For running the program with provided input
```bash
python rectangle.py
# This would output list for Input  - [(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
```

To get output list for custom input use following

```bash
ipython
```
In python console
```python
from rectangle import get_vertices
get_vertices([(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)])
```
## For Visual Testing

Visual Testing with random input
```bash
python visual_test.py
```

Visual Testing with custom input in python console
```python
from visual_test import test
test([(1, 5, 10), (4, 6, 8), (10, 15, 10), (11, 12, 8)])
```
