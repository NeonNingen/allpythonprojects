@echo off

cecho {0C}This line is red{#}

REM Print ASCII char 0x07 (beep) 
cecho {\u07 \u07}

cecho This {black on blue}word{#} is black on a blue background