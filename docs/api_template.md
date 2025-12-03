---
title: Operator Name
summary: Short description of what this operator does.
---

# `your.addon_operator_id`

## 📝 Summary
A concise description of what the operator does, when it should be used,  
and what part of the add-on or pipeline it belongs to.

---

# 🔧 Operator Information

| Field | Value |
|------|-------|
| **Identifier** | `your.addon_operator_id` |
| **Label** | `Your Operator Label` |
| **Category** | `VIEW3D`, `NODE_EDITOR`, etc. |
| **Context** | Where it can run (e.g., 3D View, Geometry Nodes Editor) |
| **Poll** | Conditions under which the operator is available |

---

# ⚙️ Properties

List all operator properties, their types, defaults, and purpose.

```python
my_bool: BoolProperty(
    name="My Bool",
    default=True,
    description="Turns on feature"
)

my_enum: EnumProperty(
    name="Mode",
    items=[
        ('MODE1', "Mode 1", ""),
        ('MODE2', "Mode 2", "")
    ],
    default='MODE1'
)
