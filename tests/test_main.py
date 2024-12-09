#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pytest
from main import is_hidden, list_files


def test_is_hidden():
    assert is_hidden(".hidden_file") is True
    assert is_hidden("visible_file") is False
    with pytest.raises(AttributeError):
        is_hidden("some_file")


# Test for list_files function
def test_list_files(capsys):
    # Create a temporary directory structure for testing
    os.makedirs("test_dir/dir1", exist_ok=True)
    with open("test_dir/file1.txt", "w") as f:
        f.write("This is a test file.")
    with open("test_dir/dir1/file2.txt", "w") as f:
        f.write("This is another test file.")
    with open("test_dir/.hidden_file", "w") as f:
        f.write("This is a hidden file.")

    # Test without showing hidden files
    list_files("test_dir", depth=2, show_hidden=False)

    # Capture the output
    captured = capsys.readouterr()

    # Check the printed output
    assert "test_dir" in captured.out
    assert "└── dir1/" in captured.out
    assert "    └── file1.txt" in captured.out
    assert ".hidden_file" not in captured.out  # Ensure hidden file is not shown

    # Test with showing hidden files
    list_files("test_dir", depth=2, show_hidden=True)

    # Capture the output again
    captured = capsys.readouterr()

    # Check the printed output
    assert "test_dir" in captured.out
    assert "└── dir1/" in captured.out
    assert "    └── file1.txt" in captured.out
    assert "    └── .hidden_file" in captured.out  # Ensure hidden file is shown

    # Clean up the temporary directory
    import shutil

    shutil.rmtree("test_dir")
