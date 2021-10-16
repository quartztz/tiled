# tiled - a way to emulate the "Tile" wallpaper option on Windows, but in Linux

## The project

### About the project

I recently made the switch from a Windows 10 machine to a Chromebook running Linux through crostini. I'm enjoying the new interface, and I've found a way to do (almost) everything I used to be able to do on my previous laptop. 

Except for Tiled backgrounds. I love the way they look, and I used to look everywhere online to find small images I could make into repeating backgrounds, as well as making my own. As soon as I got my new laptop, I realized it was just missing something. 

So I set out to do it myself, and I have to say I think I got kind of close. I'll admit I spent an afternoon on this, so it may not be the most fully featured app, or the or the most seamless implementation, since I was unable to find ways of automating the actual setting of the wallpaper, but I managed to put together a small command line utility to allow a user to select a small image, and have in return a tiled background made from that image, cropped up to a given size (default is 1920x1080). 

I might add some more functionality if I ever feel the need to, but for now it's really just out there. 

### How it works

#### Try it out

To test it out, you can use the included ```example``` folder: it includes a sample image coming from my copy of the ```10PRINT``` script from old Commodore 64 computers, which lends itself pretty well to this kind of wallpaper. Simply run: 

```
python3 tiled.py example/example.png ./example/
```

and navigate to the ```example``` folder to retreive your new image.

#### Make your own

To use your own images, the syntax is very similar: simply point to your original image's path, and add an optional output directory. You'll get a tiled wallpaper of the original image of size 1920x1080, ```stretched.jpg```. You can change this size by editing the END_WIDTH and END_HEIGHT variables in ```image_stitcher.py```: as of now, this somewhat hacky solution is the only way to change it, but I might explore other ways in the future, as I get more comfortable with this kind of project. 

The first time it's called without an explicit output path, the program creates a folder in the user's home directory, called ```wallpapers```. In that folder, every time the program is called with a file with a new name, a folder is created with the name of the file that generated it, containing the output file (default ```stretched.jpg```). 

> BE CAREFUL! This means that two file with the same name **will** (for the time being, at least), generate a file with the same output name, in the same folder. The earlier one **will** be overwritten. Please take countermeasures to avoid data loss (Rename input file, for now. I might add a way to change name as an option, but I still have to understand exactly the best way to do so). 



The command uses the format: 
```
python3 tiled.py path/to/input/file optional/output/path
```

If you want to, you can add this script to your PATH and make it an executable, to simplify the command a little. I'm not sure how worth it it is, but you do you.

#### Examples

**10PRINT** (default example)

<img src="https://i.imgur.com/ckk3kgk.png">

becomes

<img src="https://i.imgur.com/NyOOTlJ.jpeg" width=75%>

**Spike Spiegel**

<img src="https://i.imgur.com/TcDmuYP.jpeg">

becomes

<img src="https://i.imgur.com/BvShbM0.jpeg" width=75%>

**JFK pride flag**

<img src="https://i.imgur.com/07YMfzW.png">

becomes

<img src="https://i.imgur.com/Pb1fsaC.jpeg" width=75%>

## TODOs

I guess there's a couple of ways I could improve this: 

- [ ]  better interface: probably not a GUI but at least something less clunky
- [ ]  more functionality, more easily accessible:
	- [ ]  allow the user to specify much more easily path to file and output directory;
	- [ ]  allow the user to pick their own final size from the command line itself;
- [ ]  tell me if there's more you would like to see! open an issue and let me know :)

## Libraries used

This program uses the Python Image Library to help with image manipulation. It quite literally wouldn't have been possible to do this without it, I think. Or rather, it would've been a lot more tedious: I guess I *could* have done it, but there's a high change I just would've quit halfway through. So big thanks to them.
