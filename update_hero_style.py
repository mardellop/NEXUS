import os

css_appends_10 = """

/* Hero UI Refinement (Video Container) */
.video-container {
    background: #1a1a1a !important;
    border: 1px solid rgba(6, 182, 212, 0.4);
    border-radius: 12px !important;
    margin-top: 40px;
    margin-bottom: 64px !important;
    box-shadow: 0 0 40px rgba(6, 182, 212, 0.2), 0 0 80px rgba(6, 182, 212, 0.1) !important;
    position: relative;
    overflow: hidden;
}

.video-placeholder {
    font-size: 42px !important;
    font-weight: 700 !important;
    letter-spacing: -1px;
    color: var(--primary) !important;
    text-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
}

.scroll-indicator {
    display: flex;
    justify-content: center;
    margin-top: -32px;
    margin-bottom: 64px;
}

.mouse {
    width: 24px;
    height: 36px;
    border: 2px solid var(--primary);
    border-radius: 12px;
    position: relative;
    display: flex;
    justify-content: center;
}

.mouse::after {
    content: '';
    width: 2px;
    height: 6px;
    background-color: var(--primary);
    border-radius: 2px;
    position: absolute;
    top: 6px;
    animation: scroll 1.5s infinite;
}

@keyframes scroll {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(12px); opacity: 0; }
}

/* Adjust demo section padding */
.demo-section {
    padding-top: 40px !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_10)

print("Hero Style Applied")
