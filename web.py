import streamlit as st
import smtplib
import ssl
from typing import Dict, Any

# --- Konfigurasi Halaman & CSS Kustom ---
st.set_page_config(
    page_title="Septem Tour & Travel",
    page_icon="✈️",
    layout="wide"
)

# Inisialisasi session state untuk tema jika belum ada
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'  # Default theme

# Fungsi untuk mengubah tema
def toggle_theme():
    """Mengubah mode tema antara 'light' dan 'dark'."""
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

# Masukkan CSS ke dalam aplikasi.
# Tambahkan kelas 'dark-mode' ke body jika tema adalah 'dark'.
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    :root {{
        --background-color: #f0f2f5;
        --text-color: #333;
        --card-background: white;
        --footer-background: #2d3748;
        --footer-text-color: white;
        --septem-blue: #38b2ac;
        --secondary-text-color: #4a5568;
        --shadow-color-light: rgba(0, 0, 0, 0.1);
        --shadow-color-dark: rgba(0, 0, 0, 0.05);
    }}

    .dark-mode {{
        --background-color: #1a202c;
        --text-color: #e2e8f0;
        --card-background: #2d3748;
        --footer-background: #1a202c;
        --footer-text-color: #cbd5e0;
        --septem-blue: #4fd1c5; /* Slightly lighter for dark mode */
        --secondary-text-color: #a0aec0;
        --shadow-color-light: rgba(255, 255, 255, 0.1);
        --shadow-color-dark: rgba(255, 255, 255, 0.05);
    }}

    /* Terapkan kelas dark-mode secara kondisional */
    .st-emotion-cache-16txte0 {{
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
    }}
    .st-emotion-cache-16txte0 .st-emotion-cache-1f8553m {{
        background-color: var(--card-background) !important;
    }}
    .st-emotion-cache-16txte0 .st-emotion-cache-vj06pl {{
        background-color: var(--card-background) !important;
    }}

    /* Teks dan Konten Utama */
    html, body, .st-emotion-cache-16txte0 {{
        font-family: 'Inter', sans-serif;
        background-color: var(--background-color) !important;
        color: var(--text-color);
        text-align: center !important;
    }}
    .st-emotion-cache-z5fcl4 {{
        max-width: 1200px;
        margin: 0 auto;
        padding-right: 2rem;
        padding-left: 2rem;
    }}
    .text-septem-blue {{
        color: var(--septem-blue);
    }}
    .bg-septem-blue {{
        background-color: var(--septem-blue);
    }}
    .st-emotion-cache-18ni7ap, .st-emotion-cache-h4xjwx {{
        padding-top: 0 !important;
        padding-right: 0 !important;
        padding-left: 0 !important;
        padding-bottom: 0 !important;
    }}
    
    /* Navbar */
    .navbar {{
        width: 100%;
        background-color: transparent; /* Tetap transparan atau sesuaikan jika perlu */
        box-shadow: none;
        padding: 1rem 2rem;
        display: flex;
        justify-content: center;
    }}
    .navbar-content {{
        max-width: 1200px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap; 
        gap: 1rem;
    }}
    .navbar-logo-container {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    .navbar-logo {{
        height: 2.5rem;
        width: 2.5rem;
        border-radius: 9999px;
        background-color: var(--septem-blue);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 1.5rem;
    }}
    .navbar-title {{
        font-size: 1.875rem;
        font-weight: 800;
        color: var(--septem-blue);
        line-height: 1;
    }}
    .navbar-title span {{
        font-weight: 400;
        color: var(--secondary-text-color);
        margin-left: 0.25rem;
    }}
    .navbar-links {{
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
        justify-content: center;
    }}
    .navbar-links .stButton > button {{
        background-color: transparent !important;
        color: var(--secondary-text-color) !important;
        font-weight: 500 !important;
        text-decoration: none !important;
        transition: color 0.3s ease !important;
        padding: 0.5rem 0 !important;
        border: none !important;
        box-shadow: none !important;
        min-height: auto !important;
        border-bottom: 2px solid transparent !important;
    }}
    .navbar-links .stButton > button:hover {{
        color: var(--septem-blue) !important;
        border-bottom: 2px solid var(--septem-blue) !important;
    }}
    .navbar-links .stButton > button[aria-selected="true"] {{
        color: var(--septem-blue) !important;
        border-bottom: 2px solid var(--septem-blue) !important;
    }}
    
    .content-container {{
        padding-top: 0rem;
    }}

    /* Hero Section */
    .hero-section {{
        background-image: url('https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bromomidnight(group).png');
        background-size: cover;
        background-position: center;
        height: 90vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
        z-index: 1;
        color: white; /* Tetap putih karena overlay */
        padding-top: 4rem;
        border-bottom-left-radius: 50px;
        border-bottom-right-radius: 50px;
        overflow: hidden;
    }}
    .hero-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.4);
        z-index: -1;
        border-bottom-left-radius: 50px;
        border-bottom-right-radius: 50px;
    }}
    .hero-content {{
        position: relative;
        z-index: 2;
        padding: 2rem;
        max-width: 800px;
        margin-top: 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    .hero-title {{
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0rem;
    }}

    /* Mengubah gaya tombol mulai perjalanan */
    .stButton[data-testid="stButton-hero_btn"] > button {{
        background-color: var(--septem-blue) !important;
        color: white !important;
        padding: 0.85rem 2rem !important;
        border-radius: 9999px !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        transition: background-color 0.3s ease, transform 0.2s ease !important;
        box-shadow: 0 4px 6px var(--shadow-color-light) !important; /* Menggunakan variabel */
        border: none !important;
        min-height: auto !important;
        margin-top: 2rem;
    }}
    .stButton[data-testid="stButton-hero_btn"] > button:hover {{
        background-color: #319795 !important;
        transform: translateY(-2px) !important;
    }}
    .hero-small-text {{
        position: absolute;
        bottom: 2.5rem;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.875rem;
        font-weight: 600;
        color: white; /* Tetap putih */
        white-space: nowrap;
    }}
    
    /* Section Headers */
    .section-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-color);
        text-align: center;
        margin-bottom: 3rem;
        margin-top: 4rem;
    }}
    
    /* WHO SEPTEM Section */
    .about-us-section {{
        text-align: center;
        padding: 4rem 0;
    }}
    .about-us-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 1.5rem;
    }}
    .about-us-text {{
        max-width: 800px;
        margin: 0 auto 2rem auto;
        font-size: 1.125rem;
        line-height: 1.75;
        color: var(--secondary-text-color);
        text-align: center;
    }}
    .about-us-images {{
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
        flex-wrap: wrap; 
    }}
    .about-us-image {{
        width: 100%; 
        max-width: 250px;
        height: 250px;
        object-fit: cover;
        border-radius: 1.5rem;
        box-shadow: 0 10px 15px var(--shadow-color-light), 0 4px 6px var(--shadow-color-dark);
    }}

    /* Card Layout */
    .card-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 0 auto;
        max-width: 1200px;
        padding-bottom: 4rem;
    }}
    .tour-card-item {{
        background-color: var(--card-background);
        border-radius: 1.25rem;
        box-shadow: 0 10px 15px var(--shadow-color-light), 0 4px 6px var(--shadow-color-dark);
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        cursor: pointer; 
    }}
    .tour-card-item:hover {{
        transform: translateY(-8px);
        box-shadow: 0 20px 25px var(--shadow-color-light), 0 10px 10px var(--shadow-color-dark);
    }}
    .tour-card-image {{
        width: 100%;
        height: 200px;
        object-fit: cover;
    }}
    .tour-card-content {{
        padding: 1.5rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        text-align: center;
    }}
    .tour-card-title {{
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.5rem;
    }}
    .tour-card-price {{
        font-size: 1.5rem;
        font-weight: 800;
        color: var(--septem-blue);
        margin-bottom: 1rem;
    }}
    .tour-card-btn {{
        background-color: var(--septem-blue);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 9999px;
        font-weight: 600;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.3s ease, transform 0.2s ease;
        margin-top: auto;
    }}
    .tour-card-btn:hover {{
        background-color: #319795;
        transform: translateY(-2px);
    }}
    .tour-card-btn svg {{
        margin-left: 0.5rem;
        font-size: 0.75rem;
    }}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 16px;
    }}
    .stTabs [data-baseweb="tab"] {{
        border-bottom: 2px solid transparent !important;
        background-color: var(--background-color) !important;
        padding: 1rem;
        color: var(--secondary-text-color) !important;
    }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        border-bottom: 2px solid var(--septem-blue) !important;
        color: var(--septem-blue) !important;
        background-color: var(--card-background) !important;
        font-weight: 600;
    }}
    .detail-card {{
        background-color: var(--card-background);
        border-radius: 1.25rem;
        padding: 2rem;
        box-shadow: 0 10px 15px var(--shadow-color-light), 0 4px 6px var(--shadow-color-dark);
        text-align: left;
    }}
    .detail-card h3 {{
        color: var(--text-color);
    }}
    .detail-card p {{
        color: var(--secondary-text-color);
    }}
    
    /* Formulir Kontak */
    .contact-form-container {{
        max-width: 800px;
        margin: 2rem auto;
        background-color: var(--card-background);
        padding: 2.5rem;
        border-radius: 1.25rem;
        box-shadow: 0 10px 15px var(--shadow-color-light), 0 4px 6px var(--shadow-color-dark);
    }}
    .contact-form-container h3 {{
        color: var(--text-color);
    }}
    .stForm label {{
        color: var(--secondary-text-color);
    }}
    .stForm button {{
        margin-top: 1.5rem;
        width: 100%;
        padding: 1rem;
        font-size: 1.125rem;
        background-color: var(--septem-blue);
        color: white;
        border-radius: 9999px;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 4px 6px var(--shadow-color-light);
    }}
    .stForm button:hover {{
        background-color: #319795;
        transform: translateY(-2px);
    }}
    
    /* Footer */
    .footer {{
        background-color: var(--footer-background);
        color: var(--footer-text-color);
        padding: 3rem 2rem;
        text-align: center;
        border-top-left-radius: 50px;
        border-top-right-radius: 50px;
        margin-top: 4rem;
    }}
    .footer-logo {{
        font-size: 2.25rem;
        font-weight: 800;
        color: white; /* Logo tetap putih */
        margin-bottom: 1rem;
    }}
    .footer-text {{
        font-size: 0.875rem;
        margin-bottom: 1.5rem;
        color: var(--footer-text-color);
    }}
    .social-icons {{
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 2rem;
    }}
    .social-icons a {{
        color: white; /* Ikon tetap putih */
        font-size: 1.5rem;
        transition: color 0.3s ease;
    }}
    .social-icons a:hover {{
        color: var(--septem-blue);
    }}
    .footer-copy {{
        font-size: 0.875rem;
        opacity: 0.75;
        color: var(--secondary-text-color);
    }}

    /* Ulasan */
    .review-card {{
        background-color: var(--card-background); 
        padding: 1.5rem; 
        border-radius: 1rem; 
        box-shadow: 0 4px 6px var(--shadow-color-light); 
        margin-bottom: 1.5rem;
        text-align: left;
    }}
    .review-card p {{
        color: var(--secondary-text-color);
    }}
