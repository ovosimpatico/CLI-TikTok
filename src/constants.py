# Do not change anything here
APP = {
    "name": "CLI TikTok",
    "version": 0.82
}


# Here are the app settings. You are free to configure this field
OPTIONS = {
    # This controls the Proxitok instance that will be scraped to obtain the URLs.
    "proxitok_instance": "https://proxitok.pabloferreiro.es",
    
    # This handles the command used to playback videos. It's heavily recommended to use MPV
    # Make sure your player can launch through the CLI and exits after playback
    "player_command": "mpv"
}