from pytube import YouTube

try:
    # Ask the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")
    
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Ask user for download location
    download_location = input("Enter the download location (leave blank for current directory): ").strip()
    if download_location == "":
        download_location = None  # Download to the current directory if blank
    
    # Ask user for video resolution
    print("Available Resolutions:")
    for stream in yt.streams.filter(progressive=True):
        print(stream.resolution)
    
    resolution_choice = input("Enter preferred resolution (e.g., '720p'): ").strip()

    # Get the stream with the chosen resolution
    selected_stream = yt.streams.filter(progressive=True, resolution=resolution_choice).first()
    
    # Download the video to the specified directory
    if download_location:
        selected_stream.download(download_location)
    else:
        selected_stream.download()
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
