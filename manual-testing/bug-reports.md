# SauceDemo Bug Reports

## BUG-001 — Incorrect Product Images

**Bug ID:** BUG-001

**Title:** Incorrect product images displayed on the Products page

**Environment:**
- Application: SauceDemo
- User: `problem_user`
- Browser: Google Chrome
- Operating System: Windows

**Severity:** Medium

**Priority:** Medium

**Preconditions:**
- SauceDemo application is accessible.
- User is logged in with the `problem_user` account.

**Steps to Reproduce:**
1. Log in using `problem_user`.
2. Navigate to the Products page.
3. Review the product images displayed.

**Expected Result:**
Each product should display the image corresponding to the correct product.

**Actual Result:**
Product images are incorrectly displayed and do not correspond to the associated products.

**Status:** Open

## BUG-002 — Products Cannot Be Added to Cart

**Bug ID:** BUG-002

**Title:** Some products cannot be added to the shopping cart

**Environment:**
- Application: SauceDemo
- User: `error_user`
- Browser: Google Chrome
- Operating System: Windows

**Severity:** High

**Priority:** High

**Preconditions:**
- SauceDemo application is accessible.
- User is logged in with the `error_user` account.

**Steps to Reproduce:**
1. Log in using `error_user`.
2. Navigate to the Products page.
3. Attempt to add the affected products to the shopping cart.
4. Observe the cart.

**Expected Result:**
The selected products should be successfully added to the shopping cart.

**Actual Result:**
Two products cannot be added to the shopping cart.

**Status:** Open

## BUG-003 — Remove Button Does Not Remove Product

**Bug ID:** BUG-003

**Title:** Remove button does not remove an added product from the cart

**Environment:**
- Application: SauceDemo
- User: `error_user`
- Browser: Google Chrome
- Operating System: Windows

**Severity:** High

**Priority:** High

**Preconditions:**
- SauceDemo application is accessible.
- User is logged in with the `error_user` account.

**Steps to Reproduce:**
1. Log in using `error_user`.
2. Navigate to the Products page.
3. Add a product to the shopping cart.
4. Click the Remove button for the added product.
5. Observe the cart indicator.

**Expected Result:**
The selected product should be removed from the shopping cart and the cart indicator should update accordingly.

**Actual Result:**
The selected product remains in the shopping cart after clicking the Remove button.

**Status:** Open