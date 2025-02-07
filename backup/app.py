import streamlit as st
import feedparser

# Função para ler o RSS
def ler_rss(url_rss):
    feed = feedparser.parse(url_rss)
    noticias = []
    for post in feed.entries:
        noticias.append({
            "Título": post.title,
            "Link": post.link,
            "Descrição": post.description
        })
    return noticias

# Lista de RSS
urls_rss = {
    "InfoMoney": "https://www.infomoney.com.br/feed/",
    "Exame": "https://exame.com/feed/"
}

# Interface com Streamlit
st.title("📢 Leitor de Notícias RSS")

# Escolher fonte RSS
opcao = st.selectbox("Escolha um site:", list(urls_rss.keys()))

# Botão para carregar
if st.button("Carregar Notícias"):
    noticias = ler_rss(urls_rss[opcao])
    for noticia in noticias:
        st.subheader(noticia["Título"])
        st.write(noticia["Descrição"])
        st.markdown(f"[Leia mais]({noticia['Link']})")
        st.write("---")