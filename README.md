# __CSCA20 Project Report: Fall 2019__

You will submit a copy of this report on Quercus each week between now and the end of the project. Each team member will need to submit a copy, so that we can go back and see what you've done over time. Your project may (and probably will) change as you progress, and that's okay, but we want to be able to track that progression.

## __Team Members__
#### Team Member A
- __First Name:__ Mengyu
- __Last Name:__ Wang
- __Student Number:__ 1002917739
- __UofT E-mail Address:__ wangmengyu.wang@mail.utoronto.ca


#### Team Member B
- __First Name:__ Huixin
- __Last Name:__ Liu
- __Student Number:__ 1002100282
- __UofT E-mail Address:__ huixi.liu@mail.utoronto.ca

#### Team Member C
- __First Name:__ Shihan
- __Last Name:__ Hu
- __Student Number:__ 1003265496
- __UofT E-mail Address:__ qunnie.hu@mail.utoronto.ca

#### Team Member D
- __First Name:__ Jinxin
- __Last Name:__ Leng
- __Student Number:__ 1002928013
- __UofT E-mail Address:__ jinxin.leng@mail.utoronto.ca


## __Project Plan__

__Project Title:__ Flight information database

__Project Description:__
The flight information database should have the following function when the user input departure city, destination, whether want a non-stop flight and whether need price sorted:
Output all the flights that the user can take from departure city to destination(including direct and one-stop flights).
Take the time of transferring between flights and show whether if the flight needs an extra day or even 2 extra days.
Take price into consideration and list the flights according to price low to high.
Able to identify capital letter and space.
Still return "No nonstop flight/No onestop flight" if no flight was found, or input was not valid.

## __Weekly Reports__
__Week 1:__
- Select 15-20 cities and input the flight information as a csv file.
- Start to add functions to the csv file.

__Week 2:__
- CSV file for data storage of flight information is completed.
- The logic parts for the program is completed and tested.
- Trying to add the listing function and make the output more readable.

__Final week:__
- The code was finished with price sorted function.
- Tested and improved the notes and small errors.
- Made sure the code is running sucessfully and did not go crash.
- After presenting the project in this week's turorial, our group summerized and organized what we want to say in the video and made a video which introduced all the functions of our project.

## __References__
1. __Read from CSV File__ _Line 9-18_
```python
# the code for def read_csv are from lab8
def read_csv():
    with open(FILE_NAME) as reader_file:
        reader = csv.reader(reader_file)
        data = list(reader)
    return (data[0], data[1:])
```
2. __Read French Characters from CSV File__ _Line 11-15_
```python
#Found error when decoding: 'utf-8' codec can't decode byte 0x8e in position 4060: invalid start byte
#reason: french characters in the data file
#used code (encoding='latin1') from https://stackoverflow.com/questions/49898909/reading-a-file-with-french-characters-in-python
    with open(FILE_NAME, encoding='latin1') as reader_file:
```
3. __Capitalize First Letter for User-input City Names__ _Line 21-22, 28_
```python
#in case of user enter city name with first letter not capitalized https://www.geeksforgeeks.org/string-capitalize-python/
departure_city = departure_city.capitalize()
```
```python
arrival_city = arrival_city.capitalize()
```
4. __Remvoe Spaces from User Inputs__ _Line 23-24, 29_
```python
#in case of user include space in input https://www.journaldev.com/23763/python-remove-spaces-from-string
departure_city = ''.join(departure_city.split())
```
```python
arrival_city = ''.join(arrival_city.split())
```
5. __Replace French characters__ _Line 25-26, 30_
```python
#in case of user input french character https://www.journaldev.com/23763/python-remove-spaces-from-string
departure_city = departure_city.replace("é", "e")
```
```python
arrival_city = arrival_city.replace("é", "e")
```


## __Repo & Video__
__Code and relative document:__
https://github.com/ShihanQunnie/csca20-project-flight-info.git

__Presentation video:__
https://youtu.be/O-97XKiLn3s
