# tiled - a way to emulate the "Tile" wallpaper option on Windows, but in Linux

## The project

### About the project

I recently made the switch from a Windows 10 machine to a Chromebook running Linux through crostini. I'm enjoying the new interface, and I've found a way to do (almost) everything I used to be able to do on my previous laptop. 

Except for Tiled backgrounds. I love the way they look, and I used to look everywhere online to find small images I could make into repeating backgrounds, as well as making my own. As soon as I got my new laptop, I realized it was just missing something. 

So I set out to do it myself, and I have to say I think I got kind of close. I'll admit I spent an afternoon on this, so it may not be the most fully featured app, or the or the most seamless implementation, since I was unable to find ways of automating the actual setting of the wallpaper, but I managed to put together a small command line utility to allow a user to select a small image, and have in return a tiled background made from that image, cropped up to a given size (default is 1920x1080). 

I might add some more functionality if I ever feel the need to, but for now it's really just out there. 

### How it works

#### Try it out

To test it out, you can use the included "example" folder: it includes a sample image coming from my copy of the 10PRINT script from old Commodore 64 computers, which lends itself pretty well to this kind of wallpaper. Simply run: 

```bash
python3 image_stitcher.py ./example/example.png ./example/
```

and navigate to the "example" folder to retreive your new image.

#### Make your own

To use your own images, the syntax is very similar: simply point to your original image's path, and add an optional output directory. You'll get a tiled wallpaper of the original image of size 1920x1080, "stretched.jpg". You can change this size by editing the END_WIDTH and END_HEIGHT variables in "image_stitcher.py": as of now, this somewhat hacky solution is the only way to change it, but I might explore other ways in the future, as I get more comfortable with this kind of project. 

## TODOs

I guess there's a couple of ways I could improve this: 

- [ ]  better interface: probably not a GUI but at least something less clunky
- [ ]  more functionality, more easily accessible:
	- [ ]  allow the user to specify much more easily path to file and output directory;
	- [ ]  allow the user to pick their own final size from the command line itself;
- [ ]  tell me if there's more you would like to see! open an issue and let me know :)

# Libraries used

This program uses the Python Image Library to help with image manipulation. It quite literally wouldn't have been possible to do this without it, I think. Or rather, it would've been a lot more tedious: I guess I *could* have done it, but there's a high change I just would've quit halfway through. So big thanks to them.
