from numpy import ALLOW_THREADS, empty
from streamlit_echarts import st_echarts
import streamlit as st
from Renderer import HtmlBlock
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# custom environment variables
import env
# clean text
import Cleaner
# resume ranker
import Rank
# using NER
import Ner
# pdf miner
import Miner


# text -> categorize probability
def ModelPredictor(text: str) -> list:
    loaded_model = env.MODEL
    return loaded_model.predict_proba([Cleaner.CleanResume(text)])


def ProcessData(text=env.TESTCASE):
    category = ['Data Scientist ', 'Database Administrator', 'Java Developer', 'Network Administrator',
                'Project Manager', 'Python Developer', 'Security Analyst', 'Software Developer',
                'Systems Administrator', 'Web Developer']

    model_result = ModelPredictor(text)
    model_result = list(map(list, model_result))[0]

    context = []
    for i, item in enumerate(model_result):
        if model_result[i] > 0:
            context.append({"value": "{:.3f}".format(model_result[i]*100), "name": category[i]})

    st.write(model_result)
    relative_accuracy = sum(model_result) / len(context)
    st.write("data score: ", relative_accuracy)

    if relative_accuracy <= env.ALLOWED_ACCURACY:
        return False
    return context


def RunModel(text, ner=False):
    data = ProcessData(text=text)
    if data is not False:
        options = {
            "title": {
                "text": 'Resume Checker',
                "subtext": 'check resume',
                "left": 'center'
            },
            "tooltip": {
                "trigger": 'item'
            },
            "legend": {
                "orient": 'vertical',
                "left": 'left',
            },
            "series": [
                {
                    "name": 'category',
                    "type": 'pie',
                    "radius": '50%',
                    "data": data,
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": 10,
                            "shadowOffsetX": 0,
                            "shadowColor": 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        }

        st_echarts(
            options=options, height="600px",
        )
    else:
        st.write("Relative Document does not seem to be of any IT person")


if __name__ == '__main__':
    st.write("Resume Analyzer, ML model based on NLTK")
    mode = env.MODE
    empty = st.empty()
    divider = """<hr style="height:2px; border:none; color:#ac0000; background-color:#eee;" />"""

    # If statebool is already initialized, don't do anything
    if 'statebool' not in st.session_state:
        st.session_state.statebool = None

    # Create a button which will set statebool to scan
    if st.button('Scan Your Resume'):
        st.session_state.statebool = 'scan'

    if st.button('Fetch Ranked Resume'):
        st.session_state.statebool = 'fetch'


    # MODE check
    if env.MODE == 'dev':
        st.write('State: ', st.session_state.statebool)

    HtmlBlock(html=divider, height=20)


    if st.session_state.statebool == 'scan':
        uploaded_file = st.file_uploader("Enter you resume file")
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()

            tempPath = os.path.join(env.CACHE_PATH, Cleaner.NameGenerator())
            with open(file=tempPath, mode='wb') as file:
                file.write(bytes_data)

            text_string = Miner.MinePDF(tempPath)
            HtmlBlock(text_string, scrolling=True)
            RunModel(text=text_string)

    elif st.session_state.statebool == 'fetch':
        text_area_data = st.text_area("Enter Your Company Requirements", height=200)

        if not 'submit' in st.session_state:
            st.session_state.submit = None

        if st.button('submit'):
            st.session_state.submit = True

        if st.session_state.submit:
            st.write("Text area: ", text_area_data)

            ranked_data = Rank.RankResume(loaded_model=env.MODEL, text=text_area_data)
            
            
            context = pd.DataFrame({
                'SR No.': ranked_data.keys(),
                'Ranking': [x[0] for x in ranked_data.values()],
                'Text': [x[1] for x in ranked_data.values()]
            })

            st.dataframe(context, width=600, height=800)


