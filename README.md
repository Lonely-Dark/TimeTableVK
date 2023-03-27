![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![GitHub repo size](https://img.shields.io/github/repo-size/Lonely-Dark/TimeTableVK?style=flat-square)
![GitHub](https://img.shields.io/github/license/Lonely-Dark/TimeTableVK?style=flat-square)

# TimeTableVK
Raspisanie_bot is a Python-based project designed to help students at the Lyceum find out their class schedules for the next day or any other date. The project is built using the poetry package manager.

## Installation
Clone the repository:

```bash
git clone https://github.com/Lonely-Dark/TimeTableVK
```
Install the required dependencies:

```bash
cd TimeTableVK/timeTableVk
poetry install
```

Create a .ini file in the root directory and add your vk token and your group_id. The .ini file should have the following format:
```makefile
[DEFAULT]
TOKEN=your_bot_token_here
GROUP_ID=group_id_here
```
## Usage
To run the bot, activate the poetry environment by running:

```bash
poetry shell
```
Then, run the bot by executing the following command:

```bash
python timeTableVk/main.py
```
You can now use the bot to get the schedule for the next day by typing 'Привет' in your Telegram chat with the bot.

To get the schedule for a specific date, type '6A 09', replacing 6A with the class and 09 with date.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue on GitHub. If you would like to contribute code, please fork the repository and submit a pull request.