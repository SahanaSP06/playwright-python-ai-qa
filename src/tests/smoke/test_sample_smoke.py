def test_basic_page_load(page):
    page.goto("https://example.com")
    assert page.title() != ""
