import serpy 

class UserSerializers(serpy.Serializer):
    """
        This class convert user data into json
    """
    id = serpy.Field()
    first_name = serpy.Field()
    last_name = serpy.Field()
    email = serpy.Field()