from nose.tools import *
from ex48.parser import *

def test_peek():
    assert_equal(peek([('verb','run'),('stop','to'),('direction','south')]),word_list[0][0])

def test_match():
    assert_equal(match([('verb','run'),('stop','to'),('direction','south')],'verb'),('verb','run'))

def test_parse_verb():
    assert_equal(parse_verb([('verb','run'),('stop','to'),('direction','south')]),('verb','run'))

def test_parse_object():
    assert_equal(parse_obj([('verb','run'),('stop','to'),('direction','south')]),('direction','south'))

def test_parse_subject():
    assert_equal(parse_subject([('verb','run'),
                                ('stop','to'),
                                ('direction','south')]),
                                ('noun','player'))
