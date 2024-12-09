import pytest
import main
from person import Person


@pytest.fixture
def mock_functions(monkeypatch):
    """Monkeypatch to replace the functions in main"""
    def dummy_login():
        """Mock login function"""
        return Person('TestUser', 'testpass', 10.00)

    def dummy_transfer_money(person):
        """Mock transfer_money function"""
        pass

    def dummy_create_ticket(person):
        """Mock create_ticket function"""
        pass

    def dummy_select_menu():
        """Mock menu selection"""
        print('Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden')
        return input('')

    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'transfer_money', dummy_transfer_money)
    monkeypatch.setattr(main, 'create_ticket', dummy_create_ticket)
    monkeypatch.setattr(main, 'select_menu', dummy_select_menu)


def test_main_exit(capsys, monkeypatch, mock_functions):
    """Test the main function with the exit option"""
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert 'Lotto' in output  # Menu was displayed


def test_main_money(capsys, monkeypatch, mock_functions):
    """Test the main function with the money transaction option"""
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert 'Lotto' in output  # Menu was displayed


def test_main_ticket(capsys, monkeypatch, mock_functions):
    """Test the main function with the ticket creation option"""
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert 'Lotto' in output  # Menu was displayed
