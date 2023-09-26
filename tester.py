def test_first():
    try:
        exec(open("haff_cod.py").read())
    except(not Exception):
        print("тест прошёд")
        pass
