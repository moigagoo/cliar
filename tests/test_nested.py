from subprocess import run


def test_helps(capfd, datadir):
    run(f'python {datadir/"nested.py"} -h', shell=True)
    assert 'Git help.' in capfd.readouterr().out

    run(f'python {datadir/"nested.py"} remote -h', shell=True)
    assert 'Remote help.' in capfd.readouterr().out

    run(f'python {datadir/"nested.py"} remote add -h', shell=True)
    assert 'Remote add help.' in capfd.readouterr().out

    run(f'python {datadir/"nested.py"} flow -h', shell=True)
    assert 'Flow help.' in capfd.readouterr().out

    run(f'python {datadir/"nested.py"} flow feature start -h', shell=True)
    assert 'Feature start help.' in capfd.readouterr().out

def test_git(capfd, datadir):
    run(f'python {datadir/"nested.py"}', shell=True)
    assert capfd.readouterr().out.strip() == 'Git root.'

def test_remote(capfd, datadir):
    run(f'python {datadir/"nested.py"} remote', shell=True)
    assert capfd.readouterr().out.strip() == 'Remote root.'

    remote_name = 'foo'
    run(f'python {datadir/"nested.py"} remote add {remote_name}', shell=True)
    assert capfd.readouterr().out.strip() == f'Adding remote {remote_name}'

    run(f'python {datadir/"nested.py"} remote show', shell=True)
    assert capfd.readouterr().out.strip() == 'Showing all remotes'

def test_flow(capfd, datadir):
    feature_name = 'bar'
    run(f'python {datadir/"nested.py"} flow feature start {feature_name}', shell=True)
    assert capfd.readouterr().out.strip() == f'Starting feature {feature_name}'
