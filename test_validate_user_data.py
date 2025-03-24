import pytest
from validation import validate_user_data  # Replace with the correct module name

# 1. Test valid user data
def test_valid_user_data():
    user_data = {
        "username": "Dijana_123",
        "email": "dijana@example.com",
        "password": "Pass@1234",
        "age": 20,
        "referral_code": "ABCDEFGH"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] is True
    assert result["errors"] == {}

# 2. Test missing required fields
@pytest.mark.parametrize("user_data, expected_errors", [
    ({"email": "user@mail.com", "password": "Password@1"}, {"username": "Username is required"}),
    ({"username": "ValidUser", "password": "Password@1"}, {"email": "Email is required"}),
    ({"username": "ValidUser", "email": "user@mail.com"}, {"password": "Password is required"})
])
def test_missing_required_fields(user_data, expected_errors):
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 3. Test invalid usernames
@pytest.mark.parametrize("user_data, expected_errors", [
    ({"username": "Us", "email": "user@mail.com", "password": "Password@1"}, {"username": "Username must be between 3 and 20 characters"}),
    ({"username": "User@123", "email": "user@mail.com", "password": "Password@1"}, {"username": "Username can only contain letters, numbers, and underscores"})
])
def test_invalid_usernames(user_data, expected_errors):
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 4. Test invalid emails
@pytest.mark.parametrize("user_data, expected_errors", [
    ({"username": "ValidUser", "email": "invalid-email", "password": "Password@1"}, {"email": "Invalid email format"})
])
def test_invalid_emails(user_data, expected_errors):
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 5. Test invalid passwords
@pytest.mark.parametrize("user_data, expected_errors", [
    ({"username": "ValidUser", "email": "user@mail.com", "password": "123"}, {"password": "Password must be at least 8 characters long"}),
    ({"username": "ValidUser", "email": "user@mail.com", "password": "Password123"}, {"password": "Password must contain at least one special character"}),
    ({"username": "ValidUser", "email": "user@mail.com", "password": "Password@!"}, {"password": "Password must contain at least one number"})
])
def test_invalid_passwords(user_data, expected_errors):
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 6. Test invalid age
@pytest.mark.parametrize("user_data, expected_errors", [
    ({"username": "ValidUser", "email": "user@mail.com", "password": "Password@1", "age": 16}, {"age": "User must be at least 18 years old"}),
    ({"username": "ValidUser", "email": "user@mail.com", "password": "Password@1", "age": "twenty"}, {"age": "Age must be a number"})
])
def test_invalid_age(user_data, expected_errors):
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 7. Test invalid referral code
@pytest.mark.parametrize("user_data, expected_errors", [
    ({"username": "ValidUser", "email": "user@mail.com", "password": "Password@1", "referral_code": "ABC123"}, {"referral_code": "Referral code must be exactly 8 characters"}),
    ({"username": "ValidUser", "email": "user@mail.com", "password": "Password@1", "referral_code": 12345678}, {"referral_code": "Referral code must be a string"})
])
def test_invalid_referral_code(user_data, expected_errors):
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 8. Test empty data
def test_empty_data():
    user_data = {}
    expected_errors = {
        "username": "Username is required",
        "email": "Email is required",
        "password": "Password is required"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

# 9. Test invalid data type (non-dictionary input)
def test_invalid_data_format():
    result = validate_user_data("Invalid data")
    expected_errors = {"global": "Invalid user data format"}
    assert result["is_valid"] is False
    assert result["errors"] == expected_errors

