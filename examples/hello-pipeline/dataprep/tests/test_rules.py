import pytest
import pandas as pd

from data_prep import *

@pytest.mark.parametrize('df_in_path, x_df_path, y_df_path', [
    ('./tests/assets/in_1.csv', './tests/assets/x_1.csv', './tests/assets/y_1.csv')
    ])
def test_apply_rules_paths(df_in_path, x_df_path, y_df_path):
    df_in = pd.read_csv(df_in_path)
    x = pd.read_csv(x_df_path)
    y = pd.read_csv(y_df_path, squeeze=True)
    x_tested, y_tested = apply_rules(df_in)

    pd._testing.assert_frame_equal(x, x_tested)
    pd._testing.assert_series_equal(y, y_tested)