import pytest
from datetime import date
from assetmodel import AutnumRecord
from pydantic import ValidationError

def test_autnum_record():
    autnum_record = AutnumRecord(number=12345)

    assert autnum_record.number == 12345

def test_autnum_record_created():
    autnum_record = AutnumRecord(number=12345, created_date='2024-02-01')

    assert autnum_record.created_date == date(2024, 2, 1)

def test_autnum_record_created_invalid_date():
    with pytest.raises(ValidationError):
        AutnumRecord(number=12345, created_date='notadate')