For some businesses, they have older machines and software that don't run on anything other than an unsupported version of Windows.

If the software gets corrupted, how to repair?

1. Virtualize the OS, possibly using Virtual Box or something more performant, but unnecessary.
    
    --------------------------------------
    |   ________          __________     |
    |  | WinXP | <----->  | Database|    |
    |  | Virt  |          |  Linux  |    |
    |  |_______|          |_________|    |
    -------------------------------------

2. Image each setup so that it would be compatible with all hardware available.
3. Set up networking for these boxes so that they interop with each other,.
4. Set up a Database Server outside the virtualization machine. Have a Master - Master setup?
5. Setup each machine to fall-back to use the other database if the connection fails, this is pretty hard probably.
