import pytest
from datetime import datetime, timedelta
from app.data_processor import process_message, calculate_age

def test_calculate_age():
    # Test with a date of birth that should result in age 30
    dob = (datetime.now() - timedelta(days=365*30)).strftime('%Y-%m-%d')
    age = calculate_age(dob)
    assert age == 30

def test_process_message():
    # Test with valid data
    message = {
        'name': 'John Doe',
        'date_of_birth': (datetime.now() - timedelta(days=365*25)).strftime('%Y-%m-%d')
    }
    result = process_message(message)
    assert 'age' in result
    assert 'is_even' in result
    assert result['age'] == 25
    assert result['is_even'] == False

def test_process_message_invalid_dob():
    # Test with invalid date of birth
    message = {
        'name': 'John Doe',
        'date_of_birth': 'invalid-date'
    }
    with pytest.raises(ValueError):
        process_message(message)

def test_process_message_missing_dob():
    # Test with missing date of birth
    message = {
        'name': 'John Doe'
    }
    with pytest.raises(ValueError):
        process_message(message) 