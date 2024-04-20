# Building simple dashboard using Dash python library

# Table Of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Application's Structure Details](#structure)
- [Examples & Usage](#examples)

<a name="#overview"/>

## Overview

This repository contains code to create simple dashboard using Plotly's Dash.
Final dashboard contains interacrtive plots, that describe 5 different data samples histograms and 5 distributions, that can estimate data (images in 'Examples & Usage' section)

<a name="#getting-started"/>

## Getting Started 

To run/create this application, you'll need Dash, dash_bootstrap_components, numpy, pandas, plotly and scipy libraries with versions provided in 'requirements.txt' file.
Then, all you need to do is to run 'main.py' script:
```
..:\app\working\directory>python main.py
```

<a name="#structure"/>

## Application's Structure Details

The core idea of Dash is to write web dashboard without writing any CSS or HTML code. While this statement is true, it can lead to some kind of frustration in the future.
Yes, wyou wont create CSS/html files for your Dash project, but you WILL use some web application logic and structure to build more complicated Dash app (smth more complex, than 'Hello World!').

But it wasnt a problem for me - python ML enthusiast, who dont know a thing about web developing. This is because Dash provides really easy-to-follow structure and instruments, that will help you to build 
these structures:

### Dash() - main application element:
First things first - we need to create an app using Dash() class. We can set .title and .layout attributes of the app and then just run it using .run() method

### .layout - is where the whole structure of the app is:
The layout is enclosed within a html.Div component, which acts as a container for all other elements. This is akin to a <div> in HTML, providing a way to group elements together.
One can understand Div component as a block of content on web page, that contain some simple web elements such as text Header, Hr line divider, buttons and etc. Worse to mention Div can (and will)
contain other Div's as well!

Various components are included within our app's layout, such as dropdowns, histograms, and sliders. These are generated using custom functions (distr_render, data_render, hist_render and sliders_render) which return HTML Div blocks.
These Div objects dont differ in extreme way from their 'parent blocks' - they just represent more concrete elements of the Dash app.

### html. and dcc. objects - these are our 'bricks':
Talking about the creation if out Div block elements, I can divide them into two groups.
 - If you need some basic web objects, like text or a button, you'll find it in dash.html class
 - Looking for more complex interactive web elements? See Dash.dcc class (Dash Core Components). There you'll find customizible fancy-looking Sliders, Dropdown menus, Graph and so on.

### Input/Output idea - create relations between your elements
If you want your button to affect application's plot, take a look on dash.dependencies .Input and .Output functions. Combined with your applications .callback(Input, Output) decorator,
you can easily create a relation between app's elements. Input takes two positional arguments: 
 - **id** of element, that provides 'info', such as slider's custom id (ids.MI_SLIDER in my app);
 - **value** of element, in which we are interested in ('value' of  slider).


## Examples & Usage

Based on structure's logic and web elements described above, we now can see a working example of my Dash app:

<p align="center">
	<img src="./readme_images/img1.jpg" />
</p>

<p align="center">
	<img src="./readme_images/img2.jpg" />
</p>

<p align="center">
	<img src="./readme_images/img3.jpg" />
</p>


