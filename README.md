
# DroidLicious

### Dataset

DroidLicious provides a comprehensive dataset of Android applications, meticulously labeled and categorized into malicious and benign apps. The dataset includes detailed dataflows extracted using the DroidLicious system parser.

- **Sample Data:** [Sample Dataset](https://drive.google.com/open?id=1hQNAKUYAYPucsP_7NAnrdHjJ40mUkIFf) <br />
  The sample dataset comprises 3529 Android applications, with 2263 identified as malicious and 1266 as benign. The dataset contains 585,211 dataflows in the following format:

  ```
  --------------------------------
  | Name | Source | Sink | Label |
  --------------------------------
  ```

  Another representation of the dataflows is provided as:

  ```
  --------------------------------
  | Name | Src n ~> Snk n | Label |
  --------------------------------
  ```

  - [Link to detailed format description](https://drive.google.com/open?id=1awd2af829WcJLuBAaH45mfZBFaM-K7gr)

- **Full Dataset:** [Full Dataset](https://drive.google.com/file/d/1gJtLkvSE7McSHozcdnhlAObOtAQFJb--/view?usp=sharing)

### Controller

To run DroidLicious, follow these instructions:

1. **Pre-requisite:**
   Before running the controller, update line 12 in `startFlowDroid.py` as required.

2. **Commands:**

   To execute DroidLicious, use the following commands:

   ```
   python main.py "Apk/txt path"
   ```

   For additional options, use:

   ```
   python main.py --fd_option "options" "Apk path"
   ```

Ensure that you have the necessary dependencies installed and the APK/txt files are correctly placed in the specified paths.

---
