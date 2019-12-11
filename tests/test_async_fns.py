from subprocess import run


def test_help(capfd, datadir):
    run(f'python {datadir/"async_fns.py"} wait -h', shell=True)

    output = capfd.readouterr().out

    assert '-s SECONDS-TO-WAIT, --seconds-to-wait SECONDS-TO-WAIT' in output

def test_wait(capfd, datadir):
    seconds_to_wait = 1.0

    run(
        f'python {datadir/"async_fns.py"} wait -s "{seconds_to_wait}"',
        shell=True
    )

    seconds_awaited = float(capfd.readouterr().out.strip())
    assert round(seconds_awaited, 1) == round(seconds_to_wait, 1)
