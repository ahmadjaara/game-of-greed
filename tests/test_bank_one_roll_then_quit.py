from tests.flow.flo import Flo


def test_one_and_done():
    Flo.test("tests/flow/bank_one_roll_then_quit.sim.txt")
