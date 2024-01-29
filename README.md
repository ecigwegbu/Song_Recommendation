**My hack idea**
> What's the idea?
- Make recommendations to popular songs similar to those he/she has recently Shazamed. These songs could be similar in multiple ways. E.g. there is another song by the same artist. The metric used for popularity is the number of Shazams made by users worldwide in the last week. This way, the user can discover new songs at the same time as others, and never feel left out. This project is a web application with a command-line user interface. Conceptually, it would be a tool integrated into the Shazam app or accessed by an API, so that the user is given a song recommendation automatically, as soon as they Shazam a song.

> What's the minimum viable product you can create?
- Recommend most tagged song in the last 24 hours worldwide that is in the same album as song the user tagged.

> Main components
- Client application with command-line interface
- REST server for housing worldwide tag data
- Apple MusicKit APIs

> Incomplete extensions
- Recomendations for popular new albums by the same artist to the user.
- Docker provisions made for tag-server. While these worked before, there are now issues with the use of Apache Spark, which is a distributed application, within the Docker container.

**Resouces I'll use**
> You are required either to use a MusicKit API or data provided of Shazams that users have created. What are you going to use?

- Tag samples
- Apple MusicKit API (used in incomplete extension)

> In addition to the above, what other resources are you going to use?
As of now, no other resources are foreseen to be needed.

**Language(s) I'll use**
> This will help us idenfity who can help you from the team for your hack.
Python will be used.

**How to run**
- Create virtual environment in root folder using `python3 -m venv .venv'
- Activate the virtual environment using `source .venv/bin/activate'
- Install requirements using 'pip install -r requirements.txt' in the root directory. 
- In a terminal enter `make server' to start the tag server. Then in a separate tab enter 'make run' to start the client app.

**This Version is courtesy of Elias Igwegbu, MannedModule Inc**
