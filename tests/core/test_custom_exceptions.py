import unittest

from rework.core.exceptions import ValidateError


class ValidateErrorTestCase(unittest.TestCase):
    def test_validate_error_with_code(self):
        detail = 'You do not have permission to perform this action.'
        code = 'permission_denied'
        ex = ValidateError(
            detail=detail,
            code=code,
        )
        self.assertEqual(ex.get_codes(), code)
        self.assertEqual(str(ex.detail), detail)
        self.assertIsNone(ex.errors)

    def test_validate_error_with_errors(self):
        detail = 'You do not have permission to perform this action.'
        code = 'permission_denied'
        errors = {
            "name": {
                "message": "This field is required.",
                "code": "required"
            },
            "age": {
                "message": "A valid integer is required.",
                "code": "invalid"
            }
        }
        ex = ValidateError(
            detail=detail,
            code=code,
            errors=errors,
        )
        self.assertEqual(ex.get_codes(), code)
        self.assertEqual(str(ex.detail), detail)
        self.assertIsInstance(ex.errors, dict)
