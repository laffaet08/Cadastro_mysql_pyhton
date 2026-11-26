import streamlit as st
import banco

st.title("HortiFruti")
st.write("Cadastro de Produtos")

with st.form("cadastro", clear_on_submit=True):
    nome=st.text_input("Nome do Produto")
    categoria=st.selectbox("Categoria", ["Fruta", "Verdura", "Legume"])
    preco = st.number_input("Preço R$", min_value=0.0,step=0.50)
    enviar = st.form_submit_button("Cadastrar")

## Verificação de erro
if enviar:
    if nome == "":
        st.warning("Digite o nome do produto!")
    else:
        banco.cadastrar(nome, categoria, preco)
        st.success("Cadastrado")
        