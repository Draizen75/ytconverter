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
