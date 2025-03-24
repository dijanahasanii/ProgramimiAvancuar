# test_user_validation.py

import unittest
from user_validation import validate_user_data

class TestUserValidation(unittest.TestCase):
    
    def test_valid_data(self):
        user_data = {
            "username": "user123",
            "email": "user@example.com",
            "password": "Password1!",
            "age": 25,
            "referral_code": "ABCDEFGH"
        }
        result = validate_user_data(user_data)
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["errors"], {})

    def test_missing_username(self):
        user_data = {
            "email": "user@example.com",
            "password": "Password1!",
            "age": 25
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["username"], "Username is required")

    def test_invalid_email(self):
        user_data = {
            "username": "user123",
            "email": "invalid-email",
            "password": "Password1!"
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["email"], "Invalid email format")

    def test_short_password(self):
        user_data = {
            "username": "user123",
            "email": "user@example.com",
            "password": "short"
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["password"], "Password must be at least 8 characters long")

    def test_missing_referral_code(self):
        user_data = {
            "username": "user123",
            "email": "user@example.com",
            "password": "Password1!"
        }
        result = validate_user_data(user_data)
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["errors"], {})

    def test_invalid_referral_code(self):
        user_data = {
            "username": "user123",
            "email": "user@example.com",
            "password": "Password1!",
            "referral_code": "short"
        }
        result = validate_user_data(user_data)
        self.assertFalse(result["is_valid"])
        self.assertEqual(result["errors"]["referral_code"], "Referral code must be exactly 8 characters")

if __name__ == "__main__":
    unittest.main()
