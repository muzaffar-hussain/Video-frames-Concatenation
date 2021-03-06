# Video-frames-Concatenation
This python program will join two videos together horizontally or vertically depending on the desired results by the user.

## Working
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
python main.py --video1 Examples/cnn-2.mp4 --video2 Examples/dlib-2.mp4 --axis 1
```
#### Note: You can cancatenate vidoes along vertical axis by using --axis 0
I used two different facial detectors on the same video so when you run this it will combine both these videos horizontally.
![](Results/cnn-2.gif)  ![](Results/dlib-2.gif)

The resulting video will be like this:


![](Results/cnn-2-dlib-2.gif)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
