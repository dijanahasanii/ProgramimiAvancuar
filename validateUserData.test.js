// validateUserData.test.js
const validateUserData = require('./validateUserData');

describe('validateUserData', () => {
    test('should return valid for correct user data', () => {
        const userData = {
            username: 'validUser123',
            email: 'user@example.com',
            password: 'Password1!',
            age: 25,
            referralCode: 'ABCDEFGH'
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(true);
        expect(result.errors).toEqual({});
    });

    test('should return invalid for missing username', () => {
        const userData = {
            email: 'user@example.com',
            password: 'Password1!',
            age: 25
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(false);
        expect(result.errors.username).toBe('Username is required');
    });

    test('should return invalid for incorrect email format', () => {
        const userData = {
            username: 'validUser123',
            email: 'invalid-email',
            password: 'Password1!',
            age: 25
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(false);
        expect(result.errors.email).toBe('Invalid email format');
    });

    test('should return invalid for password too short', () => {
        const userData = {
            username: 'validUser123',
            email: 'user@example.com',
            password: 'short',
            age: 25
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(false);
        expect(result.errors.password).toBe('Password must be at least 8 characters long');
    });

    test('should return invalid for password without number', () => {
        const userData = {
            username: 'validUser123',
            email: 'user@example.com',
            password: 'Password!',
            age: 25
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(false);
        expect(result.errors.password).toBe('Password must contain at least one number');
    });

    test('should return invalid for underage user', () => {
        const userData = {
            username: 'validUser123',
            email: 'user@example.com',
            password: 'Password1!',
            age: 17
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(false);
        expect(result.errors.age).toBe('User must be at least 18 years old');
    });

    test('should return invalid for referral code not 8 characters', () => {
        const userData = {
            username: 'validUser123',
            email: 'user@example.com',
            password: 'Password1!',
            age: 25,
            referralCode: 'short'
        };
        const result = validateUserData(userData);
        expect(result.isValid).toBe(false);
        expect(result.errors.referralCode).toBe('Referral code must be exactly 8 characters');
    });
});
