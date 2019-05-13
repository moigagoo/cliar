from subprocess import run


def test_help(capfd, datadir):
    run(f'python {datadir/"case_sensitive_args.py"} -h', shell=True)

    output = capfd.readouterr().out

    assert '-u UNIQUE, --unique UNIQUE' in output
    assert '--url URL' in output
    assert '-U USERNAME, --username USERNAME' in output
