import streamlit as st

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Septem Tour & Travel",
    page_icon="✈️",
    layout="wide"
)

# --- Inisialisasi Session State ---
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
    st.session_state.selected_tour = None
    st.session_state.show_navbar = True

# --- Data Dummy untuk Tur yang Lebih Lengkap ---
TOUR_PACKAGES_DATA = {
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
        "itinerary": "Penjemputan, menikmati sunrise Bromo, kawah, dan padang savana. Kembali ke titik awal."
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
        "itinerary": "Hari 1: Turun ke air terjun Tumpak Sewu, dilanjutkan menuju Bromo. Hari 2: Menikmati sunrise Bromo dan kembali."
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
        "itinerary": "Hari 1: Jelajah Tumpak Sewu. Hari 2: Sunrise Bromo. Hari 3: Blue fire Kawah Ijen dan kembali."
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
        "itinerary": "Jelajah kota Malang dan Batu, termasuk museum, tempat wisata, dan kuliner."
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
        "itinerary": "Eksplorasi keindahan bawah laut Raja Ampat."
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
        "itinerary": "Menjelajahi keindahan budaya dan alam Bali."
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
        "itinerary": "Menjelajahi Candi Borobudur, Candi Prambanan, dan tempat bersejarah lainnya."
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
        "itinerary": "Paket grup untuk tur Bromo Midnight."
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
        "itinerary": "Anda dapat mengajukan paket tur yang Anda inginkan."
    }
}

