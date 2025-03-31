import streamlit as st
import pandas as pd
import funcoes

st.title("Cadastro de Clientes")
nome = st.text_input("Digite o seu nome: ")
telefone = st.text_input("Digite seu número de telefone: ")
endereco = st.text_input("Digite o seu endereço: ")

if st.button("Adicionar cliente"):
    funcoes.inserirDados(nome, telefone, endereco)
    st.success("Cliente adicionado com sucesso!")

if st.button("Listar clientes"):
    dados = funcoes.listarDados()
    tb = pd.DataFrame(dados, columns=["ID", "Nome", "Telefone", "Endereco"])
    st.header("Lista de Clientes")
    st.table(tb)