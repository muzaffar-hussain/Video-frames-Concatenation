# Video-frames-Concatenation
This python program will join two videos together horizontally or vertically depending on the desired results by the user.

## Working:
The files must have same fps & dimension for optimal working as the reason of this repository is to be used for comparing different changes to the same video file.

### Installing Required libraries:
A ```requirements.txt``` file is uploaded in this repository for easy use. You can install all the required libraries by using pip as follows:
```bash
pip install -r requirements.txt
```
After you have setup your environment you can now run the program on your own videos.

### Running the script:
I have added some sample videos in the example folder to run here. To run the examples using the example files enter this:

```bash
python concatenate.py --video1 cnn-2.mp4 --video2 dlib-2.mp4 --axis 1
```
