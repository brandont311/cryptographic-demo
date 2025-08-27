import subprocess
import json
import tempfile
import os

class QuantumEngine:
    def __init__(self):
        self.engine_path = '/usr/local/bin/axiomarc-engine'
        self.demo_mode = True
        
    def encrypt(self, message):
        """Interface to AXIOMARC encryption"""
        try:
            # Create temporary files
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
                input_file.write(message)
                input_path = input_file.name
            
            # Call AXIOMARC engine
            cmd = [
                self.engine_path,
                '--encrypt',
                '--input', input_path,
                '--demo-mode' if self.demo_mode else '--full-mode'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Parse result
                output = json.loads(result.stdout)
                return {
                    'coherence': output.get('coherence_level', 0.9963),
                    'phase_stability': output.get('phase_stability', 0.9856),
                    'sto_boundary': output.get('sto_intact', True),
                    'time_ms': output.get('processing_time_ms', 10)
                }
            else:
                raise Exception(f"Engine error: {result.stderr}")
                
        finally:
            # Cleanup
            if os.path.exists(input_path):
                os.unlink(input_path)
    
    def simulate_attack(self, attack_type):
        """Simulate attack scenarios"""
        cmd = [
            self.engine_path,
            '--simulate-attack',
            '--type', attack_type,
            '--demo-mode'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            raise Exception(f"Attack simulation failed: {result.stderr}")
    
    def compress(self, data):
        """Interface to AXIOMARC compression"""
        with tempfile.NamedTemporaryFile(delete=False) as input_file:
            input_file.write(data)
            input_path = input_file.name
        
        try:
            cmd = [
                self.engine_path,
                '--compress',
                '--input', input_path,
                '--demo-mode'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                raise Exception(f"Compression failed: {result.stderr}")
                
        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)