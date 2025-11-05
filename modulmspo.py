import streamlit as st

# Page configuration
st.set_page_config(
    page_title="E-Modul MSPO FELDA",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #2E7D32;
        color: white;
        padding: 1rem;
        font-size: 1.1rem;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
    }
    .principle-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 5px solid #2E7D32;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📚 E-Modul MSPO FELDA")
st.markdown("### Malaysian Sustainable Palm Oil (MSPO) Training Modules")
st.markdown("---")

# Introduction
st.markdown("""
Selamat datang ke portal E-Modul MSPO FELDA. Sila pilih prinsip yang ingin anda akses untuk mendapatkan modul pembelajaran.
""")

st.markdown("---")

# Module links dictionary - Replace with your actual OneDrive links
modules = {
    "Prinsip 1": {
        "title": "Prinsip 1: Pematuhan Kepada Undang-Undang dan Peraturan",
        "link": "https://onedrive.live.com/your-link-here-principle-1",
        "description": "Modul pembelajaran mengenai pematuhan undang-undang dan peraturan MSPO"
    },
    "Prinsip 2": {
        "title": "Prinsip 2: Pengurusan Ladang dan Kemudahkerjaan",
        "link": "https://onedrive.live.com/your-link-here-principle-2",
        "description": "Modul pembelajaran mengenai pengurusan ladang dan kemudahkerjaan"
    },
    "Prinsip 3": {
        "title": "Prinsip 3: Amalan Pertanian Yang Baik",
        "link": "https://onedrive.live.com/your-link-here-principle-3",
        "description": "Modul pembelajaran mengenai amalan pertanian yang baik"
    },
    "Prinsip 4": {
        "title": "Prinsip 4: Tanggungjawab Alam Sekitar",
        "link": "https://onedrive.live.com/your-link-here-principle-4",
        "description": "Modul pembelajaran mengenai tanggungjawab alam sekitar"
    },
    "Prinsip 5": {
        "title": "Prinsip 5: Tanggungjawab Sosial dan Kesihatan Pekerja",
        "link": "https://onedrive.live.com/your-link-here-principle-5",
        "description": "Modul pembelajaran mengenai tanggungjawab sosial dan kesihatan pekerja"
    }
}

# Display modules in a grid
col1, col2 = st.columns(2)

for idx, (key, module) in enumerate(modules.items()):
    with col1 if idx % 2 == 0 else col2:
        with st.container():
            st.markdown(f'<div class="principle-card">', unsafe_allow_html=True)
            st.markdown(f"### {module['title']}")
            st.markdown(f"_{module['description']}_")
            if st.button(f"📥 Akses {key}", key=key):
                st.markdown(f"[Klik di sini untuk membuka modul]({module['link']})")
                st.info(f"Anda akan dibawa ke OneDrive untuk mengakses {key}")
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("""
### 📞 Maklumat Hubungan
Untuk sebarang pertanyaan mengenai modul ini, sila hubungi:
- **Email**: training@felda.gov.my
- **Telefon**: +60 3-XXXX XXXX

---
© 2024 FELDA - Malaysian Sustainable Palm Oil (MSPO)
""")

# Sidebar with additional information
with st.sidebar:
    st.image("https://via.placeholder.com/300x100/2E7D32/FFFFFF?text=FELDA+MSPO", use_column_width=True)
    st.markdown("### Panduan Penggunaan")
    st.markdown("""
    1. Pilih prinsip yang ingin dipelajari
    2. Klik butang 'Akses' untuk membuka modul
    3. Modul akan dibuka di OneDrive
    4. Muat turun atau lihat modul secara dalam talian
    """)
    
    st.markdown("---")
    st.markdown("### Tentang MSPO")
    st.markdown("""
    MSPO adalah standard pensijilan kelapa sawit Malaysia yang 
    memastikan amalan pengeluaran minyak sawit yang mampan.
    """)
