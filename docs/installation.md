# Installation

## 1. Requirements

- Blender version 4.4 or 5.0
  - Blender 4.5 doesn't work due to its internal bugs
- Supports macOS, Windows, Linux
- It will requires optex for rendering formulas (optional)
  - Make sure `optex` command is available in your system PATH
  - If you can run `optex` from a terminal, you're good to go.

---

## 2. Installing the Add-on

![Install](pics/math_anim_install.png)

1. Open Blender → **Edit → Preferences → Get-Extentions**  
2. Choose **Install from Diks...**  
3. Select the ZIP file and click the **Install from Disk** button  
4. By default, it should be enabled, double check to make sure it's enabled, if not, just enable it

---

## 3. Setting Up the Add-on

![setup](pics/math_anim_install_setup.png)

Click **Add-ons** then search **Math Anim**, expand it. 

1. The fonts path libraries are necessary unless you don't use the formula part
  * Only `.ttf` and `.otf` fonts are supported, if your PDF files are compiled with other font types, like latex with 
`.pfb` fonts (they are so outdated), it will use Blender default font instead.
  * All the needed python packages are bundled with the add-on except the `OpTex` which doesn't have a python package.
    - [OpTeX](https://github.com/olsak/OpTeX?tab=readme-ov-file) is just an latex engine (like lualatex, xelatex), it only supports modern `.ttf` and `.otf` fonts, it's optianl.
    - You can use [Typst](https://github.com/typst/typst) which is also an modern typesetting engine by only supporting `.ttf` and `.otf` fonts and the `Typst` is bundled with this add-on.
    - If you installed `OpTex`, make sure it's in your system PATH:
      - It is in the PATH if you can run `optex` from a terminal, for **Windows**, **MacOS**, and **Linux**.
      - For both `Typst` and `OpTex`, check their documentations for their free available fonts to use.
2. You can also preset formulas for both `Typst` and `OpTex` for reference or speed up your workflow. Once they're set, they will be showed up in the add-on panel under formula section, otherwise, they will not show up.
3. The `Extra Vars` are extra reserved variables for function plotting besides x,y,z,u,v,t etc, so if you set the number to 10, you will have x0, x1, ..., x9 as extra variables to use, similarly for y,z,u,v,t etc. 
4. You can also change the add-on N panel location, but it is recommended to keep it under the default **Tool** location.
