from url_util import URL


def test_url():

    url = URL('https://github.com/pallets/click')

    assert url.first_path_part == 'pallets'
    assert url.second_path_part == 'click'
