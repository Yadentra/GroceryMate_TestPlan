# Automated Test Cases for Grocery Mate Webshop

## Test Case 1: User Registration
- **Objective**: Verify that a new user can register successfully.
- **Test Techniques**: Boundary Value Analysis, Equivalence Partitioning.
- **Steps**:
  1. Navigate to the registration page.
  2. Enter valid user details (name, email, password).
  3. Click on the "Register" button.
- **Expected Result**: User should be successfully registered and redirected to the homepage with a welcome message.

## Test Case 2: User Login
- **Objective**: Ensure that registered users can log in.
- **Test Techniques**: Decision Table Testing.
- **Steps**:
  1. Navigate to the login page.
  2. Enter registered email and password.
  3. Click on the "Login" button.
- **Expected Result**: User should be logged in and redirected to the dashboard.

## Test Case 3: Product Search Functionality
- **Objective**: Verify the search functionality for products.
- **Test Techniques**: Exploratory Testing.
- **Steps**:
  1. Enter a product name in the search bar.
  2. Click the "Search" button.
- **Expected Result**: The search results should display relevant products.

## Test Case 4: Add Product to Cart
- **Objective**: Verify that a user can add products to the shopping cart.
- **Test Techniques**: State Transition Testing.
- **Steps**:
  1. Select a product from the search results.
  2. Click "Add to Cart."
- **Expected Result**: The product should be added to the cart successfully.

## Test Case 5: Checkout Process
- **Objective**: Test the complete checkout process.
- **Test Techniques**: End-to-End Testing.
- **Steps**:
  1. Navigate to the shopping cart.
  2. Click on "Checkout."
  3. Enter shipping and payment details.
  4. Confirm the order.
- **Expected Result**: Order should be placed successfully, and an order confirmation should be displayed.

## Test Case 6: Order History and Tracking
- **Objective**: Verify that users can view their order history.
- **Test Techniques**: User Interface Testing.
- **Steps**:
  1. Log in to the account.
  2. Navigate to "Order History."
- **Expected Result**: The page should display a list of previous orders.
