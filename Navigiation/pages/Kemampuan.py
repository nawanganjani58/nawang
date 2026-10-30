
import streamlit as st

st.title("💻 Kemampuan Saya")

st.write("""
Berikut adalah beberapa kemampuan yang sedang
saya pelajari dan kembangkan.
""")

st.divider()

st.subheader("Kemampuan Pemrograman")

st.write("🐍 Python")
st.progress(60)

st.write("🌐 HTML dan CSS")
st.progress(50)

st.write("📊 Pengolahan Data")
st.progress(55)

st.write("🖥️ Streamlit")
st.progress(60)

st.divider()

st.subheader("Kemampuan Lainnya")

st.markdown("""
- Komunikasi
- Kerja sama tim
- Manajemen waktu
- Pemecahan masalah
- Kemauan untuk belajar
""")

st.success("Saya akan terus mengembangkan kemampuan saya.")
