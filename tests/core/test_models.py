import importlib


def test_models_import_no_exception():
    try:
        importlib.import_module("rework.core.models")
    except Exception as e:
        raise AssertionError(f"Importing rework.core.models an exception: {e}")
