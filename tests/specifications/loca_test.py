# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals, division

import io
import os

from fontTools.ttLib import TTFont
from fontbakery.checkrunner import PASS, FAIL


def test_check_180():
  """Does the number of glyphs in the loca table match the maxp table?"""
  from fontbakery.specifications.loca import com_google_fonts_check_180 as check

  test_font_path = os.path.join("data", "test", "nunito", "Nunito-Regular.ttf")

  test_font = TTFont(test_font_path)
  status, _ = list(check(test_font))[-1]
  assert status == PASS

  test_font = TTFont(test_font_path)
  test_font["loca"].locations.pop()
  test_file = io.BytesIO()
  test_font.save(test_file)
  test_font = TTFont(test_file)
  status, _ = list(check(test_font))[-1]
  assert status == FAIL
