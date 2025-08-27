from flask import Flask, render_template, request, jsonify
import subprocess
import json
import hashlib
import time
from quantum_engine import QuantumEngine
from license_validator import validate_license

app = Flask(__name__)
quantum_engine = QuantumEngine()

@app.route('/')
def demo_home():
    return render_template('index.html')

@app.route('/api/encrypt', methods=['POST'])
def encrypt_message():
    try:
        # Validate license first
        if not validate_license(request.remote_addr):
            return jsonify({'error': 'Demo license required'}), 403
        
        data = request.json
        message = data.get('message', '')
        
        # Call AXIOMARC engine
        result = quantum_engine.encrypt(message)
        
        return jsonify({
            'success': True,
            'coherence': result['coherence'],
            'phase_stability': result['phase_stability'],
            'sto_boundary': result['sto_boundary'],
            'encryption_time': result['time_ms']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/simulate_attack', methods=['POST'])
def simulate_attack():
    try:
        data = request.json
        attack_type = data.get('attack_type', '')
        
        # Simulate attack on quantum system
        result = quantum_engine.simulate_attack(attack_type)
        
        return jsonify({
            'attack_detected': result['detected'],
            'detection_time_ms': result['detection_time'],
            'mitigation_applied': result['mitigated'],
            'system_status': result['status']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/compress', methods=['POST'])
def compress_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
            
        file = request.files['file']
        original_size = len(file.read())
        file.seek(0)  # Reset file pointer
        
        # Call AXIOMARC compression
        result = quantum_engine.compress(file.read())
        
        return jsonify({
            'original_size': original_size,
            'compressed_size': result['compressed_size'],
            'compression_ratio': result['ratio'],
            'quality_metrics': result['quality'],
            'reconstruction_perfect': result['perfect_fidelity']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)