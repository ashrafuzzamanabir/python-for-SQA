import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):
  """
  Function to test the login functionality of the Acme Bank website.

  Parameters:
  - page (Page): The Playwright Page object representing the browser page.

  This function performs the following steps:
  1. Navigates to the Acme Bank login page.
  2. Fills in the username field with 'andy'.
  3. Fills in the password field with 'i<3pandas'.
  4. Clicks the login button.
  5. Asserts that the logo, main menu, and various menu options are visible.

  This function is marked with the pytest.mark.ui and pytest.mark.acme_bank markers.

  Returns:
  None
  """

  # Arrange
  page.goto('https://demo.applitools.com/')

  # Act
  page.locator('id=username').fill('andy')
  page.locator('id=password').fill('i<3pandas')
  page.locator('id=log-in').click()

  # Assert
  expect(page.locator('div.logo-w')).to_be_visible()
  expect(page.locator('ul.main-menu')).to_be_visible()
  expect(page.get_by_text('Add Account')).to_be_visible()
  expect(page.get_by_text('Make Payment')).to_be_visible()
  expect(page.get_by_text('View Statement')).to_be_visible()
  expect(page.get_by_text('Request Increase')).to_be_visible()
  expect(page.get_by_text('Pay Now')).to_be_visible()



