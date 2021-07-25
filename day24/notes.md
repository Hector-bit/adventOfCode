Day 24:
	Part One:
		We are doing some renovation with tiles
		White on one side, black on the other
		The tiles have 6 sides, each side has a direction
		 / \   NorthWest, NorthEast
		|   |  West, East
		 \ /   SouthWest, SouthEast
		We are given a long list of instructions "nwwswee"
		"A tile is identified by a serie4s of these directions with 
		no delimiters" - Idk what this means, leave note and come back
		NOTE: So each time you pass through a tile it gets flipped
		So far it seems like there is not limit on the size of the 
		2D array for the tiles, and they all start out white and I have
		to keep track of the ones that are black.

		Plan: Do some graph stuff, have nodes that are created if you 
		go in a direction you have not gone before, then recursively
		count all the nodes that have been made
