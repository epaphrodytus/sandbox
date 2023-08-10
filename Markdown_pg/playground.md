# Markdown experimentation

The goal of this file is to explore the various markdown options that are
available to us.  
There is a possibility that there are some syntax that are not recognized,
those are summarized in the 'Unsupported' section

The information on this page is derived from the following links:  
[Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)  
[Markdown Extended Syntax](https://www.markdownguide.org/extended-syntax/)

## Table of Contents

1. [Text](#text)
   - [In-line](#in-line)
   - [Blocks](#blocks)
     - [Blockquote](#blockquote)
     - [Code Blocks](#code-blocks)
2. [List](#list)
3. [Linking](#linking)
4. [Tables](#tables)
5. [Badges](#badges)
6. [Misc.](#misc)

## Text

### In-line

Normal: A quick brown fox jumps over the lazy dog.  
Bolded: **A quick brown fox jumps over the lazy dog.**  
Strikethrough: ~~A quick brown fox jumps over the lazy dog.~~  
Italics: _A quick brown fox jumps over the lazy dog._  
Bold-italics: **_A quick brown fox jumps over the lazy dog._**  
Highlighting: <mark>A quick brown fox jumps over the lazy dog.</mark>  
Subscripting: H<sub>2</sub>O  
Superscripting: y = n<sup>2</sup>  
Footnoting: This is a footnote [^1]  
Named Footnoting: This is a named footnote [^reference]  
Third footnote: This is the third footnote [^wrapper]  
[^1]: Note that although the footnote link is here in the raw code, it is placed at the bottom in reality
[^reference]: Even though you use reference as a text id, it still shows up as 2 in reality

    Your reference can be indented and have it's own interesting set of contents

        `like so`

[^wrapper]: This is how it will look

The above set of Markdown formattings are represented in the raw code as follows:

```
Normal: A quick brown fox jumps over the lazy dog.
Bolded: **A quick brown fox jumps over the lazy dog.**
Strikethrough: ~~A quick brown fox jumps over the lazy dog.~~
Italics: _A quick brown fox jumps over the lazy dog._
Bold-italics: **_A quick brown fox jumps over the lazy dog._**
Highlighting: <mark>A quick brown fox jumps over the lazy dog.</mark>
Subscripting: H<sub>2</sub>O
Superscripting: y = n<sup>2</sup>
Footnoting: This is a footnote [^1]
Named Footnoting: This is a named footnote [^reference]
Third footnote: This is the third footnote [^wrapper]
[^1]: Note that although the footnote link is here in the raw code, it is placed at the bottom in reality
[^reference]: Even though you use reference as a text id, it still shows up as 2 in reality

    Your reference can be indented and have it's own interesting set of contents

        `like so`

[^wrapper]: This is how it will look

```

You can also use in-line breaklines
In the raw markdown file,

> the following lines  
> are all written on the same line  
> All<br>of<br>this<br>are<br>on<br>the<br>same<br>line

The raw code that produces the above blockquote is as follows:

```
> the following lines
> are all written on the same line
> All<br>of<br>this<br>are<br>on<br>the<br>same<br>line
```

### Blocks

#### **Blockquote**

> A blockquote can be done like this to highlight  
> chunks of text like so  
> it is best practice to include a '>' on every line

The Markdown used to create the above is as follows:

```
> A blockquote can be done like this to highlight
> chunks of text like so
> it is best practice to include a '>' on every line
```

#### **Code blocks**

There are 3 main ways to write code blocks

##### _In-line Back Quotes_

`The in-line code blocks are fairly restrictive`  
`If you wish to write across multiple lines`  
`You need to use multiple blocks`

The Markdown used to create the above is as follows:

```
`The in-line code blocks are fairly restrictive`
`If you wish to write across multiple lines`
`You need to use multiple blocks`
```

##### _Indentation_

    By Putting in 4 spaces before a block
    You get and leaving an empty line before and after
    You get a code block as well
        You can place indents in the code block
        by putting in another 4 spaces

The Markdown used to create the above is as follows:

```
    By Putting in 4 spaces before a block
    You get and leaving an empty line before and after
    You get a code block as well
        You can place indents in the code block
        by putting in another 4 spaces
```

##### _Fenced Code blocks_

```
By wrapping your text in triple back quotes
You also get a code block that accounts for new lines
This method avoids the use of indentations in the
raw Markdown File
  You can also indent code at any level
    In this type of code block.
```

The Markdown used to create the above is as follows:

````
```
By wrapping your text in triple back quotes
You also get a code block that accounts for new lines
This method avoids the use of indentations in the
raw Markdown File
  You can also indent code at any level
    In this type of code block.
```
````

## List

### _Ordered List_

1. Item 1
2. Item 2
3. Item 3

The Markdown used to create the above is as follows:

```
1. Item 1
2. Item 2
3. Item 3
```

### _Unordered List_

- First Item
- Second Item
- Third Item

The Markdown used to create the above is as follows:

```
- First Item
- Second Item
- Third Item
```

### _Indented list_

1. First Item
2. Second Item
   1. Indented Ordered 1
   2. Indented Ordered 2
3. Third Item
   - Indented Unordered 1
   - Indented Unorderd 2

The Markdown used to create the above is as follows:

```
1. First Item
2. Second Item
   1. Indented Ordered 1
   2. Indented Ordered 2
3. Third Item
   - Indented Unordered 1
   - Indented Unorderd 2
```

### Task List

- [x] this is a completed task
- [ ] this is an uncompleted task

The Markdown used to create the above is as follows:

```
- [x] this is a completed task
- [ ] this is an uncompleted task
```

## Linking

### _Image_

![cute-grill-alert](https://pbs.twimg.com/media/EPEQZZoUcAYC-bc?format=jpg&name=small)

The Markdown used to create the above is as follows:

```
![cute-grill-alert](https://pbs.twimg.com/media/EPEQZZoUcAYC-bc?format=jpg&name=small)
written in the format
![web-reader-name](link)
```

_Website link_

Find the best grill in the East [here](https://www.youtube.com/@OozoraSubaru)!

The Markdown used to create the above is as follows:

```
Find the best grill in the East [here](https://www.youtube.com/@OozoraSubaru)!
```

## Tables

| This is the left column                     |                   center                   |        This is the right column |
| :------------------------------------------ | :----------------------------------------: | ------------------------------: |
| Justification by colon position             |                     J                      | colon on the right in this case |
| You could fill in any number of things here |                     A                      |          This could be anything |
| Long or short                               |                     B                      |                     This is nan |
| You could also put a link to best wolf      | [link](https://www.youtube.com/@OokamiMio) |                  FubuMio 最高！ |
| You may also put code blocks                |                     C                      |     `something like this works` |
| You may also format text like **so**        |                    _so_                    |                  or ~~like so~~ |
| Emojis                                      |                     🚨                     |                       Also work |

The Markdown used to create the above is as follows:

```
| This is the left column                     |                   center                   |        This is the right column |
| :------------------------------------------ | :----------------------------------------: | ------------------------------: |
| Justification by colon position             |                     J                      | colon on the right in this case |
| You could fill in any number of things here |                     A                      |          This could be anything |
| Long or short                               |                     B                      |                     This is nan |
| You could also put a link to best wolf      | [link](https://www.youtube.com/@OokamiMio) |                  FubuMio 最高！ |
| You may also put code blocks                |                     C                      |     `something like this works` |
| You may also format text like **so**        |                    _so_                    |                  or ~~like so~~ |
| Emojis                                      |                     🚨                     |                       Also work |
```

Due to how messy it can get in the raw it might be better to use other options available.

## Badges

You may create badges from this [link](https://shields.io/badges/static-badge) to shields.io

![Static Badge](https://img.shields.io/badge/experimentation-markdown-blue)
![Static Badge](https://img.shields.io/badge/test-markdown-blue)

The Markdown used to create the above is as follows:

```
![Static Badge](https://img.shields.io/badge/experimentation-markdown-blue)
![Static Badge](https://img.shields.io/badge/test-markdown-blue)
```

## Misc.

You can also add header lines at random locations by putting 3 hyphens '---' as a paragaph:

---

The above line is not associated with any header.
<br><br><br>
The Markdown used to create the above is as follows:

```
You can also add header lines at random locations by putting 3 hyphens '---' as a paragaph:

---

The above line is not associated with any header.
```
