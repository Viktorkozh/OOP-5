#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from main import is_hidden, list_files


def test_is_hidden():
    appdata_path = os.path.join(os.environ["USERPROFILE"], "AppData")
    assert is_hidden(appdata_path)


def test_list_files(capsys):
    user_home = os.environ["USERPROFILE"]

    list_files(user_home, depth=1, show_hidden=False)
    captured = capsys.readouterr()

    assert "Music/" in captured.out
    assert "Downloads/" in captured.out
    assert "Pictures/" in captured.out

    list_files(user_home, depth=1, show_hidden=True)
    captured = capsys.readouterr()

    assert "AppData/" in captured.out
