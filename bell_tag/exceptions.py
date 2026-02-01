class BellTagError(Exception):
    """Base exception for Bell Tag"""
    pass

class VerificationFailed(BellTagError):
    """Raised when server verification fails"""
    pass
