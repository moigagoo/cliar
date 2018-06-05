from subprocess import run


def test_help(capfd, datadir):
    run(f'python {datadir/"noroot.py"}', shell=True)
    assert 'Basic math operations.' in capfd.readouterr().out
