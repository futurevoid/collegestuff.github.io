import streamlit as st


st.set_page_config(
         page_title="CS Fundamentals CS101",
     page_icon="",
     initial_sidebar_state="auto",
 )



remove_menu_footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility:hidden; }
</style>
"""

css = st.markdown("""<style>
.list1{
  text-align: center;
  }
  html body div#root div div.withScreencast div div.stApp.css-ffhzg2.eczokvf1 div.appview-container.css-1wrcr25.egzxvld4 section.main.css-k1vhr4.egzxvld3 footer.css-1lsmgbg.egzxvld0{
    visibility: hidden;
  }
  html body div#root div div.withScreencast div div.stApp.css-ffhzg2.eczokvf1 header.css-1avcm0n.e8zbici2 div.css-14xtw13.e8zbici0 span#MainMenu button.css-1rs6os.edgvbvh3{
    visibility: hidden;
  }
  html body div#root div div.withScreencast div div.stApp.css-ffhzg2.eczokvf1 header.css-hy8qiv.e8zbici2{
    visibility:hidden;

  }
  .css-1avcm0n{
      visibility:hidden;
    
  }
  #root > div:nth-child(1) > div.withScreencast > div > div > header{
      visibility:hidden;
      }
  </style>""",unsafe_allow_html=True)

title = st.markdown("<h1>كل الروابط المفيده للمقررات الفرقه الاولى في الذكاء الاصطناعي التطبيقي</h1>",unsafe_allow_html=True)
st.title("""All useful links for Freshmen FCAI Applied AI""")

subtitle= st.markdown(""" <h2 style = "color:rgb(0,250,154)"> <em>CS Fundamentals</em> </h2> """,unsafe_allow_html=True)
content = st.markdown("""
                      
##Generations of Computers   

[Generations of Computers](https://youtu.be/FLst_k_eWkE)

## Read-Only Memory (ROM)

[Read-Only Memory (ROM)](https://youtu.be/8UZvuoIzfFM)

## Random Access Memory (RAM)

[Random Access Memory (RAM)](https://www.youtube.com/watch?v=PVad0c2cljo)

## CPU Cache Explained - What is Cache Memory?

[CPU Cache Explained - What is Cache Memory?](https://www.youtube.com/watch?v=yi0FhRqDJfo)

## What is a System Bus?

[What is a System Bus?](https://youtu.be/3gtrJarCmY8)

## What is a Source Code?

[What is a Source Code?](https://www.youtube.com/watch?v=QFKkOYeB-VY)


















""",unsafe_allow_html=True)