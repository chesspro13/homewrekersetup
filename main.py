import os


class main:

    # Steps:

    # 1) Make a directory in the home directory '/' called speaker
    #       > mkdir /speaker

    # 2) Make a directory in the speaker directory '/speaker' called commands
    #       > mkdir /speaker/commands

    # 3) Make a directory in the speaker directory '/speaker' called commands
    #       > mkdir /speaker/songs

    # 4) Move to the speaker directory '/speaker'
    #       > cd /speaker

    # 5) Clone the music_client git repository
    #       > git clone https://github.com/chesspro13/music_client

    # 5) Clone the HomeWreker git repository
    #       > git clone https://github.com/chesspro13/HomeWreker


    def install(self):

        os.system("git config --global pull.ff only")

        try:
            if os.path.isdir("/songs"):
                print("There is already a /songs directory.")
            else:
                os.system("mkdir /speaker/songs")
        except Exception as e:
            print("There was an issue creating the songs directory!")
            print(e)

        try:
            if os.path.isdir("/speaker/music_client"):
                print("There is already a directory called /speaker/music_client. attempting an update.")
                os.system("git -C /speaker/music_client pull main")
            else:
                print("There is no directory called /speaker/music_client! Attempting to download!")
                os.system("sudo mkdir /speaker && sudo mkdir /speaker/music_client")
                os.system("sudo git clone https://github.com/chesspro13/music_client /speaker/music_client")
        except Exception as e:
            print("There was an issue installing or updating music_client!")
            print(e)

    def checkSystemForRequirements(self):
        print("Starting file check...")

    def __init__(self):
        self.installDir = "/"
