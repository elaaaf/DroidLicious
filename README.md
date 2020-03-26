# DroidLicious

### Dataset:
- A sample of the data: https://drive.google.com/open?id=1hQNAKUYAYPucsP_7NAnrdHjJ40mUkIFf <br />
This labeled dataset has 3529 android applications, 2263 of them are malicious and 1266 are benign, with 585,211 dataflows extracted using DroidLicious system parser, in the form of:<br/>
-------------------------------<br/>
|Name | Source| Sink | label  |<br/>
-------------------------------<br/>


- Another form is: <br/>
-------------------------------<br/>
|Name | Src n ~> Snk n | label|<br/>
-------------------------------<br/>
link :https://drive.google.com/open?id=1awd2af829WcJLuBAaH45mfZBFaM-K7gr

-command <br/>
-------------------------------<br/>
python main.py "Apk/txt path" <br/>
-------------------------------<br/>
python main.py --fd_option "options" "Apk path"
