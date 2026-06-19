# Formula Generating and Animating

The underlying workflow for formula/text typesetting is extracted from PDF, and then the layout is reconstructed using geometry nodes. The layout is preserved as much as possible, but there are some cavets to be aware of: 
- For large formula/text body, it can be slow since a lot of geometry nodes are generated. 
- There are three types of objects in PDF, char, stroke, and fill, and some math symbols can be a combination of 
  them, for example, a sqrt is composed of stroke and char, and so the arrangement in the geometry nodes, you need 
  to adjust the settings of both parts, e.g., change the positions, to make it look correct.
  - The stroke and fill are for drawing shapes, and the char is for text. The fill is not used in default, you need 
    to enable it in the settings if you want to use it. 
- Two PDF generating engines, `optex` and `typst`, are supported for quick and simple formula/text generating. They 
  will be compiled to PDF internally, and then the layout will be extracted from the PDF. For complex layout, for 
  example, change different fonts for different formula/text, producing PDF locally and use the PDF may be better. 

1. Choose formula source:
   - `optex code` or `typst code`
       - You can type simple math formula or text of optex or typst, it will compile to PDF internally.
       - Candidate math commands for `optex` and `typst` are supported when typing in **math mode**, need press `Enter` key to complete the typing.
       - For `optex code`, you can choose different *font family* for **math mode**, making sure the *font* is available in your system. For **Text Mode**, each input can have different *font*.
       - For `typst code`, each input can have different *font* for both **math mode** and **text mode**.
   - optex file or typst file
       - If you want complex layout, uploading a file is a good choice. It will compile to PDF internally.
   - PDF
       - You can upload PDF file, it will be used directly.
       - When extracting the layout from PDF, it will detect the used *fonts* automatically, but only *.ttf* and 
       *.otf* fonts info stored which you should have done `Build Font Lib` in the `preference`. Beware this when 
       you compile your PDF to make sure the compiled PDF contains *fonts* that are available in your system, 
       otherwise the formula will not display correctly.
2. Create formula.
    - Click `Create Formula` button to create formula. 
3. Adjust settings.
    - You can adjust the settings of formula, such as *Curve Radius*, *color* and *Font* which are for majority of formulas, go to `Individual Settings` or `Group Settings` to change particular part of the formula. 

## Animating Formulas
- Preset animations
- Morphing between and across formulas with other types
