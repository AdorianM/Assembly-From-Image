# Assembly From Image

Transform an image into an assembly variable.

Just drag & drop your PNG file to Serve.exe (or manually run the .py script with the png location as an argument) and you'll get a file containing the declaration of an assembly compatible variable.

![image](https://user-images.githubusercontent.com/67052082/167021662-eedb0a66-96b2-4bad-b25d-7d9f127d7f32.png)

Customization can be added if you run the application. A small interface with features like: selecting input/output location, selecting a variable name.

An input directory can be selected to convert all the images inside it. The directory input has priority over the file input in the case both are selected. Additionally, the directory should only contain image files.

![image](https://user-images.githubusercontent.com/67052082/178140620-13b7cd6e-2106-4bfc-86bf-290ae5b14a74.png)

The generated output is an [.inc file](https://github.com/AdorianM/Assembly-From-Image/blob/master/example_asm_project/face.inc) which can be imported in any Assembly  x86 code. For [example](https://github.com/AdorianM/Assembly-From-Image/tree/master/example_asm_project), this could be used by a library with the capability to draw a canvas to show an image:

![example output](https://user-images.githubusercontent.com/67052082/172018167-0af98a8b-193c-429c-a2a1-1eb57fcb1be8.png)

✨ More features on the way ✨
