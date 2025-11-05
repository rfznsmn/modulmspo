import streamlit as st
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="E-Modul MSPO FELDA 2.0",
    page_icon="feldalogo.png",
    layout="wide",
)

# --- Custom CSS Styling ---
st.markdown("""
<style>
/* General layout */
.main {
    padding: 1.5rem 3rem;
    background-color: #fafafa;
    font-family: "Segoe UI", sans-serif;
}

/* Title styling */
h1, h2, h3 {
    color: #1B5E20;
}

/* Announcement cards */
.announcement-card {
    background: white;
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #2E7D32, #43A047);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.9rem;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #1B5E20, #2E7D32);
    transform: translateY(-2px);
}

/* Module cards */
.principle-card {
    background-color: white;
    padding: 1.3rem 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border-left: 6px solid #2E7D32;
    margin-bottom: 1.5rem;
    transition: transform 0.2s ease;
}
.principle-card:hover {
    transform: translateY(-3px);
}
.principle-title {
    font-weight: 600;
    font-size: 1.1rem;
    color: #2E7D32;
    margin-bottom: 0.6rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #E8F5E9;
}
.sidebar-title {
    color: #1B5E20;
    font-weight: bold;
    font-size: 1.1rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.title("🌿 E-Modul MSPO FELDA 2.0")
st.markdown("### Portal Latihan Pensijilan *Malaysian Sustainable Palm Oil (MSPO) 2.0*")
st.markdown("---")

st.markdown("""
Selamat datang ke **E-Modul MSPO FELDA 2.0** — satu platform latihan digital bagi memantapkan pemahaman 
dan pelaksanaan prinsip-prinsip MSPO di semua rancangan FELDA.
""")

st.markdown("---")

# --- Announcement Board ---
st.markdown("## 📢 Pengumuman")

announcements = [
    {
        "date": "1 November 2025",
        "title": "FELDA Berjaya Capai 100% Pensijilan MSPO! 🎉",
        "content": """Tahniah kepada semua rancangan atas kejayaan ini.  
FELDA kini berjaya mencapai **100% pensijilan MSPO** bagi semua rancangan, hasil usaha berterusan semua pihak."""
    },
    {
        "date": "November 2025",
        "title": "📅 Jadual Internal Audit November",
        "content": """Audit dalaman akan dijalankan seperti berikut:
        
• Gugusan Jengka 18: 5–7 November 2025

• Gugusan Maokil: 11–13 November 2025  

Sila pastikan semua dokumentasi lengkap sebelum tarikh audit."""
    },
    {
        "date": "November 2025",
        "title": "📅 Jadual External Audit November",
        "content": """Tiada audit luaran MSPO dijadualkan pada bulan ini.  
Teruskan mengekalkan pematuhan kepada standard MSPO."""
    }
]

for a in announcements:
    with st.container():
        st.markdown(f"""
        <div class="announcement-card">
            <h4>{a['title']}</h4>
            <p><em>{a['date']}</em></p>
            <p>{a['content']}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- Module Links ---
st.markdown("## 📘 Modul Latihan")

modules = {
    "Prinsip 1": {
        "title": "Komitmen dan Tanggungjawab Pengurusan",
        "link": "https://onedrive.live.com/your-link-here-principle-1",
    },
    "Prinsip 2": {
        "title": "Ketelusan",
        "link": "https://onedrive.live.com/your-link-here-principle-2",
    },
    "Prinsip 3": {
        "title": "Pematuhan Kepada Undang-Undang dan Perkara Berkaitan",
        "link": "https://onedrive.live.com/your-link-here-principle-3",
    },
    "Prinsip 4": {
        "title": "Tanggungjawab Sosial, Kesihatan, Keselamatan dan Terma Pekerjaan",
        "link": "https://onedrive.live.com/your-link-here-principle-4",
    },
    "Prinsip 5": {
        "title": "Alam Sekitar, Sumber Asli, Kepelbagaian Biologi dan Penjagaan Ekosistem",
        "link": "https://onedrive.live.com/your-link-here-principle-5",
    },
    "Rujukan": {
        "title": "Dokumen Manual, Polisi dan Prosedur",
        "link": "https://onedrive.live.com/your-link-here-rujukan",
    }
}

cols = st.columns(3)
for idx, (key, module) in enumerate(modules.items()):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="principle-card">
            <div class="principle-title">📗 {key}: {module['title']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"📥 Akses {key}", key=key):
            st.markdown(f"[Buka Modul 🔗]({module['link']})", unsafe_allow_html=True)

st.markdown("---")

# --- Footer ---
st.markdown("""
### 📞 Hubungi Kami
Untuk sebarang pertanyaan berkaitan E-Modul MSPO FELDA:
- **Email**: training@felda.gov.my  
- **Telefon**: +60 3-XXXX XXXX

---
© 2025 FELDA | Malaysian Sustainable Palm Oil (MSPO)
""")

# --- Sidebar ---
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/2E7D32/FFFFFF?text=FELDA+MSPO", use_column_width=True)
    st.markdown('<div class="sidebar-title">📖 Panduan Penggunaan</div>', unsafe_allow_html=True)
    st.markdown("""
    1. Pilih prinsip yang ingin dipelajari  
    2. Klik butang **Akses**  
    3. Modul akan dibuka di OneDrive  
    4. Lihat atau muat turun modul  
    """)
    st.markdown('<div class="sidebar-title">🌱 Tentang MSPO</div>', unsafe_allow_html=True)
    st.markdown("""
    **MSPO (Malaysian Sustainable Palm Oil)** memastikan pengeluaran minyak sawit secara mampan melalui amalan terbaik, pematuhan undang-undang, dan tanggungjawab sosial.
    """)
