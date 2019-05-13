XPath - the basics
===========================

So this is some short hand notes on how to do XPathing.


### Absolute vs Relative Pathing
`/element` - This gets the direct sibling of the parent element, this is known as absolute search.

To select the body tag in this html.

    <html>
        <body>
        </body>
    </html>
    
/html/body    
        
`//element` - This is relative search, can be found anywhere on the page. This searches anywhere, relative to the base root.

In the above example body can be selected by 

`//body`

So another relative search. let's try to get to that p element

    <p> Don't get me</p>
     <div>
        <span>
            <p>But get me</p>
        </span>
    </div>
    
We can search this in two ways.

`/div/span/p` - Absolute search
`//div//p` - relative search


### XPATH matches the first found element

To match the second element, we can use the `[]` After the selector to select which number

     <div>
        <span>
            <p> Don't get me</p>
            <p>But get me</p>
        </span>
    </div>

`/div/span/p[1]` to Get the second one 

# Cheat Sheet

  * Get Element By ID `//*[@id='name']`
  * Get Element By Class `//*[@contains(@class, 'foo')]`
  * Get Element with Attribute 'href'- `//*[@contains(@href, 'foo')]`
  * Get the Third p element selected - `//p[2]`

