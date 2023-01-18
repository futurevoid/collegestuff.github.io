import streamlit as st


st.set_page_config(
         page_title="فرقه اولى ذكاء اصطناعي  Freshman FCAI AI ",
     page_icon="",
     initial_sidebar_state="collapsed",
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

subtitle= st.markdown(""" <h2 style = "color:rgb(0, 255, 255)"> <em>Electronics IT101</em> </h2> """,unsafe_allow_html=True)
content = st.markdown("""
## introduction to electronics english  

[Basic Electronics For Beginners By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=uXr4lXYjXuU)

## introduction to electronics arabic عربي  

[Introduction to electronics in Arabic](https://www.youtube.com/watch?v=iptorUBENF8)

## Ohm's Law  

[Ohm's Law By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=_rSHqvjDksg)

[Introduction to circuits and Ohm's law | Circuits | Physics | Khan Academy](https://www.youtube.com/watch?v=F_vLWkkOETI)

## Voltage Current and Resistance  

[Voltage Current and Resistance By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=08YugQce9OA)

## Series and Parallel Circuits  

[Series and Parallel Circuits By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=7mdc-lRrW1c)

## Diodes Explained  

[Diode Explained By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=g54vURe47gM)

## Semiconductors  

[Semiconductors By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=ethnHSgVbHs)

## Half wave Rectifiers  

[Half wave Rectifiers By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=joDlqsknn-w)

## Full wave Rectifiers  

[Full wave Rectifiers By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=pb5nzUBehyY)

## Full wave Bridge Rectifiers  

[Full wave Bridge Rectifiers By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=EkHch86UXpY)

## Zener Diodes  

[Zener Diodes By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=mmiHX_IzvDw)

## Clipper Circuits

[Clipper Circuits By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=HegEFPLSbLY)

## Clamper Circuits  

[Clamper Circuits By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=PRzrS6NOyAY)

## Transistors  

[Transistors By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=AcxDiesy-nI)

## Bipolar Junction Transistors (BJT)  

[Bipolar Junction Transistors (BJT) By TheOrganicChemistryTutor](h<https://www.youtube.com/watch?v=VJJuxQk5fTY)

## Voltage Multipliers  

[Voltage Multipliers - Half Wave Voltage Doubler Circuit By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=yfykYXdAUNY)

[Voltage Multipliers - Full Wave Voltage Doubler Circuit By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=iDQRB8DOJE4)

[Voltage Multiplier Circuit Using Diodes and Capacitors By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=litsAzP4oqw)

## Voltage Regulators

[Voltage Regulators By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=iomZgZYN3WY)

## Light Emitting Diodes (LEDs)  

[LEDs - Light Emitting Diodes - Basic Introduction By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=Hl4v1aUFWrs)

## Varactor Diodes  

[Varactor Diodes By TheOrganicChemistryTutor](https://www.youtube.com/watch?v=aXuM3eW1fcQ)
""",unsafe_allow_html=True)
