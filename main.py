import streamlit as st
import positive
import negative
import multiplication
import division

st.title('Simple Calculator')

num1 = st.number_input("Enter the first number:")
operator = st.selectbox("Select operator", ('+', '-', '*', '/'))
num2 = st.number_input("Enter the second number:")

if st.button("Calculate"):
    try:
        if operator == '+':
            result = positive.positive(num1, num2)
        elif operator == '-':
            result = negative.negative(num1, num2)
        elif operator == '*':
            result = multiplication.multiplication(num1, num2)
        elif operator == '/':
            if num2 == 0:
                st.error("Division by zero is not allowed. Please try again.")
            else:
                result = division.division(num1, num2)
        st.success(f"The result of {num1} {operator} {num2} = {result}")
    except ValueError:
        st.error("Please enter valid numbers.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
