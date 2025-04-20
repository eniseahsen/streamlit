import streamlit as st
import fitz #PyMuPDF

st.title("PDF'ten OCR ile Metin Çıkarma ve Analiz Platformu")

uploaded_file = st.file_uploader("PDF dosyası yükleyin",type="pdf")

if uploaded_file:
    # wb: write binary->dosyayı ikili modda açar (PDF,resim,ses gibi dosyalar için)
    with open("temp.pdf","wb") as f:
        f.write(uploaded_file.read())

        doc = fitz.open("temp.pdf")
        extracted_text = []
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            extracted_text.append(f"---Sayfa {page_num}---\n\n"+text)
        full_text = "".join(extracted_text)  #join-> tek bir metin halie getiriyor

        st.subheader("Çıkarılan Metin: ")
        st.text_area("",full_text,height=400)


else:
    st.info("Lütfen PDF dosyası ekleyin..")




