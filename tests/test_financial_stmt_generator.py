"""Test FinancialStatementGenerator class."""
from financial_stmt_generator import FinancialStatementGenerator


def test_run():
    """Unit test for run()."""
    generator = FinancialStatementGenerator("dev")
    generator.run("dev")
    assert generator.asset_parsers[0].total_amount > 0


def test_mine_data():
    """Unit test for mine_data()."""
    generator = FinancialStatementGenerator("dev")
    generator.mine_data()
    assert "credit card" not in vars(generator)
