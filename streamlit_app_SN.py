import streamlit as st
from Pages.pages_1 import func_page_1
from Pages.pages_2 import func_page_2
from datetime import datetime
from Views import FeedView, AddPostView
from Services import get_feed, add_post
AddPostView(add_post)
st.write("___")
FeedView(get_feed)

st.set_page_config(

    page_title='Hello world',
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello world**'
        }
)
st.sidebar.title("🎈 Hello World")
st.title('🎈 Hello world')

st.title("Clock")
clock = st.empty()
while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info('**Current time: ** %s' % (time))
    if time == '22:08:00':
        clock.empty()
        st.warning("Time's up!")
        break

def main():
    st.sidebar.subheader('Page selection')
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page',
    'Page 1','Page 2'])
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page_1,
        'Page 2': run_page_2
    }

    # Run selected page
    pages_main[page_selection]()

def main_page():
    st.title('Main Page')
def run_page_1():
    func_page_1()
def run_page_2():
    func_page_2()
if __name__ == '__main__':
    main()
