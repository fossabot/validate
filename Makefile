# Controls
.PHONY : commands install clean test

install:
	pip install -r requirements.txt
	pip install -e .

test:
	pytest --cov=validate
	codecov

clean :
	@rm -rf bin/__pycache__
	@find . -name .DS_Store -exec rm {} \;
	@find . -name '*~' -exec rm {} \;
	@find . -name '*.pyc' -exec rm {} \;
