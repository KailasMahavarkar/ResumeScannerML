# # import streamlit.components.v1 as components
# import os

# def HtmlOpener(filename=None, assetDirectory='Atemp'):
#     rootPath = os.path.abspath(os.path.dirname(__file__))
#     assetPath = os.path.join(rootPath, assetDirectory)
#     filePath = os.path.join(assetPath, filename)
#     try:
#         with open(file=filePath, encoding='cp1252', mode='r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return False

# def HtmlRenderer(filename=None, width=None, height=None, scrolling=False):
#     return components.html(
#         html=HtmlOpener(filename=filename), width=width,
#         height=height, scrolling=scrolling
#     )

# def HtmlBlock(html, width=None, height=None, scrolling=False):
#     return components.html(
#         html=html, width=width,
#         height=height, scrolling=scrolling
#     )

# if __name__ == '__main__':
#     pass
#     # res = HtmlRenderer('Home.html', 600, 600, False)
#     # print(res)