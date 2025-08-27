class QuantumSecurityDemo {
    constructor() {
        this.coherenceLevel = 0.9963;
        this.phaseStability = 0.9856;
        this.stoIntegrity = true;
        this.isUnderAttack = false;
        
        this.initializeDemo();
    }
    
    initializeDemo() {
        this.startPhaseVisualization();
        this.startMetricsUpdates();
        this.logMessage('quantum', 'Quantum-inspired protection system online');
        this.logMessage('traditional', 'Traditional encryption active');
    }
    
    startPhaseVisualization() {
        const canvas = document.getElementById('phase-canvas');
        const ctx = canvas.getContext('2d');
        let time = 0;
        
        const drawPhase = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw coherence waves
            ctx.strokeStyle = '#00ff66';
            ctx.lineWidth = 2;
            ctx.beginPath();
            
            for (let x = 0; x < canvas.width; x++) {
                const y = canvas.height/2 + 
                         Math.sin((x + time) * 0.02) * 30 * this.coherenceLevel +
                         Math.sin((x + time) * 0.05) * 15 * this.phaseStability;
                
                if (x === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.stroke();
            
            time += 2;
            requestAnimationFrame(drawPhase);
        };
        
        drawPhase();
    }
    
    startMetricsUpdates() {
        setInterval(() => {
            if (!this.isUnderAttack) {
                // Natural fluctuations
                this.coherenceLevel = 0.9963 + (Math.random() - 0.5) * 0.001;
                this.phaseStability = 0.9856 + (Math.random() - 0.5) * 0.002;
            }
            
            this.updateMetricsDisplay();
        }, 100);
    }
    
    updateMetricsDisplay() {
        document.getElementById('coherence-value').textContent = 
            (this.coherenceLevel * 100).toFixed(2) + '%';
        document.getElementById('phase-value').textContent = 
            (this.phaseStability * 100).toFixed(2) + '%';
        
        // Update coherence bar
        const bar = document.getElementById('coherence-bar');
        bar.style.width = (this.coherenceLevel * 100) + '%';
        
        if (this.coherenceLevel < 0.95) {
            bar.style.background = 'linear-gradient(45deg, #ff6600, #ff0033)';
        } else {
            bar.style.background = 'linear-gradient(45deg, #00ff66, #0066ff)';
        }
    }
    
    logMessage(system, message) {
        const logContainer = document.getElementById(`${system}-messages`);
        const timestamp = new Date().toLocaleTimeString();
        const logEntry = document.createElement('div');
        logEntry.innerHTML = `<strong>${timestamp}:</strong> ${message}`;
        logContainer.appendChild(logEntry);
        logContainer.scrollTop = logContainer.scrollHeight;
    }
}

// Attack Simulation Functions
function simulateTraditionalAttack(attackType) {
    const demo = window.quantumDemo;
    
    switch(attackType) {
        case 'mitm':
            demo.logMessage('traditional', '🚨 Man-in-the-middle attack detected');
            setTimeout(() => {
                document.getElementById('traditional-status').className = 'protection-status compromised';
                document.getElementById('traditional-status').textContent = 'COMPROMISED - MITM ATTACK';
                demo.logMessage('traditional', '❌ Encryption bypassed - data intercepted');
            }, 2000);
            break;
            
        case 'quantum':
            demo.logMessage('traditional', '🚨 Quantum computer attack initiated');
            setTimeout(() => {
                document.getElementById('traditional-status').className = 'protection-status compromised';
                document.getElementById('traditional-status').textContent = 'COMPROMISED - QUANTUM ATTACK';
                demo.logMessage('traditional', '❌ RSA keys factored - system compromised');
            }, 3000);
            break;
    }
}

function simulateQuantumAttack(attackType) {
    const demo = window.quantumDemo;
    demo.isUnderAttack = true;
    
    switch(attackType) {
        case 'phase':
            demo.logMessage('quantum', '🚨 Phase disruption attack detected');
            demo.coherenceLevel = 0.85;
            demo.phaseStability = 0.75;
            
            setTimeout(() => {
                demo.logMessage('quantum', '🛡️ Quantum correction protocols activated');
                demo.logMessage('quantum', '✅ Phase coherence restored - attack neutralized');
                demo.coherenceLevel = 0.9963;
                demo.phaseStability = 0.9856;
                demo.isUnderAttack = false;
            }, 3000);
            break;
            
        case 'coherence':
            demo.logMessage('quantum', '🚨 Coherence disruption detected');
            demo.logMessage('quantum', '🔍 STO boundary analysis initiated');
            demo.logMessage('quantum', '✅ Attack vector isolated and neutralized');
            break;
    }
}

// Compression Demo
function startCompression() {
    window.location.href = '/compression-demo';
}

// Schedule Call
function scheduleCall() {
    window.open('https://calendly.com/your-calendar', '_blank');
}

// Initialize demo when page loads
window.addEventListener('load', () => {
    window.quantumDemo = new QuantumSecurityDemo();
});