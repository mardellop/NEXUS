(function() {
    // Force scroll to top on reload
    if ('scrollRestoration' in history) {
        history.scrollRestoration = 'manual';
    }
    
    window.addEventListener('load', () => {
        window.scrollTo(0, 0);
    });

    // High-end UI Click Sound (Short & Clean)
    let audioCtx;
    
    function playClick() {
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.05);
        
        gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
        
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        osc.start();
        osc.stop(audioCtx.currentTime + 0.05);
    }

    document.addEventListener('mousedown', (e) => {
        const target = e.target.closest('a, button, .dot, .star, .social-icon');
        if (target) {
            playClick();
        }
    });
})();
