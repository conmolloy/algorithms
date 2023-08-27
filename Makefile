

testy:
	poetry run python -m test.test_linear_search


test-search:
	poetry run python -m unittest discover -s test -p "test*.py"