# --- CSS Kustom ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    html, body, .st-emotion-cache-16txte0 {
        font-family: 'Inter', sans-serif;
        background-color: #f0f2f5 !important;
        color: #333;
    }
    
    .st-emotion-cache-z5fcl4 {
        max-width: 1200px;
        margin: 0 auto;
        padding-right: 2rem;
        padding-left: 2rem;
    }
    
    .text-septem-blue {
        color: #38b2ac;
    }
    .bg-septem-blue {
        background-color: #38b2ac;
    }
    .st-emotion-cache-18ni7ap {
        padding-top: 0;
        padding-right: 0;
        padding-left: 0;
        padding-bottom: 0;
    }
    .st-emotion-cache-h4xjwx {
        padding-top: 0rem;
    }
    
    /* Navbar */
    .navbar-fixed {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        z-index: 1000;
        padding: 1rem 2rem;
        display: flex;
        justify-content: center;
    }
    .navbar-content {
        max-width: 1200px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .navbar-logo-container {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .navbar-logo {
        height: 2.5rem;
        width: 2.5rem;
        border-radius: 9999px;
        background-color: #38b2ac;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 1.5rem;
    }
    .navbar-title {
        font-size: 1.875rem;
        font-weight: 800;
        color: #38b2ac;
        line-height: 1;
    }
    .navbar-title span {
        font-weight: 400;
        color: #4a5568;
        margin-left: 0.25rem;
    }
    .navbar-links {
        display: flex;
        gap: 2rem;
    }
    .navbar-links .stButton > button {
        background-color: transparent !important;
        color: #4a5568 !important;
        font-weight: 500 !important;
        text-decoration: none !important;
        transition: color 0.3s ease !important;
        padding: 0.5rem 0 !important;
        border: none !important;
        box-shadow: none !important;
        min-height: auto !important;
    }
    .navbar-links .stButton > button:hover {
        color: #38b2ac !important;
        border-bottom: 2px solid #38b2ac !important;
    }
    
    .content-container {
        padding-top: 5rem;
    }

    /* Hero Section */
    .hero-section {
        background-image: url('https://images.unsplash.com/photo-1549419165-2a412c140df0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80');
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
        color: white;
        padding-top: 4rem;
        border-bottom-left-radius: 50px;
        border-bottom-right-radius: 50px;
        overflow: hidden;
    }
    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.4);
        z-index: -1;
        border-bottom-left-radius: 50px;
        border-bottom-right-radius: 50px;
    }
    .hero-content {
        position: relative;
        z-index: 2;
        padding: 2rem;
        max-width: 800px;
        margin-top: 2rem;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    .hero-btn {
        background-color: #38b2ac;
        color: white;
        padding: 0.85rem 2rem;
        border-radius: 9999px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: background-color 0.3s ease, transform 0.2s ease;
        box-shadow: 0 4px 6px rgba(56, 178, 172, 0.3);
    }
    .hero-btn:hover {
        background-color: #319795;
        transform: translateY(-2px);
    }
    .hero-small-text {
        position: absolute;
        bottom: 2.5rem;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.875rem;
        font-weight: 600;
        color: white;
        white-space: nowrap;
    }
    
    /* Section Headers */
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        text-align: center;
        margin-bottom: 3rem;
        margin-top: 4rem;
    }
    
    /* WHO SEPTEM Section */
    .about-us-section {
        text-align: center;
        padding: 4rem 0;
    }
    .about-us-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 1.5rem;
    }
    .about-us-text {
        max-width: 800px;
        margin: 0 auto 2rem auto;
        font-size: 1.125rem;
        line-height: 1.75;
        color: #4a5568;
    }
    .about-us-images {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 2rem;
    }
    .about-us-image {
        width: 250px;
        height: 250px;
        object-fit: cover;
        border-radius: 1.5rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }

    /* Card Layout */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 0 auto;
        max-width: 1200px;
        padding-bottom: 4rem;
    }
    .tour-card-item {
        background-color: white;
        border-radius: 1.25rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
    }
    .tour-card-item:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    .tour-card-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
    }
    .tour-card-content {
        padding: 1.5rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }
    .tour-card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.5rem;
    }
    .tour-card-price {
        font-size: 1.5rem;
        font-weight: 800;
        color: #38b2ac;
        margin-bottom: 1rem;
    }
    .tour-card-btn {
        background-color: #38b2ac;
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
    }
    .tour-card-btn:hover {
        background-color: #319795;
        transform: translateY(-2px);
    }
    .tour-card-btn svg {
        margin-left: 0.5rem;
        font-size: 0.75rem;
    }
    .stButton > button {
        background-color: #38b2ac;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 9999px;
        font-weight: 600;
        border: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #319795;
        transform: translateY(-2px);
    }
    .stButton > button:active {
        background-color: #2b6cb0;
        transform: translateY(0);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
    }
    .stTabs [data-baseweb="tab"] {
        border-bottom: 2px solid transparent !important;
        background-color: #f0f2f5 !important;
        padding: 1rem;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 2px solid #38b2ac !important;
        color: #38b2ac !important;
        background-color: white !important;
        font-weight: 600;
    }
    .detail-card {
        background-color: white;
        border-radius: 1.25rem;
        padding: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    /* Formulir Kontak */
    .contact-form-container {
        max-width: 800px;
        margin: 2rem auto;
        background-color: white;
        padding: 2.5rem;
        border-radius: 1.25rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    .stForm button {
        margin-top: 1.5rem;
        width: 100%;
        padding: 1rem;
        font-size: 1.125rem;
    }
    
    /* Footer */
    .footer {
        background-color: #2d3748;
        color: white;
        padding: 3rem 2rem;
        text-align: center;
        border-top-left-radius: 50px;
        border-top-right-radius: 50px;
        margin-top: 4rem;
    }
    .footer-logo {
        font-size: 2.25rem;
        font-weight: 800;
        color: white;
        margin-bottom: 1rem;
    }
    .footer-text {
        font-size: 0.875rem;
        margin-bottom: 1.5rem;
        color: #cbd5e0;
    }
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    .social-icons a {
        color: white;
        font-size: 1.5rem;
        transition: color 0.3s ease;
    }
    .social-icons a:hover {
        color: #38b2ac;
    }
    .footer-copy {
        font-size: 0.875rem;
        opacity: 0.75;
        color: #a0aec0;
    }
</style>
""", unsafe_allow_html=True)

# Callback function untuk mengalihkan halaman
def set_page(page_name):
    st.session_state.current_page = page_name

def show_navbar():
    st.markdown("""
    <div class="navbar-fixed">
        <div class="navbar-content">
            <div class="navbar-logo-container">
                <div class="navbar-logo">S</div>
                <div class="navbar-title">SEPTEM<span>TOUR</span></div>
            </div>
    """, unsafe_allow_html=True)
    
    # Menggunakan st.columns untuk menempatkan tombol secara horizontal
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        if st.button("Home"):
            st.session_state.current_page = 'home'
            st.rerun()
    with col2:
        if st.button("Packet Tour"):
            st.session_state.current_page = 'tour_packages'
            st.rerun()
    with col3:
        if st.button("Rent Car"):
            st.session_state.current_page = 'rent_car'
            st.rerun()
    with col4:
        if st.button("Galeri"):
            st.session_state.current_page = 'gallery'
            st.rerun()
    with col5:
        if st.button("Hubungi Kami"):
            st.session_state.current_page = 'contact_us'
            st.rerun()
    with col6:
        if st.button("Ulasan Kami"):
            st.session_state.current_page = 'reviews'
            st.rerun()

    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Fungsi-fungsi Halaman ---
def show_hero_section():
    st.markdown('<a id="beranda"></a>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-section">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title">Selamat Datang di<br>Septem Tour.</h1>
            <p class="hero-subtitle">Mulai Perjalanan Anda</p>
            <a href="#packet-tour" class="hero-btn">Mulai Perjalanan Anda</a>
            <p class="hero-small-text">KAMI ADALAH SEPTEM TOUR</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_about_us():
    st.markdown('<a id="about-us"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>SIAPA KAMI?</h2>", unsafe_allow_html=True)
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
            <img class="about-us-image" src="https://images.unsplash.com/photo-1549419165-2a412c140df0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80">
            <img class="about-us-image" src="https://images.unsplash.com/photo-1544464870-7634f107f96b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80">
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_tour_packages():
    st.markdown('<a id="packet-tour"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>CARI TUR ANDA</h2>", unsafe_allow_html=True)
    
    tour_keys = list(TOUR_PACKAGES_DATA.keys())
    
    num_cols = 3
    for i in range(0, len(tour_keys), num_cols):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            index = i + j
            if index < len(tour_keys):
                key = tour_keys[index]
                package = TOUR_PACKAGES_DATA[key]
                with cols[j]:
                    st.markdown(f"""
                    <div class="tour-card-item">
                        <img src="https://placehold.co/600x400/38b2ac/FFFFFF?text={package['nama'].replace(' ', '+')}" alt="{package['nama']}" class="tour-card-image">
                        <div class="tour-card-content">
                            <h3 class="tour-card-title">{package['nama']}</h3>
                            <p class="tour-card-price">{package['harga']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("Baca Selengkapnya", key=f"btn_{key}"):
                        st.session_state.current_page = 'detail_tour'
                        st.session_state.selected_tour = key
                        st.rerun()

def show_tour_detail(tour_id):
    if tour_id and tour_id in TOUR_PACKAGES_DATA:
        package = TOUR_PACKAGES_DATA[tour_id]
        
        st.markdown(f"<h1 class='section-title'>{package['nama']}</h1>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Informasi Dasar", "Destinasi", "Fasilitas", "Itinerary", "Pesan Tour"])

        with tab1:
            st.header("Informasi Dasar")
            st.image("https://placehold.co/800x400/38b2ac/FFFFFF?text=" + package['nama'].replace(' ', '+'))
            st.markdown(f"""
            <div class="detail-card">
                <p><strong>Harga:</strong> {package['harga']}</p>
                <p><strong>Durasi:</strong> {package['durasi']}</p>
                <p><strong>Kategori:</strong> {package['kategori']}</p>
                <p><strong>Level:</strong> {package['level']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with tab2:
            st.header("Destinasi & Aktifitas")
            st.write(f"Paket tur ini akan membawa Anda ke {package['destinasi']}.")
            st.write(f"Anda akan melakukan aktifitas: {package['aktivitas']}.")
        
        with tab3:
            st.header("Fasilitas & Transportasi")
            st.write(f"Paket ini sudah termasuk: {package['fasilitas']}.")
            st.write(f"Transportasi yang digunakan: {package['transportasi']}.")
            st.write(f"Titik Penjemputan & Pengantaran: {', '.join(package['pickup_dropoff'])}")
            
        with tab4:
            st.header("Itinerary")
            st.write(package['itinerary'])

        with tab5:
            st.header("Pesan Sekarang")
            st.markdown(f"""
            <a href="https://wa.me/6281234567890?text=Halo%20Septem%20Tour,%20saya%20tertarik%20dengan%20paket%20{package['nama']}.%20Mohon%20info%20lebih%20lanjut." target="_blank" class="hero-btn" style="display: block; width: fit-content; margin: 1rem auto;">Pesan Sekarang Melalui WhatsApp</a>
            """, unsafe_allow_html=True)

        st.button("Kembali ke Halaman Utama", on_click=lambda: set_page('home'))

    else:
        st.error("Paket tur tidak ditemukan.")
        if st.button("Kembali ke Halaman Utama"):
            set_page('home')

def show_rent_car():
    st.markdown('<a id="rent-car"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Sewa Mobil 🚗</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="contact-form-container">', unsafe_allow_html=True)
        st.markdown("<h3>Formulir Sewa Mobil</h3>", unsafe_allow_html=True)
        with st.form("rent_car_form"):
            car_type = st.selectbox("Jenis Mobil", ["Pilih Jenis Mobil", "Avanza", "Innova Reborn", "Hiace", "Jeep 4x4"])
            pickup_date = st.date_input("Tanggal Pengambilan")
            return_date = st.date_input("Tanggal Pengembalian")
            pickup_location = st.text_input("Lokasi Pengambilan", placeholder="Contoh: Surabaya")
            return_location = st.text_input("Lokasi Pengembalian", placeholder="Contoh: Malang")
            submitted_car = st.form_submit_button("Ajukan Sewa")
            if submitted_car:
                if car_type != "Pilih Jenis Mobil" and pickup_date and return_date and pickup_location and return_location:
                    st.success("🎉 Pengajuan sewa mobil berhasil! Kami akan segera menghubungi Anda.")
                else:
                    st.error("Mohon lengkapi semua data.")
        st.markdown('</div>', unsafe_allow_html=True)

def show_gallery():
    st.markdown('<a id="galeri"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Galeri 🖼️</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.125rem; color: #4a5568;'>Bagian ini akan menampilkan koleksi foto-foto perjalanan kami yang menakjubkan!</p>", unsafe_allow_html=True)
    gallery_images = [
        "https://images.unsplash.com/photo-1510414002633-91c6e12e131d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80",
        "https://images.unsplash.com/photo-1544464870-7634f107f96b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80",
        "https://images.unsplash.com/photo-1621941620865-c3f25c7e0c8b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80",
    ]
    cols = st.columns(len(gallery_images))
    for i, img_url in enumerate(gallery_images):
        with cols[i]:
            st.image(img_url, caption=f"Foto {i+1}", use_container_width=True)

def show_contact_us():
    st.markdown('<a id="hubungi-kami"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Hubungi Kami 📞</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="contact-form-container">', unsafe_allow_html=True)
        st.markdown("<h3>Kirimkan Pesan Anda</h3>", unsafe_allow_html=True)
        with st.form("contact_us_form"):
            name = st.text_input("Nama Lengkap")
            email = st.text_input("Email Anda")
            subject = st.text_input("Subjek")
            message = st.text_area("Pesan Anda", height=150)
            submitted_contact = st.form_submit_button("Kirim Pesan")
            if submitted_contact:
                if name and email and subject and message:
                    st.success("Terima kasih! Pesan Anda telah terkirim dan kami akan segera merespons.")
                else:
                    st.error("Mohon lengkapi semua kolom yang wajib diisi.")
        st.markdown('</div>', unsafe_allow_html=True)

def show_reviews():
    st.markdown('<a id="ulasan-kami"></a>', unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Ulasan Pelanggan ⭐</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.125rem; color: #4a5568;'>Lihat apa kata pelanggan kami tentang pengalaman perjalanan mereka bersama Septem Tour!</p>", unsafe_allow_html=True)
    reviews_data = [
        {"name": "Ani Sutra", "review": "Perjalanan ke Bromo sangat luar biasa! Pemandu ramah dan pelayanan prima."},
        {"name": "Budi Santoso", "review": "Paket tour Bali sangat terencana dengan baik. Rekomendasi sekali!"},
        {"name": "Citra Dewi", "review": "Sewa mobil di Septem Tour sangat mudah dan unitnya bersih. Top!"},
    ]
    
    for review in reviews_data:
        st.info(f"**{review['name']}**: {review['review']}")

def show_footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-logo">SEPTEM TOUR</div>
        <p class="footer-text">Jalan Raya Tidar, Malang, Jawa Timur</p>
        <div class="social-icons">
            <a href="#"><i class="fab fa-facebook-f"></i></a>
            <a href="#"><i class="fab fa-instagram"></i></a>
            <a href="#"><i class="fab fa-whatsapp"></i></a>
        </div>
        <p class="footer-copy">Hak Cipta © 2024 Septem Tour & Travel. Semua Hak Dilindungi.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Logic Halaman Utama ---
if st.session_state.show_navbar:
    with st.container():
        show_navbar()

st.markdown('<div class="content-container">', unsafe_allow_html=True)

if st.session_state.current_page == 'home':
    show_hero_section()
    show_about_us()
elif st.session_state.current_page == 'detail_tour':
    show_tour_detail(st.session_state.selected_tour)
elif st.session_state.current_page == 'tour_packages':
    show_tour_packages()
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