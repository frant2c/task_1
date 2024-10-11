import pytest


@pytest.mark.parametrize(
    "test_value", [10**7, 15 * 10**6, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 15 * 10**8]
)
def test_popularity_of_programming_languages(
    test_value, get_popular_programming_languages_table
):
    for entry in get_popular_programming_languages_table.entries:
        assert entry.popularity >= test_value, (
            f"{entry.websites} (Frontend: {entry.frontend}|Backend:"
            f"{entry.backend}) has {entry.popularity} unique visitors "
            f"per month. (Expected more than {test_value})"
        )
