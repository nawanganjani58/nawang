import streamlit as st
st.title("👤 Profil Saya")

col1, col2, col3 = st.columns([1, 2, 3])

with col1:
    st.image(
        "Navigiation/pages/nawang.jpeg",
        caption="Foto Profil",
        use_container_width=True
    )

with col2:
    st.header("Biodata")

    st.write("**Nama:** Nawang Anjani")
    st.write("**Tempat Tinggal:** Jambi")
    st.write("**Status:** Mahasiswa")
    st.write("**Program Studi:** Sistem Informasi")
    st.write("**Hobi:** Bermain voli")

st.divider()

st.subheader("Tentang Saya")

st.write("""
Saya adalah seorang mahasiswa yang tertarik mempelajari
teknologi informasi, pemrograman, dan pengembangan website.
Saya terus belajar untuk meningkatkan kemampuan dan
menambah pengalaman di bidang teknologi.
""")
