class PositionService:
    singleton = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.visible = True

    # a class method to create a Person object by birth year.
    @classmethod
    def get_instance(cls):
        if PositionService.singleton == None:
            PositionService.singleton = PositionService()
        return PositionService.singleton


# non OO service api

# set the x position of your circle
def set_position_x(x):
    instance = PositionService.get_instance()
    instance.x = x


# set the y position of your circle
def set_position_y(y):
    instance = PositionService.get_instance()
    instance.y = y


# set both x and y positions of your circle
def set_position(x, y):
    instance = PositionService.get_instance()
    instance.x = x
    instance.y = y


# get the x position
def get_position_x():
    instance = PositionService.get_instance()
    return instance.x


# get the y position
def get_position_y():
    instance = PositionService.get_instance()
    return instance.y


# return Ture/False if you've "hidden" your shape by erasing it
def is_visible():
    instance = PositionService.get_instance()
    return instance.visible


# Pass in a Boolean to indicate that you've hidden or displayed your shape
# By convention, True is visible, False is hidden
def set_visible(visibility):
    instance = PositionService.get_instance()
    instance.visible = visibility
