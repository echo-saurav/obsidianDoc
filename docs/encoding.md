---
layout: default
title: encoding
---
# encoding
## convert to base64 any file
```bash
base64 -w 0  input/file/path > output/file/path

```

*ex: *
```bash
base64 -w 0  ./static/MerriweatherSans-Regular.ttf > merriweather.t  
xt

```


## export font into css with base64
CSS snippet for Open Sans Bold: 

```css
@font-face {
  font-family: 'Open Sans';
  src: url(data:application/x-font-woff;charset=utf-8;base64,<base64_encoded>) format('woff');
  font-weight: 700;
  font-style: normal;
}
```