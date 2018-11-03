import rps
# kdyz dam jen import rps, nacte mi to cele to RPS a tam jsou ty inputy, ktere mi nebudou fungovat


def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True
    
def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True
    
def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True
    
def test_lizard_is_invalid_play():
    assert rps.is_valid_play('lizard') is False


#-----------------------------------------------
#tady testuju jestli tah pocitace funguje a delam to stokrat
def test_computer_play_is_valid():
    for _ in range(100):
        play = rps.generate_computer_play()
        assert rps.is_valid_play(play)
        
def test_computer_plays_randomly():
    # mam tu for v zapisu jako comprehension, muzu pouzit i normalni for cyklus
    plays = [rps.generate_computer_play() for _ in range(5000)]
    
    rocks = plays.count('rock')
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    
    print(rocks, papers, scissors)
    
    assert rocks > 200
    assert papers > 200
    assert scissors > 200
    
def test_paper_beats_rock():
    result = rps.evaluate_game('paper', 'rock')
    assert result == 'human'
    
def test_paper_beats_rock_2():
    result = rps.evaluate_game('rock', 'paper')
    assert result == 'computer'

def test_rock_beats_scissors():
    result = rps.evaluate_game('rock', 'scissors')
    assert result == 'human'

def test_rock_beats_scissors_2():
    result = rps.evaluate_game('scissors', 'rock')
    assert result == 'computer'    
    
def test_scissors_beats_paper():
    result = rps.evaluate_game('scissors', 'paper')
    assert result == 'human'
    
def test_scissors_beats_paper_2():
    result = rps.evaluate_game('paper', 'scissors')
    assert result == 'computer'

def test_rock_ties_rock():
    result = rps.evaluate_game('rock', 'rock')
    assert result == 'tie'
    
def test_paper_ties_paper():
    result = rps.evaluate_game('paper', 'paper')
    assert result == 'tie'
    
def test_scissors_ties_scissors():
    result = rps.evaluate_game('scissors', 'scissors')
    assert result == 'tie'
    

# falesny input

def input_faked_rock(prompt):
    print(prompt)
    return 'rock'

# monkeypatch plati jen v ramci testu, pomoci monkeypatche podvrhnu input, ale bacha co prepisuju
# fixture capsys zachyti vsechno co se vypisuje na obrazovku - err i out. My pouzivame jen ten output, protoze error vypis tam nemame
#muzu si psat vlastni fixtures - fixture muze brat jako argument dalsi fixture
    
def test_full_game(capsys):
    
    rps.main(input=input_faked_rock)
    
    captured = capsys.readouterr()
    assert 'rock, paper or scissors? ' in captured.out
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    