import os

css_appends_3 = """

/* Override Demo Card */
.demo-card {
    background: #ffffff;
    border: 1px solid rgba(6, 182, 212, 0.2);
    border-radius: 24px;
    padding: 24px 24px 0 24px;
    margin-bottom: 80px;
    box-shadow: 0 25px 50px -12px rgba(6, 182, 212, 0.25), 0 0 15px rgba(6, 182, 212, 0.05);
    position: relative;
    overflow: hidden;
    backdrop-filter: none;
    display: flex;
    flex-direction: column;
}

.demo-video-area {
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-radius: 16px;
    height: 400px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 0;
}

.play-button-large {
    width: 64px;
    height: 64px;
    background-color: var(--primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    margin: 0;
    cursor: pointer;
    box-shadow: 0 10px 20px rgba(6, 182, 212, 0.4);
    transition: transform 0.2s, box-shadow 0.2s;
}

.play-button-large:hover {
    transform: scale(1.05);
    box-shadow: 0 15px 30px rgba(6, 182, 212, 0.5);
}

.video-placeholder-bottom {
    position: absolute;
    bottom: 12px;
    left: 12px;
    right: 12px;
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(255, 255, 255, 0.95);
    padding: 16px 20px;
    border-radius: 8px;
    font-size: 14px;
    color: var(--text-gray);
    margin-bottom: 0;
    border: 1px solid rgba(6, 182, 212, 0.2);
    box-shadow: 0 10px 15px -3px rgba(6, 182, 212, 0.1), 0 4px 6px -4px rgba(6, 182, 212, 0.1);
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top: none;
    padding-top: 0;
    margin-top: 0;
}

.metric {
    text-align: center;
    border-right: 1px solid rgba(6, 182, 212, 0.3);
    padding: 32px 0;
}

.metric:last-child {
    border-right: none;
}

.metric h3 {
    font-size: 32px;
    font-weight: 800;
    color: var(--primary);
    margin-bottom: 4px;
}

.metric p {
    font-size: 13px;
    color: var(--text-gray);
}

@media (max-width: 900px) {
    .metric {
        border-right: none;
        border-bottom: 1px solid rgba(6, 182, 212, 0.3);
    }
    .metric:last-child {
        border-bottom: none;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_appends_3)

print("Card CSS applied successfully")
