
// AI Guide - Frontend Logic
(function () {
    console.log('AI Guide: Initializing...');

    const API_ENDPOINT = '/api/guide/track/';
    const SESSION_KEY = localStorage.getItem('site_manager_session') || generateUUID();
    localStorage.setItem('site_manager_session', SESSION_KEY);

    let idleTimer;
    let pageStartTime = Date.now();

    // Generate UUID
    function generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
            var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    // Track Event
    function trackEvent(eventType, data = {}) {
        const payload = {
            session_key: SESSION_KEY,
            event_type: eventType,
            path: window.location.pathname,
            timestamp: new Date().toISOString(),
            data: data
        };

        // Use sendBeacon for reliability on unload
        if (navigator.sendBeacon) {
            const blob = new Blob([JSON.stringify(payload)], { type: 'application/json' });
            navigator.sendBeacon(API_ENDPOINT, blob);
        } else {
            fetch(API_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(payload)
            }).catch(err => console.error('Guide Error:', err));
        }
    }

    // Get CSRF Token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Listeners
    window.addEventListener('load', () => trackEvent('page_view'));

    // Idle Tracking (30s)
    document.addEventListener('mousemove', resetIdleTimer);
    document.addEventListener('keypress', resetIdleTimer);

    function resetIdleTimer() {
        clearTimeout(idleTimer);
        idleTimer = setTimeout(() => trackEvent('idle', { duration: 30 }), 30000);
    }

    // Element Clicks (Buy Buttons)
    document.addEventListener('click', (e) => {
        if (e.target.closest('.btn-buy') || e.target.closest('.plan-card')) {
            trackEvent('click', { target: 'buy_button', text: e.target.innerText });
        }
    });

    // Time on Page (every 1 min)
    setInterval(() => {
        const timeSpent = Math.floor((Date.now() - pageStartTime) / 1000);
        trackEvent('time_on_page', { seconds: timeSpent });
    }, 60000);

    // Render Guide UI
    function renderGuide() {
        const container = document.createElement('div');
        container.id = 'ai-guide-container';
        container.innerHTML = `
            <div id="guide-bubble" class="guide-bubble" style="display: none;">
                <span id="guide-message">Hi! Need help finding a roadmap?</span>
                <div id="guide-actions" class="guide-actions"></div>
                <button onclick="closeGuide()" class="guide-close">&times;</button>
            </div>
            <div id="guide-avatar" class="guide-avatar" onclick="toggleGuide()">
                <img src="/static/images/bot-avatar.png" alt="AI Guide" onerror="this.src='https://ui-avatars.com/api/?name=AI&background=6366f1&color=fff'">
            </div>
        `;
        document.body.appendChild(container);

        // Add Styles
        const style = document.createElement('style');
        style.textContent = `
            #ai-guide-container {
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 10000;
                font-family: 'Inter', sans-serif;
            }
            .guide-avatar {
                width: 60px;
                height: 60px;
                background: linear-gradient(135deg, #6366f1, #a855f7);
                border-radius: 50%;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
                display: flex;
                align-items: center;
                justify-content: center;
                transition: transform 0.3s;
                overflow: hidden;
                border: 2px solid white;
            }
            .guide-avatar:hover { transform: scale(1.1); }
            .guide-avatar img { width: 100%; height: 100%; object-fit: cover; }
            
            .guide-bubble {
                position: absolute;
                bottom: 75px;
                right: 0;
                background: white;
                color: #0f172a;
                padding: 16px;
                border-radius: 16px;
                width: 280px;
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
                animation: slideIn 0.3s ease;
                border: 1px solid #e2e8f0;
            }
            .guide-bubble::after {
                content: '';
                position: absolute;
                bottom: -8px;
                right: 24px;
                border-width: 8px 8px 0;
                border-style: solid;
                border-color: white transparent transparent;
                filter: drop-shadow(0 2px 1px rgba(0,0,0,0.05));
            }
            #guide-message {
                font-size: 0.95rem;
                line-height: 1.5;
                font-weight: 500;
                color: #334155;
            }
            .guide-actions {
                display: flex;
                flex-direction: column;
                gap: 8px;
                margin-top: 12px;
            }
            .guide-btn {
                padding: 8px 12px;
                border-radius: 8px;
                font-size: 0.85rem;
                font-weight: 600;
                text-align: center;
                cursor: pointer;
                text-decoration: none;
                transition: all 0.2s;
                border: 1px solid transparent;
            }
            .guide-btn-primary {
                background: #6366f1;
                color: white;
            }
            .guide-btn-primary:hover {
                background: #4f46e5;
                transform: translateY(-1px);
            }
            .guide-btn-secondary {
                background: #f1f5f9;
                color: #475569;
                border-color: #e2e8f0;
            }
            .guide-btn-secondary:hover {
                background: #e2e8f0;
                color: #1e293b;
            }
            .guide-close {
                position: absolute;
                top: 8px;
                right: 8px;
                background: none;
                border: none;
                font-size: 18px;
                cursor: pointer;
                color: #94a3b8;
                width: 24px;
                height: 24px;
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 50%;
            }
            .guide-close:hover { background: #f1f5f9; color: #64748b; }
            @keyframes slideIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        `;
        document.head.appendChild(style);
    }

    // Initialize UI
    renderGuide();

    // Poll for Suggestions (Every 30s)
    setInterval(() => {
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has('debug_guide')) {
            // Force fetch for debugging
            fetchSuggestions();
        } else {
            fetchSuggestions();
        }
    }, 20000); // 20s

    function fetchSuggestions() {
        fetch('/api/guide/suggest/?session=' + SESSION_KEY)
            .then(res => res.json())
            .then(data => {
                if (data.show_message) {
                    showGuideMessage(data.message, data.actions);
                }
            })
            .catch(() => { });
    }

    // Expose helpers
    window.toggleGuide = function () {
        const bubble = document.getElementById('guide-bubble');
        const isHidden = bubble.style.display === 'none';

        if (isHidden) {
            // If opening, check if we need to show the main menu (if no active message)
            // Or just always show main menu if it was closed?
            // Let's always reset to main menu on fresh open for consistency
            renderMainMenu();
            bubble.style.display = 'block';
            trackEvent('guide_open');
        } else {
            bubble.style.display = 'none';
            trackEvent('guide_close');
        }
    };

    window.closeGuide = function () {
        document.getElementById('guide-bubble').style.display = 'none';
    };

    // --- Menu Logic ---

    function renderMainMenu() {
        showGuideMessage("Hi! 👋 How can I help you today?", [
            { label: '🚀 Find a Roadmap', type: 'action', action: 'trigger_modal', data: 'roadmapSuggestorModal' },
            { label: '✨ View Features', type: 'action', action: 'show_features' },
            { label: '📞 Contact Support', type: 'link', url: '/contact/' }
        ]);
        // Remove auto-hide for menu
        clearTimeout(window.guideAutoHideTimer);
    }

    function renderFeaturesList() {
        showGuideMessage("Here's what I can do for you:", [
            { label: '📚 Structured Roadmaps', type: 'link', url: '/roadmaps/' },
            { label: '🤖 AI Mentor', type: 'link', url: '/ai/chat/' },
            { label: '🏆 Gamification & XP', type: 'link', url: '/dashboard/' },
            { label: '⬅️ Back to Menu', type: 'action', action: 'show_menu' }
        ]);
        // Remove auto-hide for menu
        clearTimeout(window.guideAutoHideTimer);
    }

    window.showGuideMessage = function (msg, actions = []) {
        const bubble = document.getElementById('guide-bubble');
        document.getElementById('guide-message').innerText = msg;

        const actionsContainer = document.getElementById('guide-actions');
        actionsContainer.innerHTML = '';

        if (actions && actions.length > 0) {
            actions.forEach((action, index) => {
                const btn = document.createElement('a');
                // Style first button as primary, others as secondary
                btn.className = index === 0 ? 'guide-btn guide-btn-primary' : 'guide-btn guide-btn-secondary';
                btn.innerText = action.label;

                if (action.type === 'link') {
                    btn.href = action.url;
                } else if (action.type === 'action') {
                    btn.href = '#';
                    btn.onclick = (e) => {
                        e.preventDefault();
                        handleGuideAction(action);
                    };
                }
                actionsContainer.appendChild(btn);
            });
        }

        bubble.style.display = 'block';

        // Auto hide only if no actions (actions require interaction)
        // We use a global timer so we can clear it if needed
        if (!actions || actions.length === 0) {
            window.guideAutoHideTimer = setTimeout(() => { bubble.style.display = 'none'; }, 10000);
        }
    };

    function handleGuideAction(action) {
        if (action.action === 'quiz') {
            window.location.href = '/ai/chat/?roadmap_id=&initial_msg=Create a quiz for ' + action.data;
        } else if (action.action === 'enroll') {
            enrollUser(action.data);
        } else if (action.action === 'trigger_modal') {
            const modalId = action.data;
            const modalEl = document.getElementById(modalId);
            if (modalEl && window.bootstrap) {
                const modal = new bootstrap.Modal(modalEl);
                modal.show();
            } else {
                console.error("Modal not found or Bootstrap missing");
                alert("Could not open the roadmap finder. Please try refreshing.");
            }
        } else if (action.action === 'show_features') {
            renderFeaturesList();
        } else if (action.action === 'show_menu') {
            renderMainMenu();
        }
    }

    function enrollUser(roadmapId) {
        fetch('/api/guide/ext/enroll/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ roadmap_id: roadmapId })
        })
            .then(res => res.json())
            .then(data => {
                alert(data.message);
                if (data.status === 'success') location.reload();
            });
    }

})();
