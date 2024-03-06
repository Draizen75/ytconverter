# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

import streamlit as st
import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError
import base64

# Function to download video as mp3
def download_audio(url):
    try:
        yt = YouTube(url)
        st.write("Checking...")
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        st.success("Checking Complete!")
        st.write("Title: ", yt.title)
        
        # Read the file as bytes
        with open(new_file, "rb") as file:
            audio_bytes = file.read()
        
        # Download button
        b64 = base64.b64encode(audio_bytes).decode()
        href = f"data:audio/mp3;base64,{b64}"
        
        st.markdown(f'<a href="{href}" download="audio.mp3"><button>Download Audio</button></a>', unsafe_allow_html=True)
        
    except RegexMatchError:
        st.error("Invalid YouTube URL. Please enter a valid URL.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Main function for Streamlit app
def main():
    st.title('YouTube to MP3 Downloader')
    st.write("Enter a YouTube video URL below:")
    url = st.text_input("URL:")
    if st.button("Check"):
        if url.strip() != "":
            download_audio(url)
        else:
            st.warning("Please enter a YouTube URL.")

if __name__ == "__main__":
    main()

