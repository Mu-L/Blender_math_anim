# Function Plotting and Animation

## Creating a Function Plot

1. Select Function type
   - Currently there are types of `Explicit Function`, `Parametric Function`, `Polar Function`, `Implicit Function` and `ODE Function` and `Function Data`. 
   - By default, the variables can be (x, y, z), (u, v, w)  or t, and the priority of variable names is (x, y, z) > (u, v, w) > t; except for `Polar Function`, the variables options are θ > u > t. You can check the description of each function type in the UI by putting the mouse in the input field. 
   - Variables with index have same priority as the ones without index, e.g. x, x0, x2, y, y1, ... .
   - If your dimension is less than 3, put `0` to the unused fields.
2. Enter a mathematical expression, e.g.: `sin(2*pi*t)`, press `Enter`, if there are warnings popup, press `Enter` or `Esc` till the warning message disappear, then correct the expression based on the warning tips.
   - Once the expression is valid, the variables and parameters will be detected and listed in the UI, you can 
   adjust their values accordingly or do it later after the plotting.
   ```
   You can set all the fields to 0 at the begining, then input the expressions field by field to avoid the warning messages. 
   ```
3. For `Parameter Function` and `ODE Function`, you can plot branch or composed branch vs variable, e.g., if you choose branch `x` it will plot `x` vs `t`, and compose `x*2 + y` will plot `x*2 + y` vs `t`, etc.
4. For `ODE Function`, you can plot more complicated by adding `stop` condition and update state accordingly when you choose `Diffsol Methods` solver.
   - `Stop` condition expression will be evaluated at each step, once it is satisfied, the solver will update the state given by the update state expression, for the state update, make sure the state is different even if it's continued, e.g. adding a tiny step 1e-12, otherwise, it may fail to change the new state. 
        - If you set the `stop` condition to `x - 1`,  it means `x - 1 = 0`
        - `State` update expression should be same dimension as your functions, if you having `x` and `y`, then you should update both states, e.g. `x + 1e-12, -0.8*y`, keep in mind to change the `x` by giving it a tiny step to make sure the state is different, otherwise, it may fail to change the new state. 
6. Create the plot
    - You need to have a plotter object (Grease Pencil) first, you can create one by clicking `Add Plotter` button or select one from the dropdown list if you have already created them. Only objects created by the add-on are effective to be used.
    - The plotting and its axis are created as Grease Pencil layers. 
        - When you `Adding Plotting`, two new layers will be created,  one is for the plotting and one if for the axis.
        - When you `Update Plotting`, you need to make sure the selected layer is not axis layer, otherwise, the plotting will not be updated.
7. Live update and control the plotting
    - You can select the **plotting layer** and control the plotting by checking `Current Plot Control`
    - It will control the plotting and axis as a whole.

## Supported Expressions and operators
At one hand, I intend to support as many math functions as possible, on the other hand, the speed is the priority, 
so I choose [`asteval`](https://lmfit.github.io/asteval/basics.html) for `Explicit Function`, `Parametric Function` 
and `Polar Function` for its rich math functions supported, [`numexpr`](https://numexpr.readthedocs.io/en/latest/user_guide.html) for `Implicit Function` for its speed, and [`meval`](https://docs.rs/meval/latest/meval/) for `ODE 
Function` for its powerful support for ODEs. Check their documentation for the supported expressions and operators, especially for `meval`, it only supports a limited set of expressions and operators compared to the other two, for example, it uses `^` for power while `asteval` and `numexpr` use `**`.
- Caution: constants like `pi`, `e`, etc. should not be used as parameters.
- `prod` and `sum` are supported for `Explicit Function`, `Parametric Function` and `Polar Function` which are backed by `asteval`. 
    - sum_{i=start}^{[i=]end}(expr) and prod_{i=start}^{[i=]end}(expr) are the form to use, the index must be an integer, and the start and end can be integer parameters, the [i=] part in the end index can be omitted, e.g. `sum_{i=0}^{10}(sin(i*x + a))` is same as `sum_{i=1}^{i=10}(sin(i*x +a))`.
    - `i, j, k, l, m, n` are preset integer parameters, so you can control the start and end index like this: `sum_{k=i}^{n}(sin(k*x + a))`, then you can control the `i` and `n` to change the start and end index.

## Plotting settings
You can adjust the plotting or axis settings to change the appearance of the plotting, e.g. color, thickness, etc. 
through the layer settings, by selecting the corrosponding plotting or axis layer.
- `Object Settings` is for the whole object, but it will be overrided by the `Layer Settings`.


## Animating the plottings
- Preset animations
    - There are serveral preset animations,
- Keyframe variables and parameters
    - all variables and parameters can be keyframed, you can right click the variable or parameter and select `Insert Keyframe` to insert keyframe for it, then you can adjust the value of the variable or parameter at different frames to create animation.
- Add drivers
    - You can add drivers to the variables and parameters to create more complicated animation, e.g. you can add a driver to the parameter `a` to make it change with respect to the frame number like `frame/10`, then `a` will increase by 0.1 every frame, which will create an animation of the plotting changing over time.
    - If the driver is from other objects' properties, it may not update lively, you can add `+ 0*frame` to the driver expression to make it update every frame, e.g. `variable + 0*frame` where the variable is represent for a property driver.
