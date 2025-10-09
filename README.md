# bio_collocation

A Python package for biological collocation analysis.

## Installation

```bash
pip install -e .
```

## Features

- **io**: Input/output operations for data files
- **surrogate**: Surrogate modeling tools
- **collocation**: Collocation methods implementation
- **plotting**: Visualization utilities
- **stan**: CmdStanPy integration for Bayesian inference
- **cli**: Command-line interface tools

## Dependencies

- cmdstanpy
- arviz
- numpy
- scipy
- matplotlib
- xarray

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT