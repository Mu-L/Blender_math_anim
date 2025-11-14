# Function Animation

## Creating a Function Plot

1. Add → Math Anim → **Function**
2. Enter a mathematical expression, e.g.: sin(2*pi*t)
3. Set domain:
   - `t_min`, `t_max`
4. Set resolution (`samples`)
5. Click **Generate**

## Supported Expressions
- `sin`, `cos`, `tan`
- `exp`, `log`
- `sqrt`
- `abs`
- All NumPy-like operators via `numexpr`

## Parameter Sliders

The add-on auto-detects parameters:

Example: sin(a * t + phi)
→ creates sliders for `a`, `phi`.

## Animating the Curve

### Writing Animation
Creates a start-to-finish drawing effect.

### Parameter Animation
Add keyframes to detected sliders.

### Updating in Real-Time
Enable **Live Update** to update the mesh as sliders change.
