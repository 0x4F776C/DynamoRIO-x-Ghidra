# DynamoRIO-x-Ghidra
Convert drcov text log for use in Ghidra scripting engine

## Why is this helpful?
It was a pain in the ass perform malware code coverage analysis in Ghidra without assistance. Therefore, I utilised DynamoRIO and Ghidra scripting engine to reduce the need of analysing the binary function by function. At some point I got lazy and decided to create a simple script to dump drcov output into a Python friendly format.

## What to improve?
Still unsure of how I am going to perform analysis for packed malwares with this method. Will update once I figure it out.
Do PM me or drop me an email if you can help! Thanks!

### Update
1. Modified Ghidra script to obtain functions via function addresses with debug features
2. Color coding feature

Reference:

[Check out DynamoRIO here!](https://dynamorio.org/)

[Check out Ghidra here!](https://ghidra-sre.org/)

[Check out Ghidra Python snippets here!](https://github.com/HackOvert/GhidraSnippets)
