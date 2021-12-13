<div id="top"></div
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<br />
<!--
<div align="center">
  <a href="https://github.com/itzilly/pygimkitplayer">
    <img src="https://github.com/itzilly/PyGimkitPlayer/icon.png" alt="Logo" width="120" height="120">
  </a>
-->
<h3 align="center">PyGimkitPlayer</h3>

  <p align="center">
    A basic 'cheat' for Gimkit Live
    <br />
    <a href="https://github.com/itzilly/pygimkitplayer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/itzilly/pygimkitplayer">View Demo (Coming Soon!)</a>
    ·
    <a href="https://github.com/itzilly/pygimkitplayer/issues">Report Bug</a>
    ·
    <a href="https://github.com/itzilly/pygimkitplayer/issues">Request Feature</a>
  </p>
</div>


<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#created-with">Created With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <!-- <li><a href="#Build">Build</a></li> -->
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<br></br>
## About The Project

This is a simple script to help you win easy Gimkit games. Using a learning-style loop, this script searches its local database for the answer to the question. If no answer has been logged, it will take a random guess. This will then reveal the answer whether the guess is correct or incorrect. The script then logs the question and its correlating answer in a json file the script can call at any time. (As well as allow the user to input the correct answer). As of now, this script is extremely inconsistent, reading the wrong text from the screen, and if the question or answer aren't exactly the same (case sensitive) it will not recognize if the question/answer has been logged.   

<p align="right"><a href="#top">Top</a></p>



<br></br>
### Created With

* [Python 3.10](https://www.python.org/downloads/release/python-3100)
* [PyTesseract](https://github.com/madmaze/pytesseract)
* [OpenVC](https://github.com/opencv/opencv-python)
* [Tesseract](https://tesseract-ocr.github.io)

<p align="right"><a href="#top">Top</a></p>


## Getting Started

How to use this script on your computer.

<br></br>
### Prerequisites

These are the must-haves to clone this script:
* Python 3.10
* Windows/Mac/Linux Operating System (This script will NOT work on a chromebook!)
* Git (<a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">How to install GIT</a>)
* Tesseract OCR (How to install Tesseract for <a href="https://github.com/UB-Mannheim/tesseract/wiki">Windows 10</a>, <a href="https://www.oreilly.com/library/view/building-computer-vision/9781838644673/95de5b35-436b-4668-8ca2-44970a6e2924.xhtml">Mac</a>, <a href="https://linuxhint.com/install-tesseract-ocr-linux/">Linux</a>)

<br></br>
### Installation
1. Open your terminal window (or git window) and copy and paste the following:
    ```git
    $ git clone https://github.com/itzilly/PyGimkitPlayer/PyGimkitPlayer.git
    ```
2. cd into the cloned directory
    ```sh
    $ cd PyGimkitPlayer
    ```
3. Install the required libraries:
    ```sh
    $ pip install -r requirements.txt
    ```
4. Open `tesseract_call.py` in your favorite text editor. Set the variable named ``'tesseract_installation_location'`` to the FULL path of the executable of Tesseract (which you should have already done)
(Example: tesseract_installation_location = "C:\\Program Files (x84)\\Tesseract-OCR\\tesseract.exe)"

5. Save and exit your text editor
6. Run the script:
    ```sh
    python main.py
    ```

<!--
<br></br>
### Installation
(This is if you want to run the program, not edit it!)

1. Download the zip file from the <a href=https://github.com/itzilly/PyGimkitPlayer/releases>releases</a> page
2. Extract the contents to a folder of your choice
3. Run `install.exe` if on windows. If you're on Mac or Linux, you need to clone the repo Follow the steps in <a href="#Build">Build</a>
4. Enjoy!
<p align="right"><a href="#top">Top</a></p>

<!--
<br></br>
### Build
1. Open your terminal window and copy and paste
    ```git
    $ git clone https://github.com/itzilly/PyGimkitPlayer/PyGimkitPlayer.git
    ```
2. cd into the cloned directory
    ```sh
    $ cd PyGimkitPlayer
    ```
3. Install the required libraries:
    ```sh
    $ pip install -r requirements.txt
    ```
4. Download and install `tesseract` (<a href="https://www.oreilly.com/library/view/building-computer-vision/9781838644673/95de5b35-436b-4668-8ca2-44970a6e2924.xhtml")>Mac</a>, <a href="https://linuxhint.com/install-tesseract-ocr-linux/">Linux</a)
5. Open your

<br></br>
<br></br>
-->
## License

Distributed under the MIT License. See <a href="https://github.com/itzilly/PyGimkitPlayer/LICENSE.txt">`LICENSE.txt`</a> for more information.

<p align="right"><a href="#top">Top</a></p>


[issues-shield]: https://img.shields.io/github/issues/itzilly/PyGimkitPlayer.svg?style=for-the-badge
[issues-url]: https://github.com/itzilly/PyGimkitPlayer/issues
[releases-url]: https://github.com/itzilly/PyGimkitPlayer/releases
[license-shield]: https://img.shields.io/github/license/itzilly/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/itzilly/PyGimkitPlayer/LICENSE.txt
