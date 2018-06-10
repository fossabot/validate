import pytest
import validate.chapter as ch

def test_get():
    assert ch.get('https://www.datacamp.com/api/courses/672')['id'] == 672
    with pytest.raises(Exception):
        assert ch.get('https://nonsense')
