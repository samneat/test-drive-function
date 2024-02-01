from lib.track_task import *

def test_with_empty_input():
    result = track_task("")
    assert result == []

def test_with_text_but_no_TODO():
    result = track_task("go to the shops")
    assert result == []

def test_string_containing_TODO():
    result = track_task("#TODO go fishing")
    assert result == ["go fishing"]

def test_string_containing_TODO_without_hashtag():
    result = track_task("TODO wash the dishes")
    assert result == []

def test_string_containing_lowercase_to_do():
    result = track_task("#todo clean the car")
    assert result == []

def test_multiple_tasks():
    track_task("#TODO wash the dishes")
    result = track_task("#TODO clean the car")
    assert result == ["clean the car"]