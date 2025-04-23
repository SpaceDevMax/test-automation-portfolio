# Math Tests

This subfolder contains automated test scripts for mathematical operations and functions. The tests are designed to validate the correctness of mathematical computations in various scenarios.

## Overview

The `math-tests` directory includes test cases for basic arithmetic, geometric calculations, and other mathematical utilities. These tests ensure reliability and accuracy in mathematical implementations.

## Prerequisites

- Python 3.8+
- Required libraries: `pytest`, `numpy` (install via `pip install pytest numpy`)

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the math-tests folder:
   ```bash
   cd path/to/math-tests

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

  ## Running Tests

  To execute all tests, run:
  ```bash
  pytest
  ```
  To run a specific test file:
  ```bash
  pytest test_arithmetic.py
  ```

## Test Structure
  test_arithmetic.py: Tests for basic operations (addition, subtraction, multiplication, division).
  test_geometry.py: Tests for geometric calculations (area, perimeter, etc.).
  test_utils.py: Tests for utility functions (factorials, prime checks, etc.).

  