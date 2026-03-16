
css_chatbot = """
/* Chatbot Styles */
.chatbot-container {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 2000;
}

.chatbot-button {
    width: 60px;
    height: 60px;
    background: var(--primary);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    box-shadow: 0 10px 25px rgba(6, 182, 212, 0.4);
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border: none;
}

.chatbot-button:hover {
    transform: scale(1.1) rotate(5deg);
}

.chatbot-window {
    position: absolute;
    bottom: 80px;
    right: 0;
    width: 380px;
    height: 550px;
    background: white;
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    display: none;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid rgba(6, 182, 212, 0.2);
    animation: slideUpChat 0.4s ease-out;
}

@keyframes slideUpChat {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.chatbot-header {
    background: #0b1120;
    color: white;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.header-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.chatbot-header .logo-mini {
    width: 30px;
    height: 30px;
    background: var(--primary);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    font-size: 14px;
}

.close-chat {
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    opacity: 0.7;
}

.chatbot-messages {
    flex: 1;
    padding: 20px;
    overflow-y: auto;
    background: #f8fafc;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.message {
    max-width: 85%;
    padding: 12px 16px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.5;
}

.message.bot {
    background: white;
    color: #1f2937;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.message.user {
    background: var(--primary);
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}

.chatbot-input-area {
    padding: 20px;
    border-top: 1px solid #e2e8f0;
    display: flex;
    gap: 10px;
    background: white;
}

.chatbot-input-area input {
    flex: 1;
    border: 1px solid #e2e8f0;
    padding: 12px 16px;
    border-radius: 12px;
    outline: none;
    font-size: 14px;
}

.chatbot-send-btn {
    background: var(--primary);
    color: white;
    border: none;
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.typing-indicator {
    font-size: 11px;
    color: var(--text-light);
    margin-bottom: 8px;
    display: none;
}

@media (max-width: 480px) {
    .chatbot-window {
        width: calc(100vw - 40px);
        right: -10px;
        height: 70vh;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_chatbot)

print("Chatbot Styles Appended")
