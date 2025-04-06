# DynamoRIO-x-Ghidra
Convert drcov text log for use in Ghidra scripting engine

<!-- display-subdirectories: false -->

## Why is this helpful?
While performing malware code analysis. I realised it was tedious to do pinpoint how the binary works and in what particular order (function calls). Therefore, I utilised DynamoRIO and Ghidra scripting engine to remove functions that weren't called during the run.

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
