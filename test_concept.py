import pytest
import allure
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.feature("Addition Feature")
@allure.story("Testing Addition Functionality")
def test_addition():
    """Test case for addition"""
    with allure.step("Step 1: Define numbers"):
        num1, num2 = 3, 5
        logger.info(f"Numbers defined: num1={num1}, num2={num2}")

    with allure.step("Step 2: Perform addition"):
        result = num1 + num2
        logger.info(f"Addition result: {result}")

    with allure.step("Step 3: Assert result"):
        assert result == 8, "Addition result is incorrect"
        logger.info("Addition assertion passed!")

@allure.feature("Subtraction Feature")
@allure.story("Testing Subtraction Functionality")
def test_subtraction():
    """Test case for subtraction"""
    with allure.step("Step 1: Define numbers"):
        num1, num2 = 10, 4
        logger.info(f"Numbers defined: num1={num1}, num2={num2}")

    with allure.step("Step 2: Perform subtraction"):
        result = num1 - num2
        logger.info(f"Subtraction result: {result}")

    with allure.step("Step 3: Assert result"):
        assert result == 6, "Subtraction result is incorrect"
        logger.info("Subtraction assertion passed!")

@allure.feature("Multiplication Feature")
@allure.story("Testing Multiplication Functionality")
def test_multiplication():
    """Test case for multiplication"""
    with allure.step("Step 1: Define numbers"):
        num1, num2 = 2, 6
        logger.info(f"Numbers defined: num1={num1}, num2={num2}")

    with allure.step("Step 2: Perform multiplication"):
        result = num1 * num2
        logger.info(f"Multiplication result: {result}")

    with allure.step("Step 3: Assert result"):
        assert result == 12, "Multiplication result is incorrect"
        logger.info("Multiplication assertion passed!")
