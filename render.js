window.onload=function(){Array.prototype.slice.call(document.querySelectorAll(".formula")).forEach(function(e){katex.render(e.getAttribute("alt"),e,{displayMode:e.tagName==="DIV"})})}
