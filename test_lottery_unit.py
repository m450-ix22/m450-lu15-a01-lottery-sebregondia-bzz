import pytest
from person import Person
from lottery import create_ticket
from ticket import Ticket


@pytest.fixture
def mock_person():
    """Fixture to create a mock person object"""
    return Person('TestUser', 'testpass', 10.00)


def test_create_ticket(mock_person, monkeypatch):
    """Test the create_ticket function"""
    inputs = iter([5, 10, 15, 20, 25, 30, 3])  # Mock user inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tickets = []

    def mock_print_ticket(ticket):
        tickets.append(ticket)

    monkeypatch.setattr('lottery.print_ticket', mock_print_ticket)

    create_ticket(mock_person)

    assert mock_person.balance == 8.00  # Balance reduced by 2.00
    assert len(tickets) == 1  # One ticket created
    ticket = tickets[0]
    assert ticket.joker == 3
    assert sorted(ticket.numbers) == [5, 10, 15, 20, 25, 30]
