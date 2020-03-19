# DroidLicious

### Dataset:
- A sample of the data: https://drive.google.com/open?id=1hQNAKUYAYPucsP_7NAnrdHjJ40mUkIFf <br />
This labeled dataset has 3529 android applications, 2263 of them are malicious and 1266 are benign, with 585,211 dataflows.

### System Parser: <br />  
  - Parser_1.java: flowdroid txt files to parsed txt files in the form src ~> snk <br />
  - Parser_2.java: parsed txt files to .csv file in the form:<br />
  --------------------------------<br />
  | Index | Name | Source | Sink |<br />
  --------------------------------<br />

### User Parser: <br />  
- UserParserComponent.py: this parser takes only one input and returns a list of file sources and sinks, it meant to be used by the interface user. Please be sure to download the ParserFD.class file and include the required inputs as stated in the code comments.
