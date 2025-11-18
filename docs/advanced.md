# Performance Tips

- Use **numexpr** for fast expression evaluation
- Optimize sample count for better live animation
- Avoid super heavy curves
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

- parameter value changes
- domain or sample count changes

# Add-on Architecture

Main components:

## Function Engine
- Expression parser → variable detection → parameter detection
- numexpr evaluator
- Grease pencil generator

## UI Panels
- Function panel
- Drawing panel
- Formula panel
- Morph panel

## Drivers and Animation
- Drivers and keyframes

