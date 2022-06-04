# Assembly project which uses a generated variable

## Canvas

Any library with the capability to draw a canvas and pixels on the screen using assembly could be used. 
In this case, the files `canvas.lib` and `canvas.dll` provide a `BeginDrawing` function which handles that.

## Assembly code

The details of the implementation can be seen in `example.asm`, but essentially:
- the data is collected from `face.inc` (a file generated using the application)
- every double word in `face.inc` corresponds to a pixel
- starting from a given coordinate, two loops iterate through every double word and put it on the canvas at the corresponding location

## Results

Compiling and running gives the following result:

![image](https://user-images.githubusercontent.com/67052082/172018167-0af98a8b-193c-429c-a2a1-1eb57fcb1be8.png)
