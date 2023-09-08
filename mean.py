import streamlit as st
import numpy as np

def calculate_mean(degrees):
    mean = np.mean(degrees)
    return mean

def main():
    st.header("calculate the mean of students degrees")
    st.write("Enter the degrees of students:  ")

   
    degrees = st.text_input("Enter degrees(useing commn)")

    if degrees:
       
        degrees_list = [float(x.strip()) for x in degrees.split(',')]

        if len(degrees_list) > 0:
            
            mean = calculate_mean(degrees_list)
            st.write("Mean:", mean)

if __name__ == "__main__":
    main()