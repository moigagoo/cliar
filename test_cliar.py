from subprocess import run
from math import factorial, log


def test_positional_args(capfd):
    x, y = 12, 34

    run(f'python testmath.py add {x} {y}')
    assert int(capfd.readouterr().out) == x + y

def test_optional_args(capfd):
    x, power = 12, 3

    run(f'python testmath.py power {x} --power {power}')
    assert int(capfd.readouterr().out) == x ** power

    run(f'python testmath.py power {x} -p {power}')
    assert int(capfd.readouterr().out) == x ** power

    run(f'python testmath.py power {x}')
    assert int(capfd.readouterr().out) == x ** 2


def test_no_args(capfd):
    from math import pi

    run('python testmath.py pi')
    assert float(capfd.readouterr().out) == pi

    run('python testmath.py avg')
    assert float(capfd.readouterr().out) == sum((1, 2, 3))/3

def test_root_command(capfd):
    version = '0.1.0'

    run('python testmath.py')
    assert capfd.readouterr().out.strip() == 'Welcome to math!'

    run('python testmath.py --version')
    assert capfd.readouterr().out.strip() == version

    run('python testmath.py -v')
    assert capfd.readouterr().out.strip() == version


def test_nargs(capfd):
    numbers = 1, 2, 42, 101

    run(f'python testmath.py summ {" ".join(str(number) for number in numbers)}')
    assert int(capfd.readouterr().out) == sum(numbers)

    numbers = 1, 2, 42.2, 101.1

    run(f'python testmath.py avg --numbers {" ".join(str(number) for number in numbers)}')
    assert float(capfd.readouterr().out) == sum(numbers)/len(numbers)

    run(f'python testmath.py avg -n {" ".join(str(number) for number in numbers)}')
    assert float(capfd.readouterr().out) == sum(numbers)/len(numbers)


def test_negative_numbers(capfd):
    x, y = 12, -34

    run(f'python testmath.py add {x} {y}')
    assert int(capfd.readouterr().out) == x + y


def test_type_casting(capfd):
    error = "argument {arg}: invalid int value: '{value}'"
    x, y = 12, 34.0

    run(f'python testmath.py add {x} {y}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(arg='y', value=y))

    x, y = 12.0, 34.0

    run(f'python testmath.py add {x} {y}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(arg='x', value=x))

    x, y = 'foo', 42

    run(f'python testmath.py add {x} {y}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(arg='x', value=x))


def test_missing_args(capfd):
    error = 'the following arguments are required: {args}'
    x = 12

    run(f'python testmath.py add {x}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args='y'))

    run(f'python testmath.py add')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args='x, y'))


def test_redundant_args(capfd):
    error = 'unrecognized arguments: {args}'
    x, y, z = 12, 34, 56

    run(f'python testmath.py add {x} {y} {z}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args=z))

    x, y, z = 12, 34, '-f'

    run(f'python testmath.py add {x} {y} {z}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args=z))

    x, y, z, q = 12, 34, '--flag', 'value'

    run(f'python testmath.py add {x} {y} {z} {q}')
    assert capfd.readouterr().err.splitlines()[-1].endswith(error.format(args=f'{z} {q}'))


def test_open(capfd):
    filename = 'numbers.txt'
    with open(filename) as file:
        numbers = (float(line) for line in file.readlines())

    run('python testmath.py sumfile numbers.txt')
    assert float(capfd.readouterr().out) == sum(numbers)


def test_aliases(capfd):
    x, y = 12, 34

    run(f'python testmath.py sum {x} {y}')
    assert int(capfd.readouterr().out) == x + y

    run(f'python testmath.py plus {x} {y}')
    assert int(capfd.readouterr().out) == x + y


def test_help(capfd):
    run('python testmath.py --help')
    assert  'Basic math operations.' in capfd.readouterr().out

    run('python testmath.py -h')
    assert  'Basic math operations.' in capfd.readouterr().out

    run('python testmath.py add --help')
    help_message = capfd.readouterr().out
    assert 'Add two numbers.' in help_message
    assert 'First operand' in help_message
    assert 'Second operand' in help_message

    run('python testmath.py add -h')
    help_message = capfd.readouterr().out
    assert 'Add two numbers.' in help_message
    assert 'First operand' in help_message
    assert 'Second operand' in help_message


def test_ignore(capfd):
    n = 6

    run(f'python testmath.py calculate-factorial {n}')
    assert "invalid choice: 'calculate-factorial'" in capfd.readouterr().err.splitlines()[-1]


def test_pseudonym(capfd):
    n = 6

    run(f'python testmath.py fac 6')
    assert int(capfd.readouterr().out) == factorial(n)


def test_arg_map(capfd):
    x, base = 1000, 10

    run(f'python testmath.py log {x} --to {base}')
    assert float(capfd.readouterr().out) == log(x, base)

    run(f'python testmath.py log {x} -t {base}')
    assert float(capfd.readouterr().out) == log(x, base)


def test_metavars(capfd):
    run('python testmath.py log --help')
    assert '-t BASE, --to BASE' in capfd.readouterr().out

    run('python testmath.py log -h')
    assert '-t BASE, --to BASE' in capfd.readouterr().out
