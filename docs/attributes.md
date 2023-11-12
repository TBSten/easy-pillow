# easy pillow 's basic attributes

## a.align(vertical, horizontal)

- `a.layout.vertical.center`

- `a.layout.vertical.top`

- `a.layout.vertical.bottom`

- `a.layout.horizontal.center`

- `a.layout.horizontal.left`

- `a.layout.horizontal.right`

## a.direction

alias: `a.dir`

```py
p.box(
    a.dir.top_to_bottom,
    p.box(...),
    p.box(...),
)
```

## a.backgroundColor(color)

alias: `a.bgColor`

```py
p.box(
    a.backgroundColor((255,255,255,255)),
)
```

## a.backgroundImage(image)

alias: `a.bgImage`

```py
p.box(
    a.backgroundImage("./background.png"),
)
```

## a.backgroundGradient(image)

alias: `a.bgGradient`

```py
p.box(
    a.backgroundGradient("./background.png"),
)
```

## a.border(color, width, style)

```py
p.box(
    a.border((255,255,255,255), width),
)
```

## a.padding(top, right, bottom, left, vertical, horizontal, all)

```py
p.box(
    a.padding(top=10,right=10,bottom=10,left=10),
)
```

```py
p.box(
    a.padding(vertical=10, horizontal=10),
)
```

```py
p.box(
    a.padding(all=10),
)
```
