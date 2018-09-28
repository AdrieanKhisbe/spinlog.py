from spinlog.core import handle_multiline


def test_handle_multiline_with_empty_or_none():
    assert handle_multiline("") == ""
    assert handle_multiline(None) == None

def test_handle_multiline_with_single_line():
    tests = ["ABC", "Text with space", "Another one bites the dust"]
    for sample_text in tests:
        assert handle_multiline(sample_text) == sample_text


def test_handle_multiline_with_multiline_line():
    assert (handle_multiline("Text with newline\nbecause I have lot to tell") ==
            "Text with newline\n  because I have lot to tell")
    assert (handle_multiline("A\nB\nC") ==
            "A\n  B\n  C")
