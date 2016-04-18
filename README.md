# lab_1_APPPOO
Conway's Game of Life

Develop simple implementation of Conway's Game of Life Automaton.
Conditions:
1. Will use one OOP language. Otherwise you have to prove that your language have at least polymorphism (I will challenge you wink emoticon. This language should be cross platform, at least to be compiled on MAC smile emoticon
2. You are not allowed to use external libs. (At all)
3. Field are infinite.
4. Your application will run in console.
5. Your application will take -i(--input) argument with preset file path. Preset file will contain state of automaton which will be loaded in your app as first generation.
6. Your application will take -n(--number-of-iterations) argument for number of required generation to be evaluated. After evaluation the final state of automaton will be outputted to console directly.
7. Your application will take -o(--output) argument as output file path. If no output indicated then show final state in console. Output should contain all alive cells and not be bigger that is needed to include them(rectangle small as it is possible).
8. Input and output state files format is an array of binary values. Eg.
00000
00100
00010
01110
00000

