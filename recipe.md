# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def track_task():
    #Parameters:
        #text
    #Return:
        #list
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given an empty string
It will return an empty list
"""
track_task("") => []

"""
Given an text with no `#TODO`
It will return an empty list
"""
track_task("go to the shops") => []

"""
Given an text containing `#TODO`
It will return a list containing tasks
"""
track_task("#TODO go fishing") => ['go fishing']

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
