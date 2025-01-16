from rest_framework_simplejwt.tokens import RefreshToken

def blacklist_token(token):
    """
    Blacklists a given refresh token.
    """
    try:
        RefreshToken(token).blacklist()
        return {"message": "Successfully logged out."}, 200
    except Exception as e:
        return {"error": str(e)}, 500
