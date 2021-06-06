import pytest



def test_one():
	assert True

def test_two():
	assert False

@pytest.mark.skip("Not relevant")
def test_three():
	assert True