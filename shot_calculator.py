def main():
    die_count = 1
    die_size = 6
    ballistic_skill = 3
    ballistic_modifier = calc_ballistic_modifier(ballistic_skill)
    die_count = ballistic_modifier * die_count
    avg = calc_die_roll_avg(die_count, die_size)


def calc_ballistic_modifier(ballistic_skill: int) -> float:
    return 1 - ((ballistic_skill - 1)/6)
# test calc_ballistic_modifier 
    

    

def calc_die_roll_avg(die_count, die_size, min_roll=1): 
    """Returns number of shots given input at # of sides of di(c)e
    n*(m+1)/2
    """
    die_count = float(die_count)
    die_size = float(die_size)
    if die_size == 0:
        return die_count
    return die_count*((die_size + min_roll)/2)




# D6 2D6 3D6 4D6 D3 2D3 D3+3 D6+3 D6MIN3

def test_roll_count_int():
    assert calc_die_roll_avg(3,6.0) == 10.5

def test_die_size_int():
    assert calc_die_roll_avg(3.0,6) == 10.5

def test_roll_count_die_size_int():
    assert calc_die_roll_avg(3,6) == 10.5

def test_1D0():
    assert calc_die_roll_avg(1.0,0.0) == 1 

def test_0D0():
    assert calc_die_roll_avg(0.0,0.0) == 0

def test_100D20():
    assert calc_die_roll_avg(100.0,20.0) == 1050 

def test_min_roll3():
    assert calc_die_roll_avg(die_count=3, die_size=6, min_roll=3) == 13.5

def test_half_roll():
    assert calc_die_roll_avg(die_count=0.666, die_size=6, min_roll=1) == 2.331
 
