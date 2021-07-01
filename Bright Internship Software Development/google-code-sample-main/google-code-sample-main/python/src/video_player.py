"""A video player class."""

from .video_library import VideoLibrary

"""There is something wrong with the module loading I was unable to fix this problem."""

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all avaliable videos:")
        print("")
        for video in self._video_library:
            print(video)
            print("")
        
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        if video_id == amazing_cats_video_id:
            if video_playing != null:
                print("Stopping video: {video_playing}")
                print("Playing video: Amazing cats")
            else:
                print("Playing video: Amazing cats")
            video_playing = Amazing cats

        elif video_id == another_cat_video_id:
            if video_playing != null:
                print("Stopping video: {video_playing}")
                print("Playing video: Another cat video")
            else:
                print("Playing video: Another cat video")
            video_playing = Another cat video

        elif video_id == funny_dogs_video_id:
            if video_playing != null:
                print("Stopping video: {video_playing}")
                print("Playing video: Funny dogs")
            else:
                print("Playing video: Funny dogs")
            video_playing = Funny dogs

        elif video_id == life_at_google_video_id:
            if video_playing != null:
                print("Stopping video: {video_playing}")
                print("Playing video: Life at Google")
            else:
                print("Playing video: Life at Google")
            video_playing = Life at Google

        elif video_id == nothing_video_id:
            if video_playing != null:
                print("Stopping video: {video_playing}")
                print("Playing video: Video about nothing")
            else:
                print("Playing video: Video about nothing")
            video_playing = Video about nothing

        else:
            print("Cannot play video: Video does not exist")

        

    def stop_video(self):
        """Stops the current video."""

        if video_playing == Amazing cats:
            print("Stopping video: Amazing cats")

        elif video_playing == Another cat video:
            print("Stopping video: Another cat video")

        elif video_playing == Funny dogs:
            print("Stopping video: Funny dogs")

        elif video_playing == Life at Google:
            print("Stopping video: Life at Google")

        elif video_playing == Video about nothing:
            print("Stopping video: Video about nothing")

        else:
            print("Cannot stop video: No video is currently playing")

        

    def play_random_video(self):
        """Plays a random video from the video library."""

        import random
        random_number = random.randrange(1, 6)

        if random_number == 1:
            print("Stopping video: {video_playing}")
            print("Playing video: Amazing cats")
            video_playing = Amazing cats   

        elif random_number == 2:
            print("Stopping video: {video_playing}")
            print("Playing video: Another cat video")
            video_playing = Another cat video

        elif random_number == 3:
            print("Stopping video: {video_playing}")
            print("Playing video: Funny dogs")
            video_playing = Funny dogs

        elif random number == 4:
            print("Stopping video: {video_playing}")
            print("Playing video: Life at Google")
            video_playing = Life at Google

        elif random number == 5:
            print("Stopping video: {video_playing}")
            print("Playing video: Video about nothing")
            video_playing = Video about nothing

        

    def pause_video(self):
        """Pauses the current video."""

        if video_playing == Amazing cats:
            print("Pausing video: Amazing cats")
            video_paused = Amazing cats

        elif video_paused == Amazing cats:
            print("Video already paused: Amazing cats")
            video_playing = Amazing cats

        elif video_playing == Another cat video:
            print("Pausing video: Another cat video")
            video_paused = Another cat video

        elif video_paused == Another cat video:
            print("Video already paused: Another cat video")
            video_playing = Another cat video

        elif video_playing == Funny dogs:
            print("Pausing video: Funny dogs")
            video_paused = Funny dogs

        elif video_paused == Funny dogs:
            print("Video already paused: Funny dogs")
            video_playing = Funny dogs

        elif video_playing == Life at Google:
            print("Pausing video: Life at Google")
            video_paused = Life at Google

        elif video_paused == Life at Google:
            print("Video already paused: Life at Google")
            video_playing = Life at Google

        elif video_playing == Video about nothing:
            print("Pausing video: Video about nothing")
            video_paused = Video about nothing

        elif video_paused == Video about nothing:
            print("Video already paused: Video about nothing")
            video_playing = Video about nothing

        else:
            print("Cannot pause video: No video is currently playing")



    def continue_video(self):
        """Resumes playing the current video."""

        if video_paused == Amazing cats:
            print("Continuing video: Amazing cats")
            video_playing = Amazing cats

        elif video_paused == Another cat video:
            print("Continuing video: Another cat video")
            video_playing = Another cat video

        elif video_paused == Funny dogs:
            print("Continuing video: Funny dogs")
            video_playing = Funny dogs

        elif video_paused == Life at Google:
            print("Continuing video: Life at Google")
            video_playing = Life at Google

        elif video_paused == Video about nothing:
            print("Continuing video: Video about nothing")
            video_playing = Video about nothing

        else:
            print("Cannot continue video: Video is not paused")

        

    def show_playing(self):
        """Displays video currently playing."""

        if video_playing == Amazing cats:
            print("Currently playing: Amazing cats {}")
            if video_paused == Amazing cats:
                print(" - PAUSED")

        if video_playing == Another cat video:
            print("Currently playing: Another cat video {}")
            if video_paused == Another cat video:
                print(" - PAUSED")

        if video_playing == Funny dogs:
            print("Currently playing: Funny dogs {}")
            if video_paused == Funny dogs:
                print(" - PAUSED")

        if video_playing == Life at Google:
            print("Currently playing: Life at Google {}")
            if video_paused == Life at Google:
                print(" - PAUSED")

        if video_playing == Video about nothing:
            print("Currently playing: Video about nothing {}")
            if video_paused == Video about nothing:
                print(" - PAUSED")

        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        playlist_list = []

        if playlist_name != playlist:
            print("Successfully created new playlist: {playlist_name}")
            playlist = playlist_name
            playlist_list.append(playlist)

        else:
            print("Cannot create playlist: A playlist with the same name already exists")
        
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if video_id == amazing_cats_video_id: 
            print("Added video to {playlist_name}: Amazing cats")      
        
        elif video_id == another_cat_video_id: 
            print("Added video to {playlist_name}: Another cat video")

        elif video_id == funny_dogs_video_id: 
            print("Added video to {playlist_name}: Funny dogs")

        elif video_id == life_at_google_video_id: 
            print("Added video to {playlist_name}: Life at Google")

        elif video_id == nothing_video_id: 
            print("Added video to {playlist_name}: Video about nothing")

        elif playlist_list.count(playlist_name) == 0:
            print("Cannot add video to {playlist_name}: Playlist does not exist")

        else:
            print("Cannot add video to {playlist_name}: Video does not exist")



    def show_all_playlists(self):
        """Display all playlists."""

        if playlist_list[0] != null
            print("Showing all playlists:)
            print(playlist_list)

        else:
            print("No playlists exist yet")


                  
    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
