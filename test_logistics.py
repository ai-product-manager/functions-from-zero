from mylib.logistics import distance_between_two_points


def test_distance_between_two_points():
    assert distance_between_two_points("Lima", "Arequipa") == 765.3868858019406
