import unittest
from classes import Television

class TestClasses(unittest.TestCase):

    def setUp(self) -> None:
        """
        Prepares the tv object for the program 
        """
        self.tv = Television()

    def tearDown(self) -> None:
        """
        Deletes the tv created by the setUp method when the program is finished
        """
        del self.tv

     
    def test_power(self):
        """
        Tests the power method of the TV
        """
        assert(self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0")
        self.tv.power()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0")
        self.tv.power()
        assert(self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0")
    

    def test_channel_up(self):
        """
        Tests the channel_up method of the TV
        """
        self.tv.channel_up()
        assert(self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0")
        self.tv.power()

        self.tv.channel_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0")
        
        new_channel = 2
        count = 0
        for index in range(62):
            self.tv.channel_up()
            assert(self.tv.__str__() == "TV status: Is on = True, Channel = " + str(new_channel + count) + ", Volume = 0")
            count += 1

        self.tv.channel_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0")
        self.tv.channel_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0")
        
        
   

    def test_channel_down(self):
        """
        Tests the channel_down method of the TV
        """
        self.tv.channel_down()
        assert(self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0")
        self.tv.power()
        self.tv.channel_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 63, Volume = 0")
        self.tv.channel_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 62, Volume = 0")
        self.tv.channel_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 61, Volume = 0")
        self.tv.channel_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 60, Volume = 0")
    

    def test_volume_up(self):
        """
        Tests the volume_up method of the TV
        """
        self.tv.volume_up()
        assert(self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0")
        self.tv.power()

        self.tv.volume_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1")
        
        new_vol = 2
        count = 0
        for index in range(8):
            self.tv.volume_up()
            assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = " + str(new_vol + count))
            count += 1
        
        self.tv.volume_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 10")
        self.tv.volume_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 10")

    
    def test_volume_down(self):
        """
        Tests the volume_down method of the TV
        """
        self.tv.volume_down()
        assert(self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0")
        self.tv.power()
        
        # this turns the TV on and volume up all the way so that volume_down can be tested fully
        self.tv.volume_up()
        self.tv.volume_up()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2")

        self.tv.volume_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1")
        self.tv.volume_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0")
        self.tv.volume_down()
        assert(self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0")
    

if __name__ == "__main__":
    unittest.main()