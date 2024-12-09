import pytest
from unittest.mock import patch
import main


def test_main_exit(capsys):
    """Test the main function with the exit option."""
    inputs = ['Z']
    with patch('builtins.input', side_effect=inputs):
        main.main()
    output = capsys.readouterr().out
    assert "Login erfolgreich!" in output
    assert "Programm beendet." in output


def test_main_money(capsys):
    """Test the main function with the money transaction option."""
    inputs = ['A', 'Z']
    with patch('builtins.input', side_effect=inputs):
        main.main()
    output = capsys.readouterr().out
    assert "Kontofunktion ausgewählt." in output
    assert "Programm beendet." in output


def test_main_ticket(capsys):
    """Test the main function with the ticket creation option."""
    inputs = ['B', 'Z']
    with patch('builtins.input', side_effect=inputs):
        main.main()
    output = capsys.readouterr().out
    assert "Lottotipps ausgewählt." in output
    assert "Programm beendet." in output


def test_main_invalid_option(capsys):
    """Test the main function with an invalid menu option."""
    inputs = ['X', 'Z']
    with patch('builtins.input', side_effect=inputs):
        main.main()
    output = capsys.readouterr().out
    assert "Ungültige Option. Bitte erneut wählen." in output


def test_main_error_handling():
    """Test the main function to handle unexpected errors."""
    with patch('main.input', side_effect=RuntimeError("Simulierter Fehler")):
        with pytest.raises(RuntimeError, match="Simulierter Fehler"):
            main.main()
