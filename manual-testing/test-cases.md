# SauceDemo Test Cases

# TC-001 — Successful Login

Test Case ID: TC-001

Title: Verify that a user can log in with valid credentials

Preconditions:

SauceDemo application is accessible.

A valid SauceDemo user account is available.

Test Steps:

Navigate to the SauceDemo login page.

Enter the username standard_user.

Enter the valid password.

Click the Login button.

Expected Result:

The user is successfully logged in and redirected to the Products page.

Actual Result:

The user was successfully logged in and redirected to the Products page.

Status: PASS

# TC-002 — Invalid Login

Test Case ID: TC-002

Title: Verify that a user cannot log in with an incorrect password

Preconditions:

SauceDemo application is accessible.

A valid username is available.

Test Steps:

Navigate to the SauceDemo login page.

Enter the username standard_user.

Enter an incorrect password.

Click the Login button.

Expected Result:

The user should not be logged in and an appropriate error message should be displayed.

Actual Result:

The user was not logged in and the error message "Epic sadface: Username and password do not match any user in this service" was displayed.

Status: PASS

# TC-003 — Add and Remove Product

Test Case ID: TC-003

Title: Verify that a user can add a product to the cart and remove it

Preconditions:

SauceDemo application is accessible.

User is logged in with valid credentials.

Test Steps:

Navigate to the Products page.

Select a specific product, such as Sauce Labs Backpack.

Click the Add to cart button.

Open the shopping cart.

Verify that the selected product is displayed.

Remove the product from the cart.

Expected Result:

The selected product should be added to the cart and displayed correctly. After selecting Remove, the product should no longer be present in the cart.

Actual Result:

The product was successfully added to the cart and displayed correctly. After selecting Remove, the product was successfully removed from the cart.

Status: PASS

# TC-004 — Checkout Validation

Test Case ID: TC-004

Title: Verify that required checkout fields cannot be left empty

Preconditions:

SauceDemo application is accessible.

User is logged in with valid credentials.

A product has been added to the shopping cart.

Test Steps:

Open the shopping cart.

Click Checkout.

Leave the First Name field empty.

Leave the Last Name field empty.

Leave the Postal Code field empty.

Click Continue.

Expected Result:

The checkout process should not continue and appropriate validation messages should be displayed for the required fields.

Actual Result:

The checkout process did not continue and a validation message indicated that the First Name field was required.

Status: PASS

# TC-005 — Complete Order

Test Case ID: TC-005

Title: Verify that a user can successfully complete an order

Preconditions:

SauceDemo application is accessible.

User is logged in with valid credentials.

A product has been added to the shopping cart.

Test Steps:

Open the shopping cart.

Click Checkout.

Enter a valid first name.

Enter a valid last name.

Enter a valid postal code.

Click Continue.

Verify that the selected product and its price are displayed correctly.

Click Finish.

Expected Result:

The order should be completed successfully and an order confirmation message should be displayed.

Actual Result:

The order was completed successfully and the message "Thank you for your order!" was displayed.

Status: PASS