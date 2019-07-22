from subprocess import run


def test_connect(capfd, datadir):
    user = 'user'
    password = 'password'
    hostname = 'hostname'

    run(
        f'python {datadir/"global_args.py"} --as {user} -p {password} connect {hostname}',
        shell=True
    )
    capfd.readouterr().out == f'Connecting to {hostname}, user="{user}", password="{password}"'
