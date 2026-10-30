import streamlit as st
st.title("📱 Media Sosial Saya")

st.write("""
Selamat datang di halaman media sosial saya.
Kamu bisa mengunjungi akun Instagram saya melalui
tombol di bawah ini.
""")

st.divider()

st.subheader("📸 Instagram Saya")

st.markdown("""
Hai semuanya! 👋
Yuk, kunjungi akun Instagram saya untuk melihat
foto dan aktivitas saya.
""")

st.link_button(
    "📷 Kunjungi Instagram Saya",
    "https://www.instagram.com/nwnganjani?dlrf=MW0waGJjaGIwZDNvZQ%3D%3D&utm_source=qr"
)

st.divider()

st.write("📷 Username: @nwnganjani")

st.caption("Terima kasih sudah mengunjungi media sosial saya ❤️")