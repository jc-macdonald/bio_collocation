"""Test basic package structure and imports."""

import sys
import os

# Add the parent directory to the path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_main_package_import():
    """Test that the main package can be imported."""
    import bio_collocation
    assert bio_collocation is not None


def test_io_module_import():
    """Test that the io module can be imported."""
    import bio_collocation.io
    assert bio_collocation.io is not None


def test_surrogate_module_import():
    """Test that the surrogate module can be imported."""
    import bio_collocation.surrogate
    assert bio_collocation.surrogate is not None


def test_collocation_module_import():
    """Test that the collocation module can be imported."""
    import bio_collocation.collocation
    assert bio_collocation.collocation is not None


def test_plotting_module_import():
    """Test that the plotting module can be imported."""
    import bio_collocation.plotting
    assert bio_collocation.plotting is not None


def test_stan_module_import():
    """Test that the stan module can be imported."""
    import bio_collocation.stan
    assert bio_collocation.stan is not None


def test_cli_module_import():
    """Test that the cli module can be imported."""
    import bio_collocation.cli
    assert bio_collocation.cli is not None


if __name__ == "__main__":
    test_main_package_import()
    test_io_module_import()
    test_surrogate_module_import()
    test_collocation_module_import()
    test_plotting_module_import()
    test_stan_module_import()
    test_cli_module_import()
    print("All tests passed!")