</style>
""", unsafe_allow_html=True)


# --- Data Dummy untuk Tur yang Lebih Lengkap ---
TOUR_PACKAGES_DATA: Dict[str, Dict[str, Any]] = {
    "bromo-midnight": {
        "nama": "Bromo Midnight",
        "durasi": "1 Hari",
        "harga": "Rp 500.000",
        "destinasi": "Bromo",
        "kategori": "Wisata Alam & Lanskap Tropis Indonesia",
        "level": "Petualangan Ringan",
        "pickup_dropoff": {"Surabaya", "Malang"},
        "aktivitas": "Sunrise, Sesi Foto & Trekking",
        "transportasi": "Jeep 4x4",
        "fasilitas": "Jeep 4x4, Tiket Masuk, Air Mineral",
        "itinerary": "Penjemputan, menikmati sunrise Bromo, kawah, dan padang savana. Kembali ke titik awal.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bromo.png" 
    },
    "bromo-tumpak-sewu-2d1n": {
        "nama": "Bromo - Tumpak Sewu (2D1N)",
        "durasi": "2 Hari 1 Malam",
        "harga": "Rp 600.000",
        "destinasi": "Bromo, Tumpak Sewu",
        "kategori": "Wisata Alam & Lanskap Tropis Indonesia",
        "level": "Petualangan Sedang",
        "pickup_dropoff": {"Surabaya", "Malang"},
        "aktivitas": "Trekking, Sunrise, Sesi Foto",
        "transportasi": "Avanza/Innova Reborn/Hiace",
        "fasilitas": "Transportasi, Hotel, Tiket Masuk, Konsumsi",
        "itinerary": "Hari 1: Turun ke air terjun Tumpak Sewu, dilanjutkan menuju Bromo. Hari 2: Menikmati sunrise Bromo dan kembali.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bromotumpaksewu.png" 
    },
    "tumpak-sewu-bromo-ijen-3d2n": {
        "nama": "Tumpak Sewu - Bromo - Ijen (3D2N)",
        "durasi": "3 Hari 2 Malam",
        "harga": "Rp 500.000",
        "destinasi": "Tumpak Sewu, Bromo, Kawah Ijen",
        "kategori": "Wisata Alam & Lanskap Tropis Indonesia",
        "level": "Petualangan Ringan",
        "pickup_dropoff": {"Surabaya", "Malang", "Banyuwangi"},
        "aktivitas": "Sunrise, Sesi Foto, Trekking, Blue Fire (Kondisional)",
        "transportasi": "Avanza/Innova Reborn/Hiace & Jeep 4x4",
        "fasilitas": "Transportasi, Hotel (2 malam), Tiket Masuk, Konsumsi",
        "itinerary": "Hari 1: Jelajah Tumpak Sewu. Hari 2: Sunrise Bromo. Hari 3: Blue fire Kawah Ijen dan kembali.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/tumpaksewubromoijen.png" 
    },
    "city-tour-malang-batu": {
        "nama": "City Tour Malang - Batu",
        "durasi": "1 Hari",
        "harga": "Rp 500.000",
        "destinasi": "Malang, Batu",
        "kategori": "Wisata Kota",
        "level": "Santai",
        "pickup_dropoff": {"Malang"},
        "aktivitas": "Jalan-jalan, Wisata Kuliner",
        "transportasi": "Avanza/Innova Reborn/Hiace",
        "fasilitas": "Transportasi, Tiket Masuk, Pemandu",
        "itinerary": "Jelajah kota Malang dan Batu, termasuk museum, tempat wisata, dan kuliner.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/malangbatu.jpg" 
    },
    "raja-ampat": {
        "nama": "Raja Ampat, Indonesia",
        "durasi": "4 Hari 3 Malam",
        "harga": "Rp 600.000",
        "destinasi": "Raja Ampat",
        "kategori": "Wisata Alam & Laut",
        "level": "Petualangan",
        "pickup_dropoff": {"Papua"},
        "aktivitas": "Snorkeling, Diving, Island Hopping",
        "transportasi": "Kapal, Speedboat",
        "fasilitas": "Transportasi, Penginapan, Tiket, Snorkeling",
        "itinerary": "Eksplorasi keindahan bawah laut Raja Ampat.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/rajaampat.jpg" 
    },
    "city-tour-bali": {
        "nama": "City Tour Bali",
        "durasi": "2 Hari 1 Malam",
        "harga": "Rp 500.000",
        "destinasi": "Bali",
        "kategori": "Wisata Budaya & Alam",
        "level": "Santai",
        "pickup_dropoff": {"Denpasar"},
        "aktivitas": "Jalan-jalan, Kunjungan Pura, Wisata Pantai",
        "transportasi": "Avanza/Innova Reborn",
        "fasilitas": "Transportasi, Hotel, Tiket Masuk",
        "itinerary": "Menjelajahi keindahan budaya dan alam Bali.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bali.jpg" 
    },
    "city-tour-yogyakarta": {
        "nama": "City Tour Yogyakarta",
        "durasi": "2 Hari 1 Malam",
        "harga": "Rp 600.000",
        "destinasi": "Yogyakarta",
        "kategori": "Wisata Sejarah & Budaya",
        "level": "Santai",
        "pickup_dropoff": {"Yogyakarta"},
        "aktivitas": "Kunjungan Candi, Wisata Kuliner",
        "transportasi": "Avanza/Innova Reborn",
        "fasilitas": "Transportasi, Hotel, Tiket Masuk, Pemandu",
        "itinerary": "Menjelajahi Candi Borobudur, Candi Prambanan, dan tempat bersejarah lainnya.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/yogyakarta.jpg" 
    },
    "bromo-midnight-group": {
        "nama": "Bromo Midnight (GROUP)",
        "durasi": "1 Hari",
        "harga": "Rp 500.000",
        "destinasi": "Bromo",
        "kategori": "Wisata Alam & Lanskap Tropis Indonesia",
        "level": "Petualangan Ringan",
        "pickup_dropoff": {"Surabaya", "Malang"},
        "aktivitas": "Sunrise, Sesi Foto & Trekking",
        "transportasi": "Jeep 4x4",
        "fasilitas": "Jeep 4x4, Tiket Masuk, Air Mineral",
        "itinerary": "Paket grup untuk tur Bromo Midnight.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bromomidnight(group).png" 
    },
    "request-package": {
        "nama": "Request Package",
        "durasi": "Sesuai Permintaan",
        "harga": "Rp 500.000",
        "destinasi": "Sesuai Permintaan",
        "kategori": "Sesuai Permintaan",
        "level": "Sesuai Permintaan",
        "pickup_dropoff": {},
        "aktivitas": "Sesuai Permintaan",
        "transportasi": "Sesuai Permintaan",
        "fasilitas": "Sesuai Permintaan",
        "itinerary": "Anda dapat mengajukan paket tur yang Anda inginkan.",
        "image_url": "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/requestpackage.jpg" 
    }
}

# --- Inisialisasi Session State ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
    st.session_state.selected_tour = None
    st.session_state.reviews = [
        {"name": "Ani Sutra", "review": "Perjalanan ke Bromo sangat luar biasa! Pemandu ramah dan pelayanan prima."},
        {"name": "Budi Santoso", "review": "Paket tour Bali sangat terencana dengan baik. Rekomendasi sekali!"},
        {"name": "Citra Dewi", "review": "Sewa mobil di Septem Tour sangat mudah dan unitnya bersih. Top!"},
    ]

# --- Callback function untuk mengalihkan halaman ---
def set_page(page_name, tour_id=None):
    """Fungsi untuk mengalihkan halaman dan memperbarui session state."""
    st.session_state.current_page = page_name
    st.session_state.selected_tour = tour_id
    st.query_params['page'] = page_name
    if tour_id:
        st.query_params['tour_id'] = tour_id
    else:
        st.query_params.pop('tour_id', None)

# --- Fungsi Tampilan Halaman ---
def show_navbar():
    """Menampilkan navigasi bar di bagian atas halaman."""
    st.markdown("""
    <div class="navbar">
        <div class="navbar-content">
            <div class="navbar-logo-container">
                <div class="navbar-logo">S</div>
                <div class="navbar-title">SEPTEM<span>TOUR</span></div>
            </div>
            <div class="navbar-links">
    """, unsafe_allow_html=True)
    
    with st.container():
        col_nav1, col_nav2, col_nav3, col_nav4, col_nav5, col_theme = st.columns([1, 1, 1, 1, 1, 0.5])
        with col_nav1:
            st.button("Home", on_click=set_page, args=('home',), key='nav_home')
        with col_nav2:
            st.button("Rent Car", on_click=set_page, args=('rent_car',), key='nav_rent')
        with col_nav3:
            st.button("Galeri", on_click=set_page, args=('gallery',), key='nav_gallery')
        with col_nav4:
            st.button("Hubungi Kami", on_click=set_page, args=('contact_us',), key='nav_contact')
        with col_nav5:
            st.button("Ulasan Kami", on_click=set_page, args=('reviews',), key='nav_reviews')
        with col_theme:
            theme_icon = "☀️" if st.session_state.theme == 'light' else "🌙"
            st.button(theme_icon, on_click=toggle_theme, key='theme_toggle', help="Toggle Dark/Light Mode")
    
    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_hero_section():
    """Menampilkan bagian hero (header utama) dengan gambar latar belakang."""
    st.markdown('<a id="beranda"></a>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title">Selamat Datang di<br>Septem Tour.</h1>
            <h3 style="margin-top: -1rem; margin-bottom: 2rem; color: white;">Mulai Perjalanan Anda</h3>
            
    """, unsafe_allow_html=True)

    st.button("Pesan Paket Tour", on_click=set_page, args=('tour_packages',), key='hero_btn')

    st.markdown("""
        </div>
        <p class="hero-small-text">KAMI ADALAH SEPTEM TOUR</p>
    </div>
    """, unsafe_allow_html=True)

