
import pandas as pd
import streamlit as st

from digitlens.ui import render_header


def render_page():

    render_header(
        "About DigitLens",
        "Tujuan, teknologi, alur pemrosesan, dan ruang lingkup prototype.",
    )

    st.markdown(
        """
        <div class="soft-card" style="padding:25px;">
            <div class="eyebrow">ABOUT THE PROJECT</div>
            <h2 style="margin:10px 0;color:#0F1515;">
                What is DigitLens?
            </h2>
            <p style="color:#526B69;line-height:1.9;">
                DigitLens merupakan prototype aplikasi pengenalan
                rangkaian digit dari gambar. Sistem menyiapkan gambar,
                memisahkan kandidat digit, mengklasifikasikan setiap
                potongan menggunakan model CNN, lalu menyusun hasilnya
                kembali dari kiri ke kanan.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # WORKFLOW
    st.markdown("## Cara kerja DigitLens")
    st.caption("Lima tahapan dalam proses pengenalan angka.")

    process_items = [
        ("01", "Input", "Pengguna mengunggah gambar berisi angka."),
        ("02", "Preprocessing", "Gambar diubah menjadi grayscale dan disiapkan."),
        ("03", "Segmentation", "Area kandidat digit ditemukan dan dipotong."),
        ("04", "Classification", "CNN mengklasifikasikan setiap potongan menjadi 0–9."),
        ("05", "Sequence", "Hasil digit digabungkan dari kiri ke kanan."),
    ]

    first_row = st.columns(3, gap="medium")

    for col, (number, title, description) in zip(
        first_row, process_items[:3]
    ):
        with col:
            st.markdown(
                f"""
                <div class="soft-card" style="min-height:175px;">
                    <span class="step-number">{number}</span>
                    <h3 style="font-size:1.1rem;margin-top:15px;">
                        {title}
                    </h3>
                    <p class="muted" style="font-size:.88rem;line-height:1.7;">
                        {description}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    second_row = st.columns(2, gap="medium")

    for col, (number, title, description) in zip(
        second_row, process_items[3:]
    ):
        with col:
            st.markdown(
                f"""
                <div class="soft-card" style="min-height:150px;">
                    <span class="step-number">{number}</span>
                    <h3 style="font-size:1.1rem;margin-top:15px;">
                        {title}
                    </h3>
                    <p class="muted" style="font-size:.88rem;line-height:1.7;">
                        {description}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    # ALGORITHMS
    st.markdown("## Algoritma yang dibandingkan")
    st.caption(
        "Tiga algoritma yang direncanakan dalam eksperimen evaluasi."
    )

    algorithms = [
        (
            "CNN",
            "Convolutional Neural Network",
            "Deep Learning yang mempelajari pola visual pada citra digit.",
        ),
        (
            "SVM",
            "Support Vector Machine",
            "Algoritma klasifikasi yang mencari batas pemisah antar kelas.",
        ),
        (
            "RF",
            "Random Forest",
            "Ensemble Learning yang menggabungkan banyak decision tree.",
        ),
    ]

    algo_cols = st.columns(3, gap="medium")

    for col, (short, full, description) in zip(algo_cols, algorithms):
        with col:
            st.markdown(
                f"""
                <div class="soft-card" style="min-height:190px;">
                    <div class="eyebrow">{short}</div>
                    <h3 style="font-size:1.1rem;margin-top:12px;">
                        {full}
                    </h3>
                    <p class="muted" style="font-size:.88rem;line-height:1.7;">
                        {description}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")

    # DEVELOPMENT STATUS
    st.markdown("## Status pengembangan")

    status_df = pd.DataFrame(
        [
            {"Komponen": "Upload dan preview gambar", "Status": "Ready"},
            {"Komponen": "Informasi gambar", "Status": "Ready"},
            {"Komponen": "Preprocessing gambar", "Status": "Ready"},
            {"Komponen": "Segmentasi connected components", "Status": "Prototype ready"},
            {"Komponen": "Integrasi klasifikasi CNN", "Status": "Implemented"},
            {"Komponen": "SVM dan Random Forest di aplikasi", "Status": "Not integrated"},
            {"Komponen": "Penggabungan hasil digit", "Status": "Implemented"},
            {"Komponen": "Riwayat dan export CSV", "Status": "Ready"},
        ]
    )

    st.dataframe(
        status_df,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        "Status Implemented menunjukkan kode integrasi sudah tersedia; "
        "pengujian runtime dan evaluasi model tetap perlu diverifikasi."
    )

    # LIMITATIONS
    st.markdown("## Ruang lingkup dan keterbatasan")

    st.warning(
        "DigitLens saat ini ditujukan untuk satu baris angka yang "
        "terpisah dengan jelas. Angka yang saling menempel, tulisan "
        "bertingkat, banyak baris, latar kompleks, atau goresan digit "
        "yang terputus dapat menyebabkan segmentasi kurang tepat.",
        icon="⚠️",
    )

    st.info(
        "Hasil pengenalan dipengaruhi kualitas gambar, keberhasilan "
        "segmentasi, dan kesesuaian preprocessing dengan data training.",
        icon="ℹ️",
    )
