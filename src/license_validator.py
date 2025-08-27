import hashlib
import hmac
import time
import requests

class LicenseValidator:
    def __init__(self):
        self.license_server = "https://your-license-server.com"
        self.demo_time_limit = 3600  # 1 hour demo sessions
        
    def validate_license(self, client_ip):
        """Validate demo license"""
        try:
            # Check if this IP has an active demo session
            session_data = self.get_session_data(client_ip)
            
            if session_data and not self.is_session_expired(session_data):
                return True
            
            # Create new demo session
            return self.create_demo_session(client_ip)
            
        except Exception as e:
            print(f"License validation error: {e}")
            return False
    
    def create_demo_session(self, client_ip):
        """Create new demo session"""
        session_id = hashlib.sha256(f"{client_ip}{time.time()}".encode()).hexdigest()
        
        session_data = {
            'session_id': session_id,
            'client_ip': client_ip,
            'start_time': time.time(),
            'demo_features': ['encrypt', 'attack_sim', 'compress'],
            'rate_limit': 100  # requests per hour
        }
        
        # Store session (you'd use Redis or database in production)
        self.store_session(session_id, session_data)
        return True
    
    def get_hardware_fingerprint(self):
        """Get hardware fingerprint for licensing"""
        # Implementation depends on your licensing strategy
        pass

def validate_license(client_ip):
    """Global license validation function"""
    validator = LicenseValidator()
    return validator.validate_license(client_ip)