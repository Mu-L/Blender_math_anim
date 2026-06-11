# Formula Generating and Animating

You can create formula using Typst or OpTeX or PDF.

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

## Animating Formulas
- Preset animations
- Morphing between and across formulas with other types
