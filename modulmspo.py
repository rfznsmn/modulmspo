import streamlit as st
from datetime import datetime

# --- Page Configuration ---
# NOTE: Make sure 'feldalogo.png' is in the same directory or replace it with a valid URL.
st.set_page_config(
    page_title="E-Modul MSPO FELDA 2.0",
    page_icon="feldalogo.png", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS Styling ---
# Adjusted for better readability, modern feel, and grid support.
st.markdown("""
<style>
/* General layout and background */
.stApp {
    background-color: #F8F8F8; /* Light grey background for professional feel */
}

/* Titles */
h1, h2, h3 {
    color: #1B5E20; /* Dark Green - Primary Brand Color */
    font-family: 'Montserrat', sans-serif;
}
.st-emotion-cache-18ni2g6 { /* Targeting main area padding */
    padding-top: 2rem;
    padding-left: 5rem;
    padding-right: 5rem;
}

/* Announcement cards (Use st.info/st.success in new code, but keeping card style for flexibility) */
.announcement-card {
    background: white;
    border-radius: 12px; /* Slightly rounder corners */
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08); /* Stronger but cleaner shadow */
    transition: transform 0.2s ease;
    height: 100%; /* Important for columns to align */
}
.announcement-card h4 {
    color: #004D40; /* Darker title for contrast */
    margin-top: 0;
}
.announcement-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}

/* Module cards - Modified to look like clean button areas */
.principle-card {
    background-color: white;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    border-left: 6px solid #4CAF50; /* Brighter green accent */
    margin-bottom: 1.5rem;
    cursor: pointer; /* Suggests clickability */
    transition: all 0.2s ease;
    min-height: 120px;
}
.principle-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
}
.principle-title {
    font-weight: 700;
    font-size: 1.2rem;
    color: #2E7D32;
    margin-bottom: 0.5rem;
}

/* Streamlit Buttons (Standard style is preferred but keeping custom for a strong brand look) */
.stButton>button {
    width: 100%;
    background: #4CAF50; /* A pleasant green */
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.8rem;
    font-size: 1rem;
    font-weight: 600;
    margin-top: 10px; /* Space below card */
    transition: background 0.3s ease, transform 0.1s ease;
}
.stButton>button:hover {
    background: #388E3C;
    transform: none; /* Removed translate for standard button feel */
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #E8F5E9; /* Very light green */
    padding-top: 2rem;
}
.sidebar-title {
    color: #1B5E20;
    font-weight: bold;
    font-size: 1.2rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# --- Header Section (Use st.image for better integration) ---
st.image("https://via.placeholder.com/300x50/1B5E20/FFFFFF?text=FELDA+GROUP+LOGO", width=250)
st.title("🌿 E-Modul MSPO FELDA 2.0")
st.markdown(
    "### Portal Latihan Pensijilan **_Malaysian Sustainable Palm Oil (MSPO) 2.0_**"
)

st.info(
    "Selamat datang ke **E-Modul MSPO FELDA 2.0** — satu platform latihan digital bagi memantapkan pemahaman dan pelaksanaan prinsip-prinsip MSPO di semua rancangan FELDA. Gunakan menu di bawah untuk akses modul."
)

st.markdown("---")

# --- Announcement Board (Updated Content) ---
st.markdown("## 📢 Pengumuman Terkini")

# Store the multi-line content using HTML lists for better formatting
announcements = [
    {
        "date": "1 November 2025",
        "title": "FELDA Capai 100% Pensijilan MSPO! 🎉",
        "content": "Tahniah kepada semua rancangan atas kejayaan ini. FELDA kini berjaya mencapai **100% pensijilan MSPO** bagi semua rancangan, hasil usaha berterusan semua pihak."
    },
    {
        "date": "November 2025",
        "title": "📅 Jadual Audit Dalaman",
        "content": """
        Audit dalaman akan dijalankan seperti berikut:
        <ul style="list-style-type: none; padding-left: 0.5rem;">
            <li><span style="font-weight: bold;">Gugusan Jengka 18:</span> 5–7 Nov 2025</li>
            <li><span style="font-weight: bold;">Gugusan Maokil:</span> 11–13 Nov 2025</li>
            <li><span style="font-weight: bold;">Gugusan Segamat:</span> 18–20 Nov 2025</li>
        </ul>
        <p style='margin-top: 0.5rem;'>Sila pastikan semua dokumentasi lengkap sebelum tarikh audit.</p>
        """
    },
    {
        "date": "November 2025",
        "title": "📅 Jadual Audit Luaran",
        "content": """
        <ul style="list-style-type: none; padding-left: 0.5rem;">
            <li>Tiada audit luaran MSPO dijadualkan pada bulan ini.</li>
            <li>Audit Seterusnya: <span style="font-weight: bold; color: #388E3C;">Januari 2026</span> (Gugusan Kuantan)</li>
        </ul>
        <p style='margin-top: 0.5rem;'>Teruskan mengekalkan pematuhan kepada standard MSPO. Semak status di bahagian Rujukan.</p>
        """
    }
]

# Create a 2-column layout for announcements
cols_announcements = st.columns(2)
for i, a in enumerate(announcements):
    col = cols_announcements[i % 2] # Cycle through columns 0 and 1
    with col:
        # NOTE: The content is now rendered directly within the announcement-card HTML.
        st.markdown(f"""
        <div class="announcement-card">
            <h4>{a['title']}</h4>
            <p style='color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;'>{a['date']}</p>
            {a['content']} 
        </div>
        """, unsafe_allow_html=True)
        # Add a subtle separator for the third announcement if it's the last one
        if i == len(announcements) - 1 and len(announcements) % 2 != 0:
             st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- Module Links (Using st.columns for professional grid) ---
st.markdown("## 📚 Modul MSPO 2.0 - Akses Sumber")
st.markdown("Sila klik butang **Akses Modul** untuk melihat dokumen rujukan di OneDrive/Sharepoint.")

modules = {
    "P1": {
        "title": "Komitmen dan Tanggungjawab Pengurusan",
        "icon": "🤝",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FP1%20Komitmen%20dan%20Tanggungjawab%20Pengurusan&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
    },
    "P2": {
        "title": "Ketelusan",
        "icon": "📄",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FP2%20Ketelusan&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
    },
    "P3": {
        "title": "Pematuhan Kepada Undang-Undang",
        "icon": "⚖️",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FP3%20Pematuhan%20kepada%20Keperluan%20Undang%2Dundang&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
    },
    "P4": {
        "title": "Tanggungjawab Sosial & Keselamatan",
        "icon": "👨‍🏭",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FP4%20Tanggungjawab%20Sosial%2C%20Keselamatan%2C%20Kesihatan%20dan%20Keadaan%20Pekerjaan&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
    },
    "P5": {
        "title": "Alam Sekitar & Penjagaan Ekosistem",
        "icon": "🌳",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FP5%20Alam%20Sekitar%2C%20Sumber%20Asli%2C%20Biodiversiti%20dan%20Perkhidmatan%20Ekosistem&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
    },
    "MANUAL": {
        "title": "Dokumen Manual, Polisi dan Prosedur",
        "icon": "📑",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FP6%20Polisi%20dan%20Prosedur&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
     },
    "ICS": {
        "title": "Internal Control System-Group Manager",
        "icon": "🗂️",
        "link": "https://feldagov-my.sharepoint.com/personal/jk_felda_feldagov_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjk%5Ffelda%5Ffeldagov%5Fonmicrosoft%5Fcom%2FDocuments%2FSupporting%20Documents%20MSPO%202%2E0%2FInternal%20Control%20System%20%28ICS%29&viewid=4533d408%2D9220%2D4295%2Db459%2D4fc98a267c5c&ga=1",
    }
}

# Create a grid of 2 columns for the module cards
cols_modules = st.columns(2)
module_keys = list(modules.keys())

for i, key in enumerate(module_keys):
    module = modules[key]
    col = cols_modules[i % 2] # Cycle through columns 0 and 1

    with col:
        # Principle Card (uses markdown for visual)
        st.markdown(f"""
        <div class="principle-card">
            <div class="principle-title">{module['icon']} {key}: {module['title']}</div>
        </div>
        """, unsafe_allow_html=True)

        # Standard Streamlit button (Recommended over complex HTML buttons)
        if st.button(f"📥 Akses Modul {key}", key=f"btn_{key}"):
            st.web_browser(module['link'])

st.markdown("---")


# --- Footer ---
st.markdown("## 📞 Hubungi Kami")

col_email, col_copyright = st.columns([2, 1])

with col_email:
    st.markdown("""
    Untuk sebarang pertanyaan berkaitan E-Modul MSPO FELDA:
    * **Email**: kelestarian.f@felda.net.my
    * **Hotline**: +603-21912191
    """)

with col_copyright:
    st.markdown(f"""
    <div style="text-align: right; color: #666; font-size: 0.85rem;">
    © {datetime.now().year} FELDA | Malaysian Sustainable Palm Oil (MSPO)
    </div>
    """, unsafe_allow_html=True)


# --- Sidebar (More structured and useful) ---
with st.sidebar:
    # Use a solid image/color for the header logo
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/250x70/1B5E20/FFFFFF?text=FELDA+MSPO+2.0", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sidebar-title">📖 Panduan Penggunaan</div>', unsafe_allow_html=True)
    st.info("""
    1. **Pilih Prinsip:** Tentukan modul MSPO yang ingin dipelajari (P1 hingga P5).
    2. **Akses Modul:** Klik butang **'Akses Modul'** untuk setiap prinsip.
    3. **Tinjauan:** Dokumen rujukan akan dibuka di pelayar baru (OneDrive/SharePoint).
    """)

    st.markdown('<div class="sidebar-title">🌱 Tentang MSPO</div>', unsafe_allow_html=True)
    st.success("""
    **MSPO (Malaysian Sustainable Palm Oil)** adalah skim pensijilan nasional yang memastikan pengeluaran minyak sawit secara **mampan** melalui amalan terbaik, pematuhan undang-undang, dan tanggungjawab sosial.
    """)

    # Current Date for reference
    st.markdown(f"""
    <div style="margin-top: 2rem; border-top: 1px solid #ddd; padding-top: 1rem;">
    <p style='font-size: 0.8rem; color: #666;'>Tarikh Terkini: {datetime.now().strftime("%d %B %Y")}</p>
    </div>
    """, unsafe_allow_html=True)
