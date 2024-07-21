[![MIT License][license-shield]][license-url]

<!-- Project Title and description -->
<br />
<div align="center">
  <a href="https://github.com/santi224m/1001-albums-picker">
    <img src="https://raw.githubusercontent.com/santi224m/1001-albums-picker/main/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Albums Picker</h3>

  <p align="center">
    Picks a random album from <a href="https://en.wikipedia.org/wiki/1001_Albums_You_Must_Hear_Before_You_Die">1001 Albums You Must Hear Before You Die</a>
    or from <a href="https://www.qobuz.com/us-en/awards/qobuz/discotheque_ideale/download-streaming-albums">The Qobuz Essential Discography</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

![1001 Albums Picker Screen Shot][terminal-screenshot]

Running the program selects an album at random from the book [1001 Albums You Must Hear Before You Die](https://en.wikipedia.org/wiki/1001_Albums_You_Must_Hear_Before_You_Die) or from [The Qobuz Essential Discography](https://www.qobuz.com/us-en/awards/qobuz/discotheque_ideale/download-streaming-albums) if you use the ```--qobuz``` argument. The goal of the project is to help people find new music.

<!-- INSTALLATION -->
## Installation

The recommended method for installing ```albums-picker``` is [pipx](https://pipx.pypa.io/stable/):

```bash
pipx install albums-picker
```

To use with pip instead:

```bash
pip install albums-picker
```

<!-- USAGE EXAMPLES -->
## Usage

You can run ```albumsPicker``` just by typing:

```bash
albumsPicker
```

```bash
usage: albumsPicker [--qobuz] [--json] [--help]

Choose a random album from "1001 Albums You Must Hear Before You Die" or from "The Qobuz Essential Discography"

options:
  -h, --help   show this help message and exit
  -j, --json   Print album in json format
  -q, --qobuz  Choose an album from The Qobuz Essential Discography
```

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/santi224m/1001-albums-picker.svg?style=for-the-badge
[license-url]: https://github.com/santi224m/1001-albums-picker/blob/main/LICENSE
[terminal-screenshot]: https://raw.githubusercontent.com/santi224m/1001-albums-picker/main/images/screenshot_updated.png
<a href="https://www.flaticon.com/free-icons/vinyl" title="vinyl icons">Vinyl icons created by Freepik - Flaticon</a>
