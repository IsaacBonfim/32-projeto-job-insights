from src.counter import count_ocurrences


def test_counter():
    result = count_ocurrences('src/jobs.csv', 'PYTHON')
    result_lower = count_ocurrences('src/jobs.csv', 'python')
    assert result == 1639
    assert result_lower == 1639
