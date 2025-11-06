# modulmspo_modern_responsive.py
import streamlit as st
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="E-Modul MSPO FELDA 2.0",
    page_icon="feldalogo.png",  # FELDA logo (header favicon)
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Responsive + Modern CSS ---
st.markdown(
    """
    <style>
    /* --- Base / App --- */
    :root{
        --felda-orange: #FF6600;
        --felda-dark: #2B2B2B;
        --felda-earth: #6B4B2A;
        --felda-green: #1B5E20;
        --bg: #FAFAF9;
        --card-bg: #FFFFFF;
        --muted: #6B6B6B;
    }

    .stApp {
        background-color: var(--bg);
        color: var(--felda-dark);
        font-family: "Inter", "Helvetica Neue", Arial, sans-serif;
    }

    /* --- Header / logo --- */
    .header-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 0.5rem 1rem;
        margin-bottom: 0.25rem;
    }
    .header-logo {
        width: 220px;
        max-width: 35%;
        height: auto;
    }
    .header-title {
        margin: 0;
        padding: 0;
    }
    .header-sub {
        margin-top: -0.25rem;
        color: var(--muted);
        font-size: 0.95rem;
    }

    /* --- Cards --- */
    .card {
        background: var(--card-bg);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 6px 18px rgba(16, 24, 40, 0.08);
        border: 1px solid rgba(16,24,40,0.03);
    }

    .announcement-card {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .announcement-card h4 {
        margin: 0 0 0.25rem 0;
        color: var(--felda-earth);
        font-size: 1.05rem;
    }
    .announcement-card p.date {
        margin: 0 0 0.5rem 0;
        color: var(--muted);
        font-size: 0.88rem;
    }

    .principle-card {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        justify-content: space-between;
        padding: 1rem;
        border-radius: 10px;
        min-height: 110px;
    }
    .principle-title {
        font-weight: 700;
        color: var(--felda-green);
        font-size: 1rem;
    }
    .principle-desc {
        color: var(--muted);
        font-size: 0.95rem;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
        font-weight: 700;
        font-size: 0.95rem;
        border: none;
    }
    .link-btn {
        background: linear-gradient(90deg, var(--felda-orange), #e85a00);
        color: white !important;
        border: none !important;
        box-shadow: 0 6px 14px rgba(255,102,0,0.15);
    }

    /* Footer small text */
    .footer-small {
        color: var(--muted);
        font-size: 0.85rem;
    }

    /* Sidebar tweaks */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #fff, #FAFBFA);
        padding: 1rem 0.75rem 2rem 0.75rem;
    }
    .sidebar-logo {
        width: 160px;
        max-width: 100%;
        margin: 0 auto 0.5rem auto;
        display: block;
    }
    .sidebar-title {
        color: var(--felda-green);
        font-weight: 700;
        margin-bottom: 0.25rem;
        font-size: 0.98rem;
    }

    /* --- Responsive behavior --- */
    /* Make cards and buttons full width on small screens and adjust padding */
    @media (max-width: 900px) {
        .header-logo { width: 160px; }
        .header-row { padding: 0.5rem 0.5rem; gap: 0.6rem; }
        .stApp { padding: 0; }
    }

    @media (max-width: 768px) {
        .header-logo { width: 120px; }
        .header-title { font-size: 1.05rem; }
        .header-sub { font-size: 0.9rem; }

        /* Force streamlit columns to behave like stacked blocks */
        .css-1lcbmhc { /* row block wrapper - fallback, may vary */
            flex-direction: column !important;
        }
        .css-1d391kg, .css-12oz5g7 { /* common column class fallbacks */
            width: 100% !important;
            min-width: 100% !important;
        }

        .announcement-card, .principle-card, .card {
            width: 100% !important;
            box-sizing: border-box;
        }

        .stButton>button {
            width: 100% !important;
        }
    }

    /* Accessibility: ensure text contrast and readable sizes */
    h1, h2, h3, h4, p, li, a, span, div {
        color: var(--felda-dark) !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header with FELDA logo (top) ---
# Official FELDA logo (white background, orange "f") - hosted on FELDA website
FELDA_LOGO = "https://felda.gov.my/images/photo/logo/logo.png"

# Use a header row: logo + title
st.markdown(
    f"""
    <div class="header-row">
        <img src="{FELDA_LOGO}" class="header-logo" alt="FELDA logo" />
        <div>
            <h1 class="header-title">🌿 E-Modul MSPO FELDA 2.0</h1>
            <div class="header-sub">Portal Latihan Pensijilan — Malaysian Sustainable Palm Oil (MSPO) 2.0</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# --- Intro / Info ---
st.info(
    "Selamat datang ke **E-Modul MSPO FELDA 2.0** — platform latihan digital untuk meningkatkan pemahaman dan pelaksanaan prinsip MSPO. Gunakan butang di bawah setiap modul untuk membuka sumber di SharePoint/OneDrive."
)

st.markdown("## 📢 Pengumuman Terkini")

# Announcement data (kept simple and readable)
announcements = [
    {
        "date": "1 November 2025",
        "title": "FELDA Capai 100% Pensijilan MSPO! 🎉",
        "content": "Tahniah kepada semua rancangan atas kejayaan ini. FELDA kini berjaya mencapai 100% pensijilan MSPO bagi semua rancangan, hasil usaha berterusan semua pihak."
    },
    {
        "date": "5–7 Nov 2025",
        "title": "Audit Dalaman - Gugusan Jengka 18",
        "content": "Sila pastikan semua dokumentasi lengkap sebelum tarikh audit. Rujuk checklist dalaman dan sediakan semua bukti objektif yang berkaitan."
    },
    {
        "date": "18–20 Nov 2025",
        "title": "Audit Luaran - Gugusan Triang",
        "content": "Pastikan akses pintu masuk log dan rekod latihan pekerja dikemaskini."
    }
]

# Render announcements in two columns on wider screens, stacked on mobile
cols = st.columns(2)
for i, ann in enumerate(announcements):
    col = cols[i % 2]
    with col:
        st.markdown(
            f"""
            <div class="card announcement-card">
                <h4>{ann['title']}</h4>
                <p class="date">{ann['date']}</p>
                <div style="color: #444; font-size:0.95rem;">{ann['content']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("---")

# --- Module Links Section ---
st.markdown("## 📚 Modul MSPO 2.0 — Akses Sumber")
st.mark
