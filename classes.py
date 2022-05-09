class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 63     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 10      # Maximum TV volume

    def __init__(self):
        """
        This intitializes the TV Object
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        This method is used to turn the TV on/off.
        """
        
        if self.__status:
            self.__status = False
        else:
            self.__status = True


    def channel_up(self):
        """
        This method is used to adjust the TV channel by raising the value by 1
        It also sets the channel back to the MIN_CHANNEL if the max was already reached
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1

    def channel_down(self):
        """
        This method is used to adjust the TV channel by decreasing the value by 1
        It also sets the channel back to the MAX_CHANNEL if the min was already reached
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            elif self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1

    def volume_up(self):
        """
        This method is used to adjust the volume by increasing the value by 1
        It will not go any higher than MAX_VOLUME
        """
        
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        This method is used to adjust the volume by decreasing the value by 1
        It will not go any lower than MIN_VOLUME
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        This method is used to print the status of the TV if using a terminal based program

        :return: the status of the TV as a string
        """
        return "TV status: Is on = " + str(self.__status) +", Channel = " + str(self.__channel) + ", Volume = " + str(self.__volume)
    
    def get_status(self):
        """
        This method is used to get the status of the TV for use in other programs

        :return: the status of the TV as a tuple
        """
        return self.__status,self.__channel,self.__volume