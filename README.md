https://gist.github.com/mmalex/3a538aaba60f0ca21eac868269525452

^^ this link describes a cool way to get rid of individual read and write heads and wrap-around logic when implementing delay lines.
I have used it, but struggled to understand what was happening. I asked my ol' pal ChadGPT to help me. 
Chad at first could not understand what was different about this strategy, but eventually saw and helped me think through it. 
I then asked if Chad could write some python to visualize the effect. After a few false starts, he did indeed write the code. Go Chad. 

this is implmented in the ROOM and CHORUS modules in the eurorack repository. works great.
