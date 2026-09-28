# SauceDemo QA Portfolio

QA testing portfolio project for the SauceDemo e-commerce web application.

This project demonstrates manual testing and automated UI testing using Selenium WebDriver, Python, and pytest.

## Project Overview

This project focuses on testing the SauceDemo e-commerce web application.

The testing covers key user workflows including:

- User authentication
- Product browsing and sorting
- Adding and removing products from the cart
- Checkout validation
- Order completion

The project includes both manual test documentation and automated UI tests.

## Testing Scope

### In Scope

- User login and authentication
- Product display and sorting
- Adding and removing products
- Shopping cart functionality
- Checkout field validation
- Order summary verification
- Order completion

### Out of Scope

- Performance and load testing
- Security testing
- Backend infrastructure testing
- Real payment processing
- Cross-browser compatibility testing

## Manual Testing

Manual testing was performed to validate the main functional workflows of the application.

### Test Documentation

- [Test Plan](manual-testing/test-plan.md)
- [Test Cases](manual-testing/test-cases.md)
- [Test Execution](manual-testing/test-execution.md)
- [Bug Reports](manual-testing/bug-reports.md)

### Manual Test Results

| Metric | Result |
|---|---:|
| Test Cases | 5 |
| Passed | 5 |
| Failed | 0 |
| Pass Rate | 100% |
| Defects Identified | 3 |

## Automation

The UI automation tests were developed using:

- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- pytest fixtures

### Automated Test Cases

The automation suite covers:

1. Successful login
2. Invalid login
3. Adding and removing a product
4. Checkout validation
5. Completing an order

### Automation Test Results

| Metric | Result |
|---|---:|
| Automated Tests | 5 |
| Passed | 5 |
| Failed | 0 |
| Pass Rate | 100% |

## Project Structure

```text
saucedemo-qa-portfolio/
├── manual-testing/
│   ├── test-plan.md
│   ├── test-cases.md
│   ├── test-execution.md
│   └── bug-reports.md
│
├── automation/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_add_product.py
│   ├── test_checkout_validation.py
│   ├── test_complete_order.py
│   └── pages/
│       ├── login_page.py
│       ├── products_page.py
│       └── checkout_page.py
│
├── .gitignore
├── requirements.txt
└── README.md

## Tools & Technologies

- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- pytest fixtures
- Git
- GitHub
- Markdown

## How to Run

### Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

### Run All Automated Tests

```bash
pytest automation
```

### Run an Individual Test

For example:

```bash
pytest automation/test_login.py
```

## Defects

Three reproducible defects were identified during testing using SauceDemo's special test users.

| ID | Description | Severity | Priority |
|---|---|---|---|
| BUG-001 | Incorrect product images displayed for `problem_user` | Medium | Medium |
| BUG-002 | Some products cannot be added to the cart for `error_user` | High | High |
| BUG-003 | Remove button does not remove an added product from the cart for `error_user` | High | High |

Detailed defect reports, including reproduction steps, expected results, and actual results, are available in the [Bug Reports](manual-testing/bug-reports.md) document.