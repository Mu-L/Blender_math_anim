# Performance Tips

- Use **numexpr** for fast expression evaluation
- Default sample count is optimized for animation
- Heavy curves: disable live update while adjusting parameters
- Use GPU subdivision sparingly
- Try to keep expression complexity low

# Expression Engine (numexpr)

The add-on uses `numexpr` instead of Python `eval`:

### Benefits
- Faster evaluation
- Prevents arbitrary code execution
- Vectorized math
- Safe execution sandbox

### Supported features
- All NumPy-compatible functions
- Elementwise operations
- Logical and comparison operators

# Live Update System

Live update regenerates the curve automatically when:

- expression changes
- slider value changes
- domain or sample count changes

Implementation details:
- On property update, compute curve using `numexpr`
- Update mesh vertices only (no recreation)
- Threaded execution planned for future versions

# Add-on Architecture

Main components:

## Function Engine
- Expression parser → variable detection → parameter detection
- numexpr evaluator
- Mesh generator

## UI Panels
- Function panel
- Drawing panel
- Formula panel
- Morph panel
- Slider panel

## Drivers and Animation
- Sliders map to keyframes
- Mesh updates through handlers

