from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.1.0',
    author='Sarthak Jaggi',
    author_email='jaggisarthak4@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)