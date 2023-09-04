---
publish: true
review-frequency: normal
link:
- '[[PKM]]'
- '[[Obsidian]]'
tags:
- idea
---
2021-12-29-We

# Suggestion on how to Obsidian

- Personal knowledge management

- People can be different and think and operation differently, but the way we interact with the world tend to be similar.
	-	The limits to our brain, the amount of information we can store and put down on paper
	- Some ways of doing PKM work better than others
	- The ways which will work best for you will take time to discover
	
1. Find what is worth trying and try them	
	- [[What is Gall's Law]]:
		> Every functional complex system emerges out of a simpler system that worked first.
	- Nick Milo (Maybe): "You have to earn [[Manage Complexity|complexity]]"
	
2. Let fruitful process grow and let friction do the pruning
	- What is the fruit I am trying to grow with PKM?
	- The ability to retain knowledge better
	- One don't just watch a plant grow in real time, it is incremental over really long time

Vimrc config
```
" Have j and k navigate visual lines rather than logical ones
nmap j gj
nmap k gk
" I like using H and L for beginning/end of line
nmap H ^
nmap L $
" Quickly remove search highlights
" nmap <F9> :nohl

" Yank to system clipboard
set clipboard=unnamed

" Go back and forward with Ctrl+O and Ctrl+I
" (make sure to remove default Obsidian shortcuts for these to work)
exmap back obcommand app:go-back
nmap <C-o> :back
exmap forward obcommand app:go-forward
nmap <C-i> :forward
```


---
# References
https://www.nickseitz.com/writing/obsidian-day-one-starterpack
My simple note-taking setup: https://youtu.be/E6ySG7xYgjY