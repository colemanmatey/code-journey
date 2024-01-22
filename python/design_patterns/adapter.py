"""
The Adapter Design Pattern

The Adapter Design Pattern is a structural pattern that allows the interface 
of an existing class to be used as another interface. It is often used to make 
existing classes work with others without modifying their source code. The 
Adapter Pattern is particularly useful when integrating new features or 
components into an existing system.
"""


class LegacyAuthSystem:
    """Legacy Authentication System"""
    def authorize(self, username, password):
        print(f"Legacy authentication for {username}")


class ModernAuthSystem:
    """Modern Authentication System"""
    def authenticate(self, email, secret_key):
        print(f"Modern authentication for {email}")


class AuthAdapter(ModernAuthSystem):
    """Adapter class to make the new system (ModernAuthSystem) compatible with the old system (LegacyAuthSystem)"""
    def __init__(self, modern_auth):
        self.modern_auth = modern_auth

    def authorize(self, username, password):
        """Adapt the interface to call the new authentication system"""
        email = f"{username}@company.com"
        secret_key = password.upper() # Adapt the password format if needed
        self.modern_auth.authenticate(email, secret_key)


# Client code using the existing LegacyAuthSystem
def authenticate_user(auth_system, username, password):
    auth_system.authorize(username, password)


# Instantiate the existing LegacyAuthSystem
legacy_auth = LegacyAuthSystem()

# Use the legacy authenticaton system
authenticate_user(legacy_auth, "jane_doe", "password456")

# Instantiate the new ModernAuthSystem
modern_auth = ModernAuthSystem()

# Use the Adapter to make the ModernAuthSystem compatible with the LegacyAuthSystem
adapter = AuthAdapter(modern_auth)

# Use the adapter to authenticate a user without modifying the client code
authenticate_user(adapter, "john_doe", "password123")
