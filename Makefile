all: compile execute

execute:
	debug.exe
	
compile:
	g++ main.cpp -o debug.exe