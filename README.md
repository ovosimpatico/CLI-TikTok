<p align="center">
    <a href="https://github.com/ovosimpatico/CLI-TikTok/">
        <img src="docs/assets/logo.png" alt="Logo" width="160" height="160">
    </a>

<h2 align="center"> TikTok CLI tool</h2>

[![Discord][discord-shield]][discord-url]
[![Downloads][downloads-shield]][downloads-url]
[![Language][language-shield]][language-url]
[![License][license-shield]][license-url]

<ol>
    <li><a href="#about-the-project">About the Project</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#a-note-about-web-scraping">Web Scraping Warning</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
</ol>


> ### State of the project
>
> TikTok-CLI is no longer functional due to issues with our main data source, [Proxitok](https://github.com/pablouser1/ProxiTok).
>
> The project is currently discontinued and I will no longer be actively maintaining or developing it.
>
> However, I'm open to community contributions:
> - If you'd like to submit pull requests or bug fixes, I'll still review and add them.
> - If anyone is interested in taking over the project's development, please reach out to me.
>
> I appreciate the interest and support from the community. While I recommend users look for alternative solutions, I'm grateful for any efforts to keep this project alive.
>
> Thank you to everyone who has used or contributed to TikTok-CLI.

## About the project
This is a TikTok archiver and viewer. It supports watching or archiving your liked tiktoks or from a specific creator.

## Installation

####    If you have [Chocolatey](https://chocolatey.org/) installed, run `choco install mpv python` and skip steps 1 and 2.

1) Download the latest version of [Python](https://www.python.org/downloads/), make sure it is added to the PATH. (This is an option on installation.)

2) Download the latest version of [MPV](https://mpv.io/installation/), make sure it is added to the PATH.

3) Download the [source code](https://github.com/ovosimpatico/CLI-TikTok/archive/refs/heads/main.zip) (recommended) or the latest [release](https://github.com/ovosimpatico/CLI-TikTok/releases).

4) Extract **all** files to an empty folder.

5) Move your `user_data.json` file to the folder. Refer to [How to get video list](docs/HowToGetVideoList.md)
 for more details on how to get yours.

6) Open a terminal within the folder.

7) Run `main.py`

## A note about web scraping

This software scrapes a third-party website (Proxitok) to obtain the data required. In a larger scale, this can be very bad for the website administrators.

[See my in-depth note about this here](docs/WebScraping.md)

If you use CLI Tiktok for more than light tasks, consider [running your own Proxitok instance](https://github.com/pablouser1/ProxiTok/wiki/Self-hosting).

## Contributing

Any contributions you make are **greatly appreciated**.

## Acknowledgements

- [MPV](https://mpv.io/)
- [YT-DLP](https://github.com/yt-dlp/yt-dlp)
- [ProxiTok](https://github.com/pablouser1/ProxiTok)

## Disclaimer
This project is not associated or endorsed by ByteDance. ByteDance, and all associated properties are trademarks or registered trademarks of ByteDance Ltd.

By using this software, you acknowledge that use of this software is done so at your own risk.



[downloads-shield]: https://img.shields.io/github/downloads/ovosimpatico/CLI-TikTok/total?style=for-the-badge&logo=github
[downloads-url]: https://github.com/ovosimpatico/CLI-TikTok/releases/latest

[language-shield]: https://img.shields.io/github/languages/top/ovosimpatico/CLI-TikTok?logo=python&logoColor=yellow&style=for-the-badge
[language-url]: https://www.python.org/

[license-shield]: https://img.shields.io/github/license/ovosimpatico/CLI-TikTok?style=for-the-badge
[license-url]: https://github.com/ovosimpatico/CLI-TikTok/blob/main/LICENSE

[discord-shield]: https://img.shields.io/discord/1068543728274382868?color=7289da&label=Support&logo=discord&logoColor=7289da&style=for-the-badge
[discord-url]: https://discord.gg/7qK8sfEq2q
[discord-banner]: https://discordapp.com/api/guilds/1068543728274382868/widget.png?style=banner2
