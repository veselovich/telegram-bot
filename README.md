# "Useful people" teleram bot
#### Video Demo:  <URL HERE>
#### Description:

This project was done as a final project of [Harward CS50](https://cs50.harvard.edu/x/2023/) course.

While creating, materials of ["Telegram Bot (aiogram) - essentials"](https://www.youtube.com/watch?v=ayUBlf9pvn0&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr) was used.
***
#### Project
Project is a Python Aiogram library-based application for [Telegram](https://telegram.org) messenger. This bot has a database, which stores an information about users of this bot. Each user can add infomation about itself (only) or search for an other random user. No registration is needed. An idea of the bot is to help people to find each other by information they provided about themselves.
***
#### Core Files
- **main.py** - main executive file
- **database.py** - contains functions, that allowes to lauch, shutdown and use database
- **keyboards.py** - contains functions, that gives user access to keyboards
- **profile.db** - database file, which contains information about users who created their profiles
***
#### Deployment files ([Heroku](https://heroku.com/)):
- **Procfile**
- **runtime.txt**
- **requirements.txt**

_Please notice:_
- _For deployment you need bot account using [BotFather](https://t.me/BotFather)_
- _config.py file contains testing API and not required for deployment. Use Heroku CLI to assign API_TOKEN_
***
#### Roadmap
- [x] basic commands handlers
- [x] profile creating process (using FSM)
- [x] database connection (using sqlite3)
- [x] random contact search (using CallbackQuery)
- [ ] categorizing contacts/search by categories
- [ ] like/dislike system
- [ ] profile rating
- [ ] inline mode of the bot
- [ ] antiflood throttler
- [ ] connecting to the payment system
***
#### License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/veselovich/tg-bot/blob/main/MIT-LICENSE.txt) file for details.
