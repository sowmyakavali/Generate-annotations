# Generate-annotations

#### Its just a simple opencv project to directly generate images and annotations from video

## Process

#### Create Virtual environment

    $python -m venv venv
    $venv\Scripts\activate
    $pip install -r requirements.txt
#### Run

    python main.py -v {path to video} -l {class name}

    Ex : python main.py -v video.mp4 -l car

    > Here you can able to annotate for only one class at a time
    > After video opened , Enter 
            s key to pause that frame and 
            draw rectanle box on the frame where the object is present,after then press Enter key , 
            again draw another box and press enter if there are multiple objects. 
    > Press esc key after you completed marking all objects in that particular frame. 
    > Repeat the step 2 and 3.    

#### Output
    Generates image and .xml file, which having the bounding boxes.
