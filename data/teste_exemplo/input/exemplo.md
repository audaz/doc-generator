# Headers

# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------


Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------

------

# Emphasis

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_


------

# Lists

```
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list.
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

* Unordered list can use asterisks
- Or minuses
+ Or pluses

1. Make my changes
    1. Fix bug
    2. Improve formatting
        - Make the headings bigger
2. Push my commits to GitHub
3. Open a pull request
    * Describe my changes
    * Mention all the members of my team
        * Ask for feedback

  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!
```




<%*
const file_aa = tp.file.path() 
//let file_xx = file_aa.replace(/\\/g, "\\\\").replace(/\//g, "\\\\") 
let file_xx = file_aa.replace(/\\/g, "\\").replace(/\//g, "\\") 
file_xx = "\"" + file_xx + "\""
console.log(file_xx) 
output = await tp.user.docgen({file_x: "\"" + file_xx + "\"", b: "value_2"}) 
console.log(output)
%>


....