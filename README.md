## ![alt tag](https://s28.postimg.org/mjrge9wf1/Logomakr_4u33_PB.png/)

An application that uses motion detection to allow the user to use their hands to write text, and send it to friends on Facebook and Twitter. Project for HackTheValley 2017.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installation

1. `git clone` the repo onto your computer.
2. Run `pip install requirements.txt` to install all python dependencies
3. Run `npm install` to install all node.js dependencies
4. Download and unzip the [Leap Motion SDK](https://developer.leapmotion.com/get-started/).

To begin the application, run `run.bat`.

## Demo

See a video [here](https://www.youtube.com/watch?v=1UKUhG-x6Zc).

## Usage

Overview: Your left hand is used for controlling when data is being recorded, and the right hand is used as a cursor.

Details:
* To prepare to write, place both hands over the sensor and do an upward movement with your left hand.
* Point your index finger on your left hand. This is the finger you "write" with.
* Ball your left hand into a fist to start recording your righ hand index finger's movements. These movements appear on screen.
* When you want to "lift your pen off of the paper" open your left hand again. Use this to move from letter to letter.
* To erase, open your right and keep your left hand balled into a fist.
* To undo, swipe left hand upwards.
* To adjust your brush size, hover over one of the red squares on the left of the screen with your right hand index finger. There are three size, large (top), medium (middle), and small (bottom).
* Once satified with your image, swipe left to send a Facebook message OR swipe right with your left hand to post to Twitter.

## Built With

* [Leap Motion SDK](https://developer.leapmotion.com/get-started/) - a motion sensor used to detect hand movements.
* [Google Cloud Vision API](https://cloud.google.com/vision/docs/) - For the .jpg to text conver
* [imgurpython](https://github.com/Imgur/imgurpython) - Used to host images temporarily when passing images to Google Cloud API.
* [facebook-chat-api](https://github.com/Schmavery/facebook-chat-api) - Used to make Facebook posts.
* [twitter-api](https://github.com/geduldig/TwitterAPI) - Used to make Twitter posts.
* [pyGame](http://www.pygame.org/lofi.html) - Used to make canvas/writing interface.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for detail.
