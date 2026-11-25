
import streamlit as st

from digitlens.history_store import history_dataframe
from digitlens.ui import render_header


def render_page():

    render_header(
        "Activity History",
        "Pantau aktivitas pengenalan angka yang dilakukan selama sesi aplikasi.",
    )

    history_df = history_dataframe()

    total = len(history_df)
    with_segments = (
        int((history_df["Kandidat digit"] > 0).sum())
        if total else 0
    )
    no_segments = total - with_segments

    # SUMMARY
    st.markdown("## Ringkasan aktivitas")

    col1, col2, col3 = st.columns(3, gap="medium")

    col1.metric("Total aktivitas", total)
    col2.metric("Kandidat digit ditemukan", with_segments)
    col3.metric("Tidak ditemukan", no_segments)

    st.write("")

    # HISTORY TABLE
    st.markdown("## Riwayat pemrosesan")
    st.caption(
        "Daftar gambar yang sudah diproses oleh DigitLens."
    )

    if history_df.empty:

        st.markdown(
            """
            <div class="soft-card" style="
                text-align:center;
                padding:45px 20px;
            ">
                <div style="font-size:38px;">◷</div>
                <h3 style="margin-top:12px;">
                    Belum ada aktivitas
                </h3>
                <p class="muted">
                    Riwayat akan muncul setelah kamu menjalankan
                    proses pengenalan angka.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        return

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True,
    )

    st.write("")

    # ACTIONS
    download_col, clear_col = st.columns([1, 1])

    csv_data = history_df.to_csv(index=False).encode("utf-8-sig")

    with download_col:
        st.download_button(
            "Download history (CSV)",
            data=csv_data,
            file_name="digitlens_history.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with clear_col:
        if st.button(
            "Clear history",
            type="secondary",
            use_container_width=True,
        ):
            st.session_state.scan_history = []
            st.session_state.last_segmentation = None
            st.rerun()

    st.caption(
        "Riwayat disimpan sementara di memori sesi. "
        "Menghapus riwayat tidak menghapus file gambar yang sudah tersimpan."
    )
