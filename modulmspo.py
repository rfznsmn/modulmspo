import streamlit as st

# Page configuration
st.set_page_config(
    page_title="E-Modul MSPO FELDA",
    page_icon="feldalogo.png",
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
st.title("E-Modul MSPO FELDA 2.0")
st.markdown("### Modul Latihan Bagi Program Pensijilan Malaysian Sustainable Palm Oil (MSPO) 2.0")
st.markdown("---")

# Introduction
st.markdown("""
Selamat datang ke portal E-Modul MSPO FELDA 2.0.
""")

st.markdown("---")

# Announcement Board
st.markdown("### 📢 Papan Pengumuman")

# Announcements list - Edit this section to update announcements
announcements = [
    {
        "date": "1 November 2025",
        "title": "FELDA Berjaya Capai 100% Pensijilan MSPO! 🎉",
        "content": "Tahniah kepada semua rancangan yang terlibat. Alhamdulillah, FELDA telah berjaya mencapai 100% pensijilan MSPO untuk semua rancangan.",
        "type": "success"
    },
    {
        "date": "November 2025",
        "title": "Jadual Internal Audit Oktober",
        "content": "Audit dalaman Gugusan Jengka 18 akan dijalankan pada 5-7 November 2025."
        "Audit dalaman Gugusan Maokil akan dijalankan pada 11-13 November 2025."
        "Sila pastikan semua dokumentasi lengkap.",
        "type": "info"
    },
    {
        "date": "November 2025",
        "title": "Jadual External Audit Oktober",
        "content": "Tiada Audit luaran MSPO dijadualkan pada bulan ini.",
        "type": "warning"
    }
]

# Display announcements
for announcement in announcements:
    if announcement["type"] == "success":
        st.success(f"**{announcement['title']}** | _{announcement['date']}_\n\n{announcement['content']}")
    elif announcement["type"] == "info":
        st.info(f"**{announcement['title']}** | _{announcement['date']}_\n\n{announcement['content']}")
    elif announcement["type"] == "warning":
        st.warning(f"**{announcement['title']}** | _{announcement['date']}_\n\n{announcement['content']}")
    else:
        st.write(f"**{announcement['title']}** | _{announcement['date']}_\n\n{announcement['content']}")

st.markdown("---")

# Module links dictionary - Replace with your actual OneDrive links
modules = {
    "Prinsip 1": {
        "title": "Prinsip 1: Komitmen dan Tanggungjawab Pengurusan",
        "link": "https://onedrive.live.com/your-link-here-principle-1",
        #"description": "Modul pembelajaran bagi Komitmen dan Tanggungjawab Pengurusan"
    },
    "Prinsip 2": {
        "title": "Prinsip 2: Ketelusan",
        "link": "https://onedrive.live.com/your-link-here-principle-2",
        #"description": "Modul pembelajaran mengenai pengurusan ladang dan kemudahkerjaan"
    },
    "Prinsip 3": {
        "title": "Prinsip 3: Pematuhan Kepada Undang-Undang dan Perkara Berkaitan",
        "link": "https://onedrive.live.com/your-link-here-principle-3",
        #"description": "Modul pembelajaran mengenai amalan pertanian yang baik"
    },
    "Prinsip 4": {
        "title": "Prinsip 4: Tanggungjawab Sosial, Kesihatan, Keselamatan dan Terma Pekerjaan",
        "link": "https://onedrive.live.com/your-link-here-principle-4",
        #"description": "Modul pembelajaran mengenai tanggungjawab alam sekitar"
    },
    "Prinsip 5": {
        "title": "Prinsip 5: Alam Sekitar, Sumber Asli, Kepelbagaian Biologi dan Penjagaan Ekosistem",
        "link": "https://onedrive.live.com/your-link-here-principle-5",
        #"description": "Modul pembelajaran mengenai tanggungjawab sosial dan kesihatan pekerja"
    },
    "Rujukan": {
        "title": "Dokumen Manual, Polisi dan Prosedur",
        "link": "https://onedrive.live.com/your-link-here-principle-5",
        #"description": "Modul pembelajaran mengenai tanggungjawab sosial dan kesihatan pekerja"
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
