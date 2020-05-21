Imagine you're a turtle starting at 0,0 that needs to follow the directions in a text file. Inside the text file, you will see characters such as LLRFLFLF. Each letter represents a movement, L means the turtle turns counterclockwise, R means the turtle turns clockwise, and F means forward. Note, turning the turtle only changes the turtle's orientation. This is an application that takes in a text file and displays in a visual manner the path the turtle travels and highlights the locations where the turtle crosses his own path.  

### Project
_______________________________________________________________________________________________
Prerequisites
```
python==3.8.3
flask==1.1.2
Werkzeug==1.0.1
```
Create a virtual environment inside the project’s root directory using the following command to run the code
On macOS and Linux:
```
python3 -m venv env
```
On Windows:
```
py -m venv env
```
Activate the virtual environment using the following command
On macOS and Linux:
```
source env/bin/activate
```
On Windows:
```
.\env\Scripts\activate
```
Install the project’s dependencies inside an active virtual environment with the incantation 
```
pip install -r requirements.txt
```
#### Dataset
____________________________________________________________________________________________________
There is directions zip file which contains different text files with commmands. 

#### Execution
____________________________________________________________________________________________________
Download the code and install the dependencies required. To run the application, execute the following command and open http://127.0.0.1:5000 in your browser. Upload the file using the 'Browse' and 'Upload' buttons. The path traveled by turtle is displayed as a graph.
The graph represents the following things:
1. the end location of the turtle, which is displayed as a coordinate highlighted in red.
2. the orientation of the turtle, which is depicted by the arrow associated with the point. 
3. all of the points where the turtle has traveled to more than once, which are highlighted in green.
```
python __init__.py
```
![path traveled based on instructions](https://github.com/pkaplish20/AltaML_Coding_Exercise/blob/master/Assets/Path.png)
