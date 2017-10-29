# sport-yello
A Twitter chatbot that tweets latest news in the field of sports. Say [yello](https://twitter.com/sport_yello)! 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software. 
Please check out the blogs mentioned under Acknowledgements to see a detailed way of how to get the softwares installed and running. 


-[Python 3.x](https://www.python.org/downloads/release/python-362/) 
-[Heroku](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
-[Git bash](https://git-scm.com/downloads)  



## Deployment

To repeatedly post tweets, you could keep the script running in the background but that'd mean you'd need to keep your system running and connected 24x7. 

Or you could use: 
- Heroku 
- nohup 
- Cron 

I used Heroku for deployment. It seemed easier since I have a Windows machine and I was lazy to search for equivalent Bash commands for Win. 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you [Lauren Orsini](https://readwrite.com/author/lauren-orsini/) for the writing this [fantastic blog](http://readwrite.com/2014/06/20/random-non-sequitur-twitter-bot-instructions/?_escaped_fragment_=) upon which the blog below was based
* Thank you [@Sarah](https://tutorials.botsfloor.com/@sarahnadia) for this [awesome blog](https://tutorials.botsfloor.com/how-to-code-a-simple-twitter-bot-for-complete-beginners-36e37231e67d) that truly fills up some blanks
* Hat tip to [Tom Meagher](https://github.com/tommeagher/heroku_ebooks) for his git repo that houses the heroku worker script! 

## Future Work 

For starters, I hope to implement a bot from scratch and use tweepy. 
Currently, the bot can only tweet. It cannot RT, DM or reply. 

[Tweepy](http://docs.tweepy.org/en/v3.5.0/index.html) has a lot of cool methods that'll allow me to extend the functionalities of the bot. For e.g. find relevant hashtags according to location, locate relevant people to follow, etc. and those listed above. 
