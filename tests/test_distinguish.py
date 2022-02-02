from wordlemize import color

def test_word_distinghuishes_others_from_self():
    assert color.pair('those', 'those', 'prose')
    assert color.pair('prose', 'those', 'prose')
    assert color.pair('bills', 'bills', 'kills')
    assert color.pair('kills', 'bills', 'kills')

def test_distinguish_pair_not_commutative():
    assert color.pair('prose', 'those', 'chose') == False
    assert color.pair('prose', 'those', 'chose') == True