from src.data import load_data
import sys, os


def test_load_data():
    print(sys.path) 
    data = load_data()
    assert data is not None
    assert data.shape[1] == 81 
    assert os.path.exists("data/raw_data.csv") 


def test_clean_data():
    from src.data import clean_data
    data = load_data()
    data = clean_data(data)
    assert data.isna().sum().sum() == 0
    assert data.duplicated().sum() == 0
    assert data.shape[0] > 0
    assert data.shape[1] == 75
