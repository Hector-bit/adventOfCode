Final day in 2020 advent of code and I have no motivation to finish

long story short you can't get into the hotel room because of the 
incomptent check in staff, elevator is broken and you don't want to travel 25 flights of stairs again. Now I have to fix the rfid chip on the hotel keycard

The cryptographic handshake works like this:
	- the card transforms the "subject number" of 7 according
	to the card's secret "loop size". the result is called the
	card's "public key(card)"
	- The door transforms the subject number of 7 according to 
	the door's "public key(door)"
	- The card and door use the wireless RFID signal to transmit
	the two public keys (your puzzle input) to the other device.
	Now, both the door and card have each others public key, and
	so do I now because computer idk
	- The card transforms the subject number of the door's public
	key according to the card's loop size. The result is the
	"ENCRYPTION KEY".
	- The door transforms the subject number of the card's public
	key according to the door's loop size. The result is the same 
	ENCRYPTION KEY as the card caculated

use the public keys given to find out what single proccess turns
7 => proccess(loops x times) => public key (card)
7 => proccess(loops x times) => public key (door)
then doing the same thing with the public keys should get the same 
encryption key
public key (card) => proccess => ek
public key (door) => proccess => ek
