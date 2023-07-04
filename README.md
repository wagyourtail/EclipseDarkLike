# EclipseDarkLike

This theme is designed to more faithfully replicate the color pallete of Eclipse's Dark theme for java code, with some minor changes for code readability. 

Notable changes: 
* Slight desaturation from the true colors in eclipse, this makes the text appear more similar in-editor. 
* certain functions in eclipse not working with IDEA's color options 
* Added underlines to final/effectively final values in methods, this can easily be changed in the java color style section, Java->Parameters->Parameter and un-check "Effects" as well as Variables->Local Variable.
* I also left javadoc hilighting alone as Dracula's hilighting's a bit nicer in my opinion.
* error hilighting is not completely fixed as that isn't part of theme but is under "Inspections"


## FAQ
**Q:** _Why did I make a git repo for a theme plugin? can't you just edit it directly?, like seriously it's not like it's a binary file, the theme
jar literally contains the source code_

**A:** _[because they made me](./why/dumb_email_exchange.md)_

## Installation

### Plugin
1. Install from the [JetBrains Plugin Repository](https://plugins.jetbrains.com/plugin/17464-eclipsedarklike-color-scheme)

### Manual (icls file)
1. Download the [EclipseDarkLike](./EclipseDarkLike-Dark.icls) file
2. Open IntelliJ IDEA
3. Go to `File | Settings | Editor | Color Scheme`
4. Click the gear icon and select `Import Scheme`
5. Select the `EclipseDarkLike.icls` file

### Manual (jar file) (not recommended)
1. Download the `color-scheme` zip from the actions page
2. Extract the zip
3. Open IntelliJ IDEA
4. Go to `File | Settings | Plugins` (or install like a color scheme with the same steps as Manual)
5. Click the gear icon and select `Install Plugin from Disk`
6. Select the contained jar file from the extracted zip