def show_about_us():
    """Menampilkan bagian 'Tentang Kami'."""
    st.markdown('<a id="about-us"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>SIAPA KAMI?</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("""
        <div class="about-us-section">
            <p class="about-us-text">
                SEPTEM TOUR adalah 7 keajaiban dalam liburan. Perusahaan kami di namai sesuai harapan dan keinginan kami untuk
                menjadi cakupan global dalam 7 benua untuk bidang perjalanan.
                <br><br>
                SEPTEM TOUR HADIR untuk mendorong talenta-talenta pariwisata lokal yang memiliki gairah dan antusias untuk
                mewadahi minat dan kegembiraan para wisatawan lokal maupun mancanegara dalam menjelajahi dan menikmati Indonesia, baik
                alam maupun budayanya.
                <br><br>
                Pekerjaan kami dimulai di gunung berapi ikonik alam yang kami temui di kota kami.
                Gunung Bromo Ijen menjadi paket awal kami saat memulai perusahaan operator tur ini.
            </p>
            <div class="about-us-images">
                <img class="about-us-image" src="https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bromomidnight(group).png" alt="Bromo">
                <img class="about-us-image" src="https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/bromomidnight(group).png" alt="Ijen">
            </div>
        </div>
        """, unsafe_allow_html=True)

def show_tour_packages():
    """Menampilkan daftar paket tur dalam format grid."""
    st.markdown('<a id="packet-tour"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>CARI TUR ANDA</h2>", unsafe_allow_html=True)
    
    tour_keys = list(TOUR_PACKAGES_DATA.keys())
    
    st.markdown('<div class="card-grid">', unsafe_allow_html=True)
    
    # Gunakan layout kolom Streamlit untuk membuat grid
    num_cols = 3
    for i in range(0, len(tour_keys), num_cols):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            if i + j < len(tour_keys):
                key = tour_keys[i + j]
                package = TOUR_PACKAGES_DATA[key]
                with cols[j]:
                    # Menggunakan st.container untuk mengelompokkan elemen dalam "kartu"
                    with st.container(border=True):
                        st.image(package['image_url'], caption=package['nama'], use_container_width=True)
                        st.markdown(f"<h3 class='tour-card-title'>{package['nama']}</h3>", unsafe_allow_html=True)
                        st.markdown(f"<p class='tour-card-price'>{package['harga']}</p>", unsafe_allow_html=True)
                        st.button("Baca Selengkapnya", key=f"btn_{key}", on_click=set_page, args=('detail_tour', key))

    st.markdown('</div>', unsafe_allow_html=True)

def show_tour_detail(tour_id):
    """Menampilkan detail dari paket tur yang dipilih."""
    if tour_id and tour_id in TOUR_PACKAGES_DATA:
        package = TOUR_PACKAGES_DATA[tour_id]
        
        st.markdown(f"<h1 class='section-title'>{package['nama']}</h1>", unsafe_allow_html=True)
        st.image(package['image_url'], use_container_width=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Informasi Dasar", "Destinasi", "Fasilitas", "Itinerary", "Pesan Tour"])

        with tab1:
            st.markdown(f"""
            <div class="detail-card">
                <h3>Informasi Dasar</h3>
                <p><strong>Harga:</strong> {package['harga']}</p>
                <p><strong>Durasi:</strong> {package['durasi']}</p>
                <p><strong>Kategori:</strong> {package['kategori']}</p>
                <p><strong>Level:</strong> {package['level']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.markdown(f"""
            <div class="detail-card">
                <h3>Destinasi & Aktifitas</h3>
                <p>Paket tur ini akan membawa Anda ke <strong>{package['destinasi']}</strong>.</p>
                <p>Anda akan melakukan aktifitas: <strong>{package['aktivitas']}</strong>.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with tab3:
            st.markdown(f"""
            <div class="detail-card">
                <h3>Fasilitas & Transportasi</h3>
                <p>Paket ini sudah termasuk: <strong>{package['fasilitas']}</strong>.</p>
                <p>Transportasi yang digunakan: <strong>{package['transportasi']}</strong>.</p>
                <p>Titik Penjemputan & Pengantaran: <strong>{', '.join(package['pickup_dropoff'])}</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
        with tab4:
            st.markdown(f"""
            <div class="detail-card">
                <h3>Itinerary</h3>
                <p>{package['itinerary']}</p>
            </div>
            """, unsafe_allow_html=True)

        with tab5:
            st.markdown(f"""
            <div class="detail-card">
                <h3>Pesan Sekarang</h3>
                <p>Untuk memesan paket ini, silakan hubungi kami melalui WhatsApp dengan menekan tombol di bawah ini.</p>
                <a href="https://wa.me/6282233020807?text=Halo%20Septem%20Tour,%20saya%20tertarik%20dengan%20paket%20{package['nama']}.%20Mohon%20info%20lebih%20lanjut." target="_blank" class="tour-card-btn" style="display: block; width: fit-content; margin: 1rem auto;">Pesan Sekarang Melalui WhatsApp</a>
            </div>
            """, unsafe_allow_html=True)

        st.button("Kembali ke Paket Tour", on_click=set_page, args=('tour_packages',), key='back_to_packages')

    else:
        st.error("Paket tur tidak ditemukan.")
        st.button("Kembali ke Halaman Utama", on_click=set_page, args=('home',), key='not_found_home')
    
def show_rent_car():
    """Menampilkan halaman formulir sewa mobil."""
    st.markdown('<a id="rent-car"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Sewa Mobil 🚗</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="contact-form-container">', unsafe_allow_html=True)
        st.markdown("<h3>Formulir Sewa Mobil</h3>", unsafe_allow_html=True)
        with st.form("rent_car_form"):
            col1, col2 = st.columns(2)
            with col1:
                car_type = st.selectbox("Jenis Mobil", ["Pilih Jenis Mobil", "Avanza", "Innova Reborn", "Hiace", "Jeep 4x4"])
            with col2:
                pickup_location = st.text_input("Lokasi Pengambilan", placeholder="Contoh: Surabaya")
            
            col1, col2 = st.columns(2)
            with col1:
                pickup_date = st.date_input("Tanggal Pengambilan")
            with col2:
                return_location = st.text_input("Lokasi Pengembalian", placeholder="Contoh: Malang")
            
            return_date = st.date_input("Tanggal Pengembalian")

            submitted_car = st.form_submit_button("Ajukan Sewa")
            if submitted_car:
                if car_type != "Pilih Jenis Mobil" and pickup_date and return_date and pickup_location and return_location:
                    st.success("🎉 Pengajuan sewa mobil berhasil! Kami akan segera menghubungi Anda.")
                else:
                    st.error("Mohon lengkapi semua data.")
        st.markdown('</div>', unsafe_allow_html=True)

def show_gallery():
    """Menampilkan halaman galeri dengan gambar-gambar."""
    st.markdown('<a id="galeri"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Galeri 🖼️</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.125rem; color: var(--secondary-text-color);'>Bagian ini akan menampilkan koleksi foto-foto perjalanan kami yang menakjubkan!</p>", unsafe_allow_html=True)
    gallery_images = [
        "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/galeri1.jpg", 
        "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/galeri1.jpg", 
        "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/galeri1.jpg",
        "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/galeri1.jpg",
        "https://raw.githubusercontent.com/tourandtravel382/tourandtravel/main/images/galeri1.jpg" 
    ]
    cols = st.columns(len(gallery_images))
    for i, img_url in enumerate(gallery_images):
        with cols[i]:
            st.image(img_url, caption=f"Foto {i+1}", use_container_width=True)

def show_contact_us():
    """Menampilkan halaman formulir kontak."""
    st.markdown('<a id="hubungi-kami"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Hubungi Kami 📞</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="contact-form-container">', unsafe_allow_html=True)
        st.markdown("<h3>Kirimkan Pesan Anda</h3>", unsafe_allow_html=True)
        with st.form("contact_us_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Nama Lengkap")
            with col2:
                email = st.text_input("Email Anda")
            subject = st.text_input("Subjek")
            message = st.text_area("Pesan Anda", height=150)
            submitted_contact = st.form_submit_button("Kirim Pesan")
            
            if submitted_contact:
                if name and email and subject and message:
                    try:
                        # Pastikan Anda sudah mengatur secrets.toml di environment deployment Anda
                        email_sender = st.secrets["email"]["email_address"]
                        email_password = st.secrets["email"]["app_password"]
                        email_receiver = email_sender

                        email_body = f"""
Nama: {name}
Email Pengirim: {email}
Subjek: {subject}
Pesan: {message}
"""
                        full_message = f"Subject: Pesan dari Formulir Kontak\n\n{email_body}"
                        context = ssl.create_default_context()

                        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                            smtp.login(email_sender, email_password)
                            smtp.sendmail(email_sender, email_receiver, full_message)
                        
                        st.success("Terima kasih! Pesan Anda telah terkirim dan kami akan segera merespons.")

                    except Exception as e:
                        st.error(f"Pesan gagal dikirim. Pastikan Anda telah mengatur `secrets.toml` dengan benar. Kesalahan: {e}")
                        
                else:
                    st.error("Mohon lengkapi semua kolom yang wajib diisi.")
        st.markdown('</div>', unsafe_allow_html=True)

def show_reviews():
    """Menampilkan halaman ulasan pelanggan dan formulir penambahan ulasan."""
    st.markdown('<a id="ulasan-kami"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Ulasan Pelanggan ⭐</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.125rem; color: var(--secondary-text-color);'>Lihat apa kata pelanggan kami tentang pengalaman perjalanan mereka bersama Septem Tour!</p>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    for i, review in enumerate(st.session_state.reviews):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="review-card">
                <p style="font-weight: bold; margin-bottom: 0.5rem; color: var(--text-color);">{review['name']}</p>
                <p style="font-style: italic; color: var(--secondary-text-color);">"{review['review']}"</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; margin-top: 2rem; color: var(--text-color);'>Tambahkan Ulasan Anda</h3>", unsafe_allow_html=True)
    with st.form("review_form"):
        name_input = st.text_input("Nama Anda")
        review_input = st.text_area("Ulasan Anda", height=100)
        submitted = st.form_submit_button("Kirim Ulasan")

        if submitted and name_input and review_input:
            new_review = {"name": name_input, "review": review_input}
            st.session_state.reviews.append(new_review)
            st.success("Terima kasih! Ulasan Anda telah berhasil ditambahkan.")
            st.experimental_rerun() # Rerun untuk memperbarui tampilan ulasan
        elif submitted:
            st.error("Mohon isi nama dan ulasan Anda.")

def show_home_page():
    """Menampilkan konten halaman utama."""
    show_hero_section()
    show_about_us()

def show_footer():
    """Menampilkan footer di bagian bawah halaman."""
    st.markdown("""
    <div class="footer">
        <div class="footer-logo">SEPTEM TOUR</div>
        <p class="footer-text">Jalan Raya Tidar, Malang, Jawa Timur</p>
        <div class="social-icons">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="https://wa.me/6282233020807" target="_blank"><i class="fab fa-whatsapp"></i></a>
        </div>
        <p class="footer-copy">© 2024 Septem Tour. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Main App Logic ---
show_navbar()

# Dapatkan halaman dari query params atau session state
if 'page' in st.query_params:
    st.session_state.current_page = st.query_params['page']
    if st.session_state.current_page == 'detail_tour' and 'tour_id' in st.query_params:
        st.session_state.selected_tour = st.query_params['tour_id']

# Konten utama
st.markdown('<div class="content-container">', unsafe_allow_html=True)

if st.session_state.current_page == 'home':
    show_home_page()
    show_tour_packages()
elif st.session_state.current_page == 'tour_packages':
    show_tour_packages()
elif st.session_state.current_page == 'detail_tour':
    show_tour_detail(st.session_state.selected_tour)
elif st.session_state.current_page == 'rent_car':
    show_rent_car()
elif st.session_state.current_page == 'gallery':
    show_gallery()
elif st.session_state.current_page == 'contact_us':
    show_contact_us()
elif st.session_state.current_page == 'reviews':
    show_reviews()

st.markdown('</div>', unsafe_allow_html=True)

show_footer()
