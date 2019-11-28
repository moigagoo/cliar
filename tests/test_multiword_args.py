from subprocess import run


def test_help(capfd, datadir):
    run(f'python {datadir/"multiword_args.py"} say -h', shell=True)

    output = capfd.readouterr().out

    assert 'words-to-say' in output
    assert '-t, --to-upper' in output

def test_say(capfd, datadir):
    words_to_say = 'hello world'
    repeat_words = 3

    run(f'python {datadir/"multiword_args.py"} say "{words_to_say}"', shell=True)
    assert capfd.readouterr().out.strip() == words_to_say

    run(f'python {datadir/"multiword_args.py"} say "{words_to_say}" --to-upper', shell=True)
    assert capfd.readouterr().out.strip() == words_to_say.upper()

    run(f'python {datadir/"multiword_args.py"} say "{words_to_say}" --repeat-words {repeat_words}', shell=True)
    assert capfd.readouterr().out.strip().splitlines() == [words_to_say] * repeat_words
