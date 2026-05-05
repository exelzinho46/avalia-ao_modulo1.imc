import streamlit as st

st.title("calculadore IMC 📱")
st.subheader("feito com streamlit ❤️")

altura = st.number_input("digite a sua altura", min_value=0.0)
peso = st.number_input("digite o seu peso", min_value=0.0)
if st.button("Calcular"):
    imc = peso / altura ** 2
    st.info(f"{imc:.2f}")
    
    if imc < 18.5:
       
        st.error("abaixo do peso ")
    
    elif imc < 24.9:
        
        st.success("no peso irmao ")
    elif imc < 29.9:
        
        st.warning("sobrepeso ")
    elif imc < 34.9:
        
        st.error("obesidade ")
    elif imc < 39.9:
       
        st.error("obesidade severa ")
    else:
       
        st.error("obesidade morbida ")

    
