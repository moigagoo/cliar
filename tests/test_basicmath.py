from subprocess import run
from math import factorial, log


def test_positional_args(capfd, datadir):
    x, y = 12, 34

    run(f'python {datadir/"basicmath.py"} add {x} {y}', shell=True)
    assert int(capfd.readouterr().out) == x + y


def test_optional_args(capfd, datadir):
    x, power = 12, 3

    run(f'python {datadir/"basicmath.py"} power {x} --power {power}', shell=True)
    assert int(capfd.readouterr().out) == x ** power

    run(f'python {datadir/"basicmath.py"} power {x} -p {power}', shell=True)
    assert int(capfd.readouterr().out) == x ** power

    run(f'python {datadir/"basicmath.py"} power {x}', shell=True)
    assert int(capfd.readouterr().out) == x ** 2


def test_no_args(capfd, datadir):
    from math import pi

    run(f'python {datadir/"basicmath.py"} pi', shell=True)
    assert float(capfd.readouterr().out) == pi

    run(f'python {datadir/"basicmath.py"} avg', shell=True)
    assert float(capfd.readouterr().out) == sum((1, 2, 3))/3


def test_root_command(capfd, datadir):
    version = '0.1.0'

    run(f'python {datadir/"basicmath.py"}', shell=True)
    assert capfd.readouterr().out.strip() == 'Welcome to math!'

    run(f'python {datadir/"basicmath.py"} --version', shell=True)
    assert capfd.readouterr().out.strip() == version

    run(f'python {datadir/"basicmath.py"} -v', shell=True)
    assert capfd.readouterr().out.strip() == version


def test_nargs(capfd, datadir):
    numbers = 1, 2, 42, 101

    run(
        f'python {datadir/"basicmath.py"} summ {" ".join(str(number) for number in numbers)}',
        shell=True
    )
    assert int(capfd.readouterr().out) == sum(numbers)

    numbers = 1, 2, 42.2, 101.1

    run(
        f'python {datadir/"basicmath.py"} avg --numbers {" ".join(str(number) for number in numbers)}',
        shell=True
    )
    assert float(capfd.readouterr().out) == sum(numbers)/len(numbers)

    run(f'python {datadir/"basicmath.py"} avg -n {" ".join(str(number) for number in numbers)}', shell=True)
    assert float(capfd.readouterr().out) == sum(numbers)/len(numbers)


def test_negative_numbers(capfd, datadir):
    x, y = 12, -34

    run(f'python {datadir/"basicmath.py"} add {x} {y}', shell=True)
    assert int(capfd.readouterr().out) == x + y


def test_type_casting(capfd, datadir):
    error = "argument {arg}: invalid int value: '{value}'"
    x, y = 12, 34.0

    run(f'python {datadir/"basicmath.py"} add {x} {y}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(arg='y', value=y))

    x, y = 12.0, 34.0

    run(f'python {datadir/"basicmath.py"} add {x} {y}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(arg='x', value=x))

    x, y = 'foo', 42

    run(f'python {datadir/"basicmath.py"} add {x} {y}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(arg='x', value=x))


def test_missing_args(capfd, datadir):
    error = 'the following arguments are required: {args}'
    x = 12

    run(f'python {datadir/"basicmath.py"} add {x}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args='y'))

    run(f'python {datadir/"basicmath.py"} add', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args='x, y'))


def test_redundant_args(capfd, datadir):
    error = 'unrecognized arguments: {args}'
    x, y, z = 12, 34, 56

    run(f'python {datadir/"basicmath.py"} add {x} {y} {z}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args=z))

    x, y, z = 12, 34, '-f'

    run(f'python {datadir/"basicmath.py"} add {x} {y} {z}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args=z))

    x, y, z, q = 12, 34, '--flag', 'value'

    run(f'python {datadir/"basicmath.py"} add {x} {y} {z} {q}', shell=True)
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args=f'{z} {q}'))


def test_open(capfd, datadir):
    filename = datadir / 'numbers.txt'
    with open(filename) as file:
        numbers = (float(line) for line in file.readlines())

    run(f'python {datadir/"basicmath.py"} sumfile {filename}', shell=True)
    assert float(capfd.readouterr().out) == sum(numbers)


def test_aliases(capfd, datadir):
    x, y = 12, 34

    run(f'python {datadir/"basicmath.py"} sum {x} {y}', shell=True)
    assert int(capfd.readouterr().out) == x + y

    run(f'python {datadir/"basicmath.py"} plus {x} {y}', shell=True)
    assert int(capfd.readouterr().out) == x + y


def test_help(capfd, datadir):
    run(f'python {datadir/"basicmath.py"} --help', shell=True)
    assert 'Basic math operations.' in capfd.readouterr().out

    run(f'python {datadir/"basicmath.py"} -h', shell=True)
    assert 'Basic math operations.' in capfd.readouterr().out

    run(f'python {datadir/"basicmath.py"} add --help', shell=True)
    help_message = capfd.readouterr().out
    assert 'Add two numbers.' in help_message
    assert 'First operand' in help_message
    assert 'Second operand' in help_message

    run(f'python {datadir/"basicmath.py"} add -h', shell=True)
    help_message = capfd.readouterr().out
    assert 'Add two numbers.' in help_message
    assert 'First operand' in help_message
    assert 'Second operand' in help_message


def test_ignore(capfd, datadir):
    n = 6

    run(f'python {datadir/"basicmath.py"} calculate-factorial {n}', shell=True)
    assert "invalid choice: 'calculate-factorial'" in capfd.readouterr().err.splitlines()[-1]


def test_pseudonym(capfd, datadir):
    n = 6

    run(f'python {datadir/"basicmath.py"} fac 6', shell=True)
    assert int(capfd.readouterr().out) == factorial(n)


def test_arg_map(capfd, datadir):
    x, base = 1000, 10

    run(f'python {datadir/"basicmath.py"} log {x} --to {base}', shell=True)
    assert float(capfd.readouterr().out) == log(x, base)

    run(f'python {datadir/"basicmath.py"} log {x} -t {base}', shell=True)
    assert float(capfd.readouterr().out) == log(x, base)


def test_metavars(capfd, datadir):
    run(f'python {datadir/"basicmath.py"} log --help', shell=True)
    assert '-t BASE, --to BASE' in capfd.readouterr().out

    run(f'python {datadir/"basicmath.py"} log -h', shell=True)
    assert '-t BASE, --to BASE' in capfd.readouterr().out


def test_set_name():
    from pytest import raises

    from cliar import Cliar, set_name

    with raises(NameError) as excinfo:
        class _(Cliar):
            @set_name('')
            def _(self):
                pass

    assert 'Command name cannot be empty' in str(excinfo.value)


def test_str_arg(capfd, datadir):
    message = 'Hello Cliar'
    run(f'python {datadir/"basicmath.py"} echo "{message}"', shell=True)
    assert capfd.readouterr().out.strip() == message
