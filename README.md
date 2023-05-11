# Discord-Plays-Omori
Play Omori with Friends on Discord while Streaming by typing commands on Discord.

If you want to Stream the Game with a Keyboard Overlay, I Suggest using NohBoard 
https://github.com/ThoNohT/NohBoard

move "Omori.kb" file in the NohBoard Folder and you should have a custom Omori Keyboard. optionally, you could also move the "NohBoard.config" file.
For Streaming with the Keyboard Overlay, you can setup OBS however way you like. once you are done, simply Right click the Preview, Select "Fullscreen Projector (Preview)" and Stream that window on Discord.

In "Omori.py"
at Line 8, replace "channel ID" for the Channel's ID (without the inverted Commas) you want to read commands from. you can also insert multiple Channel IDs seperated by a Comma.
at Line 101, replace "Insert-Bot-Token-Here" with your Bot's Token. make sure the bot has appropriate permissions to read the messages and you are good to go.
