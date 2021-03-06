from subprocess import run


def test_connect(capfd, datadir):
    user = 'user'
    password = 'password'
    hostname = 'hostname'

    run(
        f'python {datadir/"global_args.py"} --as {user} -p {password} connect {hostname}',
        shell=True
    )

    output = capfd.readouterr().out.strip()

    assert output == f'Connecting to {hostname}, user="{user}", password="{password}"'

def test_upload(capfd, datadir):
    user = 'user'
    password = 'password'
    filename = 'filename'

    run(
        f'python {datadir/"global_args.py"} --as {user} -p {password} utils upload {filename}',
        shell=True
    )

    output = capfd.readouterr().out.strip()

    assert output == f'Uploading {filename}, user="{user}", password="{password}"'
